import utils
import random


class Generator:
	"""
	ToDo description
	"""

	def __init__(self):
		self.row_size = None
		self.col_size = None
		self.maze = None

	def init_maze(self, /, rows: int = 10, columns: int = 10, algo='iter-back'):
		"""

		:param rows:
		:param columns:
		:param algo:
		:return:
		"""
		self.row_size = columns
		self.col_size = rows
		self.maze = []

		for i in range(self.col_size):
			for j in range(self.row_size):
				self.maze.append(0b1111)

		# self.print_maze(index=True)

		first, last = 0, 0
		if algo == 'iter-back':
			first, last = self._iterative_backtracking()

		# self.print_maze()
		return self.maze, self.row_size, self.col_size, first, last

	def print_maze(self, /, index=False):
		if index:
			self._print_indexes()
			return

		print()
		for row in range(self.col_size):
			line = []
			for row_tile in range(self.row_size):
				line.append(self.maze[row * self.row_size + row_tile])
			print(line)

	def print_cell_state_by_coords(self, row, row_tile):
		index = row * self.row_size + row_tile
		self._print_cell_state(index)

	def print_cell_state_by_index(self, index):
		self._print_cell_state(index)

	def _print_indexes(self):
		margin = len(str(self.row_size * self.col_size))

		for row in range(self.col_size):
			line = []
			for row_tile in range(self.row_size):
				line.append(f"{row * self.row_size + row_tile:{margin}d}")
			print(line)

	def _print_cell_state(self, index):
		margin = 8
		print(f"cell index: {index:>{margin}d}")
		print(f"row:        {utils.get_row(index, self.row_size):>{margin}d}")
		print(f"column:     {utils.get_column(index, self.row_size):>{margin}d}")
		print(f"cell state: {self.maze[index]:08b}")
		print(f"top:        {utils.top(self.maze[index]):>{margin}d}")
		print(f"right:      {utils.right(self.maze[index]):>{margin}d}")
		print(f"bottom:     {utils.bottom(self.maze[index]):>{margin}d}")
		print(f"left:       {utils.left(self.maze[index]):>{margin}d}")

	def _iterative_backtracking(self):
		first, last = self._choose_exits()
		stack = [first]
		self.maze[first] = utils.mark_visited(self.maze[first])

		while len(stack) > 0:
			current = stack.pop(-1)
			neighbors = utils.unvisited_neighbors(self, current)
			if len(neighbors) == 0:
				continue
			stack.append(current)
			next_cell = random.choice(neighbors)
			self._remove_walls(current, next_cell)
			self.maze[next_cell] = utils.mark_visited(self.maze[next_cell])
			stack.append(next_cell)

		print("\nChecking first:")
		self.print_cell_state_by_index(first)
		print("\nChecking last:")
		self.print_cell_state_by_index(last)

		return first, last

	def _choose_exits(self):
		""" Randomly selects 2 cells from the maze's periphery and removes their outside walls """

		print("\nRetrieving list of candidates")
		candidates = self._select_candidates()
		print("\nChoosing exits")
		first, last = random.sample(candidates, 2)
		self.maze[first] = utils.mark_entrance(self.maze[first])
		self.maze[last] = utils.mark_exit(self.maze[last])

		print("\nRemoving first exit wall")
		self._remove_exit_wall(first)
		self.print_cell_state_by_index(first)

		print("\nRemoving second exit wall")
		self._remove_exit_wall(last)
		self.print_cell_state_by_index(last)

		return first, last

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
		""" Removes the wall of the exit cell, depending on which side of the maze it is located at """
		exit_row = utils.get_row(exit_index, self.row_size)
		exit_col = utils.get_column(exit_index, self.row_size)

		if self._remove_corner_wall(exit_index, exit_row, exit_col):  # checks if the cell is in a corner
			return

		if exit_row == 0:  # top of the maze
			self.maze[exit_index] -= 1
			return

		if exit_row == (self.col_size - 1):  # bottom of the maze
			self.maze[exit_index] -= 4
			return

		if exit_col == 0:  # left side
			self.maze[exit_index] -= 8
			return

		if exit_col == (self.row_size - 1):  # right side
			self.maze[exit_index] -= 2
			return

	def _remove_corner_wall(self, exit_index, exit_row, exit_col):
		""" Checks if exit cell is in the corner and if so, randomly removes one of the walls and returns 1 """

		if exit_row == 0 and exit_col == 0:
			walls = (1, 8)
			self.maze[exit_index] -= random.choice(walls)
			return 1

		if exit_row == 0 and exit_col == (self.row_size - 1):
			walls = (1, 2)
			self.maze[exit_index] -= random.choice(walls)
			return 1

		if exit_row == (self.col_size - 1) and exit_col == 0:
			walls = (4, 8)
			self.maze[exit_index] -= random.choice(walls)
			return 1

		if exit_row == (self.col_size - 1) and exit_col == (self.row_size - 1):
			walls = (4, 2)
			self.maze[exit_index] -= random.choice(walls)
			return 1

		return 0

	def _remove_walls(self, current, next_cell):
		""" Removes walls between adjacent cells """
		if current < next_cell:
			direction = 'bottom-right'
			wall = next_cell - current
		else:
			direction = 'top-left'
			wall = current - next_cell

		if direction == 'bottom-right' and wall == 1:
			self.maze[current] -= 2
			self.maze[next_cell] -= 8

		if direction == 'bottom-right' and wall == self.row_size:
			self.maze[current] -= 4
			self.maze[next_cell] -= 1

		if direction == 'top-left' and wall == 1:
			self.maze[current] -= 8
			self.maze[next_cell] -= 2

		if direction == 'top-left' and wall == self.row_size:
			self.maze[current] -= 1
			self.maze[next_cell] -= 4
