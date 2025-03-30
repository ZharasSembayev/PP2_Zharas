import pygame, sys
from pygame.locals import *
import random, time


pygame.init()


background = pygame.image.load('car_images/AnimatedStreet.png')


BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.SysFont("Verdana", 60)  
font_small = pygame.font.SysFont("Verdana", 20) 
game_over = font.render("Game Over", True, BLACK)


WIDTH, HEIGHT = background.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car game")


SPEED = 5
SCORE = 0 
COINS_COLLECTED = 0
clock = pygame.time.Clock()  


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('car_images/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('car_images/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > HEIGHT:
            SCORE += 1 
            self.rect.top = 0 
            self.rect.center = (random.randint(30, WIDTH - 30), 0) 

# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('car_images/Coin.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), random.randint(-100, -40))

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > HEIGHT:
            self.rect.top = random.randint(-100, -40)
            self.rect.centerx = random.randint(40, WIDTH - 40) 


P1 = Player()
E1 = Enemy()


enemies = pygame.sprite.Group()
enemies.add(E1)  

coins = pygame.sprite.Group()
for _ in range(1): 
    coins.add(Coin())

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)  
all_sprites.add(E1)  


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
N = 5

running = True
while running:
    screen.blit(background, (0, 0)) 
    if COINS_COLLECTED == N: 
        SPEED += 5
        N += 5
        
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        if isinstance(entity, Enemy):
            entity.move()  
        else:
            entity.update()  

    
    for coin in coins:
        screen.blit(coin.image, coin.rect)
        coin.move()  
        
        if pygame.sprite.collide_rect(P1, coin):
            COINS_COLLECTED += random.randint(1,3) 
            coin.rect.top = random.randint(-100, -40)  
            coin.rect.centerx = random.randint(40, WIDTH - 40)  

    
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(scores, (10, 10))  

    
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    screen.blit(coins_text, (WIDTH - 100, 10))  

    
    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(RED)
        screen.blit(game_over, (WIDTH//2 - 170, HEIGHT//2 - 30))  
        pygame.display.update()
        time.sleep(2)
        running = False

    pygame.display.update()
    FPS = 60
    clock.tick(FPS)


pygame.quit()
sys.exit()