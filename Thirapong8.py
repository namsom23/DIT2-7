import tkinter as tk
import random

# ค่าคงที่
GAME_WIDTH = 600
GAME_HEIGHT = 400
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

# ตัวแปร global
direction = "right"
queued_direction = "right"
game_running = True

# ฟังก์ชันงู
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for _ in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )

def next_turn():
    global direction, queued_direction, game_running, snake, food

    if not game_running:
        return

    direction = queued_direction
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    x %= GAME_WIDTH
    y %= GAME_HEIGHT

    new_head = [x, y]

    if new_head in snake.coordinates:
        game_over()
        return

    snake.coordinates.insert(0, new_head)
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if new_head == food.coordinates:
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    window.after(SPEED, next_turn)

def change_direction(new_direction):
    global direction, queued_direction
    opposites = {"left": "right", "right": "left", "up": "down", "down": "up"}
    if new_direction != opposites.get(direction):
        queued_direction = new_direction

def game_over():
    global game_running
    game_running = False
    canvas.delete("all")
    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2 - 20,
        font=('consolas', 30), text="GAME OVER", fill="red"
    )
    canvas.create_text(
        GAME_WIDTH / 2, GAME_HEIGHT / 2 + 20,
        font=('consolas', 20), text="กด R เพื่อเล่นใหม่", fill="white"
    )

def restart_game(event=None):
    global direction, queued_direction, game_running, snake, food

    canvas.delete("all")
    direction = "right"
    queued_direction = "right"
    game_running = True

    snake = Snake()
    food = Food()
    next_turn()

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("🐍 งูกินอาหาร by ChatGPT")
window.resizable(False, False)

canvas = tk.Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# เริ่มเกม
window.update()
snake = Snake()
food = Food()
next_turn()

# ควบคุม
window.bind('<Left>', lambda e: change_direction("left"))
window.bind('<Right>', lambda e: change_direction("right"))
window.bind('<Up>', lambda e: change_direction("up"))
window.bind('<Down>', lambda e: change_direction("down"))
window.bind('r', restart_game)
window.bind('R', restart_game)

window.mainloop()