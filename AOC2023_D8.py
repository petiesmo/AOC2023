#Day 8: Haunted Wasteland
#Rules:
# Based on instruction list RLRLR, select Left or Right at each node to step through

# TaskA: Starting at AAA, how many steps required to reach ZZZ?
# TaskB: Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?

import math as m
from itertools import cycle
from pathlib import Path
import re
import AOC2023_utils as A23

def parse_input(input_values):
	instr = input_values[0]
	nodes = [n.split(' = ') for n in input_values[2:]]
	nodeLR = {n:lr[1:-1].split(', ') for n,lr in nodes}
	return instr, nodeLR

def mainA(instr, nodemap):
	node,fin,steps = 'AAA', 'ZZZ', 0
	path = ['AAA']
	for ins in cycle(instr):
		turn = 0 if ins=='L' else 1
		node = nodemap[node][turn]
		path.append(node)
		steps += 1
		if node == fin: break
	print(f'{path=}')
	print(f'Num Steps: {steps}')


def mainB(hands,bids):

	winnings = 1
	print(f'All winnings: {sum(winnings)}')

if __name__ == '__main__':
	fi = Path(__file__)
	inp = fi.parent / f"{fi.stem}.inp"
	values = A23.get_data(fi)
	values_ = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''.split('\n')
	
	instr,nodemap = parse_input(values)
	#print(f'{instr=}')
	#print(f'{nodemap=}')
	
	mainA(instr,nodemap)
	#mainB(h,b) 

#Result:
#Test values - A) 6 steps  B) 
#Answer A: 13939 steps
#Answer B: 