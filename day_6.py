def part_1():
    times = input().split()[1:]
    distances = input().split()[1:]
    res = 1
    j = 0
    for time in times:
        i = 1
        temp = 0
        while i < int(time):
            if (int(time) - i) * i > int(distances[j]):
                temp += 1
            i += 1
        j += 1
        res *= temp
    return res

def part_2():
    times = input().split()[1:]
    distances = input().split()[1:]
    time = []
    distance = []
    for t in times:
        time += t
    for d in distances:
        distance += d
    times = 0
    for i, t in enumerate(time):
        times += int(t) * 10**(len(time)-i-1)
    
    distances = 0
    for i, d in enumerate(distance):
        distances += int(d) * 10**(len(distance)-i-1)
    res = 0
    
    i = 1
    while i < int(times):
        if (int(times) - i) * i > int(distances):
            res += 1
        i += 1
      
    return res


#print(part_1())
print(part_2())