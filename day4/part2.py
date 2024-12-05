import os

from part1 import DIRECTIONS, verify_word, find_matches, read_data

def find_x_mas_matches(mas_matches: list[dict]) -> list[dict]:
    diagonal_mas_matches = [match for match in mas_matches if 0 not in match['direction']]
    x_mas_matches = list()
    for match_1 in diagonal_mas_matches:
        match_1_center = (match_1['start'][0] + match_1['direction'][0],
                          match_1['start'][1] + match_1['direction'][1])
        for match_2 in diagonal_mas_matches:
            if match_1 == match_2:
                continue
            
            match_2_center = (match_2['start'][0] + match_2['direction'][0],
                              match_2['start'][1] + match_2['direction'][1])
            if match_1_center == match_2_center:
                x_mas_matches.append(match_1)

    return x_mas_matches

if __name__ == '__main__':
    input_path = os.path.join('day4', 'input.txt')
    data = read_data(input_path)
    mas_matches = find_matches(data, 'MAS')

    x_mas_matches = find_x_mas_matches(mas_matches)
    print(f'{(len(x_mas_matches) // 2)=}')