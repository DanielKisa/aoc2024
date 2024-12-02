import os
import numpy as np

def read_data(input_path: str) -> tuple[np.ndarray, np.ndarray]:
    left_list = list()
    right_list = list()
    with open(input_path, mode='r') as file:
        for line in file:
            left, right = [int(val) for val in line.split('   ')]
            left_list.append(left)
            right_list.append(right)
    
    return np.array(left_list), np.array(right_list)

if __name__ == '__main__':
    input_path = os.path.join('day1', 'input.txt')
    data_left, data_right = read_data(input_path)

    data_left_sorted = np.sort(data_left)
    data_right_sorted = np.sort(data_right)

    abs_diff = np.abs(data_right_sorted - data_left_sorted)
    abs_diff_sum = np.sum(abs_diff)
    print(f"{abs_diff_sum=}")