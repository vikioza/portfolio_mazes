from random import choice, sample
from tile import *


class Maze:
	"""ToDo description"""
	row_size: int
	col_size: int
	tiles: list
	first: int
	last: int

	def __init__(self, /, rows: int = 10, columns: int = 10, algo='iter-back'):
		self.row_size: int = columns
		self.col_size: int = rows
		self.tiles: list = []

		self.tiles = [Tile() for _ in range(self.col_size * self.row_size)]

		self.first, self.last = 0, 0
		if algo == 'iter-back':
			self.first, self.last = self._iterative_backtracking()
			self.clear_visited()

	def get_details(self):
		return self.tiles, self.row_size, self.col_size, self.first, self.last

	def print_maze(self, /, index=False):
		"""
		Prints to console a text-based maze. Each tile is represented by its numerical state.
		Optionally, can print out indices instead of the numerical representations.
		Used for testing and debugging purposes.
		"""
		if index:
			self._print_indexes()
			return

		print()
		for row in range(self.col_size):
			line = []
			for row_tile in range(self.row_size):
				line.append(self.tiles[row * self.row_size + row_tile].get_state())
			print(line)

	def _print_indexes(self):
		"""Prints to console a text-based maze of tiles, represented by their indices."""
		margin = len(str(self.row_size * self.col_size))

		for row in range(self.col_size):
			line = []
			for row_tile in range(self.row_size):
				line.append(f"{row * self.row_size + row_tile:{margin}d}")
			print(line)

	def print_cell_state_by_coords(self, row, row_tile):
		self._print_cell_state(row * self.row_size + row_tile)

	def print_cell_state_by_index(self, index):
		self._print_cell_state(index)

	def _print_cell_state(self, index):
		margin = 8
		print(f"self index: {index:>{margin}d}")
		print(f"row:        {get_row(index, self.row_size):>{margin}d}")
		print(f"column:     {get_column(index, self.row_size):>{margin}d}")
		print(f"self state: {self.tiles[index].get_state():08b}")
		print(f"top:        {self.tiles[index].has_top():>{margin}d}")
		print(f"right:      {self.tiles[index].has_right():>{margin}d}")
		print(f"bottom:     {self.tiles[index].has_bottom():>{margin}d}")
		print(f"left:       {self.tiles[index].has_left():>{margin}d}")

	def _iterative_backtracking(self):
		self.first, self.last = self._choose_exits()
		stack = [self.first]
		self.tiles[self.first].mark_visited()

		while len(stack) > 0:
			current = stack.pop(-1)
			neighbors = self.unvisited_neighbors(current)
			if len(neighbors) == 0:
				continue
			stack.append(current)
			next_cell = choice(neighbors)
			self._remove_walls(current, next_cell)
			self.tiles[next_cell].mark_visited()
			stack.append(next_cell)

		return self.first, self.last

	def _choose_exits(self):
		""" Randomly selects 2 cells from the maze's periphery and removes their outside walls """

		candidates = self._select_candidates()
		self.first, self.last = sample(candidates, 2)
		self.tiles[self.first].mark_entrance()
		self.tiles[self.last].mark_exit()

		self._remove_exit_wall(self.first)
		self._remove_exit_wall(self.last)

		return self.first, self.last

	def _select_candidates(self, /, finish=False):
		""" Returns a list of cells at the periphery of the maze """

		candidates = []
		index = 0
		for row_tile in range(self.row_size):
			candidates.append(index)
			index += 1
		for column_tile in range(self.col_size):
			if column_tile == 0 or column_tile == self.col_size - 1:
				continue
			candidates.append(index)
			index += self.row_size - 1
			candidates.append(index)
			index += 1
		for row_tile in range(self.row_size):
			candidates.append(index)
			index += 1
		return candidates

	def _remove_exit_wall(self, exit_index):
		""" Removes the wall of the exit self, depending on which side of the maze it is located at """
		exit_row = get_row(exit_index, self.row_size)
		exit_col = get_column(exit_index, self.row_size)

		if self._remove_corner_wall(exit_index, exit_row, exit_col):
			return

		if exit_row == 0:
			self.tiles[exit_index].remove_top()
			return

		if exit_col == (self.row_size - 1):
			self.tiles[exit_index].remove_right()
			return

		if exit_row == (self.col_size - 1):
			self.tiles[exit_index].remove_bottom()
			return

		if exit_col == 0:
			self.tiles[exit_index].remove_left()
			return

	def _remove_corner_wall(self, exit_index, exit_row, exit_col):
		""" Checks if exit self is in the corner and if so, randomly removes one of the walls and returns 1 """

		if exit_row == 0 and exit_col == 0:
			walls = (1, 8)
			self.tiles[exit_index].remove_wall(choice(walls))
			return 1

		if exit_row == 0 and exit_col == (self.row_size - 1):
			walls = (1, 2)
			self.tiles[exit_index].remove_wall(choice(walls))
			return 1

		if exit_row == (self.col_size - 1) and exit_col == 0:
			walls = (4, 8)
			self.tiles[exit_index].remove_wall(choice(walls))
			return 1

		if exit_row == (self.col_size - 1) and exit_col == (self.row_size - 1):
			walls = (4, 2)
			self.tiles[exit_index].remove_wall(choice(walls))
			return 1

		return 0

	def _remove_walls(self, current, next_cell):
		""" Removes walls between adjacent cells """
		direction, distance = self._get_direction_and_distance(current, next_cell)

		if direction == 'bottom-right' and distance == 1:
			self.tiles[current].remove_right()
			self.tiles[next_cell].remove_left()

		if direction == 'bottom-right' and distance == self.row_size:
			self.tiles[current].remove_bottom()
			self.tiles[next_cell].remove_top()

		if direction == 'top-left' and distance == 1:
			self.tiles[current].remove_left()
			self.tiles[next_cell].remove_right()

		if direction == 'top-left' and distance == self.row_size:
			self.tiles[current].remove_top()
			self.tiles[next_cell].remove_bottom()

	@staticmethod
	def _get_direction_and_distance(current, next_cell):
		if current < next_cell:
			direction = 'bottom-right'
			distance = next_cell - current
		else:
			direction = 'top-left'
			distance = current - next_cell
		return direction, distance

	def unvisited_neighbors(self, current):
		"""Checks for unvisited neighbors and returns them as a list"""

		neighbors = []

		# top neighbor
		if get_row(current, self.row_size) > 0:  # if tile not on the top border
			n_index = current - self.row_size
			if not self.tiles[n_index].visited():
				neighbors.append(n_index)

		# right neighbor
		if get_column(current, self.row_size) < self.row_size - 1:  # if tile not on the right border
			n_index = current + 1
			if not self.tiles[n_index].visited():
				neighbors.append(n_index)

		# bottom neighbor
		if get_row(current, self.row_size) < self.col_size - 1:  # if tile not on the bottom border
			n_index = current + self.row_size
			if not self.tiles[n_index].visited():
				neighbors.append(n_index)

		# left neighbor
		if get_column(current, self.row_size) > 0:  # if tile not on the left border
			n_index = current - 1
			if not self.tiles[n_index].visited():
				neighbors.append(n_index)

		return neighbors

	def clear_visited(self):
		for tile in self.tiles:
			if tile.visited():
				tile.unmark_visited()
