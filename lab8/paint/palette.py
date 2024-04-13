import pygame
pygame.init()

fps = 120
timer = pygame.time.Clock()
W = 800
H = 600
active_size = 0
active_color = 'white'
painting = []

screen = pygame.display.set_mode([W, H])
pygame.display.set_caption('Paint')


def draw_menu():
    pygame.draw.rect(screen, 'antiquewhite2', [0, 0, W, 70])
    pygame.draw.line(screen, 'bisque4', (0, 70), (W, 70), 2)
    xl_brush = pygame.draw.rect(screen, 'bisque4', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35,35), 20)
    l_brush = pygame.draw.rect(screen, 'bisque4', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95,35), 15)
    m_brush = pygame.draw.rect(screen, 'bisque4', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155,35), 10)
    s_brush = pygame.draw.rect(screen, 'bisque4', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215,35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    
    cadetblue = pygame.draw.rect(screen, 'cadetblue', [W - 35, 10 , 25, 25])
    orangered2 = pygame.draw.rect(screen, 'orangered2', [W - 35, 35 , 25, 25])
    plum2 = pygame.draw.rect(screen, 'plum2', [W - 60, 35, 25, 25])
    seagreen4 = pygame.draw.rect(screen, 'seagreen4', [W - 60, 10 , 25, 25])
    white = pygame.draw.rect(screen, 'white', [W - 85, 10 , 25, 25])
    black = pygame.draw.rect(screen, 'black', [W - 85, 35, 25, 25])
    colors_list = [cadetblue, orangered2, plum2, seagreen4, white, black]
    rgb_list = ['cadetblue', 'orangered2', 'plum2', 'seagreen4', 'white', 'black']
    return brush_list, colors_list, rgb_list

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])
        
run = True    
while run:
    timer.tick(fps) 
    screen.fill('white')
    mouse = pygame.mouse.get_pos()

    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))
    draw_painting(painting)
    
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    
    brushes, colors, rgbs = draw_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
                
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]
    
    
        
    pygame.display.flip()
pygame.quit()