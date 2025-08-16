import os

from part1 import read_data

def uncompress_part2(data: str) -> list[str]:
    uncompressed = list()
    val = 0
    for i in range(len(data)):
        n = int(data[i])
        if n == 0:
            continue
        if i % 2 == 0:
            uncompressed.append([str(val)] * n)
            val += 1
        else:
            uncompressed.append(['.'] * n)

    if '.' in uncompressed[-1]:
        uncompressed.pop()
    return uncompressed

def make_compact_part2(uncompressed_data: list[str]) -> list[str]:
    compact_data = uncompressed_data.copy()
    idx_from_right = len(compact_data) - 1
    while idx_from_right > 0:
        group_to_move = compact_data[idx_from_right]
        if '.' in group_to_move:
            idx_from_right -= 1
            continue
        for i in range(idx_from_right):
            group_to_replace = compact_data[i]
            if group_to_replace.count('.') >= len(group_to_move):
                first_gap_index = group_to_replace.index('.')
                group_to_replace[first_gap_index : first_gap_index + len(group_to_move)] = group_to_move
                group_to_move[:] = ['.'] * len(group_to_move)
                break
        idx_from_right -= 1

    final_data = list()
    for group in compact_data:
        final_data.extend(group)
    return final_data
    
def calculate_checksum_naive_part2(data: str) -> int:
    uncompressed_data = uncompress_part2(data)
    compact_data = make_compact_part2(uncompressed_data)

    compact_data = list(map(lambda x: '0' if x == '.' else x, compact_data))
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
    checksum = calculate_checksum_naive_part2(data)
    
    print(f'{checksum=}')