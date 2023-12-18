#AOC2023 Day3 - Gondola Gear Ratios
import AOC2023_utils as A23
from copy import deepcopy
import math as m
import re

#Part A Question:
#What is the sum of all of the part numbers in the engine schematic?
#(any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
#(Periods (.) do not count as a symbol.))

def parse_lines(lines):
    # Determine number positions, and symbol positions
    # Determine if adjacent to a symbol
    for line in lines[1:-1]:
        linestr = ''.join(line)
        linenums = re.finditer('\d+', linestr)
        linechars = re.finditer('[^\d|/.]', linestr)
        print(list(linenums))
        print(list(linechars))
    return None


def mainA(values): 
    
    print(f'Answer A: {sum(poss)} total')

#Part B Question
#

def mainB(values):
    powers=1
    print(f'Answer B: {sum(powers)} total')

if __name__ == '__main__':
    values1 = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

    values_ = A23.get_data(__file__)
    values_ = values1.split('\n')
    values = A23.pad_data(values_, '.')
    print(values)
    parse_lines(values)
    #mainA(values)
    #mainB(values)

#Result:
#Answer A: total_score= 2913
#Answer B: total_score2 = 55593