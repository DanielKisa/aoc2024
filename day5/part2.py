import os
import numpy as np

from part1 import read_data, is_valid_update, get_middle_number

def reorder_update(update: list[int], rules: list[tuple[int, int]]) -> list[int]:
    rules_filtered = [rule for rule in rules if (rule[0] in update and rule[1] in update)]
    reordered_update = update.copy()
    valid = False
    while not valid:
        valid = True
        for rule in rules_filtered:
            index_prev, index_next = [reordered_update.index(value) for value in rule]
            if index_prev > index_next:
                val = reordered_update.pop(index_prev)
                reordered_update.insert(index_next, val)
                valid = False
                break
    return reordered_update

if __name__ == '__main__':
    input_path = os.path.join('day5', 'input.txt')
    rules, updates = read_data(input_path)

    valid_mask = [is_valid_update(rules, update) for update in updates]
    invalid_updates = [update for valid, update in zip(valid_mask, updates) if not valid]
    reordered_invalid_updates = [reorder_update(update, rules) for update in invalid_updates]
    middle_numbers = [get_middle_number(update) for update in reordered_invalid_updates]
    print(f'{sum(middle_numbers)=}')