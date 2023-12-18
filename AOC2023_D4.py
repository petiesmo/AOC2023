#AOC2023 Day4 - Scratchcards
import AOC2023_utils as A23
from pprint import pprint

#Part A Question:
#What is the sum of all of the card point values

def parse_card(line):
    # Determine winners, card_values
    card = line.split(': ')
    winners, card_values = card[1].split(' | ')
    win = winners.strip().replace('  ', ' ').split(' ')
    cval = card_values.strip().replace('  ', ' ').split(' ')
    return win, cval

def score_scratchcard(winners, card_values):
    matches = len(set(winners) & set(card_values))
    score = 2 ** (matches-1) if matches else 0
    return score

def mainA(values): 
    cards = [parse_card(line) for line in values]
    [print(card) for card in cards]
    scores = [score_scratchcard(w,cv) for w,cv in cards]  
    print(scores)  
    print(f'Answer A: {sum(scores)} total')

#Part B Question
#Based on the number of matches, copies of scorecards are won
#How many total scratchcards do you have at the end?

def mainB(values):
    cards = [parse_card(line) for line in values]
    print(cards)
    matches = [len(set(wi) & set(cv)) for wi,cv in cards]
    print(matches)
    copies = [1 for card in cards]
    for i,m in enumerate(matches):
        if m == 0: continue
        #For each copy of the current card, Add 1 bonus card to the next M succeeding cards (based on M # of matches) 
        for j in range(i+1, i+m+1):
            copies[j] += copies[i]  
    print(copies)
    print(f'Answer B: {sum(copies)} total')

if __name__ == '__main__':
    values1 = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

    values = A23.get_data(__file__)
    #values = values1.split('\n')
    #print(values)
    #mainA(values)
    mainB(values)

#Result:
#Test data score: 8,2,2,1,0,0 = 13
#Answer A: total_score= 20667
#Answer B: total_score2 = 5833065