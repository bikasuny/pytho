import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((200, 100))
pygame.display.set_caption("My Game")

sky_surface = pygame.image.load('graphics/sky.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(sky_surface, (0, 0))
   
    pygame.display.update()
    clock.tick(60)