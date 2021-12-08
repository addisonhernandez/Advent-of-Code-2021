"""Advent of Code 2021: Day 4
https://adventofcode.com/2021/day/4
"""

import numpy as np


def main():
    with open("day4.txt", "r") as infile:
        # Generate input list
        host_calls = np.fromstring(infile.readline(), dtype=int, sep=",")

        # Generate Bingo boards
        boards = np.fromfile(infile, dtype=int, sep=" ").reshape((-1, 5, 5))

    number_of_boards = boards.shape[0]
    print(f"Created {number_of_boards} boards of size {boards[0].shape}")

    marked = np.zeros(boards.shape, dtype=bool)
    winners = set()

    # While no one has won, iterate over input list
    for call in np.nditer(host_calls):
        it = np.nditer(boards, flags=["multi_index"])
        for board_number in it:
            if board_number != call:
                continue
            # mark boards
            board, row, col = it.multi_index
            marked[board, row, col] = True

            # check for a winner
            if not winning_board(marked, board, row, col):
                continue
            score = winning_score(boards[board], marked[board], call)
            winners.add(board)

            if len(winners) == number_of_boards:
                print(f"Final winner: {board}\t{score = }")
                return


def winning_board(arr: np.ndarray, board: int, row: int, col: int) -> bool:
    """Checks for a winning bingo board.

    Only check a single board for a completely marked row or column.
    The board, row, and column are determined by the latest marked number.
    """
    return np.all(arr[board, row, :]) or np.all(arr[board, :, col])


def winning_score(board: np.ndarray, marked: np.ndarray, last_called: int) -> int:
    return board.sum(where=np.invert(marked)) * last_called


if __name__ == "__main__":
    main()
