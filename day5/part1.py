import os
import time
import numpy as np

def read_data(input_path: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules = list()
    updates = list()
    with open(input_path, mode='r') as file:
        for line in file:
            line = line.replace('\n', '')
            if '|' in line:
                rules.append(tuple([int(val) for val in line.split('|')]))
            elif ',' in line:
                updates.append([int(val) for val in line.split(',')])
    return rules, updates

def is_valid_update(rules: list[tuple[int, int]], update: list[int]) -> bool:
    for rule in rules:
        if not (rule[0] in update and rule[1] in update):
            continue
        index_prev, index_next = [update.index(value) for value in rule]
        if index_prev > index_next:
            return False
    return True

def get_middle_number(update: list[int]) -> int:
    return update[len(update) // 2]

if __name__ == '__main__':
    input_path = os.path.join('day5', 'input.txt')
    rules, updates = read_data(input_path)

    valid_mask = [is_valid_update(rules, update) for update in updates]
    valid_updates = [update for valid, update in zip(valid_mask, updates) if valid]
    middle_numbers = [get_middle_number(update) for update in valid_updates]
    print(f'{sum(middle_numbers)=}')