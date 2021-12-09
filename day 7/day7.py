"""Advent of Code 2021: Day 7
https://adventofcode.com/2021/day/7
"""

import numpy as np


def main():
    # Parse crab positions from file
    with open("day 7/day7.txt") as infile:
        crabs = np.loadtxt(infile, dtype=int, delimiter=",")

    # Part 1: Calculate optimal position for constant fuel usage
    pos = int(np.median(crabs))
    print(f"{pos = }\tTotal cost: {total_cost(crabs, pos)}")

    # Part 2: Calculate optimal position for increasing fuel usage
    pos = int(np.mean(crabs))
    print(f"{pos = }\tTotal cost: {total_cost(crabs, pos, part_2=True)}")


def total_cost(arr: np.ndarray, pos: int, part_2=False) -> int:
    """Calculates fuel consumption to move crabs at positions in `arr` to `pos`.

    Part 1: constant fuel consumption is the absolute value of difference of
        current crab position and final position
    Part 2: each move the crab makes increases fuel consumption by 1.
        2 moves -> (1 + 2) fuel consumed
        3 moves -> (1 + 2 + 3) fuel consumed
        n moves -> (1 + 2 + ... + n) fuel consumed
        sum(1 to n) = n * (n + 1) / 2
    """
    cost = np.abs(arr - pos)
    return np.sum(cost * (cost + 1) // 2) if part_2 else np.sum(cost)


if __name__ == "__main__":
    main()
