from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept() # Aceptamos la conexión de WebSocket
    try:
        while True:
            data = await websocket.receive_text() # Recibimos los datos del cliente
    except WebSocketDisconnect:
        print("Client disconnected")