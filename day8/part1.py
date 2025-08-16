import os

def read_data(path: str) -> tuple[dict[str, list[tuple[int, int]]], int, int]:
    with open(path, mode='r') as file:
        contents = file.read().splitlines()
    
    unique_strings = set()
    for line in contents:
        unique_strings = unique_strings.union(set(line))
    keys = unique_strings - set('.')
    data = {key: [] for key in keys}
    
    for y, line in enumerate(contents):
        for x, char in enumerate(line):
            if char != '.':
                data[char].append((x, y))

    y_length = len(contents)
    x_length = len(contents[0])

    return data, x_length, y_length

def get_antinodes(antenna_positions: list[tuple[int, int]], x_max: int, y_max: int) -> list[tuple[int, int]]:
    antinode_positions = list()
    for antenna_1 in antenna_positions:
        for antenna_2 in antenna_positions:
            delta_x = antenna_2[0] - antenna_1[0]
            delta_y = antenna_2[1] - antenna_1[1]
            if not (delta_x == 0 and delta_y == 0):
                potential_antinode = (antenna_1[0] - delta_x, antenna_1[1] - delta_y)
                if (0 <= potential_antinode[0] <= x_max) and (0 <= potential_antinode[1] <= y_max):
                    antinode_positions.append(potential_antinode)
    
    return antinode_positions

if __name__ == '__main__':
    input_path = os.path.join('day8', 'input.txt')
    data, x_length, y_length = read_data(input_path)
    x_max = x_length - 1
    y_max = y_length - 1
    all_antinodes = list()
    for key in data.keys():
        antinodes = get_antinodes(data[key], x_max, y_max)
        all_antinodes.extend(antinodes)
    
    all_antinodes_without_duplicates = set(all_antinodes)
    print(f'Number of unique antinode positions: {len(all_antinodes_without_duplicates)}')