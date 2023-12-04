import re
from collections import defaultdict
def check_pivot(matrix, i, j, dim):
    for x in range(j - dim - 1, j):
        if i + 1 < len(matrix) and not matrix[i + 1][x].isdigit() and matrix[i + 1][x] != '.':
            return True
        if i - 1 > 0 and not matrix[i - 1][x].isdigit() and matrix[i - 1][x] != '.':
            return True
    if not matrix[i][j - dim - 1].isdigit() and matrix[i][j - dim - 1] != '.':
        return True
    if j < len(matrix):
        if (i - 1 > 0 and not matrix[i - 1][j].isdigit() and matrix[i - 1][j] != '.') or (
                i + 1 < len(matrix) and not matrix[i + 1][j].isdigit() and matrix[i + 1][j] != '.') or (
                not matrix[i][j].isdigit() and matrix[i][j] != '.'):
            return True

    return False


def create_num(matrix, i, start, end, num1, num2):
    if start > 0 and end <= len(matrix[i]):
        if len(num1) == 0:
            for z in range(start, end):
                if matrix[i][z].isdigit():
                    num1.append(matrix[i][z])
                else:
                    break
        else:
            for z in range(start, end):
                if matrix[i][z].isdigit():
                    num2.append(matrix[i][z])
                else:
                    break


def check_gear(matrix, i, j):
    no = 0
    num1 = []
    num2 = []
    if i + 1 < len(matrix):
        if matrix[i + 1][j].isdigit():
            if j + 1 < len(matrix) and j + 2 < len(matrix) and matrix[i + 1][j + 1].isdigit() and matrix[i + 1][
                j + 2].isdigit():
                num1.append(matrix[i + 1][j])
                num1.append(matrix[i + 1][j + 1])
                num1.append(matrix[i + 1][j + 2])
                no += 1
            elif j + 1 < len(matrix) and j - 1 >= 0 and matrix[i + 1][j + 1].isdigit() and matrix[i + 1][
                j - 1].isdigit():
                num1.append(matrix[i + 1][j - 1])
                num1.append(matrix[i + 1][j])
                num1.append(matrix[i + 1][j + 1])
                no += 1
            elif j - 1 >= 0 and j - 2 >= 0 and matrix[i + 1][j - 1].isdigit() and matrix[i + 1][j - 2].isdigit():
                num1.append(matrix[i + 1][j - 2])
                num1.append(matrix[i + 1][j - 1])
                num1.append(matrix[i + 1][j])
                no += 1
        else:
            if j - 1 >= 0:
                if matrix[i + 1][j - 1].isdigit():
                    no += 1
                    create_num(matrix, i + 1, j - 3, j, num1, num2)
            if j + 1 <= len(matrix[i]):
                if matrix[i + 1][j + 1].isdigit():
                    no += 1
                    create_num(matrix, i + 1, j + 1, j + 4, num1, num2)

    if i - 1 >= 0:
        if matrix[i - 1][j].isdigit() and no < 2:
            if j + 1 < len(matrix) and j + 2 < len(matrix) and matrix[i - 1][j + 1].isdigit() and matrix[i - 1][
                j + 2].isdigit():
                if len(num1) == 0:
                    num1.append(matrix[i - 1][j])
                    num1.append(matrix[i - 1][j + 1])
                    num1.append(matrix[i - 1][j + 2])
                else:
                    num2.append(matrix[i - 1][j])
                    num2.append(matrix[i - 1][j + 1])
                    num2.append(matrix[i - 1][j + 2])
                no += 1
            elif j + 1 < len(matrix) and j - 1 > 0 and matrix[i - 1][j + 1].isdigit() and matrix[i - 1][
                j - 1].isdigit():
                if len(num1) == 0:
                    num1.append(matrix[i - 1][j - 1])
                    num1.append(matrix[i - 1][j])
                    num1.append(matrix[i - 1][j + 1])
                else:
                    num2.append(matrix[i - 1][j - 1])
                    num2.append(matrix[i - 1][j])
                    num2.append(matrix[i - 1][j + 1])
                no += 1
            elif j - 1 >= 0 and j - 2 >= 0 and matrix[i - 1][j - 1].isdigit() and matrix[i - 1][j - 2].isdigit():
                if len(num1) == 0:
                    num1.append(matrix[i - 1][j - 2])
                    num1.append(matrix[i - 1][j - 1])
                    num1.append(matrix[i - 1][j])
                else:
                    num2.append(matrix[i - 1][j - 2])
                    num2.append(matrix[i - 1][j - 1])
                    num2.append(matrix[i - 1][j])
                no += 1
        elif no < 2:
            if j - 1 >= 0:
                if matrix[i - 1][j - 1].isdigit():
                    no += 1
                    create_num(matrix, i - 1, j - 3, j, num1, num2)
                if matrix[i][j - 1].isdigit() and no < 2:
                    if i == 1: print("BBB:" + matrix[i][j -1])
                    no += 1
                    create_num(matrix, i, j - 3, j, num1, num2)
                    print(num1, num2)
            if j + 1 <= len(matrix[i]) and no < 2:
                if matrix[i - 1][j + 1].isdigit():
                    if i == 1: print("AAA:" + matrix[i - 1][j + 1])
                    no += 1
                    create_num(matrix, i - 1, j + 1, j + 4, num1, num2)
                if matrix[i][j + 1].isdigit() and no < 2:
                    no += 1
                    create_num(matrix, i, j + 1, j + 4, num1, num2)
    return num1, num2

def p2():
    lines = []
    while len(lines) < 140:
        lines.append(input())
    adj = defaultdict(list)
    for i, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            for a, b in idxs:
                if 0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] == "*":
                    adj[a, b].append(m.group())
    return sum(int(x[0]) * int(x[1]) for x in adj.values() if len(x) == 2)

def part_2():
    matrix = []
    res = 0
    num1 = []
    num2 = []
    while len(matrix) < 140:
        matrix.append(input())

    for i in range(0, len(matrix)):
        print("RIGA: " + str(i))
        for j in range(0, len(matrix[i])):
            if i == 1:
                print(matrix[i][j])
            if matrix[i][j] == "*":
                num1, num2 = check_gear(matrix, i, j)
                if len(num1) != 0 and len(num2) != 0:
                    print(num1, num2)
                    n1 = "".join(num1)
                    n2 = "".join(num2)
                    res += (int(n1) * int(n2))
    print(res)
def part_1():
    matrix = []
    res = 0
    temp = []
    while len(matrix) < 140:
        matrix.append(input())

    for i in range(0, len(matrix)):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j].isdigit():
                for z in range(j, len(matrix[i])):
                    if matrix[i][z].isdigit():
                        temp.append(matrix[i][z])
                    else:
                        break
                j += len(temp)
                valid = check_pivot(matrix, i, j, len(temp))
                if valid:
                    num = "".join(temp)
                    res += int(num)
                temp.clear()
            else:
                j += 1
    print(res)


# part_1()
part_2()
#print(p2())
