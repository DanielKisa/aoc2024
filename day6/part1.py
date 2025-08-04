import os
import copy

GUARD = ord('^')
OBSTACLE = ord('#')
VISITED = ord('X')
ADDED_OBSTACLE = ord('O')

class Direction:
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    TOP = (0, -1)
    BOTTOM = (0, 1)

    @staticmethod
    def turn_right(direction: tuple[int, int]) -> tuple[int, int]:
        if direction == Direction.LEFT:
            return Direction.TOP
        elif direction == Direction.RIGHT:
            return Direction.BOTTOM
        elif direction == Direction.TOP:
            return Direction.RIGHT
        elif direction == Direction.BOTTOM:
            return Direction.LEFT
        else:
            raise ValueError('Invalid direction')

def read_data(input_path: str) -> list[list[int]]:
    lab_map = list()
    with open(input_path, mode='r') as file:
        for line in file:
            line = line.replace('\n', '')
            lab_map.append([ord(x) for x in line])
    return lab_map

def find_start(lab_map: list[list[int]]) -> tuple[int, int]:
    for row in range(len(lab_map)):
        for col in range(len(lab_map[0])):
            if lab_map[row][col] == GUARD:
                return (col, row)

def make_step(lab_map: list[list[int]], position: tuple[int, int],
              direction: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    rows = len(lab_map)
    cols = len(lab_map[0])
    position_x, position_y = position
    direction_x, direction_y = direction
    if not ((0 <= (position_x + direction_x) < cols) and
           (0 <= (position_y + direction_y) < rows)):
        return position, direction, True

    if lab_map[position_y + direction_y][position_x + direction_x] in (OBSTACLE, ADDED_OBSTACLE):
        return make_step(lab_map, position, Direction.turn_right(direction))
        # return position, Direction.turn_right(direction), False
    else:
        new_position = (position_x + direction_x, position_y + direction_y)
        return new_position, direction, False

def traverse_lab(lab_map: list[list[int]], position: tuple[int, int],
                 direction: tuple[int, int]) -> list[list[int]]:
    traversed_lab_map = copy.deepcopy(lab_map)
    finished = False
    while not finished:
        position, direction, finished = make_step(lab_map, position, direction)
        traversed_lab_map[position[1]][position[0]] = VISITED
    return traversed_lab_map

def save_map(lab_map: list[list[int]], output_path: str) -> None:
    with open(output_path, mode='w') as file:
        for line in lab_map:
            file.write(''.join([chr(x) for x in line]) + '\n')

if __name__ == '__main__':
    input_path = os.path.join('day6', 'input.txt')
    output_path = os.path.join('day6', 'part1_output.txt')

    lab_map = read_data(input_path)
    start = find_start(lab_map)
    lab_map[start[1]][start[0]] = VISITED
    traversed_lab_map = traverse_lab(lab_map, start, Direction.TOP)

    total_visited = 0
    for line in traversed_lab_map:
        total_visited += line.count(VISITED)

    print(f'{total_visited=}')
    save_map(traversed_lab_map, output_path)