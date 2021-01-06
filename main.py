import numpy as np
import pygame
import time
import sys

# Set de size of de window
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Set de tittle of game
pygame.display.set_caption(' Game of Life')

# set color of background, grid and rectangle
bg = 0, 0, 0
grill_color = (181, 184, 178)
rect_color = (106, 13, 173)

# Set size of grid and rectangles
size_grid = (50, 50)
size_rect = (size_grid[0] - 4, size_grid[1] - 4)  # minus 4 for cut the borders

# Set the number of cells of the axes
n_cells_x = int(width / size_grid[0])
n_cells_y = int(height / size_grid[1])

# painting  background
screen.fill(bg)

# 2d matrix, and copy for
matrix_game = np.random.randint(2, size=(n_cells_x, n_cells_y))
copy_matrix = np.copy(matrix_game)
game_state = 0

# print cells
for i in range(n_cells_x):
    for j in range(n_cells_y):
        pygame.draw.rect(screen, grill_color, ((i * size_grid[0], j * size_grid[1]), size_grid), 1)

for ii in range(n_cells_x):
    for jj in range(n_cells_y):
        pos_x_clicked = (jj * size_grid[0]) + 2
        pos_y_clicked = (ii * size_grid[1]) + 2
        coor_cell_pressed = (pos_x_clicked, pos_y_clicked)

        if matrix_game[ii][jj] == 1:
            pygame.draw.rect(screen, rect_color, (coor_cell_pressed, size_rect), 0)
        elif matrix_game[ii][jj] == 0:
            pygame.draw.rect(screen, bg, (coor_cell_pressed, size_rect), 0)

start_game = False

while not start_game:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        while 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            # logical GAME
            matrix_game = np.copy(copy_matrix)

            for ii in range(n_cells_x):
                for jj in range(n_cells_y):
                    pos_x_clicked = (jj * size_grid[0]) + 2
                    pos_y_clicked = (ii * size_grid[1]) + 2
                    coor_cell_pressed = (pos_x_clicked, pos_y_clicked)

                    if matrix_game[ii][jj] == 1:
                        pygame.draw.rect(screen, rect_color, (coor_cell_pressed, size_rect), 0)
                    elif matrix_game[ii][jj] == 0:
                        pygame.draw.rect(screen, bg, (coor_cell_pressed, size_rect), 0)

            time.sleep(0.09)
            for i in range(n_cells_x):
                for j in range(n_cells_y):

                    # Una célula muerta con exactamente 3 células vecinas vivas nace
                    sum_neighbors = (matrix_game[(i % n_cells_x)][(j - 1) % n_cells_y] +
                                     matrix_game[(i % n_cells_x)][(j + 1) % n_cells_y] +
                                     matrix_game[(i - 1) % n_cells_x][j % n_cells_y] +
                                     matrix_game[(i + 1) % n_cells_x][j % n_cells_y] +
                                     matrix_game[(i - 1) % n_cells_x][(j - 1) % n_cells_y] +
                                     matrix_game[(i + 1) % n_cells_x][(j + 1) % n_cells_y] +
                                     matrix_game[(i - 1) % n_cells_x][(j + 1) % n_cells_y] +
                                     matrix_game[(i + 1) % n_cells_x][(j - 1) % n_cells_y
                                                                      ])

                    if matrix_game[i][j] == 0:
                        if sum_neighbors == 3:
                            copy_matrix[i][j] = 1
                    elif matrix_game[i][j] == 1:
                        if sum_neighbors < 2 or sum_neighbors > 3:
                            copy_matrix[i][j] = 0

            pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        click = pygame.mouse.get_pressed()
        if sum(click) >= 1:
            pos_mouse = pygame.mouse.get_pos()
            x = int(pos_mouse[0] / size_grid[0])
            y = int(pos_mouse[1] / size_grid[1])
            pos_x_clicked = (x * size_grid[0]) + 2
            pos_y_clicked = (y * size_grid[1]) + 2
            coor_cell_pressed = (pos_x_clicked, pos_y_clicked)

            if click[0] == 1:  # draw a rectangle
                pygame.draw.rect(screen, rect_color, (coor_cell_pressed, size_rect), 0)
                matrix_game[y][x] = 1
            elif click[2] == 1:  # erase selected rectangle
                pygame.draw.rect(screen, bg, (coor_cell_pressed, size_rect), 0)
                matrix_game[y][x] = 0
            copy_matrix = np.copy(matrix_game)
    pygame.display.flip()
