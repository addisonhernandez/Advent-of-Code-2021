"""Advent of Code 2021: Day 5
https://adventofcode.com/2021/day/5
"""

import numpy as np
import re


def main():
    # Read from file
    with open("day5.txt", "r") as infile:
        points = re.findall(r"\d+", infile.read())
        points = np.asarray(points, dtype=int).reshape(-1, 4)

    # Create Zeros(max, max)
    field_size = points.max() + 1
    field = np.zeros((field_size, field_size), dtype=int)

    # Draw lines
    for x, y, x2, y2 in points:
        # # Part 1: Ignore diagonal lines
        # if x != x2 and y != y2:
        #     continue
        
        dx, dy = np.sign((x2 - x, y2 - y))

        # mark field from start (x, y) -> end (x2, y2)
        endpoint = (x2 + dx, y2 + dy)
        while (x, y) != endpoint:
            field[x, y] += 1
            x, y = x + dx, y + dy

    # Count Points
    print(f"Points traversed 2+ times: {np.sum(field > 1)}")


if __name__ == "__main__":
    main()
