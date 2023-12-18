#AOC2023 Day5 - If you give a seed some fertilizer...
import AOC2023_utils as A23
from pathlib import Path
from pprint import pprint

#Part A Question:
# Input provides mappings for seed -> soil -> fertilizer -> .....  ending with "Location"
#What is the lowest location number that corresponds to any of the initial seed numbers?

def parse_mappings(data):
    # Determine Seeds, each Map
    data2 = data.split('\n\n')
    seeds = data2.pop(0)
    seedlist = [int(n) for n in seeds.split(': ')[1].split(' ')]
    data3 = [d.split(':\n') for d in data2]
    fromto = lambda k: k.rstrip(' map').split('-to-')
    mappings = {fromto(k)[0]: {
                'to': fromto(k)[1],
                'map': [tuple([int(n) for n in mp.split(' ')]) for mp in v.split('\n')]}
                for k,v in data3}
    return seedlist, mappings

def map_value(mapping, input_value):
    #mapping structure: Destination, Source, Range Length
    for dest, src, rlength in mapping:
        srng = range(src, src+rlength)
        if input_value in srng:
            drng = range(dest, dest+rlength)
            return drng[srng.index(input_value)]
    return input_value  #otherwise

def mainA(seedlist, mappings): 
    locations = list()
    for seed in seedlist:
        num = int(seed)
        media = 'seed'
        while media != 'location':
            mapping = mappings[media]
            media = mapping['to']
            maps = mapping['map']
            num = map_value(maps, num)
        locations.append(num)
    print(locations)  
    print(f'Answer A: {min(locations)} total')
    return min(locations)

#Part B Question
# The seed line describes ranges of seed numbers
# Now what is the lowest location?
def parse_mappings_B(mappings):
    #Condense mapping to a linked list (inflexible for future, 
    #   but only need to do dict lookups once)
    seed_to_location_chain = ['seed','soil','fertilizer','water','light',
             'temperature','humidity']
    mappingsB = [mappings[media]['map'] for media in seed_to_location_chain]
    return mappingsB

def find_location(seed, mapping):
    num = int(seed)
    media = 'seed'
    for maps in mapping:
        num = map_value(maps, num)
    return num

def mainB(seedlist, mappings):
    mappingsB = parse_mappings_B(mappings)
    pprint(f'{mappingsB=}')

    #Construct the set of all seeds, using the new interpretation of the seed pairs (as a range)
    #seedlistB = (set(range(seedlist[i], seedlist[i]+seedlist[i+1])) for i in range(0,len(seedlist),2))
    seedlist_ = list(zip(seedlist[::2],seedlist[1::2]))
    seedlistB = sorted([(a,a+b) for a,b in seedlist_])
    seedlistFlat = [item for row in seedlistB for item in row]
    print(seedlistFlat)
    
    locs = [find_location(seed,mappingsB) for seed in seedlistFlat]
    print(locs)
    #Speed issues: Options: Ignore/cache calculations OR Pointers OR Parallelize?
    #locations = [mainA(sl, mappings) for sl in seedlist]
    #print(f'Answer B: Overall minimum location: {min(locations)}')


if __name__ == '__main__':
    fi = Path(__file__)
    inp = fi.parent / f"{fi.stem}.inp"
    values = inp.read_text()
    seedlist, mappings = parse_mappings(values)
    print(seedlist)
    pprint(mappings)
    mainA(seedlist, mappings)

    mainB(seedlist, mappings)

#Result:
#Test values - 82,43,86,35   lowest = 35
#Answer A: total_score= 178159714
#Answer B: total_score2 = 