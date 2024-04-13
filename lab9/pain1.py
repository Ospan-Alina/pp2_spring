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

def calculate_square(x1, x2, y1, y2):
    # Calculate the dimensions of the square based on the smaller of the width and height
    side_length = min(abs(x2 - x1), abs(y2 - y1))
    # Ensure the square is drawn from the top-left corner
    if x2 < x1:
        x1 = x2
    if y2 < y1:
        y1 = y2
    return pygame.Rect(x1, y1, side_length, side_length)

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
        pygame.draw.rect(screen, (255, 0, 0), calculate_square(prevX, currX, prevY, currY), 2)

    pygame.display.flip()
