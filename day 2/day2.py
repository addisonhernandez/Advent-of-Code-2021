"""Advent of Code 2021: Day 2
https://adventofcode.com/2021/day/2
"""


def main():
    # Parse directions from file. 
    # Directions are of the format '<str: order> <int: magnitude>'
    with open("day 2/day2.txt", "r") as infile:
        directions = [line.split() for line in infile]

    # Part 1
    distance, depth = navigate(directions)
    print(f"Distance: {distance}\tDepth: {depth}\tProduct: {distance * depth}")

    # Part 2
    distance, depth = navigate_better(directions)
    print(f"Distance: {distance}\tDepth: {depth}\tProduct: {distance * depth}")


def navigate(directions):
    """Parse `directions` and generate a (distance, depth) position tuple.

    forward `x`: moves a horizontal distance `x`
    down `x`: increases depth by `x`
    up `x`: decreases depth by `x`
    """
    distance = depth = 0

    for direction in directions:
        order, magnitude = direction[0], int(direction[1])

        if order == "forward":
            distance += magnitude
        elif order == "up":
            depth -= magnitude
        elif order == "down":
            depth += magnitude

    return distance, depth


def navigate_better(directions):
    """Parse `directions` and generate a (distance, depth) position tuple.

    down `x`: increases aim by `x`
    up `x`: decreases aim by `x`
    forward `x`: moves horizontal distance `x` and increases depth by aim * `x`
    """
    distance = depth = aim = 0

    for direction in directions:
        order, magnitude = direction[0], int(direction[1])

        if order == "forward":
            distance += magnitude
            depth += aim * magnitude
        elif order == "up":
            aim -= magnitude
        elif order == "down":
            aim += magnitude

    return distance, depth


if __name__ == "__main__":
    main()
    