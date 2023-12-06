#!/usr/bin/python3

class GameResult:
    def __init__(self):
        self.minReds = 0
        self.minBlues = 0
        self.minGreens = 0


gameData = []
part1CubeMinimums = {
    'reds': 12,
    'greens': 13,
    'blues': 14
}
part1Sum = 0
part2Sum = 0

# inputFile = open('../resources/TestInputs/Day2TestInput', 'r')
inputFile = open('../resources/PuzzleInputs/Day2Input', 'r')
for line in inputFile:
    bagPulls = line[line.find(':')+1:].split(';')
    game = GameResult()
    for bagPull in bagPulls:
        results = bagPull.split(',')
        for result in results:
            value, color = result.split()
            if color == "red" and int(value) > game.minReds:
                game.minReds = int(value)
            elif color == "blue" and int(value) > game.minBlues:
                game.minBlues = int(value)
            elif color == "green" and int(value) > game.minGreens:
                game.minGreens = int(value)

    gameData.append(game)

for index, game in enumerate(gameData, start=1):
    if game.minReds <= part1CubeMinimums.get('reds') and \
            game.minBlues <= part1CubeMinimums.get('blues') and \
            game.minGreens <= part1CubeMinimums.get('greens'):
        part1Sum = part1Sum + index

    part2Sum += game.minReds * game.minBlues * game.minGreens

print(part1Sum)
print(part2Sum)
