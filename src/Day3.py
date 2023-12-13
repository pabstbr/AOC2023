#!/usr/bin/python3
import string

field = list()
symbol_set = set()
max_col = 0
max_row = 0


class FieldValue:
    def __init__(self, number, originating_row, originating_col):
        self.number = number
        self.originating_row = originating_row
        self.originating_col = originating_col

    def has_orthogonal_symbol(self):
        digits_in_number = len(str(self.number))
        min_snapshot_row = 0 if self.originating_row - 1 < 0 else self.originating_row - 1
        possible_max_row = self.originating_row + 2
        max_snapshot_row = max_row if possible_max_row > max_row \
            else possible_max_row

        min_snapshot_col = 0 if self.originating_col - 1 < 0 else self.originating_col - 1
        possible_max_col = self.originating_col + digits_in_number + 1
        max_snapshot_col = max_col if possible_max_col > max_col \
            else possible_max_col

        return_val = 0

        for row in field[min_snapshot_row:max_snapshot_row]:
            if any(char in symbol_set for char in row[min_snapshot_col:max_snapshot_col]):
                return_val = int(self.number)

        return return_val


def generate_symbols():
    global symbol_set
    for line in field:
        symbol_set.update([*str(line).translate(str.maketrans('', '', string.digits+'.'))])


def part1_calculator():
    part1_total = 0

    for index, row in enumerate(field):
        numbers_in_row = [entry for entry in
                          list(filter(None, row.translate(str.maketrans(''.join(symbol_set), '.' * len(symbol_set)))
                                      .split(".")))
                          if entry.isdigit()]
        for number in numbers_in_row:
            column = str(row).find(number)

            if column + len(number) < max_col:
                while row[column + len(number)].isdigit() or (column > 0 and row[column-1].isdigit()):
                    column = str(row).find(number, column+len(number))

            orthogonal_value = FieldValue(number, index, column).has_orthogonal_symbol()
            part1_total += orthogonal_value

    print("Total for part 1: {}".format(part1_total))


def extract_full_digit(row, starting_col):
    pointer = starting_col
    # if the starting location is a digit check to the left first
    if row[pointer].isdigit():
        while row[pointer-1].isdigit():
            pointer -= 1
    else:
        while not row[pointer].isdigit():
            pointer += 1
    first_digit_loc = pointer

    # reset the pointer if it's moved left
    pointer = starting_col if starting_col > pointer else pointer

    # Now check to the right
    while pointer + 1 < max_row and row[pointer+1].isdigit():
        pointer += 1

    return int(row[first_digit_loc:pointer+1])


def calculate_gear_ratio(row_loc, col_loc):
    first_value = 0
    for index, row in enumerate(field[max(row_loc-1, 0):min(row_loc+2, max_row)], -1):
        if any(char.isdigit() for char in row[max(col_loc-1, 0):min(col_loc+2, max_col)]):
            found_number = extract_full_digit(field[row_loc+index], max(col_loc-1, 0))
            if first_value == 0:
                first_value = found_number
            else:
                return first_value * found_number
            if sum(c.isdigit() for c in row[max(col_loc-1, 0):min(col_loc+2, max_col)] if c.isdigit) == 2 and not row[col_loc].isdigit():
                found_number = extract_full_digit(field[row_loc+index], col_loc+1)
                return first_value * found_number
    return 0


def part2_calculator():
    part2_total = 0
    for row_num, line in enumerate(field):
        gear_count = line.count('*')
        gear_col = 0
        for gear_number in range(0, gear_count):
            gear_col = line.find('*', gear_col+1)
            part2_total += calculate_gear_ratio(row_num, gear_col)
    print("Part 2 Total: {}".format(part2_total))


def main():
    global field, max_row, max_col

    # input_file = open('../resources/TestInputs/Day3TestInput', 'r')
    input_file = open('../resources/PuzzleInputs/Day3Input', 'r')

    for line in input_file:
        field.append(line.strip())

    max_row = len(field)
    max_col = len(field[0])

    generate_symbols()

    part1_calculator()
    part2_calculator()


if __name__ == "__main__":
    main()
