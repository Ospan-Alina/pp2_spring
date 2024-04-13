import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))

done = False

prevX = -1
prevY = -1
currX = -1
currY = -1

LMBPressed = False

def calculate_equilateral_triangle(x1, x2, y1, y2):
    # Calculate the center of the equilateral triangle
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    # Calculate the distance from the center to one of the vertices
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 2
    # Calculate the height of the equilateral triangle
    height = distance * math.sqrt(3)
    # Calculate the vertices of the equilateral triangle
    v1 = (center_x, center_y - distance)
    v2 = (center_x + (height / math.sqrt(3)), center_y + distance / 2)
    v3 = (center_x - (height / math.sqrt(3)), center_y + distance / 2)
    return [v1, v2, v3]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBPressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBPressed:
                currX = event.pos[0]
                currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBPressed = False
            baseLayer.blit(screen, (0, 0))
            currX = event.pos[0]
            currY = event.pos[1]
        
    if LMBPressed:
        screen.blit(baseLayer, (0, 0))
        pygame.draw.polygon(screen, (255, 0, 0), calculate_equilateral_triangle(prevX, currX, prevY, currY), 2)

    pygame.display.flip()
