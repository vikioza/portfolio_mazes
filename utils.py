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


def get_row(index, row_size):
	return int(index / row_size)


def get_column(index, row_size):
	return index % row_size

