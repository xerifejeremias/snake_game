from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
from src.functions import SnakeGame
import json
import asyncio

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
    game = SnakeGame()  # Initialize the SnakeGame instance
    while True:
        # Update game state
        game.move()
        # Send the updated game state to the front end
        await websocket.send_text(json.dumps({
            "snake": game.snake,
            "food": game.food,
            "gameOver": game.game_over
        }))
        await asyncio.sleep(0.1)  # Adjust the sleep time as needed for game speed
        data = await websocket.receive_text()
        # Process game logic here
        await websocket.send_text(f"Message text was: {data}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
