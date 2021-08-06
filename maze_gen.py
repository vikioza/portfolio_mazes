import utils
import random


class Generator:
	"""
	ToDo description
	"""

	def __init__(self, /, rows: int = 10, columns: int = 10, algo='iter-back'):
		self.row_size = None
		self.col_size = None
		self.maze = []
		self.init_maze(rows, columns, algo)

	def init_maze(self, /, rows: int = 10, columns: int = 10, algo='iter-back'):
		self.row_size = columns
		self.col_size = rows

		for i in range(self.col_size):
			for j in range(self.row_size):
				self.maze.append(0b1111)

		self.print_maze(index=True)
		self._iterative_backtracking()
		self.print_maze()

	def print_cell_state_by_coords(self, row, row_tile):
		index = row * self.row_size + row_tile
		self._print_cell_state(index)

	def print_cell_state_by_index(self, index):
		self._print_cell_state(index)

	def print_maze(self, /, index=False):
		if index:
			self._print_indexes()
			return

		for row in range(self.col_size):
			line = []
			for row_tile in range(self.row_size):
				line.append(self.maze[row * self.row_size + row_tile])
			print(line)

	def _print_indexes(self):
		margin = len(str(self.row_size * self.col_size))

		for row in range(self.col_size):
			line = []
			for row_tile in range(self.row_size):
				line.append(f"{row * self.row_size + row_tile:{margin}d}")
			print(line)

	def _print_cell_state(self, index):
		margin = 4
		print(f"cell index: {index:>4d}")
		print(f"row:        {utils.get_row(index, self.row_size):>{margin}d}")
		print(f"column:     {utils.get_column(index, self.row_size):>4d}")
		print(f"cell state: {self.maze[index]:04b}")
		print(f"top:        {utils.top(self.maze[index]):>4d}")
		print(f"right:      {utils.right(self.maze[index]):>4d}")
		print(f"bottom:     {utils.bottom(self.maze[index]):>4d}")
		print(f"left:       {utils.left(self.maze[index]):>4d}")

	def _iterative_backtracking(self):
		first, last = self._choose_exits()
		stack = [first]
		self.maze[first] = utils.mark_visited(self.maze[first])

		while len(stack) > 0:
			current = stack.pop(-1)
			neighbors = self._unvisited_neighbors(current)
			if len(neighbors) == 0:
				continue
			stack.append(current)
			next_cell = random.choice(neighbors)
			self._remove_walls(current, next_cell)
			self.maze[next_cell] = utils.mark_visited(self.maze[next_cell])
			stack.append(next_cell)

	def _choose_exits(self):
		print("\nRetrieving list of candidates")
		candidates = self._select_candidates()
		print("\nChoosing exits")
		first, last = random.sample(candidates, 2)

		print("\nRemoving first exit wall")
		self._remove_exit_wall(first)
		self.print_cell_state_by_index(first)

		print("\nRemoving second exit wall")
		self._remove_exit_wall(last)
		self.print_cell_state_by_index(last)

		return first, last

	def _select_candidates(self, /, finish=False):
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
		exit_row = utils.get_row(exit_index, self.row_size)
		exit_col = utils.get_column(exit_index, self.row_size)

		if self._remove_corner_wall(exit_index, exit_row, exit_col):
			return

		if exit_row == 0:
			self.maze[exit_index] -= 1
			return

		if exit_row == (self.col_size - 1):
			self.maze[exit_index] -= 4
			return

		if exit_col == 0:
			self.maze[exit_index] -= 8
			return

		if exit_col == (self.row_size - 1):
			self.maze[exit_index] -= 2
			return

	def _remove_corner_wall(self, exit_index, exit_row, exit_col):
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

	def _unvisited_neighbors(self, index):
		neighbors = []

		if utils.get_row(index, self.row_size) > 0:
			n_index = index - self.row_size
			if not utils.visited(self.maze[n_index]):
				neighbors.append(n_index)

		if utils.get_column(index, self.row_size) < self.row_size - 1:
			n_index = index + 1
			if not utils.visited(self.maze[n_index]):
				neighbors.append(n_index)

		if utils.get_row(index, self.row_size) < self.col_size - 1:
			n_index = index + self.row_size
			if not utils.visited(self.maze[n_index]):
				neighbors.append(n_index)

		if utils.get_column(index, self.row_size) > 0:
			n_index = index - 1
			if not utils.visited(self.maze[n_index]):
				neighbors.append(n_index)

		return neighbors

	def _remove_walls(self, current, next_cell):
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
