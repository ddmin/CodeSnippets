import random
import numpy

class DimensionMismatchError(Exception):
    def __init__(self):
        Exception.__init__(self, "\
This computation can not be performed because \
the dimensions of the matrix are \
not consistent.")


class Matrix:

    # Dunder Methods

    # Initialize Matrix
    def __init__(self, matrix):
        self.dimX = len(matrix[0])
        self.dimY = len(matrix)
        self.matrix = matrix
        self.dimension = self.dimY, self.dimX
        self.elements = [y for x in self.matrix for y in x]
        _ = self.dimX
        for x in self.matrix:
            if len(x) != _:
                raise DimensionMismatchError


# Addition
    def __add__(self, other):
        if self.dimension == other.dimension:
            return Matrix([[x2 + y2 for x2, y2 in zip(x, y)]
                           for x, y in zip(self.matrix, other.matrix)])
        else:
            raise DimensionMismatchError


# Subtraction
    def __sub__(self, other):
        if self.dimension == other.dimension:
            return Matrix([[x2 - y2 for x2, y2 in zip(x, y)]
                           for x, y in zip(self.matrix, other.matrix)])
        else:
            raise DimensionMismatchError


# Scalar Multiplication
    def __rmul__(self, other):
        return Matrix([[y * other for y in x] for x in self.matrix])


# Matrix Multiplication
    def __mul__(self, other):
        if type(other) == int:
            return self.__rmul__(other)
        elif self.dimX == other.dimY:
            master = []
            for x in range(len(self.matrix)):
                row = []
                for y in range(len(other.matrix[0])):
                    sum = 0
                    for i in range(len(self.matrix[0])):
                        sum += self.matrix[x][i] * other.matrix[i][y]
                    row.append(sum)
                master.append(row)
            return Matrix(master)
        else:
            raise DimensionMismatchError

# Matrix Format Print
    def __str__(self, commas=True):

        string_of_elements = list(map(lambda x: str(x), self.elements))
        maximum_length = 0

        for x in string_of_elements:

            if len(x) > maximum_length:
                maximum_length = len(x)
        return_string = ''

        for x in self.matrix:

            return_string += '['

            for y in x:
                return_string += (' ' * (maximum_length - len(str(y)))) + str(y)

                if commas:
                    return_string += ', '
                else:
                    return_string += ' '

            if commas:
                return_string = return_string[:-2]
            else:
                return_string = return_string[:-1]

            return_string += ']' + '\n'
        return return_string[:-1]


# ------------------------------------------------------------------------------

# Class Methods


# Fill Matrix
    def fill(self, num):
        return Matrix([[num for x in range(self.dimX)]
                       for y in range(self.dimY)])


# Return identity matrix of dimension n*n
    @staticmethod
    def identity(num):
        return Matrix([[1 if x == y else 0 for x in range(num)]
                       for y in range(num)])


# Generate Matrix with dimensions (y, x) with random numbers from low to high
    @staticmethod
    def random(y, x, low=0, high=100):
        matrix = [[random.randint(low, high)
                   for row in range(x)]
                  for _ in range(y)]

        return Matrix(matrix)


def main():

    a = Matrix.random(3, 3, low=-20, high=1000)
    b = Matrix([[4, 5, 8], [6, 8, 8], [2, 4, 7]])

    print(a)
    print()
    print(b.__str__(commas=False))


if __name__ == '__main__':
    main()