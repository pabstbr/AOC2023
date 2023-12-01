#!/usr/bin/python3

numeralDict = {
    "twone": "21",
    "eightwo": "82",
    "eighthree": "83",
    "oneight": "18",
    "threeight": "38",
    "fiveight": "58",
    "nineight": "98",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

inputFile = open('../resources/PuzzleInputs/Day1Input', 'r')
totalVal = 0
for line in inputFile:
    for key in numeralDict:
        line = line.replace(key, numeralDict[key])

    lineNums = [int(i) for i in line if i.isdigit()]

    totalVal = totalVal + (lineNums[0]*10 + lineNums[-1])

print(totalVal)