from collections import Counter

def part_1():
    result = 0
    while True:
        line = input().split()
        winning_numbers = set()
        numbers_i_have = []
        
        win = 0
        while line[win] != '|':
            if line[win].isdigit():
                winning_numbers.add(line[win])
            win += 1
        numbers_i_have = line[win+1:]
        
        count = 0
        for num in numbers_i_have:
            if num in winning_numbers:
                count += 1
        
        if count != 0:
            result += 2**(count - 1)
        
        print(result)
        
def part_2():
    histo = Counter()
    line = []
    
    l = 0
    while l < 196:
        line += input().split()
        histo[l+1] = 1
        l += 1
    win = 0
    i = 0
    l = 1
    while i < len(line):
        long = 0
        winning_numbers = set()
        numbers_i_have = []
        while win < len(line) and line[win] != '|':
            if line[win].isdigit():
                winning_numbers.add(line[win])
            win += 1
            long += 1
        while win < len(line) and line[win] != 'Card':
            if line[win].isdigit():
                numbers_i_have.append(line[win])
            win += 1
            long += 1
        count = 0
        for num in numbers_i_have:
            if num in winning_numbers:
                count += 1
                histo[l+count] += 1 * histo[l]
        l += 1
        i += long
    return sum(histo.values())
    
print(part_2())
