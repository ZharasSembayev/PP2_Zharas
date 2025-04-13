import pygame # type: ignore
import time 
pygame.init()

pygame.display.set_caption("Pygame with MickeyMouse")
bg = pygame.image.load("images/mickeyclock.png")
r = pygame.image.load('images/rightarm.png')
l = pygame.image.load("images/leftarm.png")

w, h = 1400, 1050
screen = pygame.display.set_mode((w, h))
cent = (w // 2, h // 2)

def rotate_hand(image, angle):
    rotated_image = pygame.transform.rotate(image, - angle)
    new_rect = rotated_image.get_rect(center = cent)
    return rotated_image, new_rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    current_time = time.localtime()
    m = current_time.tm_min
    s = current_time.tm_sec
    m_angle = 360 * (m / 60)
    s_angle = 360 * (s / 60)
    
    screen.fill('white')
    screen.blit(bg, (0, 0))
    
    rotated_min, min_pos = rotate_hand(r, m_angle)
    screen.blit(rotated_min, min_pos)
    rotated_second, sec_pos = rotate_hand(l, s_angle)
    screen.blit(rotated_second, sec_pos)
    
    pygame.display.flip()
    pygame.time.delay(1000)
pygame.quit()
