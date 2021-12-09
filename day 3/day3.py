"""Advent of Code 2021: Day 3
https://adventofcode.com/2021/day/3
"""

import numpy as np


def main():
    # Parse reports from file
    # Reports are 10-digit numbers in base 2
    with open("day 3/day3.txt", "r") as infile:
        reports = np.loadtxt(infile, dtype=int)

    # Part 1:
    # Generate array of most common bits by column
    common_bits = common_bit(reports)

    gamma_rate = np_2_to_10(common_bits)
    epsilon_rate = np_2_to_10(np.invert(common_bits))

    # Gamma * Epsilon rating represents power consumption
    print(f"Part 1: {gamma_rate * epsilon_rate = }")

    # Part 2:
    O2_rating = rating_filter(reports, most_common=True)
    CO2_rating = rating_filter(reports, most_common=False)

    # O2 * CO2 rating represents life support rating
    print(f"Part 2: {O2_rating * CO2_rating = }")


def common_bit(arr: np.ndarray) -> bool:
    """Determines most common bit in an array or matrix of 1s and 0s.

    For 1d array: True -> 1 is most common bit. False -> 0 is most common.
    For 2d array: return 1d array of True/False representing the most common
    bits in each column.
    """
    return arr.sum(axis=0) >= arr.shape[0] / 2


def np_2_to_10(arr: np.ndarray) -> int:
    """Converts an array of ints (or bool) representing a base 2 number to base 10.

    Ex: arr := [1, 0, 1, 0] => return 10
        arr := [0, 1, 0, 1, 1, 0] => return 22
    """
    return int("".join(np.char.mod("%i", arr)), base=2)


def rating_filter(arr: np.ndarray, most_common: bool, index=0) -> int:
    """Filters reports based on the most or least common bit in column index.

    When only one report remains, return a base10 representation of the array.
    """
    if arr.shape[0] == 1:
        return np_2_to_10(arr.flat)

    # select all entries in column `index` and find most/least common bit
    col = arr[:, index]
    bit = common_bit(col) if most_common else not common_bit(col)

    return rating_filter(arr[col == bit], most_common, index + 1)


if __name__ == "__main__":
    main()
