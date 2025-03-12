const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const resetButton = document.getElementById('resetButton');
const socket = new WebSocket('ws://localhost:8080/ws');

let gameState = {
    snake: [],
    food: {},
    gameOver: false
};

socket.onmessage = function(event) {
    gameState = JSON.parse(event.data);
    drawGame();
};

resetButton.onclick = function() {
    socket.send(JSON.stringify({ action: 'reset' }));
};

function drawGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (gameState.gameOver) {
        ctx.fillStyle = 'red';
        ctx.font = '20px Arial';
        ctx.fillText('Game Over', canvas.width / 2 - 50, canvas.height / 2);
        return;
    }
    ctx.fillStyle = 'green';
    gameState.snake.forEach(segment => {
        ctx.fillRect(segment[0] * 20, segment[1] * 20, 20, 20);
    });
    ctx.fillStyle = 'red';
    ctx.fillRect(gameState.food[0] * 20, gameState.food[1] * 20, 20, 20);
}
