import pygame
import math
import utils

TIMEOUT = 1
WIDTH = 720
MARGIN = 20
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Algorithm Visualization")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


def draw_walls(win, cell, x, y, tile_size):
	if utils.top(cell):
		pygame.draw.line(win, BLACK, (x, y), (x + tile_size, y))

	if utils.right(cell):
		pygame.draw.line(win, BLACK, (x + tile_size, y), (x + tile_size, y + tile_size))

	if utils.bottom(cell):
		pygame.draw.line(win, BLACK, (x, y + tile_size), (x + tile_size, y + tile_size))

	if utils.left(cell):
		pygame.draw.line(win, BLACK, (x, y), (x, y + tile_size))


def draw(row_size, col_size, maze):
	WIN.fill(GREY)

	print(f"\n\nREFRESH")
	width = WIDTH - MARGIN
	tile_width = width / row_size
	tile_height = width / col_size
	tile_size = min(tile_width, tile_height)
	# print(f"tile_size: {tile_size}")

	for i, tile in enumerate(maze):
		x = utils.get_column(i, row_size) * tile_size + 5
		y = utils.get_row(i, row_size) * tile_size + 5
		# print(f"i: {i}; tile: {tile}; x: {x}; y: {y}; size: {tile_size}")

		if utils.start(tile):
			# print(f"Start coords: [{math.floor(x / tile_size)},{math.floor(y / tile_size)}]")
			pygame.draw.rect(WIN, ORANGE, (x, y, tile_size+1, tile_size+1))
			draw_walls(WIN, tile, x, y, tile_size)
			continue

		if utils.end(tile):
			# print(f"End coords: [{math.floor(x / tile_size)},{math.floor(y / tile_size)}]")
			pygame.draw.rect(WIN, GREEN, (x, y, tile_size, tile_size))
			draw_walls(WIN, tile, x, y, tile_size)
			continue

		pygame.draw.rect(WIN, WHITE, (x, y, tile_size, tile_size))
		draw_walls(WIN, tile, x, y, tile_size)

	pygame.display.update()

