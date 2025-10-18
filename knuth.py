def knuth(n: int, a: int, b: int) -> int:
	if n < 1 or a < 0 or b < 0:
		raise ValueError(
			f"Knuth expects n>=1, a>=0, b>=0. Recieved n={n}, a={a}, b={b}.")

	return _knuth_rec(n, a, b)


def _knuth_rec(n: int, a: int, b: int) -> int:
	result = 1

	if n == 1:
		result = a**b

	elif b != 0:
		result = _knuth_rec(n-1, a, _knuth_rec(n, a, b-1))

	return result


def _print_knuth_rec_call(n: int, a: int, b: int) -> None:
	# Debugging tool.
	print(f"{_knuth_rec.__name__}({n}, {a}, {b})")


def print_knuth_result(n: int, a: int, b: int, result: int) -> None:
	print(f"{knuth.__name__}({n}, {a}, {b}) = {result}")


__all__ = [knuth.__name__]
