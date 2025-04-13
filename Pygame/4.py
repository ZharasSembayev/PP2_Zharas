import pygame #type: ignore
from pygame.locals import * #type: ignore
import time, random

pygame.init()
bg = pygame.image.load('images/AnimatedStreet.png')
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black")

w, h = bg.get_size()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Racer with Zharas")

speed = 5
score = 0
coins_coll = 0
lives = 3
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (w // 2, h - 2)
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
           self.rect.move_ip(-5, 0)
        if self.rect.right < w and pressed_keys[pygame.K_RIGHT]:
           self.rect.move_ip(5, 0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0)
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > h:
            score += 1 
            self.rect.top = 0 
            self.rect.center = (random.randint(30, w - 30), 0) 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), random.randint(-100, -40))
    def move(self):
        self.rect.move_ip(0, speed // 2)
        if self.rect.top > h:
            self.rect.top = random.randint(-100, -40)
            self.rect.centerx = random.randint(40, w - 40) 
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

running = True
while running :
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 2
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
            coins_coll += 1 
            coin.rect.top = random.randint(-100, -40)  
            coin.rect.centerx = random.randint(40, w - 40)         
    scores = font_small.render(f"Score: {score}", True, "black")
    screen.blit(scores, (10, 10))
    coins_text = font_small.render(f"Coins: {coins_coll}", True, "black")
    screen.blit(coins_text, (w - 100, 10))  
    lives_text = font_small.render(f"LIVES: {lives}", True, "black")
    screen.blit(lives_text, (w // 2 - 100, 10))
    
    if pygame.sprite.spritecollideany(P1, enemies):
        lives -= 1
        if lives == -1:
            screen.fill('red')
            screen.blit(game_over, (w//2 - 170, h//2 - 30))
            time.sleep(2)
            running = False 
        else:
            P1.rect.center = (w // 2, h - 20)  
            time.sleep(1)
    pygame.display.update()
    FPS = 60
    clock.tick(FPS)

pygame.quit()
