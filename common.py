import random

from typing import Dict, List

import formatting


def run_standard_text_flow(intervals, ordering_mode, show_binary, tonic):
	permutations = generate_permutations(intervals, ordering_mode)
	notes = generate_notes(permutations, tonic)
	tallies = tally_pitches(notes)

	filename = choose_filename()
	with open(filename, 'w+') as file:
		# TODO greg - write any instructions and stuff i didnt, fix newlines and spacing and evertything
		file.write(f'Possible pitch outcomes using [a systematically ordered set of] interval permutations for the {len(intervals)} entered intervals:\n')
		file.write(str(formatting.integer_intervals_to_musical_format(intervals)) + '\n')
		file.write(formatting.format_notes_for_output(notes))
		file.write(formatting.format_tallies(tallies))
		if show_binary:
			file.write(formatting.format_permuations_to_binary_string(permutations))
	print(f"Output written to: {filename}")


def tally_pitches(notes: List[List[str]]) -> Dict[str, int]:
	# TODO greg
	return {'A': 5, 'B': 3}

def generate_permutations(intervals: List[int], ordering_mode: str) -> List[List[int]]:
	# TODO greg
	return [[0,0,1],[1,0,1]]

def generate_notes(tonic: str, permutations: List[List[int]]) -> List[List[str]]:
	# TODO greg
	return [["A","B","C"],["D","E","F"]]

def choose_filename() -> str:
	# TODO greg
	return "Epic_Nightmare_Tollboth_XVI.txt"

