import asyncio
import sqlite3
from contextlib import asynccontextmanager

import uvicorn
from fastapi import BackgroundTasks, FastAPI

from .tree_manager import TreeManager


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

    (previous_pattern,) = cursor.execute(
        "SELECT pattern FROM current_pattern"
    ).fetchone()
    if previous_pattern is not None:
        await app.state.manager.run_pattern(previous_pattern)

    app.state.conn = conn

    yield

    await app.state.manager.stop_current()


app = FastAPI(lifespan=lifespan)


@app.post("/start/{pattern}")
async def start_pattern(pattern: str):
    # Create a new background task
    await app.state.manager.run_pattern(pattern)

    conn = app.state.conn
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO current_pattern VALUES (1, :pattern) ON CONFLICT DO UPDATE SET pattern = :pattern",
        {"pattern": pattern},
    )
    conn.commit()
    return {"status": f"Pattern {pattern} started"}


@app.post("/stop")
async def stop_tree():
    await app.state.manager.stop_current()

    conn = app.state.conn
    cursor = conn.cursor()
    cursor.execute("DELETE FROM current_pattern WHERE id = 1")
    conn.commit()
    return {"status": "Tree turned off"}


def start():
    """Entry point for uv run start"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
