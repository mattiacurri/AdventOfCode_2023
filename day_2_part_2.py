with open("day1.txt", 'r') as f:
    input = f.readlines()

stringNums = {
    "one": 'o1e',
    "two": 't2o',
    "three": 't3e',
    "four": 'f4r',
    "five": 'f5e',
    "six": 's6x',
    "seven": 's7n',
    "eight": 'e8t',
    "nine": 'n9e'
}

cleaned_input = []
for line in input:
    for key, value in stringNums.items():
        line = line.replace(key, value)
    cleaned_input.append(line.strip('\n'))

res = 0
for line in cleaned_input:
    output = 0
    for i in range(0, len(line)):
        if line[i].isdigit():
            output += int(line[i]) * 10
            break
    for x in range(len(line) - 1, -1, -1):
        if line[x].isdigit():
            output += int(line[x])
            break
    res += output
    print(res)
        