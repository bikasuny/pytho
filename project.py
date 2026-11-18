import pygame
import sys
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Click the Circle")

circle_pos = [400, 300]  # Starting position of the circle

font = pygame.font.SysFont(None, 36)
score = 0

def check_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()
    distance = math.hypot(mouse_pos[0] - circle_pos[0], mouse_pos[1] - circle_pos[1])
    return distance <= 50

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if check_collision():
                    score += 1
                    circle_pos = [
                        random.randint(50, 750),
                        random.randint(50, 550),
                    ]  # Move circle to a random position inside the window

    score_surface = font.render(f"score: {score}", True, (black := (0, 0, 0)))
    screen.fill((173, 216, 230))  # Light blue color
    pygame.draw.circle(screen, (255, 0, 0), circle_pos, 50)  # Red circle at current position
    screen.blit(score_surface, (10, 10))
    pygame.display.update()