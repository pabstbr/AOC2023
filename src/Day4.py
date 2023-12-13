#!/usr/bin/python3

class Scratcher:
    def __init__(self, winning_numbers, scratched_numbers):
        self.winning_numbers = winning_numbers
        self.scratched_numbers = scratched_numbers

all_scratchers = []
def part1(scratchers):
    part1_total = 0

    for scratcher in scratchers:
        card_value = 0
        for potential_winner in scratcher.scratched_numbers:
            if potential_winner in scratcher.winning_numbers:
                print("Found a winner! {}".format(potential_winner))
                card_value = 1 if card_value == 0 else card_value*2
                print("Card value now: {}".format(card_value))
        part1_total += card_value
    print("Part 1: {}".format(part1_total))


def part2(scratchers, curr_card):
    scratchcards_generated = 0

    print("Checking cards starting from {} to {}".format(curr_card+1, curr_card+len(scratchers)))

    for index, scratcher in enumerate(scratchers, curr_card):
        wins = 0
        for potential_winner in scratcher.scratched_numbers:
            if potential_winner in scratcher.winning_numbers:
                wins += 1
        # print("Generated {} more cards from {} to {}".format(wins, curr_card+1, curr_card+wins+1))
        if wins > 0:
            print("wins on this level {}".format(wins))
            downstream = part2(all_scratchers[index+1:min(index+wins+1, len(all_scratchers))], index+1)
            scratchcards_generated = (scratchcards_generated + wins + downstream)
    return scratchcards_generated


def main():
    # input_file = open('../resources/TestInputs/Day4TestInput', 'r')
    input_file = open('../resources/PuzzleInputs/Day4Input', 'r')

    scratchers = []

    for index, line in enumerate(input_file):
        no_header = line[line.index(':')+1:]
        sides = no_header.split('|')

        curr_card = Scratcher(sides[0].split(), sides[1].split())
        scratchers.append(curr_card)

        print("Card {} winners: {}\n Found: {}".format(index, curr_card.winning_numbers, curr_card.scratched_numbers))

    part1(scratchers)

    global all_scratchers
    all_scratchers = scratchers
    print("part2: {}".format(part2(scratchers, 0)+len(all_scratchers)))


if __name__ == "__main__":
    main()
