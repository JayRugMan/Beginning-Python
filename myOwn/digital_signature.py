#!/usr/bin/python3

import pygame

pygame.init()

screen_width = 500
screen_height = 300
pi = 3.1415926535846
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
window = pygame.display.set_mode([screen_width, screen_height])

window.fill(white)

##JH pygame.draw.rect(window, green, [25, 150, 66, 100])
## J
pygame.draw.line(window, black, (50, 20), (175, 20), 4)
pygame.draw.line(window, black, (112, 20), (112, 200), 4)
pygame.draw.arc(window, black, [51, 150, 64, 100], pi, 0, 4)

## R
pygame.draw.line(window, black, (200, 20), (200, 250), 4)
pygame.draw.line(window, black, (200, 20), (230, 20), 4)
pygame.draw.line(window, black, (200, 135), (230, 135), 4)
pygame.draw.arc(window, black, [167, 19, 128, 119], (pi*1.5), (pi/2), 4)
pygame.draw.line(window, black, (230, 135), (300, 250), 4)

## H
pygame.draw.line(window, black, (325, 20), (325, 250), 4)
pygame.draw.line(window, black, (325, 135), (425, 135), 4)
pygame.draw.line(window, black, (425, 20), (425, 250), 4)

pygame.display.flip()
input("press enter to quit ")
