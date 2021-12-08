"""Advent of Code 2021: Day 3
https://adventofcode.com/2021/day/3
"""

import numpy as np


def main():
    with open("day3.txt", "r") as infile:
        reports = np.loadtxt(infile, dtype=int)

    # Generate array of most common bits by column
    common_bits = common_bit(reports)

    gamma_rate = np_2_to_10(common_bits)
    epsilon_rate = np_2_to_10(np.invert(common_bits))

    # Gamma * Epsilon rating represents the power consumption
    print(f"{gamma_rate * epsilon_rate = }")

    O2_rating = rating_filter(reports, True)
    CO2_rating = rating_filter(reports, False)

    # O2 * CO2 rating represents the life support rating
    print(f"{O2_rating * CO2_rating = }")


def rating_filter(arr: np.ndarray, most_common: bool, index=0) -> int:
    """Filters reports based on the most or least common bit in column index.

    When only one report remains, return a base10 representation of the array.
    """
    if arr.shape[0] == 1:
        return np_2_to_10(arr.flat)

    col = arr[:, index]
    bit = common_bit(col) if most_common else not common_bit(col)

    return rating_filter(arr[col == bit], most_common, index + 1)


def common_bit(arr: np.ndarray) -> bool:
    """Determines most common bit in an array or matrix of 1s and 0s.

    For 1d array: True -> 1 is most common bit. False -> 0 is most common.
    For 2d matrix: return array of True/False representing the most common
    bits in each column.
    """
    return arr.sum(axis=0) >= arr.shape[0] / 2


def np_2_to_10(arr: np.ndarray) -> int:
    """Converts an array of ints representing a base 2 number to base 10.

    Ex: arr := [1, 0, 1, 0] => return 10
        arr := [0, 1, 0, 1, 1, 0] => return 22
    """
    return int("".join(np.char.mod("%i", arr)), base=2)


if __name__ == "__main__":
    main()
