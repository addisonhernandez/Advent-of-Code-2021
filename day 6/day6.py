"""Advent of Code 2021: Day 6
https://adventofcode.com/2021/day/6
"""

import numpy as np


def main():
    """
    Tracking each fish and its state is super expensive.
    Each day requires n subtractions, and n grows exponentially

    Instead, track only the total number of fish in each state.

    Each day, rotate the totals array by one (each fish drops one state),
    and add the appropriate number of spawned fish.
    """
    with open("day 6/day6.txt") as f:
        init_states = np.loadtxt(f, dtype=np.uint8, delimiter=",")

    # 1d array of size 9 (0 to 8) to track the number of fish in each state
    fish_in_state = np.zeros(9, dtype=np.uint64)
    for state in init_states:
        fish_in_state[state] += 1

    # Rotate fish tracker and add spawned fish
    days = 256
    for _ in range(days):
        fish_in_state = np.roll(fish_in_state, -1)
        fish_in_state[6] += fish_in_state[-1]

    print(f"Fish on day {days}:\t{fish_in_state.sum()}")


if __name__ == "__main__":
    main()
