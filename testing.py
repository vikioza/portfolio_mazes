"""ToDo testing for tile, maze, solver (after it's done)"""
import unittest
from maze import *

ROWS = 20
COLUMNS = 20


class MyTestCase(unittest.TestCase):

	# --------------- Tile Tests --------------- #
	def test_tile(self):
		tile = Tile()
		self.assertEqual(tile.get_state(), 0b1111)

	def test_tile_top(self):
		tile = Tile()
		self.assertTrue(tile.has_top(), 1)

		tile.remove_top()
		self.assertFalse(tile.has_top(), 1)

	def test_tile_right(self):
		tile = Tile()
		self.assertTrue(tile.has_right(), 1)

		tile.remove_right()
		self.assertFalse(tile.has_right(), 1)

	def test_tile_bottom(self):
		tile = Tile()
		self.assertTrue(tile.has_bottom(), 1)

		tile.remove_bottom()
		self.assertFalse(tile.has_bottom(), 1)

	def test_tile_left(self):
		tile = Tile()
		self.assertTrue(tile.has_left(), 1)

		tile.remove_left()
		self.assertFalse(tile.has_left(), 1)

	def test_tile_visited(self):
		tile = Tile()
		self.assertFalse(tile.visited(), 1)

		tile.mark_visited()
		self.assertTrue(tile.visited(), 1)

		tile.unmark_visited()
		self.assertFalse(tile.visited(), 1)

	def test_tile_entrance(self):
		tile = Tile()
		self.assertFalse(tile.entrance_tile(), 1)

		tile.mark_entrance()
		self.assertTrue(tile.entrance_tile(), 1)

	def test_tile_exit(self):
		tile = Tile()
		self.assertFalse(tile.exit_tile(), 1)

		tile.mark_exit()
		self.assertTrue(tile.exit_tile(), 1)

	# --------------- Maze Tests --------------- #
	def test_maze(self):
		maze = Maze(ROWS, COLUMNS)
		tiles, row_size, col_size, first, last = maze.get_details()
		self.assertEqual(row_size, COLUMNS)
		self.assertEqual(col_size, ROWS)
		self.assertEqual(len(tiles), ROWS*COLUMNS)
		self.assertTrue(maze.tiles[first].entrance_tile(), 1)
		self.assertTrue(maze.tiles[last].exit_tile(), 1)




