import pygame
import random
import time

pygame.init()


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


GREEN = (0, 255, 0)  
BLACK = (0, 0, 0)    
RED = (255, 0, 0)  
WHITE = (255, 255, 255)  


font = pygame.font.Font(None, 36)


class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100)]
        self.dx, self.dy = CELL_SIZE, 0 
        self.alive = True 

    def move(self):
        if not self.alive:
            return

        head_x, head_y = self.body[0]
        new_head = (head_x + self.dx, head_y + self.dy)

       
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            self.alive = False
            return

        
        if new_head in self.body:
            self.alive = False
            return

        self.body.insert(0, new_head)
        self.body.pop() 

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))


class Food:
    def __init__(self, snake_body):
        self.position = self.spawn_food(snake_body)
        self.spawn_time = time.time()  
        self.timer_duration = random.randint(4, 10)  

    def spawn_food(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:  
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))


running = True
snake = Snake()
food = Food(snake.body)
clock = pygame.time.Clock()
score = 0 
level = 1  
FPS = 10   

while running:
    screen.fill(BLACK)

    # Event handling
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

   
    if time.time() - food.spawn_time > food.timer_duration:
        food = Food(snake.body)  

    
    snake.draw()
    food.draw()

   
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

    if not snake.alive:
        pygame.time.delay(1000)
        running = False

pygame.quit()