import os
import copy

from part1 import GUARD, VISITED, ADDED_OBSTACLE
from part1 import Direction, read_data, find_start, make_step, traverse_lab, save_map

def is_looping_naive(lab_map: list[list[int]], position: tuple[int, int], direction: tuple[int, int]) -> bool:
    original_state = (position, direction)
    states = [original_state]
    looping = False
    finished = False
    while ((not finished) and (not looping)):
        position, direction, finished = make_step(lab_map, position, direction)
        if finished:
            break
        current_state = (position, direction)
        if current_state in states and not finished:
            looping = True
        
        states.append(current_state)

    return looping, states

def find_loops_naive(lab_map: list[list[int]], start_position: tuple[int, int]) -> int:
    traversed_lab_map = traverse_lab(lab_map, start_position, Direction.TOP)
    traversed_lab_map[start_position[1]][start_position[0]] = GUARD

    n_looping = 0
    counter = 0
    for row in range(len(lab_map)):
        for col in range(len(lab_map[0])):
            if traversed_lab_map[row][col] == VISITED:
                counter += 1
                lab_map_changed = copy.deepcopy(lab_map)
                lab_map_changed[row][col] = ADDED_OBSTACLE
                looping, _ = is_looping_naive(lab_map_changed, start_position, Direction.TOP)
                if looping:
                    n_looping += 1
                
                print(f'{counter}/5242, Looping: {looping}')
    
    return n_looping

if __name__ == '__main__':
    input_path = os.path.join('day6', 'input.txt')
    part1_result_path = os.path.join('day6', 'part1_output.txt')

    lab_map = read_data(input_path)
    start_position = find_start(lab_map)

    n_looping = find_loops_naive(lab_map, start_position)
    print(f'{n_looping=}')