import random
import numpy as np
from timeit import default_timer as timer

#Note this wouldnt work if you dont have matplotlib installed
#Uncomment this and the block in the end to test plotting
# import matplotlib.pyplot as plt


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


#Generate Random Array
def generateRandomArray(m,n):
    randomList = [[random.randint(1, 30) for i in range(n)] for j in range(m)]
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

if __name__ == '__main__':

    #THE SPLIT WOULD RETURN AN ARRAY OF STRINGS THAT HAVE "SPACES"
    rA, colA,rB,colB= input("Enter rowA, ColumnA, rowB, ColumnB values respectively ex ' 1 2 2 3' : ").split()
    #REMOVE THE SPACES AND CONVERT TO INT
    rowA = int((rA.strip()))
    columnA = int((colA.strip()))
    rowB = int((rB.strip()))
    columnB = int((colB.strip()))

    while (columnA!=rowB):
        print("INVALID INPUTS!ENTER AGAIN")
        rA, colA, rB, colB = input("Enter rowA, ColumnA, rowB, ColumnB values respectively ' 1 2 2 3' : ").split()
        rowA = int((rA.strip()))
        columnA = int((colA.strip()))
        rowB = int((rB.strip()))
        columnB = int((colB.strip()))


    print("Size of array A [",rowA,",",columnA,"]")
    print("Random array A:")
    A = generateRandomArray(rowA,columnA)
    print(A)
    print("\n")
    print("Size of array B [", rowB, ",", columnB, "]")
    print("Random array B:")
    B = generateRandomArray(rowB,columnB)
    print(B)
    print("\n")
############################ METHOD #######################

    start_time = timer()
    AB = matrixMultiply(A,B)
    end_time = timer()
    print("Matrix multiplication of A*B")
    print(AB)
    print("Method RUNNING TIME: ",(end_time - start_time))

################### NUMPY ##########################

    An = np.array(A)
    Bn = np.array(B)
    start_time = timer()
    ABn = np.matmul(An,Bn)
    end_time = timer()
    print("\n\nMatrix multiplication of A*B(numpy)")
    print(AB)
    print("NUMPY RUNNING TIME: ", (end_time - start_time))

    print("Are the two matrix multiplication results equal:  ",equals(AB,ABn))

    ######################## The loop through different sizes (copy from before) ################

    n = [100, 150,200,250, 300,350,400,450,500,550,600]
    pythonTiming = []
    myTiming = []

    for values in n:

        A = generateRandomArray(values,values)
        B = generateRandomArray(values, values)

        An = np.array(A)
        Bn = np.array(B)
        start_time = timer()
        ABn = np.matmul(An, Bn)
        end_time = timer()
        pythonTiming.append(end_time-start_time)

        start_time = timer()
        AB = matrixMultiply(A, B)
        end_time = timer()
        myTiming.append (end_time - start_time)


    print(myTiming)
    print("\n")
    print(pythonTiming)

    #
    # plt.subplot(2,1,1)
    # plt.plot(n,myTiming)
    # plt.ylabel("Time")
    # plt.xlabel("n")
    # plt.title("My Timing Diagram")
    #
    # plt.subplot(2,1,2)
    # plt.plot(n,pythonTiming)
    # plt.ylabel("Time")
    # plt.xlabel("n")
    # plt.title("My Python(numpy) Diagram")
    # plt.show()

