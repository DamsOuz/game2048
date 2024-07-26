from random import randint

import numpy as np

# On initialise le jeu
score = 0
game_matrix = np.empty((4, 4))
init_row_1, init_column_1 = randint(0, len(game_matrix) - 1), randint(0, len(game_matrix) - 1)
init_row_2, init_column_2 = randint(0, len(game_matrix) - 1), randint(0, len(game_matrix) - 1)

# On initialise deux 2 qui sont à des coordonnées distinctes
while (init_row_2 == init_row_1) and (init_column_2 == init_column_1):
    init_row_2, init_column_2 = randint(0, len(game_matrix)), randint(0, len(game_matrix) - 1)

game_matrix[init_row_1, init_column_1] = 2
game_matrix[init_row_2, init_column_2] = 2

print("hello")
