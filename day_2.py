def part_1():
    ids = 0
    while True:
        game = input()
        gamelist = game.split()
        colors = {"bl": 14, "gr": 13, "re": 12}
        possible = True

        for i in range(0, len(gamelist)):
            if "blue" in gamelist[i] or "red" in gamelist[i] or "green" in gamelist[i]:
                colors[gamelist[i][:2]] -= int(gamelist[i - 1])
            if ";" in gamelist[i]:
                if colors["bl"] < 0 or colors["gr"] < 0 or colors["re"] < 0:
                    possible = False
                    break
                else:
                    colors = {"bl": 14, "gr": 13, "re": 12}
        # check the last subset
        if colors["bl"] < 0 or colors["gr"] < 0 or colors["re"] < 0:
            possible = False
        if possible:
            ids += int(gamelist[1].replace(":", ""))
        print(ids)


def part_2():
    ids = 0
    while True:
        game = input()
        gamelist = game.split()

        colors = {"bl": 0, "gr": 0, "re": 0}

        for i in range(0, len(gamelist)):
            if "blue" in gamelist[i] or "red" in gamelist[i] or "green" in gamelist[i]:
                colors[gamelist[i][:2]] = max(colors[gamelist[i][:2]], int(gamelist[i - 1]))
        m = 0
        for color in colors.values():
            if m == 0:
                m += 1
            m *= color
        ids += m
        print(ids)


part_2()
