#AOC2023 Day2 - Snow Island cubes game
import AOC2023_utils as A23
from copy import deepcopy
import math as m

#Part A Question:
#What is the sum of the indices for valid games with only:
#12 red, 13 green, & 14 blue cubes
COLORS = [('red',12), ('green',13), ('blue',14)]

def parse_game(game):
    gameid, pulls = game.split(': ')
    gid = int(gameid.split(' ')[1])
    pdicts = list()
    for pull in pulls.split('; '):
        d = dict()
        for color in pull.split(', '):
            q,c = color.split(' ')
            d[c] = int(q)
        pdicts.append(d)
    print(pdicts)
    return gid, pdicts

def game_is_possible(pulls):
    # Possible if qty cubes shown <= known available
    return all([all([qty >= pull.get(color,0) for color,qty in COLORS]) for pull in pulls])
            
def fewest_necessary_cubes(pulls):
    # Min of each color in a game
    return {color: max([pull.get(color,0) for pull in pulls]) for color,qty in COLORS}

def mainA(values): 
    games = [parse_game(game) for game in values]
    print([game_is_possible(game) for gid,game in games])
    poss = [gid for gid,game in games if game_is_possible(game)]
    print(f'Answer A: {sum(poss)} total')

#Part B Question
#Determine minimum qty of cubes that would make games possible
#Power = red*green*blue   what is the sum of powers for all games?

def mainB(values):
    games = [parse_game(game) for game in values]
    fewest = ([fewest_necessary_cubes(game) for gid,game in games])
    print(fewest)
    powers = [m.prod(game.values()) for game in fewest]
    print(powers)
    print(f'Answer B: {sum(powers)} total')

if __name__ == '__main__':
    values1 = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    values2 = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

    #parse_game(values1)
    #mainB(values2.split('\n'))

    values = A23.get_data(__file__)
    mainA(values)
    mainB(values)

#Result:
#Answer A: total_score= 2913
#Answer B: total_score2 = 55593