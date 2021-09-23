import pygame
from tile import *


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


class MazeViz:

	@classmethod
	def draw_maze(cls, tiles, row_size, col_size):
		WIN.fill(GREY)
		width = WIDTH - MARGIN
		tile_width = width / row_size
		tile_height = width / col_size
		tile_size = min(tile_width, tile_height)

		cls.draw_tiles(tiles, row_size, tile_size)
		pygame.display.update()

	@classmethod
	def draw_tiles(cls, tiles, row_size, tile_size):
		for i, tile in enumerate(tiles):
			x = get_column(i, row_size) * tile_size + 5
			y = get_row(i, row_size) * tile_size + 5
			cls.draw_tile(tile, x, y, tile_size)

	@classmethod
	def draw_tile(cls, tile: Tile, x: int, y: int, tile_size: int):
		if tile.entrance_tile():
			cls.draw_entrance(tile, x, y, tile_size)
			return

		if tile.exit_tile():
			cls.draw_exit(tile, x, y, tile_size)
			return

		cls.draw_hallway(tile, x, y, tile_size)

	@classmethod
	def draw_entrance(cls, tile: Tile, x: int, y: int, tile_size: int):
		pygame.draw.rect(WIN, ORANGE, (x + 1, y + 1, tile_size - 1, tile_size - 1))
		cls.draw_walls(WIN, tile, x, y, tile_size)

	@classmethod
	def draw_exit(cls, tile: Tile, x: int, y: int, tile_size: int):
		pygame.draw.rect(WIN, GREEN, (x + 1, y + 1, tile_size - 1, tile_size - 1))
		cls.draw_walls(WIN, tile, x, y, tile_size)

	@classmethod
	def draw_hallway(cls, tile: Tile, x: int, y: int, tile_size: int):
		pygame.draw.rect(WIN, WHITE, (x, y, tile_size, tile_size))
		cls.draw_walls(WIN, tile, x, y, tile_size)

	@classmethod
	def draw_visited(cls, tile: Tile, x: int, y: int, tile_size: int):
		pygame.draw.rect(WIN, TURQUOISE, (x, y, tile_size, tile_size))
		cls.draw_walls(WIN, tile, x, y, tile_size)

	@classmethod
	def draw_best(cls, tile: Tile, x: int, y: int, tile_size: int):
		pygame.draw.rect(WIN, PURPLE, (x, y, tile_size, tile_size))
		cls.draw_walls(WIN, tile, x, y, tile_size)

	@classmethod
	def draw_current(cls, tile: Tile, x: int, y: int, tile_size: int):
		pygame.draw.rect(WIN, YELLOW, (x, y, tile_size, tile_size))
		cls.draw_walls(WIN, tile, x, y, tile_size)

	@staticmethod
	def draw_walls(win, tile, x, y, tile_size):
		if tile.has_top():
			pygame.draw.line(win, BLACK, (x, y), (x + tile_size, y))
		if tile.has_right():
			pygame.draw.line(win, BLACK, (x + tile_size, y), (x + tile_size, y + tile_size))
		if tile.has_bottom():
			pygame.draw.line(win, BLACK, (x, y + tile_size), (x + tile_size, y + tile_size))
		if tile.has_left():
			pygame.draw.line(win, BLACK, (x, y), (x, y + tile_size))
