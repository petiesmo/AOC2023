#AOC2023 Day1
import AOC2023_utils as A23
from copy import deepcopy

def cal_val(word):
    digits = [c for c in word if c.isnumeric()]
    cal_val = digits[0] + digits[-1]
    return int(cal_val)

NAMES = ['one','two','three','four','five','six','seven','eight','nine']
DIGITS = [str(i) for i in range(1,10)]
ND = dict(zip(NAMES,DIGITS))

def cal_val_B(word):
    cache = ''
    digits = ''
    w = list(deepcopy(word))
    while w:
        char = w.pop(0)
        if char.isnumeric():
            digits += char
            cache = ''
            continue
        cache += char
        for name in NAMES:
            if name in cache:
                digits += ND[name]
                cache = ''
    cal_val = digits[0] + digits[-1]
    return int(cal_val)            


#Part A Question:
#Cal values are first digit & last digit inlne.  What is sum of all cal vals?

def mainA(values):
    cal_vals = [cal_val(word) for word in values]
    print(cal_vals)
    print(f'Answer A: {sum(cal_vals)} total')

#Part B Question
#Digits are spelled out, also ('one', 'two', etc)?  Now what is the sum of all call vals?

def mainB(values):
    cal_vals = [cal_val_B(word) for word in values]
    print(cal_vals)
    print(f'Answer B: {sum(cal_vals)} total')

if __name__ == '__main__':
    values = ['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
    values = A23.get_data(__file__)
    mainA(values)
    values2 = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    mainB(values)

#Result:
#Answer A: total_score= 56108
#Answer B: total_score2 = 