'''Advent of Code 2021: Day 2
https://adventofcode.com/2021/day/2
'''


def navigate(directions):
    '''Parse `directions` and generate a (distance, depth) position tuple.

    forward `x`: moves a horizontal distance `x`
    down `x`: increases depth by `x`
    up `x`: decreases depth by `x`
    '''
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
    '''Parse `directions` and generate a (distance, depth) position tuple.

    down `x`: increases aim by `x`
    up `x`: decreases aim by `x`
    forward `x`: moves horizontal distance `x` and increases depth by aim * `x`
    '''
    distance = depth = aim = 0

    for d in directions:
        order, magnitude = d[0], int(d[1])

        if order == "forward":
            distance += magnitude
            depth += aim * magnitude
        elif order == "up":
            aim -= magnitude
        elif order == "down":
            aim += magnitude

    return distance, depth


if __name__ == "__main__":
    with open("day2.txt", "r") as infile:
        directions = [line.split() for line in infile]

    dis, dep = navigate_better(directions)
    print(f"Distance: {dis}\tDepth: {dep}\tProduct: {dis * dep}")