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

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB was clicked!")
            print(event.pos)
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
            print("LMB was released!")
            print(event.pos)
            LMBPressed = False
            baseLayer.blit(screen, (0, 0))
            currX = event.pos[0]
            currY = event.pos[1]
        
       

    # if LMBPressed:
    #     screen.fill((0, 0, 0))
        
    if LMBPressed:
        screen.blit(baseLayer, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), calculate_rect(prevX, currX, prevY, currY), 2)

    # screen.blit(baseLayer, (0, 0))

    pygame.display.flip()