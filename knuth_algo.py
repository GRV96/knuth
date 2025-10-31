from knuth_repo import KnuthRepo


_KNUTH_REPO = KnuthRepo()


def knuth(a: int, n: int, b: int) -> int:
	if n < 1 or a < 0 or b < 0:
		raise ValueError(
			f"Knuth expects a>=0, n>=1, b>=0. Recieved a={a}, n={n}, b={b}.")

	for x in range(b+1):
		value = _knuth_rec(a, n, x)

	return value


def _knuth_rec(a: int, n: int, b: int) -> int:
	value = _KNUTH_REPO.get_value(a, n, b)
	if value is not None:
		return value

	if n == 1:
		value = a**b
	elif b == 0:
		value = 1
	else:
		value = _knuth_rec(a, n-1, _knuth_rec(a, n, b-1))

	_KNUTH_REPO.add_value(a, n, b, value)
	return value


def _print_knuth_rec_call(a: int, n: int, b: int) -> None:
	# Debugging tool.
	print(f"{_knuth_rec.__name__}({a}, {n}, {b})")


def print_knuth_value(a: int, n: int, b: int, value: int) -> None:
	print(f"{knuth.__name__}({a}, {n}, {b}) = {value}")


__all__ = [
	knuth.__name__,
	print_knuth_value.__name__
]
