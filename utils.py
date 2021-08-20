# #################### Tile composition #################### #
# 4 bytes													 #
# first 2 bytes - prev index								 #
# index / row_size = row (y_axis)							 #
# index % row_size = column (x-axis)						 #
# [0, 0]                  -> top-right corner				 #
# [row_size, column_size] -> bottom-left corner    		 	 #
# 															 #
# 2^0 - top wall											 #
# 2^1 - right wall											 #
# 2^2 - bottom wall											 #
# 2^3 - left wall											 #
# 2^4 - marked as visited									 #
# 2^5 - entrance (first tile in the maze)					 #
# 2^6 - exit (last tile in the maze)						 #
# #################### Tile composition #################### #


def get_row(index, row_size):
	return int(index / row_size)


def get_column(index, row_size):
	return index % row_size


def top(cell):
	return cell % 2


def right(cell):
	return (cell >> 1) % 2


def bottom(cell):
	return (cell >> 2) % 2


def left(cell):
	return (cell >> 3) % 2


def visited(cell):
	return (cell >> 4) % 2


def mark_visited(cell):
	return cell + 16


def entrance_tile(cell):
	return (cell >> 5) % 2


def mark_entrance(cell):
	return cell + 32


def exit_tile(cell):
	return (cell >> 6) % 2


def mark_exit(cell):
	return cell + 64


def unvisited_neighbors(self, current):
	"""
	Checks for unvisited neighbors and returns them as a list

	:param self: a Generator or Solver object
	:param current: tile index
	"""
	neighbors = []

	# top neighbor
	if get_row(current, self.row_size) > 0:  # if tile not on the top border
		n_index = current - self.row_size
		if not visited(self.maze[n_index]):
			neighbors.append(n_index)

	# right neighbor
	if get_column(current, self.row_size) < self.row_size - 1:  # if tile not on the right border
		n_index = current + 1
		if not visited(self.maze[n_index]):
			neighbors.append(n_index)

	# bottom neighbor
	if get_row(current, self.row_size) < self.col_size - 1:  # if tile not on the bottom border
		n_index = current + self.row_size
		if not visited(self.maze[n_index]):
			neighbors.append(n_index)

	# left neighbor
	if get_column(current, self.row_size) > 0:  # if tile not on the left border
		n_index = current - 1
		if not visited(self.maze[n_index]):
			neighbors.append(n_index)

	return neighbors
