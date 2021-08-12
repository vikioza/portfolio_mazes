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


def start(cell):
	return (cell >> 5) % 2


def mark_start(cell):
	return cell + 32


def end(cell):
	return (cell >> 6) % 2


def mark_end(cell):
	return cell + 64


def get_row(index, row_size):
	return int(index / row_size)


def get_column(index, row_size):
	return index % row_size
