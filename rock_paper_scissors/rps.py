#!/usr/bin/python

import sys

possible_plays = [['rock'], ['paper'], ['scissors']]


def add_additional_player(plays):
    newArr = []
    for i in range(len(plays)):
        for move in possible_plays:
            newArr.append(plays[i] + move)
    return newArr


def rock_paper_scissors(n):

    # make list of possible plays

    if n == 0:
        return [[]]
    if n == 1:
        return possible_plays
    else:
        return add_additional_player(rock_paper_scissors(n - 1))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
