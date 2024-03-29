import ctypes
from math import ceil
from time import sleep

import pygame

user32 = ctypes.windll.user32
WINDOW_SIZE = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
HMID = WINDOW_SIZE[0] // 2

clock = pygame.time.Clock()

pygame.font.init()

MODULO = 3

finished = False
display = pygame.display.set_mode(WINDOW_SIZE)

BLACK = (153, 188, 133)
COLOR_LIST = [(153, 188, 133), (176, 87, 141), (93, 53, 135)]

triangle = [[1]]

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    display.fill(BLACK)

    SQUARE_SIZE = WINDOW_SIZE[1] / len(triangle)

    for row_index, row in enumerate(triangle):
        for col_index, col in enumerate(row):
            pygame.draw.rect(display, COLOR_LIST[triangle[row_index][col_index] % MODULO], (
                ceil(HMID - (col_index - len(row) // 2) * SQUARE_SIZE - (SQUARE_SIZE / 2) * (row_index % 2 + 1)),
                ceil(row_index * SQUARE_SIZE),
                ceil(SQUARE_SIZE),
                ceil(SQUARE_SIZE)
            ))

    triangle.append([1] + [triangle[-1][i] + triangle[-1][i + 1] for i in range(len(triangle[-1]) - 1)] + [1])
    sleep(0.02)

    pygame.display.update()
