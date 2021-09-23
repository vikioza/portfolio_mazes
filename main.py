from maze import *
from maze_viz import *
from maze_solver import *
from time import sleep

ROWS = 50
COLUMNS = 50
TIMEOUT = 1


def main():
	maze = Maze(ROWS, COLUMNS)
	solver = Solver

	tiles, row_size, col_size = maze.get_details()[:3]
	run = True
	while run:
		MazeViz.draw_maze(tiles, row_size, col_size)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		sleep(TIMEOUT)

	pygame.quit()


if __name__ == "__main__":
	main()
