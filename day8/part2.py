import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

from part1 import read_data

VISUALIZE_MAPS = False

def get_antinodes_part2(antenna_positions: list[tuple[int, int]], x_max: int, y_max: int) -> list[tuple[int, int]]:
    antinode_positions = list()
    for antenna_1 in antenna_positions:
        for antenna_2 in antenna_positions:
            delta_x = antenna_2[0] - antenna_1[0]
            delta_y = antenna_2[1] - antenna_1[1]
            if (delta_x == 0 and delta_y == 0):
                continue
            if antenna_1 not in antinode_positions:
                antinode_positions.append(antenna_1)
            potential_antinode = (antenna_1[0] - delta_x, antenna_1[1] - delta_y)
            while (0 <= potential_antinode[0] <= x_max) and (0 <= potential_antinode[1] <= y_max):
                antinode_positions.append(potential_antinode)
                delta_x += antenna_2[0] - antenna_1[0]
                delta_y += antenna_2[1] - antenna_1[1]
                potential_antinode = (antenna_1[0] - delta_x, antenna_1[1] - delta_y)
    
    return antinode_positions

def draw_map(antennas: list[tuple[int, int]], antinodes: list[tuple[int, int]], x_max: int, y_max: int) -> str:
    canvas = np.zeros((y_max + 1, x_max + 1, 3), dtype=np.uint8)
    for antenna in antennas:
        canvas[antenna[1], antenna[0], 0] = 255
    for antinode in antinodes:
        canvas[antinode[1], antinode[0], 2] = 255
    return canvas

if __name__ == '__main__':
    input_path = os.path.join('day8', 'input.txt')
    data, x_length, y_length = read_data(input_path)
    x_max = x_length - 1
    y_max = y_length - 1
    all_antinodes = list()
    for key in data.keys():
        antinodes = get_antinodes_part2(data[key], x_max, y_max)
        if VISUALIZE_MAPS:
            viz_map = draw_map(data[key], antinodes, x_max, y_max)
            fig, ax = plt.subplots()
            ax.imshow(viz_map)
            plt.show()

        all_antinodes.extend(antinodes)
    
    all_antinodes_without_duplicates = set(all_antinodes)
    print(f'Number of unique antinode positions: {len(all_antinodes_without_duplicates)}')