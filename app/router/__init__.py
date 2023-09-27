from fastapi import APIRouter

estatic = APIRouter()


@estatic.get("/")
async def start_welcome():
    return "Welcome to my API"


@estatic.get("/about")
async def start_welcome():
    return "About API"


@estatic.get("/help")
async def start_welcome():
    return "Help API"
