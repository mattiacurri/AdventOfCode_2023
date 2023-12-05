def parse_input():
    listmap = []
    while True:
        inp = input()
        if inp == "":
            break
        if inp.endswith(":"):
            continue
        listmap.append(inp.split())
        listmap.sort(key=lambda elem: elem[1])
    return listmap

def find_value(it, value):
    needed = -1
    for i, s in enumerate(it):
        if int(s[1]) <= int(value) and int(s[1]) + int(s[2]) - 1 >= int(value):
            needed = int(value) - int(s[1]) + int(s[0])
            break
    if needed == -1:
        needed = int(value)
    return needed 

def part_1():
    location = float('inf')
    seeds = input().split()[1:]
    input()
    input()
    seedtosoil = parse_input()
    soiltofertilizer = parse_input()
    fertilizertowater = parse_input()
    watertolight = parse_input()
    lighttotemperature = parse_input()
    temperaturetohumidity = parse_input()
    humiditytolocation = parse_input()
    
    for seed in seeds:
        soil = find_value(seedtosoil, seed)
        fertilizer = find_value(soiltofertilizer, soil)
        water = find_value(fertilizertowater, fertilizer)
        light = find_value(watertolight, water)
        temperature = find_value(lighttotemperature, light)
        humidity = find_value(temperaturetohumidity, temperature)
        loc = find_value(humiditytolocation, humidity)
        location = min(location, loc)
    return location
      

    
def part_2():
    location = float('inf')
    seeds = input().split()[1:]
    range_seeds = []
    i = 0
    while i < len(seeds):
        range_seeds.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1])
        i += 2
    print(range_seeds)
    input()
    input()
    seedtosoil = parse_input()
    soiltofertilizer = parse_input()
    fertilizertowater = parse_input()
    watertolight = parse_input()
    lighttotemperature = parse_input()
    temperaturetohumidity = parse_input()
    humiditytolocation = parse_input()
    
    i = 0
    while i < len(range_seeds):
        j = range_seeds[i][0]
        while j <= range_seeds[i][1]:
            soil = find_value(seedtosoil, j)
            fertilizer = find_value(soiltofertilizer, soil)
            water = find_value(fertilizertowater, fertilizer)
            light = find_value(watertolight, water)
            temperature = find_value(lighttotemperature, light)
            humidity = find_value(temperaturetohumidity, temperature)
            loc = find_value(humiditytolocation, humidity)
            location = min(location, loc)
            j += 1
        i += 1
    return location

#print(part_1())
print(part_2())