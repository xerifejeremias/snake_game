from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# Mount the 'static' directory to serve static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def get():
    with open("src/index.html") as f:
        return HTMLResponse(f.read())

# WebSocket endpoint for real-time game updates
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Process game logic here
        await websocket.send_text(f"Message text was: {data}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
