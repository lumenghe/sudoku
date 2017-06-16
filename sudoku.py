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

class Sudoku(object):
    def __init__(self, filename):
        self.matrix, self.max_value, self.block_size = self.read_instance(filename)

    def read_instance(self, filename):
        """
        Load instance from filename to self.matrix, load 0 if it is an empty value
        """
        matrix = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    row = []
                    for x in line.strip().split():
                        row.append(0 if x=='_' else int(x))
                    matrix.append(row)
        except:
            raise ValueError("could not load file {}".format(filename))
        n = len(matrix)
        if not n:
            raise ValueError("Sodoku matrix is empty")
        if not all(len(row) == n for row in matrix):
            raise ValueError("Rows should have same size as columns")
        if int(sqrt(n))**2 != n:
            raise ValueError("Size of a sudoku should be a square number")
        return matrix, n, int(sqrt(n))
