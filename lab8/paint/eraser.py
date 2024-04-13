import pygame
import sys

pygame.init()

WIDTH = 960
HEIGHT = 640

# color palette
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect_pos = [300, 200, 150, 90]


done = False

LMBpressed = False

prevX = 0
prevY = 0

currX = 0
currY = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True

        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            LMBpressed = False

    if LMBpressed:
        
        pygame.draw.line(screen, colorBLACK, (prevX, prevY), (currX, currY))
       
    prevX = currX
    prevY = currY
    
    pygame.draw.rect(screen, colorRED, rect_pos)

    pygame.display.flip()