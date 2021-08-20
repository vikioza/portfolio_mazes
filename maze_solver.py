import utils
import queue


class Solver:
	"""
	ToDo description
	"""
	def __init__(self):
		self.maze = None
		self.row_size = None
		self.col_size = None
		self.first = None
		self.last = None

	def solve(self, maze, rows, columns, entrance_tile, exit_tile, /, algo: str = "depth-first"):
		"""
		index = current_row * row_size + current_column

		:param maze: 1D array of maze tiles
		:param rows: number of rows in the mze
		:param columns: number of columns in the maze
		:param entrance_tile: index of the entrance tile
		:param exit_tile: index of the maze's exit
		:param algo: Determines which algorithm will be used to solve the maze. Options: depth-first, breadth-first,
			dijkstra, a-star
		:return:
		"""
		self.maze = maze
		self.row_size = columns
		self.col_size = rows
		self.first = entrance_tile
		self.last = exit_tile
		path = []

		if algo == "depth-first":
			path = self._depth_first()

		if algo == "breadth-first":
			path = self._breadth_first()

		if algo == "dijkstra":
			path = self._dijkstra()

		if algo == "a-star":
			path = self._astar()

		return path

	def _depth_first(self):
		return []

	def _breadth_first(self):
		return []

	def _dijkstra(self):
		return []

	def _astar(self):
		return []

	def _init_shortest_paths(self):
		shortest_paths = []
		for i in range(len(self.maze)):
			shortest_paths.append(-1)

		return shortest_paths
