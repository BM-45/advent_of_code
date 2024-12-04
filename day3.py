import re
from collections import deque

def mul_numbers(match):
    numbers = re.findall(r'\d+', match)
    return int(numbers[0])* int(numbers[1])

def process_string_part1(input_string):
    result = 0
    # Regex pattern
    pattern = r'mul\(\d{1,3},\d{1,3}\)'

    # Matches in the input string
    matches = re.findall(pattern, input_string)
    
    # Add matches.
    for match in matches:
        result += mul_numbers(match)
    
    return result



def process_string_part2(input_string):
    result = 0
    # Regex pattern
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

    # Matches in the input string
    matches = re.findall(pattern, input_string)
    
    considerExpression = True
    # Add matches.
    for match in matches:
        if match == 'do()':
            considerExpression = True
        else:
            if match == "don't()":
                considerExpression = False
            else:
                if considerExpression == True:
                    result += mul_numbers(match)
    
    return result



def file_to_string(filename):
    with open(filename, 'r') as file:
        return file.read()

input_string = file_to_string("day3.txt")
#input_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print(process_string_part2(input_string))
