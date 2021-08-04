import utils


class Generator:
	"""
	ToDo description
	"""
	def __init__(self, /, rows: int = 10, columns: int = 10, algo='iter-back'):
		self.row_size = columns
		self.col_size = rows
		self.maze = []
		self.init_maze()
		self.print_maze(index=True)
		self.print_cell_state(0, 0)
		self.select_candidates()

	def init_maze(self):
		for i in range(self.col_size):
			for j in range(self.row_size):
				self.maze.append(0b1111)

	def print_maze(self, /, index=False):
		if index:
			self.print_indexes()
			return

		for row in range(self.col_size):
			line = []
			for row_tile in range(self.row_size):
				line.append(self.maze[row * self.row_size + row_tile])
			print(line)

	def print_indexes(self):
		for row in range(self.col_size):
			line = []
			for row_tile in range(self.row_size):
				line.append(row * self.row_size + row_tile)
			print(line)

	def print_cell_state(self, row, row_tile):
		index = row * self.row_size + row_tile
		print(f"cell state: {self.maze[index]:04b}")
		print(f"top: {utils.top(self.maze[index])}")
		print(f"right: {utils.right(self.maze[index])}")
		print(f"bottom: {utils.bottom(self.maze[index])}")
		print(f"left: {utils.left(self.maze[index])}")

	def choose_first_cell(self):
		pass

	def select_candidates(self, /, finish=False):
		candidates = []
		index = 0
		for row_tile in range(self.row_size):
			candidates.append(index)
			index+=1
		for column_tile in range(self.col_size):
			if column_tile == 0 or column_tile == self.col_size - 1:
				continue
			candidates.append(index)
			index += self.row_size - 1
			candidates.append(index)
			index += 1
		for row_tile in range(self.row_size):
			candidates.append(index)
			index+=1
		print(candidates)

	def iterative_backtracking(self, ):
		pass


