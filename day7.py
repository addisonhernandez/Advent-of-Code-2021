"""Advent of Code 2021: Day 7
https://adventofcode.com/2021/day/7
"""

import numpy as np


def main():
    crabs = np.ndarray((1,))
    # Parse crab positions from file
    with open("day7.txt") as infile:
        crabs = np.loadtxt(infile, dtype=int, delimiter=",")

    # Calculate the optimal position
    pos = int(np.median(crabs))
    print(f"{pos = }\tTotal cost: {total_cost(crabs, pos)}")


def total_cost(arr: np.ndarray, pos: int, part_2=False) -> int:
    cost = np.abs(arr - pos)
    return np.sum(cost * (cost + 1) // 2) if part_2 else np.sum(cost)


if __name__ == "__main__":
    main()
