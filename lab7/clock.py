import pygame as pg 
from datetime import datetime as dt

# pygame initialization
pg.init()
screen = pg.display.set_mode((600, 450))
window_title = pg.display.set_caption("mickey mouse clock")
#icon = pg.display.set_icon(pg.image.load(r"clock_assets/icon.png"))
clock = pg.time.Clock()

# loading the images 
bg_surf = pg.image.load("images/mainclock.png")
leftarm_surf = pg.image.load("images/leftarm.png")
rightarm_surf = pg.image.load("images/rightarm.png")
bg_rect = bg_surf.get_rect(center = (300, 225))

done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    current_time = dt.now().time()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6)

    rotated_leftarm = pg.transform.rotate(leftarm_surf, seconds_angle)
    rotated_rightarm = pg.transform.rotate(rightarm_surf, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center = (340, 250))
    rightarm_rect = rotated_rightarm.get_rect(center = (230,230))

    screen.blit(bg_surf, bg_rect)
    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    pg.display.flip()
    clock.tick(60)
