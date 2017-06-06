"""
Sudoku solver using backtracking. The solver can be
used on n by n tables where n is a square number. The
solver explores the space of solutions and check whether
all constraints are satisfied a each step. If not, it goes
back to the previous choice and switch it (backtracking).

run: python sudoku.py -f sudoku9.txt
"""
from __future__ import print_function
from six.moves import range
from math import sqrt
import argparse


def string_matrix(m):
    return "\n".join(" ".join([str(i) for i in row]) for row in m)
