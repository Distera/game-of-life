import pygame
from pygame.locals import *
from tkinter import *


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.visualize_grid(matrix_of_elements)
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_square(self, x, y, color):
        pygame.draw.rect(self.screen, color, [x, y, self.cell_size, self.cell_size])

    def visualize_grid(self, matrix):
        y = 0  # we start at the top of the screen
        for row in matrix:
            x = 0  # for every row we start at the left of the screen again
            for item in row:
                if item == 0:
                    self.create_square(x, y, pygame.Color('white'))
                else:
                    self.create_square(x, y, pygame.Color('green'))

                x += self.cell_size  # for ever item/number in that row we move one "step" to the right
            y += self.cell_size  # for every new row we move one "step" downwards
        pygame.display.update()



if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)

    matrix_of_elements = [[1, 1, 0, 1],
                          [1, 0, 0, 1],
                          [1, 1, 0, 1],
                          [1, 1, 1, 1]]

    game.run()
