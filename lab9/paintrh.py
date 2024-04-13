import pygame

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

def calculate_rhombus(x1, x2, y1, y2):
    # Calculate the center of the rhombus
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    # Calculate the half-width and half-height of the rhombus
    half_width = abs(x2 - x1) // 2
    half_height = abs(y2 - y1) // 2
    # Define the vertices of the rhombus
    vertices = [(center_x, y1), (x2, center_y), (center_x, y2), (x1, center_y)]
    return vertices

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
        pygame.draw.polygon(screen, (255, 0, 0), calculate_rhombus(prevX, currX, prevY, currY), 2)

    pygame.display.flip()
