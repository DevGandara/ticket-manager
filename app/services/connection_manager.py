from fastapi import WebSocket 

class ConnectionManager:
    def __init__(self):
        self.connections = []

    async def add_connection(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def remove_connection(self, websocket: WebSocket):
        await websocket.close()
        self.connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)