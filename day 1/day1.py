"""Advent of Code 2021
https://adventofcode.com/2021/day/1
"""


def main():
    # Read sonar data from file
    with open("day 1/day1.txt", "r") as infile:
        depths = [int(line) for line in infile]

    # Part 1
    print(f"Drops: {depth_drops(depths)}")

    # Part 2
    print(f"Fuzzy: {fuzzy_drops(depths)}")


def depth_drops(depths):
    """Calculates number of times depth reading increases between two readings."""
    return sum(1 for i, d in enumerate(depths[1:]) if d > depths[i])


def fuzzy_drops(depths):
    """Calculates depth reading increases between averaged readings."""
    fuzzy_depths = [sum(depths[i : i + 3]) for i in range(len(depths) - 2)]
    return depth_drops(fuzzy_depths)


if __name__ == "__main__":
    main()
