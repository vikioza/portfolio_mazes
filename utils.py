def top(cell):
	return cell % 2


def right(cell):
	return (cell >> 1) % 2


def bottom(cell):
	return (cell >> 2) % 2


def left(cell):
	return (cell >> 3) % 2

