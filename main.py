import asyncio
from typing import Any

from litestar import Litestar, get


@get("/fast")
async def fast() -> dict[str, Any]:
    return {"message": "fast response"}


@get("/sleep/{seconds:int}")
async def sleep(seconds: int) -> dict[str, Any]:
    await asyncio.sleep(seconds)
    return {"message": f"slept for {seconds} seconds"}


@get("/new_route")
async def new_route() -> dict[str, Any]:
    return {"message": "hello world!"}


app = Litestar(route_handlers=[fast, sleep, new_route])
