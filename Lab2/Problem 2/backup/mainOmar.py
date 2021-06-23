##import matplotlib.pyplot as plt
import numpy as np
import math
import timeit
import sys

A = np.array([[]])
B = np.array([[]])
C = np.array([[]])


def main():
    global A, B, C
    print(sys.getrecursionlimit)
    rowsA = int(input("Please provide the number of Rows for Matrix A: "))
    colsA = int(input("Please provide the number of Columns for Matrix A: "))

    rowsB = int(input("Please provide the number of Rows for Matrix B: "))
    colsB = int(input("Please provide the number of Columns for Matrix B: "))

    if colsA != rowsB:
        print('The Matrix multiplication is invalid!')
        return

    A = np.random.randint(10, size=(rowsA, colsA))
    # print(A)

    B = np.random.randint(10, size=(rowsB, colsB))
    # print(B)

    C = np.zeros((rowsA, colsB), dtype=int)
    # print(C)

    initial = timeit.default_timer()

    RecursiveMultiply(0, len(A), 0, len(A[0]), 0, len(B), 0, len(B[0]), 1)
    print('Recursive Multiplication result: \n', C)

    end = timeit.default_timer()
    print()
    print("Time taken for Recursive Matrix Multiplication: ", end - initial)
    print()

    # initial = timeit.default_timer()

    # D = matrixmultiply(A,B)
    # print('Lab 1 Matrix Multiplication: \n', D)

    # end = timeit.default_timer()
    # print()
    # print("Time taken for Iterative Matrix Multiplication: ",end-initial)
    # print()

    # if (C == D).all():
    #     print('The Recursive Matrix Multiplication Result matches the Iterative Matrix Multiplication Result.')


def RecursiveMultiply(rowStartA, rowEndA, colStartA, colEndA, rowStartB, rowEndB, colStartB, colEndB, minblocksize):
    returned = 0

    if rowEndA - rowStartA > minblocksize and colEndB - colStartB > minblocksize:

        rowMidA = math.ceil((rowEndA + rowStartA) / 2)
        rowMidB = math.ceil((rowEndB + rowStartB) / 2)

        colMidA = math.ceil((colEndA + colStartA) / 2)
        colMidB = math.ceil((colEndB + colStartB) / 2)

        C[rowStartA:rowMidA, colStartB:colMidB] += RecursiveMultiply(rowStartA, rowMidA, colStartA, colMidA, rowStartB,
                                                                     rowMidB, colStartB, colMidB,
                                                                     minblocksize) + RecursiveMultiply(rowStartA,
                                                                                                       rowMidA, colMidA,
                                                                                                       colEndA, rowMidB,
                                                                                                       rowEndB,
                                                                                                       colStartB,
                                                                                                       colMidB,
                                                                                                       minblocksize)

        C[rowStartA:rowMidA, colMidB:colEndB] += RecursiveMultiply(rowStartA, rowMidA, colStartA, colMidA, rowStartB,
                                                                   rowMidB, colMidB, colEndB,
                                                                   minblocksize) + RecursiveMultiply(rowStartA, rowMidA,
                                                                                                     colMidA, colEndA,
                                                                                                     rowMidB, rowEndB,
                                                                                                     colMidB, colEndB,
                                                                                                     minblocksize)

        C[rowMidA:rowEndA, colStartB:colMidB] += RecursiveMultiply(rowMidA, rowEndA, colStartA, colMidA, rowStartB,
                                                                   rowMidB, colStartB, colMidB,
                                                                   minblocksize) + RecursiveMultiply(rowMidA, rowEndA,
                                                                                                     colMidA, colEndA,
                                                                                                     rowMidB, rowEndB,
                                                                                                     colStartB, colMidB,
                                                                                                     minblocksize)

        C[rowMidA:rowEndA, colMidB:colEndB] += RecursiveMultiply(rowMidA, rowEndA, colStartA, colMidA, rowStartB,
                                                                 rowMidB, colMidB, colEndB,
                                                                 minblocksize) + RecursiveMultiply(rowMidA, rowEndA,
                                                                                                   colMidA, colEndA,
                                                                                                   rowMidB, rowEndB,
                                                                                                   colMidB, colEndB,
                                                                                                   minblocksize)

    else:
        returned = np.matmul(A[rowStartA:rowEndA, colStartA:colEndA], B[rowStartB:rowEndB, colStartB:colEndB])

    return returned


def matrixmultiply(A, B):
    rowA, colA = np.shape(A)
    rowB, colB = np.shape(B)

    c = np.zeros((rowA, colB), dtype=int)
    for i in range(rowA):
        for j in range(colB):
            c[i][j] = 0
            for k in range(colA):
                c[i][j] = c[i][j] + (A[i][k] * B[k][j])

    return c


if __name__ == '__main__':
    main()




