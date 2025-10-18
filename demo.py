"""
Computes numbers expressed with Knuth's up-arrow notation.
"""

from argparse import ArgumentParser

from knuth import knuth, print_knuth_result


def _make_parser(description: str) -> ArgumentParser:
	parser = ArgumentParser(description=description)
	parser.add_argument("-n", type=int, required=True,
		help="Number of arrows in Knuth's notation.")
	parser.add_argument("-a", type=int, required=True, help="First operand.")
	parser.add_argument("-b", type=int, required=True, help="Second operand.")
	return parser


args = _make_parser(__doc__).parse_args()
n = args.n
a = args.a
b = args.b

result = knuth(n, a, b)
print_knuth_result(n, a, b, result)
