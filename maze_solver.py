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

	def find_path(self, maze, rows, columns, entrance_tile, exit_tile, /, algo: str = "depth-first"):
		"""index = current_row * row_size + current_column"""
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
