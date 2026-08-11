from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.routers import tickets
from app.websockets import tickets_ws

app = FastAPI()

app.include_router(tickets.router)
app.include_router(tickets_ws.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}