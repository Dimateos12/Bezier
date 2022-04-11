# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:16:24 2022

@author: Mateusz Jabłoński
"""

# p0 p1 p2 p3 -> pozycje[]
# t - parametry

import pygame
import time

pygame.init()
pygame.display.set_caption(" Krzywe Beziera ")

screenSize = (800, 900)

screen = pygame.display.set_mode(screenSize)

x, y = 500.0, 500.0
width, height = 70, 70
speed = 0.001

path_positions = {1: [(167, 312), (158, 324), (292, 137), (283, 149)],
                  2: [(283, 149), (273, 138), (347, 305), (337, 294)],
                  3: [(337, 294), (328, 306), (450, 142), (441, 154 )],
                  4: [(441, 154), (440, 139), (441, 330), (440, 315)],
                  5: [(479, 146), (464, 147), (582, 144), (567, 145)],
                  6: [(567, 145), (566, 130), (568, 332), (567, 317)],
                  7: [(567, 317), (552, 318), (556, 389), (479, 309)]
                  }

screen.fill((0, 0, 0))


def rysowanie(path_positions):
    t = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runnning = False

        t = 0

        P0 = path_positions[0]
        P1 = path_positions[1]
        P2 = path_positions[2]
        P3 = path_positions[3]

        while t < 1:
            t += speed

            P0_x = pow((1 - t), 3) * P0[0]
            P0_y = pow((1 - t), 3) * P0[1]

            P1_x = 3 * pow((1 - t), 2) * t * P1[0]
            P1_y = 3 * pow((1 - t), 2) * t * P1[1]

            P2_x = 3 * (1 - t) * pow(t, 2) * P2[0]
            P2_y = 3 * (1 - t) * pow(t, 2) * P2[1]

            P3_x = pow(t, 3) * P3[0]
            P3_y = pow(t, 3) * P3[1]

            formular = ((P0_x + P1_x + P2_x + P3_x), (P0_y + P3_y + P2_y + P1_y))
            x, y = formular

            pygame.draw.circle(screen, (255, 255, 255), (round(x), round(y)), 16)
            pygame.display.update()
        running = False


for my_var in path_positions:
    rysowanie(path_positions[my_var])


time.sleep(3)