import os
import re

def evaluate_expression(expression: str) -> int:
    number_pattern = '[0-9]+'
    matches = re.findall(number_pattern, expression)
    product = 1
    for match in matches:
        product *= int(match)
    
    return product

if __name__ == '__main__':
    input_path = os.path.join('day3', 'input.txt')
    with open(input_path, mode='r') as file:
        data = file.read()
    
    expression_pattern = 'mul\([0-9]*,[0-9]*\)'
    matches = re.findall(expression_pattern, data)

    total = 0
    for match in matches:
        total += evaluate_expression(match)
        
    print(f"{total=}")