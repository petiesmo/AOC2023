#Day 6: Wait for It
import math as m
from pathlib import Path
import re

import AOC2023_utils as A23

def parse_input(input_values):
	t,d = input_values.split('\n')
	times = [int(n) for n in re.split('\s+', t.split(': ')[1].strip())]
	dists = [int(n) for n in re.split('\s+', d.split(': ')[1].strip())]
	return times, dists

def find_winners(dgoal, tgoal):
	'''Identify how many winning solutions exist for the charge time 
		(must be greater than the stated record dist in the input)
		dist = v*t, which is dist = tcharge*(tgoal-tcharge)
		thus 0 = tcharge^2 - tgoal*tcharge + dist'''
	#Find quadratic roots for tcharge (tmin,tmax)
	a,b,c = 1, -tgoal, dgoal
	arg = b**2 - 4*a*c
	if arg < 0:
		return 1
	tmin = 1 if arg == 0 else m.ceil((-b - m.sqrt(arg))/(2*a))
	tmin = tmin if tmin > 0 else 1
	tmax = m.floor((-b + m.sqrt(arg))/(2*a))
	#Check for winning value
	if dgoal >= tmin * (tgoal - tmin): tmin += 1
	if dgoal >= tmax * (tgoal - tmax): tmax -= 1
	print(f'{dgoal=}, {tgoal=}, {tmin=}, {tmax=}')
	return tmax - tmin + 1

def mainA(times, dists):
	w = [find_winners(dist, time) for time,dist in zip(times, dists)]	
	print(f'Num winners = {w}')
	print(f'Prod: {m.prod(w)}')
	return None

#The paper was poorly kerned - only a single race (time=71530, dist=940200)
def mainB(tgoal,dgoal):
	w = find_winners(dgoal,tgoal)
	print(f'Num winners = {w}')


if __name__ == '__main__':
	fi = Path(__file__)
	inp = fi.parent / f"{fi.stem}.inp"
	values = inp.read_text()
	times, dists = parse_input(values)
	print(times, dists)

	#Test: times, dists = [7,15,30], [9,40,200]
	mainA(times, dists)
	mainB(71530, 940200) #Test answer = 71503
	mainB(50748685, 242101716911252)

#Result:
#Test values - Winners = 39,37,25,48   Prod = 288
#Answer A: Winners=39,37,25,48, Prod= 1731600
#Answer B: Winners= 40087680