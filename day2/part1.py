import os
import numpy as np

def read_data(input_path: str) -> list[list[int]]:
    reports = list()
    with open(input_path, mode='r') as file:
        for line in file:
            report = [int(val) for val in line.split(' ')]
            reports.append(report)
    return reports

def is_safe(report: list[int]) -> bool:
    diff = np.diff(report)
    diff_signs = np.sign(diff) 
    diff_sign_check = np.sum(diff_signs) == diff_signs[0] * len(diff_signs)
    diff_stepsize_check = np.all(np.logical_and(np.abs(diff) >= 1, np.abs(diff) <= 3))
    return (diff_sign_check and diff_stepsize_check)

if __name__ == '__main__':
    input_path = os.path.join('day2', 'input.txt')
    reports = read_data(input_path)

    n_safe_reports = 0
    for report in reports:
        n_safe_reports += is_safe(report)

    print(f'{n_safe_reports=}')