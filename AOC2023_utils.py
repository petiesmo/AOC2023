#AOC22Dx.py
from dataclasses import dataclass
from copy import deepcopy
import math as m
from pathlib import Path 
from pprint import pprint
import re
import string



def get_data(forfile):
    fi = Path(forfile)
    inp = fi.parent / f"{fi.stem}.inp"
    data = inp.read_text()
    return data.splitlines()

def pad_data(data, padchar='.'):
    data2 = []
    for row in list(data):
        row = list(row)
        row.insert(0, padchar)
        row.append(padchar)
        data2.append(row)
    pad = [padchar for _ in range(len(data[0]))]
    data2.insert(0,pad)
    data2.append(pad)
    return data2

#Part A Question:
#In how many assignment pairs does one range fully contain the other?

def mainA():
    pairs = get_data()
    print(f'Answer A: {len([1])}something')

#Part B Question
#In how many assignment pairs do the ranges overlap at all?

def mainB():
    pairs = get_data()
    print(f'Answer B: {len([1])} something')

if __name__ == '__main__':
    mainA()
    #mainB()

#Result:
#Answer A: total_score= 498
#Answer B: total_score2 = 2581