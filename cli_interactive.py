from typing import List, Tuple

import common

def main():
	intervals, ordering_mode, show_binary, tonic = prompt_for_all_arguments()
	common.run_standard_text_flow(intervals, ordering_mode, show_binary, tonic)


def prompt_for_all_arguments() -> Tuple[List[int], str, bool, str]:
	# TODO greg
	# display instructions, prompt validate and cast all user inputs
	return ([1,4,3], 'ord', True, 'C')

if __name__ == '__main__':
	main()