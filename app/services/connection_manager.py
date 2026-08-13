from fastapi import WebSocket 

class ConnectionManager:
    def __init__(self):
        self.connections = {}

    async def add_connection(self, ticket_id: str, websocket: WebSocket):
        await websocket.accept()
        if ticket_id not in self.connections:
            self.connections[ticket_id] = []
        self.connections[ticket_id].append(websocket) # Cada websocket representa la conexión WebSocket de ese usuario como tal

    async def remove_connection(self, ticket_id: str, websocket: WebSocket):
        for ticket_id, connection in self.connections.items():
            if websocket in connection:
                connection.remove(websocket)
                if not connection:  # Si no hay más conexiones para este ticket_id, eliminamos la entrada
                    del self.connections[ticket_id]
                break

    async def broadcast(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)