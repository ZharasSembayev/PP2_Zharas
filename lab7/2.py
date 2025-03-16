import pygame
import os
 
pygame.init()
pygame.mixer.init()
pygame.font.init()
font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((750, 500))

music_folder = 'musics'

button_images = { 
    "Play" : pygame.transform.scale(pygame.image.load('music_buttons/play.png'),(50,50)),
    "Next" : pygame.transform.scale(pygame.image.load('music_buttons/next.png'),(50,50)),
    "Back" : pygame.transform.scale(pygame.image.load('music_buttons/back.png'),(50,50))
}

button_positions = {
    "Back": (245, 400),
    "Play": (345, 400),
    "Next": (445, 400),
}

pygame.display.set_caption("Music Player")

running = True

musics = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_track = 0
def draw_track_name():
    screen.fill((255, 255, 255)) 

    track_name = musics[current_track]
    text_surface = font.render(track_name, True, (30, 30, 30))
    
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 50))
    screen.blit(text_surface, text_rect) 
    
    for text, pos in button_positions.items():
        screen.blit(button_images[text], pos)

    pygame.display.flip()
    pygame.time.delay(1000)
    
def play_music():
    track_path = os.path.join(music_folder, musics[current_track])
    pygame.mixer.music.load(track_path)
    pygame.mixer.music.play()
    draw_track_name()
def draw_buttons():
    screen.fill((255, 255, 255)) 
    for text, pos in button_positions.items():
        screen.blit(button_images[text], pos) 
    pygame.display.flip() 

while running:
    draw_buttons()
    draw_track_name()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()


            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(musics)
                play_music()
            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(musics)
                play_music()