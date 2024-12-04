import os

DIRECTIONS = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

def verify_word(data: list[list[str]], word: str, start: tuple[int, int], direction: tuple[int, int]):
    start_x, start_y = start
    direction_x, direction_y = direction
    result = True
    for i in range(len(word)):
        result = result and data[start_y + i * direction_y][start_x + i * direction_x] == word[i]
    
    return result
    

def find_matches(data: list[list[str]], word='XMAS') -> int:
    rows = len(data)
    cols = len(data[0])
    word_length = len(word)

    matches = list()
    for direction in DIRECTIONS:
        for i in range(rows):
            if (i + direction[1] * (word_length - 1) < 0) or (i + direction[1] * (word_length - 1) > rows - 1):
                continue
            for j in range(cols):
                if (j + direction[0] * (word_length - 1) < 0) or (j + direction[0] * (word_length - 1) > cols - 1):
                    continue
                word_found = verify_word(data, word, (j, i), direction)
                if word_found:
                    matches.append({
                        'start': (j, i),
                        'direction': direction
                    })

    return matches

def read_data(input_path: str) -> list[list[str]]:
    data = list()
    with open(input_path, mode='r') as file:
        for line in file:
            data.append(list(line.replace('\n', '')))
    return data

if __name__ == '__main__':
    input_path = os.path.join('day4', 'input.txt')
    data = read_data(input_path)
    xmas_matches = find_matches(data, 'XMAS')
    xmas_count = len(xmas_matches)

    print(f'{xmas_count=}')