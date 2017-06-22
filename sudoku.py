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

    def next_coord(self, i, j):
        """
        Return next coordinate in the matrix (left to right, top to bottom)
        """
        return (i, j + 1) if j < self.max_value - 1 else (i + 1, 0)

    def next_free_coord(self, i, j):
        """
        Return next empty coordinate in matrix
        """
        try:
            while self.matrix[i][j]:
                (i, j) = self.next_coord(i, j)
        except:
            i, j = self.max_value, 0
        return (i, j)

    def block_range(self, i, j):
        """
        Yield all coordinates from the same block
        """
        i_offset = self.block_size * (i // self.block_size)
        j_offset = self.block_size * (j // self.block_size)
        for k in range(i_offset, i_offset + self.block_size):
            for l in range(j_offset, j_offset + self.block_size):
                yield k,l

    def check_constraints(self, i, j, working_matrix):
        """
        The same integer should not appear twice in the same row, column, block
        """
        row_numbers = set()
        column_numbers = set()
        block_numbers = set()
        for k in range(self.max_value):
            if working_matrix[i][k] in row_numbers:
                return False
            elif working_matrix[i][k]:
                row_numbers.add(working_matrix[i][k])
            if working_matrix[k][j] in column_numbers:
                return False
            elif working_matrix[k][j]:
                column_numbers.add(working_matrix[k][j])
        for k, l in self.block_range(i, j):
            if working_matrix[k][l] in block_numbers:
                return False
            elif working_matrix[k][l]:
                block_numbers.add(working_matrix[k][l])
        return True
