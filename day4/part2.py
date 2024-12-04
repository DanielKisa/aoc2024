import os

from part1 import DIRECTIONS, verify_word, find_matches, read_data

if __name__ == '__main__':
    input_path = os.path.join('day4', 'input.txt')
    data = read_data(input_path)
    mas_matches = find_matches(data, 'MAS')

    total_x_mas_count = 0
    for match_1 in mas_matches:
        if 0 in match_1['direction']:
            continue
        for match_2 in mas_matches:
            if 0 in match_2['direction']:
                continue

            match_1_start_x, match_1_start_y = match_1['start']
            match_2_start_x, match_2_start_y = match_2['start']
            match_1_dir_x, match_1_dir_y = match_1['direction']
            match_2_dir_x, match_2_dir_y = match_2['direction']
            if (
                (match_1_start_x + match_1_dir_x == match_2_start_x + match_2_dir_x) and
                (match_1_start_y + match_1_dir_y == match_2_start_y + match_2_dir_y)
                ):
                total_x_mas_count += 1

    print(f'{total_x_mas_count=}')