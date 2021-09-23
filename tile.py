class Tile:

	def __init__(self):
		self.state: int = 0b1111

	def has_top(self):
		return self.state % 2

	def has_right(self):
		return (self.state >> 1) % 2

	def has_bottom(self):
		return (self.state >> 2) % 2

	def has_left(self):
		return (self.state >> 3) % 2

	def visited(self):
		return (self.state >> 4) % 2

	def mark_visited(self):
		self.state += 16

	def unmark_visited(self):
		self.state -= 16

	def entrance_tile(self):
		return (self.state >> 5) % 2

	def mark_entrance(self):
		self.state += 32

	def exit_tile(self):
		return (self.state >> 6) % 2

	def mark_exit(self):
		self.state += 64

	def remove_top(self):
		self.state -= 1

	def remove_right(self):
		self.state -= 2

	def remove_bottom(self):
		self.state -= 4

	def remove_left(self):
		self.state -= 8

	def remove_wall(self, wall):
		self.state -= wall

	def get_state(self):
		return self.state

	def __str__(self):
		return str(self.state)


def get_row(index, row_size):
	return int(index / row_size)


def get_column(index, row_size):
	return index % row_size


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
