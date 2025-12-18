import asyncio
import logging
import sqlite3
from contextlib import asynccontextmanager

import uvicorn
from fastapi import BackgroundTasks, FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .patterns import Pattern, PatternName, pattern_names
from .tree_manager import TreeManager

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Create a logger instance
logger = logging.getLogger(__name__)


class BrightnessRequest(BaseModel):
    brightness: float = Field(ge=0, le=1)


# Lifespan handles setup/teardown
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.manager = TreeManager()
    conn = sqlite3.connect("state.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS current_pattern(id INTEGER PRIMARY KEY, pattern TEXT NOT NULL)"
    )
    conn.commit()

    res = cursor.execute("SELECT pattern FROM current_pattern").fetchone()
    if res is not None:
        await app.state.manager.run_pattern(res[0])

    app.state.conn = conn

    yield

    await app.state.manager.stop_current()


app = FastAPI(
    title="RGB Christmas Tree",
    summary="Control the lights on an RGB LED Christmas Tree.",
    description="A set of REST APIs for controling a physical rgbxmastree attached to a raspberry pi.",
    version="2.0.0",
    redoc_url=None,
    root_path="/api/v1",
    tags=["brightness", "patterns"],
    lifespan=lifespan,
)


@app.get("/brightness", tags=["brightness"])
async def get_brightness() -> float:
    return app.state.manager.tree.brightness


@app.post("/brightness", tags=["brightness"])
async def set_brightness(body: BrightnessRequest) -> float:
    app.state.manager.tree.brightness = body.brightness
    return app.state.manager.tree.brightness


@app.get("/patterns", tags=["patterns"])
async def list_patterns() -> list[Pattern]:
    logger.info("Listing patterns")
    return pattern_names


@app.get("/patterns/current", tags=["patterns"])
async def current_pattern() -> PatternName | None:
    logger.info("Getting current pattern")

    conn = app.state.conn
    cursor = conn.cursor()
    res = cursor.execute(
        "SELECT pattern FROM current_pattern",
    ).fetchone()
    if res is None:
        return

    return res[0]


@app.post("/patterns/start/{pattern}", tags=["patterns"])
async def start_pattern(pattern: PatternName) -> PatternName:
    logging.info(f"Starting pattern: {pattern}")
    # Create a new background task
    await app.state.manager.run_pattern(pattern)

    conn = app.state.conn
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO current_pattern VALUES (1, :pattern) ON CONFLICT DO UPDATE SET pattern = :pattern",
        {"pattern": pattern},
    )
    conn.commit()
    return pattern


@app.post("/patterns/stop", tags=["patterns"])
async def stop_pattern() -> None:
    logging.info("Stopping pattern")
    await app.state.manager.stop_current()

    conn = app.state.conn
    cursor = conn.cursor()
    cursor.execute("DELETE FROM current_pattern WHERE id = 1")
    conn.commit()


# Must be mounted after the API routes or it would capture them
app.mount("/", StaticFiles(directory="public", html=True), name="public")


def start():
    """Entry point for uv run start"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
