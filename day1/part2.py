import os
import numpy as np

from part1 import read_data

if __name__ == '__main__':
    input_path = os.path.join('day1', 'input.txt')
    data_left, data_right = read_data(input_path)

    left_unique, left_counts = np.unique(data_left, return_counts=True)
    right_unique, right_counts = np.unique(data_right, return_counts=True)

    inter_values, left_indices, right_indices = np.intersect1d(left_unique, right_unique, return_indices=True)
    
    similarity_total = 0
    for value, index in zip(inter_values, right_indices):
        similarity = value * right_counts[index]
        similarity_total += similarity

    print(f'{similarity_total=}')