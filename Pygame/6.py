import pygame

pygame.init()

# Экран өлшемдері
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Бояу беті
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))  # Ақ түс

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

colors = [BLACK, RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, CYAN]
color_index = 0
color = colors[color_index]

# Күй айнымалылар
drawing = False
start_pos = None
radius = 5
tool = "brush"

# Шрифт
font = pygame.font.SysFont(None, 24)

# Негізгі цикл
running = True
while running:
    screen.blit(canvas, (0, 0))

    # Нұсқаулық жазу
    instructions = font.render("B - Brush | E - Eraser | C - Circle | R - Rect | S - Square | T - Right Triangle | P - Equilateral | O - Rhombus | TAB - Next Color | X - Clear", True, BLACK)
    screen.blit(instructions, (10, HEIGHT - 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Құрал таңдау
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tool = "rectangle"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right triangle"
            elif event.key == pygame.K_p:
                tool = "equilateral triangle"
            elif event.key == pygame.K_o:
                tool = "rhombus"

            # Түс таңдау (1–8)
            if pygame.K_1 <= event.key <= pygame.K_8:
                color = colors[event.key - pygame.K_1]

            # Қалам өлшемі
            if event.key == pygame.K_DOWN and radius > 3:
                radius -= 2
            if event.key == pygame.K_UP and radius < 30:
                radius += 2

            # Түсті ауыстыру
            if event.key == pygame.K_TAB:
                color_index = (color_index + 1) % len(colors)
                color = colors[color_index]

            # Экран тазалау
            if event.key == pygame.K_x:
                canvas.fill(WHITE)

        # Тінтуірмен салуды бастау
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        # Тінтуірді жіберу
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            x1, y1 = start_pos
            x2, y2 = end_pos

            if tool == "rectangle":
                pygame.draw.rect(canvas, color, (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 2)
            elif tool == "circle":
                radius = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5) // 2
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                pygame.draw.circle(canvas, color, center, radius, 2)
            elif tool == "square":
                size = max(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(canvas, color, (x1, y1, size, size), 2)
            elif tool == "right triangle":
                points = [(x1, y1), (x1, y2), (x2, y2)]
                pygame.draw.polygon(canvas, color, points, 2)
            elif tool == "equilateral triangle":
                points = [(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)]
                pygame.draw.polygon(canvas, color, points, 2)
            elif tool == "rhombus":
                mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
                points = [(mid_x, y1), (x2, mid_y), (mid_x, y2), (x1, mid_y)]
                pygame.draw.polygon(canvas, color, points, 2)

        # Қимыл кезінде
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.line(canvas, color, start_pos, event.pos, radius)
                start_pos = event.pos
            elif tool == "eraser":
                pygame.draw.line(canvas, WHITE, start_pos, event.pos, radius)
                start_pos = event.pos
            elif tool in ["rectangle", "circle", "square", "right triangle", "equilateral triangle", "rhombus"]:
                screen.blit(canvas, (0, 0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                if tool == "rectangle":
                    pygame.draw.rect(screen, color, (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 2)
                elif tool == "circle":
                    radius = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5) // 2
                    center = ((x1 + x2) // 2, (y1 + y2) // 2)
                    pygame.draw.circle(screen, color, center, radius, 2)

    pygame.display.update()

pygame.quit()