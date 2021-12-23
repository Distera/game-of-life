import pygame
from copy import deepcopy
from numpy import genfromtxt
import os

tile_size = 20
FPS = 6

current_field = genfromtxt(os.getenv('MAP_PATH', 'maps/map1.csv'), delimiter=',')
tiles_grid_height, tiles_grid_width = current_field.shape
RES = screen_width, screen_height = tiles_grid_width * tile_size, tiles_grid_height * tile_size

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = [[0 for i in range(tiles_grid_width)] for j in range(tiles_grid_height)]


def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0


while True:

    surface.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    [pygame.draw.line(surface, pygame.Color('darkslategray'), (x, 0), (x, screen_height)) for x in range(0, screen_width, tile_size)]
    [pygame.draw.line(surface, pygame.Color('darkslategray'), (0, y), (screen_width, y)) for y in range(0, screen_height, tile_size)]
    # draw life
    for x in range(1, tiles_grid_width - 1):
        for y in range(1, tiles_grid_height - 1):
            if current_field[y][x]:
                pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * tile_size + 2, y * tile_size + 2, tile_size - 2, tile_size - 2))
            next_field[y][x] = check_cell(current_field, x, y)

    current_field = deepcopy(next_field)
    pygame.display.flip()
    clock.tick(FPS)
