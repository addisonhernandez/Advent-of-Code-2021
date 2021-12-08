'''Advent of Code 2021
https://adventofcode.com/2021/day/1
'''


def number_of_depth_drops(depths):
    '''
    drops = 0
    for i, depth in enumerate(depths[1:]):
        if depth > depths[i]:
            drops += 1
    '''
    return sum(1 for i, d in enumerate(depths[1:]) if d > depths[i])


def number_of_fuzzy_drops(depths):
    fuzzy_depths = [sum(depths[i:i + 3]) for i in range(len(depths) - 2)]
    return number_of_depth_drops(fuzzy_depths)


if __name__ == "__main__":
    with open("day1.txt", "r") as infile:
        depths = [int(line) for line in infile]
    print(f"Drops: {number_of_depth_drops(depths)}")
    print(f"Fuzzy: {number_of_fuzzy_drops(depths)}")