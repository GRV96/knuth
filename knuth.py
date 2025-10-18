def knuth(n: int, a: int, b: int) -> int:
	if n < 1 or a < 0 or b < 0:
		raise ValueError(
			f"Knuth expects n>=1, a>=0, b>=0. Recieved n={n}, a={a}, b={b}.")

	return _knuth_rec(n, a, b)


def _knuth_rec(n: int, a: int, b: int) -> int:
	if b == 0:
		return 1

	if n == 1:
		return a**b

	return _knuth_rec(n-1, a, _knuth_rec(n, a, b-1))


__all__ = [knuth.__name__]
