import random

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(5, 5), (5, 4), (5, 3)]
        self.direction = (0, 1)
        self.food = (10, 10)
        self.game_over = False

    def move(self):
        if self.game_over:
            return

        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        if new_head in self.snake or not (0 <= new_head[0] < 20 and 0 <= new_head[1] < 20):
            self.game_over = True
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = (random.randint(0, 19), random.randint(0, 19))
        else:
            self.snake.pop()

    def change_direction(self, new_direction):
        self.direction = new_direction
