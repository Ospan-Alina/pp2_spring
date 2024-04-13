import pygame
import sys
import random 

pygame.init()

class Snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((W//2), (H//2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self. color = green
    
    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
            
    def move(self):
        current = self.get_head_position()
        x, y = self.direction
        new = (((current[0] + (x * Grid_SIZE)) % W), (current[1] + (y * Grid_SIZE)) % H)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
                
    def reset(self):
        self.length = 1
        self.positions = [((W // 2), (H // 2))]
        self.direction = random.choice([UP, DOWN , LEFT, RIGHT])
        
    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect((pos[0], pos[1]), (Grid_SIZE, Grid_SIZE))
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, 'black', rect, 1)
                
                
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
            
    
class Food(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = 'red'
        self.rand()
        
    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (Grid_SIZE, Grid_SIZE))
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, 'black', rect, 1)
        
        
        
    def rand(self):
        self.position = (random.randint(0, Grid_WIDTH - 1) * Grid_SIZE, random.randint (0, Grid_HEIGHT - 1) * Grid_SIZE)


def drawGrid(surface):
    for y in range(0, int(Grid_HEIGHT)):
        for x in range (0, int(Grid_WIDTH)):
            if ((x + y) % 2) == 0:
                rect = pygame.Rect((x * Grid_SIZE, y * Grid_SIZE), (Grid_SIZE, Grid_SIZE))
                pygame.draw.rect(surface, gray1, rect)
            else:
                rect = pygame.Rect((x * Grid_SIZE, y * Grid_SIZE), (Grid_SIZE, Grid_SIZE))
                pygame.draw.rect(surface, gray2, rect)

W = 480
H = 480
Grid_SIZE = 20
Grid_WIDTH = W // Grid_SIZE
Grid_HEIGHT = H // Grid_SIZE
gray1 = (120, 120, 120)
gray2 = (170, 170, 170)
green = (0 , 255, 0)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
font = pygame.font.Font('Pixeltype.ttf', 30)

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((W, H), 0, 32)
    
    
    surface = pygame.Surface(screen.get_size())
    
    
    drawGrid(surface)
    
    snake = Snake()
    food = Food()
    
    score = 0
    while True:
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.rand()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = font.render('Score {0}'.format(score), True, 'black')
        screen.blit(text, (5, 10))
                
        pygame.display.update()
             
main()