import pygame
import random
import time
import psycopg2
from datetime import datetime


conn = psycopg2.connect(
    dbname='snake',
    user='postgres',
    password='12345678',
    host='localhost',
    port='5432'
)
cur = conn.cursor()
conn.commit()


username = input("Enter your username: ").strip()

cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1", (user_id,))
    last_game = cur.fetchone()
    if last_game:
        score, level = last_game
    else:
        score, level = 0, 1
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    score, level = 0, 1

pygame.init()


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
FPS = 10 + (level - 1) * 2
paused = False


GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100)]
        self.dx, self.dy = CELL_SIZE, 0
        self.alive = True

    def move(self):
        if not self.alive or paused:
            return

        head_x, head_y = self.body[0]
        new_head = (head_x + self.dx, head_y + self.dy)

        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.body or
            new_head in wall.blocks):
            self.alive = False
            return

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake_body):
        self.position = self.spawn_food(snake_body)
        self.spawn_time = time.time()
        self.timer_duration = random.randint(4, 10)

    def spawn_food(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            pos = (x, y)
            center_zone = pygame.Rect(WIDTH//2 - 40, HEIGHT//2 - 40, 80, 80)
            if pos not in snake_body and pos not in wall.blocks and not center_zone.collidepoint(x, y):
                return pos

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

class Wall:
    def __init__(self, level):
        self.blocks = self.load_level(level)

    def load_level(self, level):
        walls = []
        center_x = WIDTH // 2
        center_y = HEIGHT // 2
        safe_zone = pygame.Rect(center_x - 40, center_y - 40, 80, 80)

        if level == 2:
            for i in range(5, 25):
                block = pygame.Rect(i * CELL_SIZE, 10 * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if not block.colliderect(safe_zone):
                    walls.append((i * CELL_SIZE, 10 * CELL_SIZE))

        elif level == 3:
            for i in range(8, 20):
                for y in [15 * CELL_SIZE, 25 * CELL_SIZE]:
                    block = pygame.Rect(i * CELL_SIZE, y, CELL_SIZE, CELL_SIZE)
                    if not block.colliderect(safe_zone):
                        walls.append((i * CELL_SIZE, y))

        elif level >= 4:
            for i in range(0, WIDTH, CELL_SIZE):
                block = pygame.Rect(i, HEIGHT // 2, CELL_SIZE, CELL_SIZE)
                if not block.colliderect(safe_zone):
                    walls.append((i, HEIGHT // 2))

        return walls

    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(screen, GRAY, (*block, CELL_SIZE, CELL_SIZE))


snake = Snake()
wall = Wall(level)
food = Food(snake.body)
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -CELL_SIZE, 0
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = CELL_SIZE, 0
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -CELL_SIZE
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, CELL_SIZE
            elif event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_s:
                cur.execute(
                    "INSERT INTO user_score (user_id, score, level, saved_at) VALUES (%s, %s, %s, %s)",
                    (user_id, score, level, datetime.now())
                )
                conn.commit()
                print("Game saved!")

    if not paused:
        snake.move()

        if snake.body[0] == food.position:
            weight = random.randint(1, 4)
            score += weight
            for _ in range(weight):
                snake.grow()
            food = Food(snake.body)

            if score % 3 == 0:
                level += 1
                FPS += 2
                wall = Wall(level)

        if time.time() - food.spawn_time > food.timer_duration:
            food = Food(snake.body)

    wall.draw()
    snake.draw()
    food.draw()

    score_text = font.render(f"Score: {score}  Level: {level} {'[PAUSED]' if paused else ''}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

    if not snake.alive:
        pygame.time.delay(1000)
        running = False

pygame.quit()
cur.close()
conn.close()