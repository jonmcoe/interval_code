import argparse

from typing import List, Tuple

import common

# invoke like this:
# python cli_with_arguments.py 1,2,3 ord y G
# and expect output like
#
# Received: [1, 2, 3]  ord, True, G
# Output written to: Epic_Nightmare_Tollboth_XVI.txt

def main():
	intervals, ordering_mode, show_binary, tonic = parse_all_commandline_args()
	print(f"Received: {intervals}  {ordering_mode}, {show_binary}, {tonic}")
	common.run_standard_text_flow(intervals, ordering_mode, show_binary, tonic)


def parse_all_commandline_args() -> Tuple[List[int], str, bool, str]:
	parser = argparse.ArgumentParser()
	parser.add_argument("intervals", help="intervals comma separated")
	parser.add_argument("ordering_mode", help="ordering: ord,ran,more,super")
	parser.add_argument("show_binary", help="show binary: y or n")
	parser.add_argument("tonic", help="tonic note")
	# TODO: greg to validate arguments, make help messages nicer or whatever
	# see https://docs.python.org/3/howto/argparse.html
	args = parser.parse_args()
	return (list(map(int, args.intervals.split(','))), args.ordering_mode, args.show_binary == 'y', args.tonic)



if __name__ == '__main__':
	main()