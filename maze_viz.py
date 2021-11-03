import pygame
from tile import *
from math import ceil

WIDTH = 720
BORDER_MARGIN = 20
MAZE_MARGIN = 5
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
	row_size: int
	col_size: int
	tile_size: int

	def __init__(self, row_size, col_size):
		WIN.fill(GREY)
		width = WIDTH - BORDER_MARGIN
		self.row_size = row_size
		self.col_size = col_size
		tile_width = width / self.row_size
		tile_height = width / self.col_size
		self.tile_size = ceil(min(tile_width, tile_height))

	def draw_maze(self, tiles):
		self._draw_tiles(tiles)
		pygame.display.update()

	def _draw_tiles(self, tiles):
		for i, tile in enumerate(tiles):
			x, y = self.get_coords(i)
			self.draw_tile(tile, x, y)

	def draw_tile(self, tile: Tile, x: int, y: int):
		if tile.entrance_tile():
			self._draw_entrance(tile, x, y)
			return

		if tile.exit_tile():
			self._draw_exit(tile, x, y)
			return

		if tile.visited():
			self.draw_visited(tile, x, y)
			return

		self._draw_hallway(tile, x, y)

	def _draw_entrance(self, tile: Tile, x: int, y: int):
		pygame.draw.rect(WIN, ORANGE, (x + 1, y + 1, self.tile_size - 1, self.tile_size - 1))
		self._draw_walls(WIN, tile, x, y)

	def _draw_exit(self, tile: Tile, x: int, y: int):
		pygame.draw.rect(WIN, GREEN, (x + 1, y + 1, self.tile_size - 1, self.tile_size - 1))
		self._draw_walls(WIN, tile, x, y)

	def _draw_hallway(self, tile: Tile, x: int, y: int):
		pygame.draw.rect(WIN, WHITE, (x, y, self.tile_size, self.tile_size))
		self._draw_walls(WIN, tile, x, y)

	def draw_visited(self, tile: Tile, x: int, y: int):
		pygame.draw.rect(WIN, TURQUOISE, (x, y, self.tile_size, self.tile_size))
		self._draw_walls(WIN, tile, x, y)

	def draw_best(self, tile: Tile, x: int, y: int):
		pygame.draw.rect(WIN, PURPLE, (x, y, self.tile_size, self.tile_size))
		self._draw_walls(WIN, tile, x, y)

	def draw_current(self, tile: Tile, x: int, y: int):
		pygame.draw.rect(WIN, YELLOW, (x, y, self.tile_size, self.tile_size))
		self._draw_walls(WIN, tile, x, y)

	def _draw_walls(self, win, tile, x, y):
		if tile.has_top():
			pygame.draw.line(win, BLACK, (x, y), (x + self.tile_size, y))
		if tile.has_right():
			pygame.draw.line(win, BLACK, (x + self.tile_size, y), (x + self.tile_size, y + self.tile_size))
		if tile.has_bottom():
			pygame.draw.line(win, BLACK, (x, y + self.tile_size), (x + self.tile_size, y + self.tile_size))
		if tile.has_left():
			pygame.draw.line(win, BLACK, (x, y), (x, y + self.tile_size))

	def get_coords(self, index):
		x = get_column(index, self.row_size) * self.tile_size + MAZE_MARGIN
		y = get_row(index, self.row_size) * self.tile_size + MAZE_MARGIN
		return x, y
