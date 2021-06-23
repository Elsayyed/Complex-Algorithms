import random
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

def generateRandomArray(m,n):
    randomList = [[random.randint(1, 30) for i in range(n)] for j in range(m)]
    return randomList

def generateZerosArray(m,n):
    randomList = [[0 for i in range(n)] for j in range(m)]
    return randomList

def generateFixedArray(m,n):
    randomList = [[2 for i in range(n)] for j in range(m)]
    return randomList

#The function for checking if two lists are equal(have the same elements
def equals(List1,List2):
    if (len(List1) != len(List2)):
        return False
    for i in range(len(List1)):
        for j in range(len(List1[0])):
            if List1[i][j]!=List2[i][j]:
                return False
    return True

def matrixMultiply(A,B):
    m = len(A)
    p = len(A[0])
    n = len(B[0])

    c = [[0 for i in range(n)] for j in range(m)]

    for i in range(0,m):
        for j in range(0,n):
            c[i][j] = 0
            for k in range(0,p):
                c[i][j] = c[i][j] + A[i][k]*B[k][j]
    return c

def RecursiveBlockMatrixMultiply(A,B,C,highA,lowA,highB,lowB,minBlockSize):
    rowA = len(A) #4
    rowB = len(B) #4

    if rowB > minBlockSize:
        mid = rowA//2 #2
        midB = rowB//2 #2

        C_11 = RecursiveBlockMatrixMultiply(A[:mid, :midB],B[:midB, :mid],minBlockSize)+RecursiveBlockMatrixMultiply(A[:mid, midB:],B[midB:, :mid],minBlockSize)
        C_12 = RecursiveBlockMatrixMultiply(A[:mid, :midB],B[:midB, mid:],minBlockSize)+RecursiveBlockMatrixMultiply(A[:mid, midB:],B[midB:, mid:],minBlockSize)
        C_21 = RecursiveBlockMatrixMultiply(A[mid:, :midB],B[:midB, :mid],minBlockSize)+RecursiveBlockMatrixMultiply(A[mid:, midB:],B[midB:, :mid],minBlockSize)
        C_22 = RecursiveBlockMatrixMultiply(A[mid:, :midB],B[:midB, mid:],minBlockSize)+RecursiveBlockMatrixMultiply(A[mid:,midB:],B[midB:, mid:],minBlockSize)

        C = np.vstack([np.hstack([C_11, C_12]), np.hstack([C_21, C_22])])

        # RecursiveBlockMatrixMultiply(A[:mid, :midB],B[:midB, :mid],minBlockSize)+RecursiveBlockMatrixMultiply(A[:mid, midB:],B[midB:, :mid],minBlockSize)
        # RecursiveBlockMatrixMultiply(A[:mid, :midB],B[:midB, mid:],minBlockSize)+RecursiveBlockMatrixMultiply(A[:mid, midB:],B[midB:, mid:],minBlockSize)
        # RecursiveBlockMatrixMultiply(A[mid:, :midB],B[:midB, :mid],minBlockSize)+RecursiveBlockMatrixMultiply(A[mid:, midB:],B[midB:, :mid],minBlockSize)
        # RecursiveBlockMatrixMultiply(A[mid:, :midB],B[:midB, mid:],minBlockSize)+RecursiveBlockMatrixMultiply(A[mid:,midB:],B[midB:, mid:],minBlockSize)
        #
        # # C = np.vstack([np.hstack([C_11, C_12]), np.hstack([C_21, C_22])])



    else:
        C =A * B;

    return C


if __name__ == '__main__':
    minBlockSize = 1;

    rA, colA, rB, colB = input("Enter rowA, ColumnA, rowB, ColumnB values respectively ex ' 1 2 2 3' : ").split()
    # REMOVE THE SPACES AND CONVERT TO INT
    rowA = int((rA.strip()))
    columnA = int((colA.strip()))
    rowB = int((rB.strip()))
    columnB = int((colB.strip()))

    while (columnA != rowB):
        print("INVALID INPUTS!ENTER AGAIN")
        rA, colA, rB, colB = input("Enter rowA, ColumnA, rowB, ColumnB values respectively ' 1 2 2 3' : ").split()
        rowA = int((rA.strip()))
        columnA = int((colA.strip()))
        rowB = int((rB.strip()))
        columnB = int((colB.strip()))

    print("Size of array A [",rowA,",",columnA,"]")
    print("Random array A:")
    A = generateFixedArray(rowA,columnA)
    A = np.array(A)

    print(A)
    print("\n")
    print("Size of array B [", rowB, ",", columnB, "]")
    print("Random array B:")
    B = generateFixedArray(rowB,columnB)
    B = np.array(B)
    print(B)
    print("\n")


    # C = generateZerosArray(columnA,rowB)
    #
    # C = RecursiveBlockMatrixMultiply(A,B,minBlockSize)
    #
    # print(C)

    ############################ METHOD #######################

    start_time = timer()
    C = RecursiveBlockMatrixMultiply(A, B,minBlockSize)
    end_time = timer()
    print("Matrix multiplication of A*B")
    print(C)
    print("Method RUNNING TIME: ", (end_time - start_time))

    ################### NUMPY ##########################

    An = np.array(A)
    Bn = np.array(B)
    start_time = timer()
    ABn = np.matmul(An, Bn)
    end_time = timer()
    print("\n\nMatrix multiplication of A*B(numpy)")
    print(ABn)
    print("NUMPY RUNNING TIME: ", (end_time - start_time))

    print("\nAre the two matrix multiplication results equal:  ", equals(C, ABn))

    # A = [[1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4]]
    #
    # B = [[1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4],
    #      [1,2,3,4]]

    # A = [[1,2],[1,2]]
    # B = [[1,2],[1,2]]
    n = [50,60,70,100,120,130,150,200,220,230,250]
    pythonTiming = []
    myTiming = []

    for values in n:
        print(values)
        A = generateRandomArray(values,values)
        B = generateRandomArray(values, values)

        start_time = timer()
        AB = matrixMultiply(A, B)
        end_time = timer()
        pythonTiming.append (end_time - start_time)

        A = np.array(A)
        B = np.array(B)
        start_time = timer()
        AB = RecursiveBlockMatrixMultiply(A, B,minBlockSize)
        end_time = timer()
        myTiming.append (end_time - start_time)


    print(myTiming)
    print("\n")
    print(pythonTiming)


    plt.plot(n,myTiming)
    plt.plot(n, pythonTiming)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("Timing diagram")
    plt.legend(["Recursive Block Mutiplication","Regular multiplication lab1"])
    plt.show()



