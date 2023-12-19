#Day 7: Camel Cards
#Rules:
# Cards rank A,K....,3,2
# Hand type by rank: 5kind, 4kind, FullHouse, 3kind, 2pair, 1pair, HighCard
# TieBreak within rank: Strongest card in 1st position 

# TaskA: Sum of all winnings? (Find relative rank of all hands; Winnings = Rank * Bid)
# TaskB: J is now a Joker - makes best possible hand  (J also weakest in tie break)

import math as m
from collections import Counter
from functools import total_ordering
from pathlib import Path
import re
import AOC2023_utils as A23

def parse_input(input_values):
	handbids = [tuple(line.split(' ')) for line in input_values]
	return handbids

@total_ordering
class Hand():
	HANDTYPE = {
		(5,): 10, #'5kind',
		(4,1): 9, #'4kind',
		(3,2): 8, #'FullH',
		(3,1,1): 7, #'3kind',
		(2,2,1): 6, #'2pair',
		(2,1,1,1): 5, #'1pair',
		(1,1,1,1,1): 4 #'HighC'
		}
	
	def __init__(self, hand, bid):
		self.hand = hand
		self.bid = int(bid)

	def __str__(self):
		return f'{self.hand}'

	@staticmethod
	def card_rank(card):
		if card.isnumeric(): return int(card)
		face = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
		return face[card]

	@property
	def hand_rank(self):
		'''Determine hand type and relative ranking'''
		c = Counter(self.hand)
		handtype = self.HANDTYPE[tuple(sorted(c.values(), reverse=True))]
		return handtype

	def __eq__(self, hand2):
		return self.hand == self.hand2

	def __lt__(self, hand2):
		if self.hand_rank != hand2.hand_rank:
			return self.hand_rank < hand2.hand_rank
		#Tiebreak
		for a,b in zip(self.hand, hand2.hand):
			cra, crb = self.card_rank(a), self.card_rank(b)
			if cra == crb: continue
			return cra < crb

def mainA(hands, bids):
	hs = [Hand(hand,bid) for hand,bid in zip(hands,bids)]
	ranked = sorted(hs)	
	print(f'Ranking = {[str(h) for h in ranked]}')
	winnings = [i*hand.bid for i,hand in enumerate(ranked, start=1)]
	print(f'All winnings: {sum(winnings)}')

#J is now a Joker
@total_ordering
class HandB(Hand):
	def __init__(self, hand, bid):
		super().__init__(hand, bid)

	@staticmethod
	def card_rank(card):
		rank = Hand.card_rank(card)
		if card == 'J': rank = 1
		return rank
	
	@property
	def hand_rank(self):
		'''Determine hand type and relative ranking with Jokers'''
		c = Counter(self.hand)
		if 'J' in c.keys():
			Js = c.pop('J')
			if len(c) == 0: c.update({'A':0})
			letters = sorted(c, key=c.get, reverse=True)
			# Increment the largest card by number of Js
			c[letters[0]] += Js			

		hand_dist = tuple(sorted(c.values(), reverse=True))
		handtype = self.HANDTYPE[hand_dist]
		return handtype

def mainB(hands,bids):
	hs = [HandB(hand,bid) for hand,bid in zip(hands,bids)]
	ranked = sorted(hs)	
	print(f'Ranking = {[str(h) for h in ranked]}')
	winnings = [i*hand.bid for i,hand in enumerate(ranked, start=1)]
	print(f'All winnings: {sum(winnings)}')

if __name__ == '__main__':
	fi = Path(__file__)
	inp = fi.parent / f"{fi.stem}.inp"
	values = A23.get_data(fi)
	values_test = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.split('\n')
	
	hb = parse_input(values)
	#print(hb)
	h,b = zip(*hb) 
	mainA(h,b)
	mainB(h,b) 

#Result:
#Test values - A) Winnings = 6440  B) Winnings = 5905
#Answer A: Winnings = 248113761
#Answer B: Winnings = 246285222