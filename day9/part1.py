import os

def read_data(path: str) -> str:
    with open(path, mode='r') as file:
        data = file.read()

    data = data.replace('\n', '')
    return data
    
def uncompress(data: str) -> list[str]:
    uncompressed = list()
    val = 0
    for i in range(len(data)):
        if i % 2 == 0:
            uncompressed.extend([str(val)] * int(data[i]))
            val += 1
        else:
            uncompressed.extend(['.'] * int(data[i]))

    while uncompressed[-1] == '.':
        uncompressed.pop()
    return uncompressed

def make_compact(uncompressed_data: list[str]) -> list[str]:
    compact_data = uncompressed_data.copy()
    n_gaps = compact_data.count('.')
    while n_gaps > 0:
        last_val = compact_data[-1]
        if last_val == '.':
            compact_data.pop()
        else:
            compact_data[compact_data.index('.')] = last_val
            compact_data.pop()
        n_gaps -= 1
    return compact_data
    
def calculate_checksum_naive(data: str) -> int:
    uncompressed_data = uncompress(data)
    compact_data = make_compact(uncompressed_data)

    compact_data = [int(x) for x in compact_data]
    checksum = 0
    for i in range(len(compact_data)):
        checksum += i * compact_data[i]

    return checksum

if __name__ == '__main__':
    input_path = os.path.join('day9', 'input.txt')
    data = read_data(input_path)
    # data = '2333133121414131402'
    # data = '12345'
    checksum = calculate_checksum_naive(data)

    print(f'{checksum=}')