#!/usr/bin/env python
import pygame
import sys
from pygame.locals import *  # to get inputs from keyboard
import time
import random
import Aliens
import Spaceship
import Bullet1
import Bullet2

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Space Invaders')
pygame.mouse.set_visible(0)

spaceship = pygame.image.load("spaceship.jpg")
alien = pygame.image.load("alien.jpg")
lightsaber = pygame.image.load("lightsaber.jpg")
arpita = pygame.image.load("arpita.jpg")
ball = pygame.image.load("ball.jpg")

height = screen.get_height() - 80
width = screen.get_width() - 80

x = width
y = height

screen.fill((255, 255, 255))
x_change = 0
over = False

timespawn = 10000
timedisappear = 8000
time_bullet = 500


def update():
    global numa
    flag = 0
    if numa != 16:
        i = Aliens.Aliens(
            random.choice(xnos),
            random.choice(ynos),
            pygame.time.get_ticks(),
            screen,
            arpita,
            alien)

        for j in list(aliens):
            if j.x == i.x and j.y == i.y:
                flag = 1
                break

        if flag == 1:
            update()

        elif flag == 0:
            aliens.append(i)
            numa += 1
    else:
        return


score = 0
sc = pygame.font.SysFont('Comics Sans MS', 60)
marks = sc.render("SCORE:" + " " + str(score), False, [0, 0, 0])

xnos = []
lol = 0
while lol < width:
    xnos.append(lol)
    lol += 80

ynos = []
ynos.append(0)
ynos.append(80)

aliens = []
numa = 1

bullet1 = []
number1 = 0

bullet2 = []
number2 = 0

score = 0

for i in range(numa):
    i = Aliens.Aliens(random.choice(xnos), random.choice(
        ynos), pygame.time.get_ticks(), screen, arpita, alien)
    aliens.append(i)

start = pygame.time.get_ticks()

obj_ship = Spaceship.Spaceship(x, y, spaceship, screen)
obj_ship.ship()
screen.blit(marks, (220, 320))

while not over:  # game loop

    finish = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_d:
                x_change = 80
            if event.key == pygame.K_a:
                x_change = -80
            if event.key == pygame.K_SPACE:
                number1 += 1
                obj_bullet1 = Bullet1.Bullet1(
                    x, y - 80, pygame.time.get_ticks(), screen, lightsaber)
                bullet1.append(obj_bullet1)

            if event.key == pygame.K_s:
                number2 += 1
                obj_bullet2 = Bullet2.Bullet2(
                    x, y - 80, pygame.time.get_ticks(), screen, ball)
                bullet2.append(obj_bullet2)

        if event.type == pygame.KEYUP:
            x_change = 0
        x += x_change

        if x > width or x < 0:
            x -= x_change

    screen.fill((255, 255, 255))

    if finish - start >= timespawn:
        update()
        start = pygame.time.get_ticks()

    for i in list(aliens):
        if i.new:
            i.spawn()
        else:
            i.spawn_again()

    for i in list(aliens):
        if pygame.time.get_ticks() - i.time >= timedisappear:
            aliens.remove(i)
            numa -= 1

    for i in list(bullet1):
        i.fire()
        if finish - i.time >= time_bullet:
            i.y -= 80
            # i.fire()
            i.time = pygame.time.get_ticks()
            if(i.y < 0):
                bullet1.remove(i)

    for i in list(bullet2):
        i.fire()
        if finish - i.time >= 250:
            i.y -= 80
            i.time = pygame.time.get_ticks()
            if(i.y < 0):
                bullet2.remove(i)

    for i in list(aliens):
        for j in list(bullet1):
            if(i.x == j.x and i.y == j.y):
                number1 -= 1
                numa -= 1
                bullet1.remove(j)
                aliens.remove(i)
                score += 1

        for j in list(bullet2):
            if(i.x == j.x and i.y == j.y):
                bullet2.remove(j)
                number2 -= 1
                i.time += 5000
                i.new = False
                i.spawn_again()

    obj_ship = Spaceship.Spaceship(x, y, spaceship, screen)
    obj_ship.ship()
    marks = sc.render("SCORE:" + " " + str(score), False, [0, 0, 0])
    screen.blit(marks, (220, 320))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
