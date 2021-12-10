"""Advent of Code 2021: Day 8
https://adventofcode.com/2021/day/8
"""

from collections import Counter


def main():
    # Parse input file
    inputs = []
    outputs = []
    with open("day 8/day8test.txt") as infile:
        for line in infile:
            ins, _, outs = line.partition(" | ")
            inputs.append(ins.split())
            outputs.append(outs.split())

    # Part 1: Count number of 1, 4, 7, 8 in the outputs
    print(f"Part 1: {one_four_seven_eight(outputs)}")


def one_four_seven_eight(lst: list) -> int:
    """Counts number of 1, 4, 7, and 8 in a list of 7-segment display signals.
    
    Each of 1, 4, 7, and 8 has a unique number of segments lit:
        1: two segments
        4: four segemnts
        7: three segments
        8: seven segments
    """
    c = Counter(len(item) for line in lst for item in line)
    return sum((c[2], c[4], c[3], c[7]))


if __name__ == "__main__":
    main()
