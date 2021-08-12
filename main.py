from maze_gen import *
from maze_viz import *
from time import sleep


def main():
	gen = Generator(rows=100, columns=100)
	run = True
	while run:
		draw(gen.row_size, gen.col_size, gen.maze)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		sleep(TIMEOUT)

	pygame.quit()


main()
