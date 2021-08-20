from maze_gen import *
from maze_viz import *
from maze_solver import *
from time import sleep

ROWS = 50
COLUMNS = 50
TIMEOUT = 1


def main():
	gen = Generator()
	gen.init_maze(rows=ROWS, columns=COLUMNS)

	solver = Solver
	run = True
	while run:
		draw(gen.row_size, gen.col_size, gen.maze)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		sleep(TIMEOUT)

	pygame.quit()


main()
