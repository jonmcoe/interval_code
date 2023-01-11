from typing import Dict, List


def integer_intervals_to_musical_format(integer_intervals: List[int]) -> List[str]:
	# TODO greg
	return ['m3', 'Tt', 'P4']

def format_notes_for_output(notes: List[List[str]]) -> str:
	# TODO greg
	return "A  B  C\nD# E  F\n"

def format_permuations_to_binary_string(permutations: List[List[int]]) -> str:
	# TODO greg
	return "0 0 0\n1 1 1\n"

def format_tallies(tallies: Dict[str, int]) -> str:
	# TODO greg
	return "A  5\nB  3\n"

def footer() -> str:
	return """
--------------------------------
for more info visit:
https://www.gregpfeiffer.com

Inkwell_Highway_part_VIII.txt
generated with THE INTERVAL CODE

copyright G.C.Pfeiffer ©2022
"""