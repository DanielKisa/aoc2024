import os
import re
import numpy as np

from part1 import evaluate_multiplication

if __name__ == '__main__':
    input_path = os.path.join('day3', 'input.txt')
    with open(input_path, mode='r') as file:
        data = file.read()
    
    multiplication_pattern = 'mul\([0-9]*,[0-9]*\)'
    do_pattern = 'do\(\)'
    dont_pattern = "don't\(\)"

    multiplication_matches = list(re.finditer(multiplication_pattern, data))
    do_matches = list(re.finditer(do_pattern, data))
    dont_matches = list(re.finditer(dont_pattern, data))

    do_positions = [match.span()[0] for match in do_matches]
    dont_positions = [match.span()[0] for match in dont_matches]

    do_positions.insert(0, 0)
    dont_positions.insert(0, -1)

    do_positions = np.array(do_positions)
    dont_positions = np.array(dont_positions)

    total = 0
    for multiplication_match in multiplication_matches:
        position = multiplication_match.span()[0]
        left_do_position = do_positions[do_positions < position][-1]
        left_dont_position = dont_positions[dont_positions < position][-1]
        if left_do_position > left_dont_position:
            total += evaluate_multiplication(multiplication_match.group())

    print(f'{total=}')