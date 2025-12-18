import asyncio
import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI, BackgroundTasks

from .tree_manager import TreeManager

# Lifespan handles setup/teardown
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.manager = TreeManager()
    yield
    await app.state.manager.stop_current()

app = FastAPI(lifespan=lifespan)


@app.post("/start/{pattern}")
async def start_pattern(pattern: str):
    manager = app.state.manager
    await manager.stop_current()
    
    # Create a new background task
    manager.active_task = asyncio.create_task(manager.run_pattern(pattern))
    return {"status": f"Pattern {pattern} started"}


@app.post("/stop")
async def stop_tree():
    await app.state.manager.stop_current()
    return {"status": "Tree turned off"}


def start():
    """Entry point for uv run start"""
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
