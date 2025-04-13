import pygame #type: ignore
pygame.init()
pygame.mixer.init()

w, h = 700, 300
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Pygame with Music Player')

font = pygame.font.Font(None, 36)
white = (255, 255, 255)
black = (0, 0, 0)

singer = [
    "musics/Miyagi & Andy Panda - Патрон.mp3",
    "musics/MiyaGi - Самурай.mp3",
    "musics/Sadraddin - Aiga qarap.mp3"
] 
current_music = 0
pygame.mixer.music.load('')
pygame.mixer.music.play()

def draw_interface():
    screen.fill(white)
    text = font.render(f"Right Now playing{singer[current_music].split('/')[-1]}", True, black)
    screen.blit(text, (50, 130))  
    pygame.display.flip()
def play():
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def next():
    global current_music
    current_music = (current_music + 1) % len(singer)
    pygame.mixer.music.load(singer[current_music])
    play()
    draw_interface()
def previous():
    global current_music
    current_music = (current_music - 1) % len(singer) 
    pygame.mixer.music.load(singer[current_music])
    play()
    draw_interface()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play()  
            elif event.key == pygame.K_s:
                stop()  
            elif event.key == pygame.K_RIGHT:
                next()  
            elif event.key == pygame.K_LEFT:
                previous()
pygame.quit()