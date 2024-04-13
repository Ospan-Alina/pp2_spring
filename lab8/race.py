import pygame
import sys
from random import randint
from time import sleep

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = pygame.image.load("C:/Users/proim/Downloads/pp2_spring/lab8/race_image/AnimatedStreet.png")

# color palette
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

done = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/proim/Downloads/pp2_spring/lab8/race_image/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/proim/Downloads/pp2_spring/lab8/race_image/Enemy (1).png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(0 + self.rect.w // 2 , WIDTH - self.rect.w // 2), 20)
        self.speed = 5

    def move(self):
        self.rect.move_ip(0, self.speed)
        # Three ways to do the same thing:
        # if self.rect[1] + self.rect[3] > HEIGHT:
        #     self.rect.center = (WIDTH // 2, 40)
        # if self.rect[1] + self.rect[3] > HEIGHT:
        #     self.rect.center = (WIDTH // 2, 40)
        if self.rect.bottom > HEIGHT:
            self.rect.center = (randint(0 + self.rect.w // 2 , WIDTH - self.rect.w // 2), 20)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

enemies.add(E1)
all_sprites.add(P1, E1)

FPS = 60

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            E1.speed += 1

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        print("Collision!")
        screen.fill(colorRED)
        pygame.display.flip()
        sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.flip()

    clock.tick(FPS)

# Removing the event from the timer
pygame.time.set_timer(INC_SPEED, 0)