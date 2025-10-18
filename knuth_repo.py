class KnuthRepo:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super().__new__(cls)
			cls._instance._initialize()

		return cls._instance

	def _initialize(self):
		self._content: dict[tuple[int, int, int], int] = dict()

	def add_value(self, n: int, a: int, b: int, value: int) -> None:
		self._content[(n, a, b)] = value

	def get_value(self, n: int, a: int, b: int) -> int | None:
		return self._content.get((n, a, b))


__all__ = [KnuthRepo.__name__]
