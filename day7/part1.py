import os

def read_data(path: str) -> list[int, list[int]]:
    data = list()
    with open(path, mode='r') as file:
        for line in file:
            colon_split = line.split(': ')
            result = int(colon_split[0])
            number_components = [int(val) for val in colon_split[1].split(' ')]
            data.append([result, number_components])

    return data

def evaluate_computation(result: int, components: list[int]):
    n = len(components)
    if n == 2:
        return sum(components) == result or (components[0] * components[1]) == result
    else:
        return (evaluate_computation(result, [components[0] + components[1], *components[2:]]) or
                evaluate_computation(result, [components[0] * components[1], *components[2:]]))

if __name__ == '__main__':
    input_path = os.path.join('day7', 'input.txt')
    data = read_data(input_path)
    
    total = 0
    for datapoint in data:
        if evaluate_computation(datapoint[0], datapoint[1]):
            total += datapoint[0]

    print(f'{total=}')