from queue import LifoQueue
from maze_viz import MazeViz


class Solver:
	"""
	ToDo description
	"""
	def __init__(self, drawer: MazeViz):
		self.tiles = None
		self.row_size = None
		self.col_size = None
		self.first = None
		self.last = None
		self.drawer = MazeViz

	def find_path(self, tiles, rows, columns, entrance_tile, exit_tile, /, algo: str = "depth-first"):
		"""index = current_row * row_size + current_column"""
		self.tiles = tiles
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

	def _depth_first(self, tiles):
		stack = LifoQueue()
		stack.put(self.first)
		while not stack.empty():
			current = stack.get()
			x, y = self.drawer.get_coords(current)
			self.drawer.draw_current(tiles[current], x, y)
			self.tiles[current].mark_visited()
			if current == self.last:
				print("Success")
				return
			neighbors = self.tiles.unvisited_neighbors(current)
			for neigh in neighbors:
				stack.put(neigh)

		return []

	def _breadth_first(self):

		return []

	def _dijkstra(self):

		return []

	def _astar(self):

		return []

	def _init_shortest_paths(self):
		shortest_paths = []
		for i in range(len(self.tiles)):
			shortest_paths.append(-1)

		return shortest_paths
