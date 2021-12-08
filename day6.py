"""Advent of Code 2021: Day 6
https://adventofcode.com/2021/day/6
"""

import numpy as np


def main():
    """
    Tracking each fish and its state is super expensive.
    Each day requires n subtractions, and n grows exponentially
    Initial state: 3,4,3,1,2
    After  1 day:  2,3,2,0,1
    After  2 days: 1,2,1,6,0,8
    After  3 days: 0,1,0,5,6,7,8
    After  4 days: 6,0,6,4,5,6,7,8,8

    Instead, track the total number of fish in each state:
    fish_in_state:[0,1,2,3,4,5,6,7,8]
    Initial state: 0,1,1,2,1,0,0,0,0
    After  1 day:  1,1,2,1,0,0,0,0,0
    After  2 days: 1,2,1,0,0,0,1,0,1
    After  3 days: 2,1,0,0,0,1,1,1,1
    After  4 days: 1,0,0,0,1,1,3,1,2

    Each day, rotate the array by one (each fish drops one state),
    and add the appropriate number of spawned fish.
    """
    with open("day6.txt") as f:
        init_fish = np.loadtxt(f, dtype=np.uint8, delimiter=",")

    # 1d array of size 9 (0 to 8) to track the number of fish in each state
    fish_in_state = np.zeros(9, np.uint64)
    for state in init_fish:
        fish_in_state[state] += 1
    
    # Rotate fish tracker
    days = 256
    for _ in range(days):
        fish_in_state = np.roll(fish_in_state, -1)
        fish_in_state[6] += fish_in_state[-1]

    print(f'Fish on day {days}:\t{fish_in_state.sum()}')


if __name__ == "__main__":
    main()
