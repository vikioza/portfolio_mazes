from maze import *
from maze_viz import *
from maze_solver import *
from time import sleep

ROWS = 20
COLUMNS = 20
TIMEOUT = 1


def main():
	maze = Maze(ROWS, COLUMNS)
	tiles, row_size, col_size = maze.get_details()[:3]

	drawer = MazeViz(row_size, col_size)
	solver = Solver

	run = True
	while run:
		drawer.draw_maze(tiles)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		sleep(TIMEOUT)

	pygame.quit()


if __name__ == "__main__":
	main()
