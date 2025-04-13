import pygame #type: ignore
pygame.init()

w, h = 600, 300
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Pygame with Zharas')

r = 25
x, y = w // 2, h // 2
speed = 20

running = True
while running:
    screen.fill("white")
    pygame.draw.circle(screen, 'red', (x,y), r)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y - r - speed >= 0:
                y -= speed
            elif event.key == pygame.K_DOWN and y + r + speed <= h:
                y += speed
            elif event.key == pygame.K_LEFT and x - r - speed >= 0:
                x -= speed
            elif event.key == pygame.K_RIGHT and x + r + speed <= w:
                x += speed
pygame.quit()