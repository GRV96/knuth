from knuth_repo import KnuthRepo


_KNUTH_REPO = KnuthRepo()


def knuth(n: int, a: int, b: int) -> int:
	if n < 1 or a < 0 or b < 0:
		raise ValueError(
			f"Knuth expects n>=1, a>=0, b>=0. Recieved n={n}, a={a}, b={b}.")

	for x in range(b+1):
		_knuth_rec(n, a, x)

	value = _KNUTH_REPO.get_value(n, a, b)
	if value is None:
		value = _knuth_rec(n, a, b)

	return value


def _knuth_rec(n: int, a: int, b: int) -> int:
	value = _KNUTH_REPO.get_value(n, a, b)
	if value is not None:
		return value

	if n == 1:
		value = a**b
	elif b == 0:
		value = 1
	else:
		value = _knuth_rec(n-1, a, _knuth_rec(n, a, b-1))

	_KNUTH_REPO.add_value(n, a, b, value)
	return value


def _print_knuth_rec_call(n: int, a: int, b: int) -> None:
	# Debugging tool.
	print(f"{_knuth_rec.__name__}({n}, {a}, {b})")


def print_knuth_value(n: int, a: int, b: int, value: int) -> None:
	print(f"{knuth.__name__}({n}, {a}, {b}) = {value}")


__all__ = [
	knuth.__name__,
	print_knuth_value.__name__
]
