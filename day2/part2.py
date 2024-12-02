import os
import numpy as np

from part1 import read_data, is_safe

if __name__ == '__main__':
    input_path = os.path.join('day2', 'input.txt')
    reports = read_data(input_path)

    n_safe_reports = 0
    for report in reports:
        safe = is_safe(report)
        for i in range(len(report)):
            safe = safe or is_safe(report[:i] + report[(i + 1):])
        n_safe_reports += safe

    print(f'{n_safe_reports=}')