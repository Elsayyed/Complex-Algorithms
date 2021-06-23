import random
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import math

def generateRandomArray(n):
    randomList = [random.randint(1, 30) for i in range(n)]
    return randomList

def generateZerosArray(n):
    randomList = [0 for i in range(n)]
    return randomList

def generateFixedArray(n):
    randomList = [i for i in range(n)]
    return randomList

def equals(List1,List2):
    if (len(List1) != len(List2)):
        return False
    for i in range(len(List1)):
            if List1[i]!=List2[i]:
                return False
    return True

def recursiveLCS(x,y):
    i = len(x)-1
    j = len(y)-1
    return recursiveLCSWrapper(x,y,i,j)

def recursiveLCSWrapper(x,y,i,j):

    #Base case
    if (i == -1 or j == -1):
        return 0

    if (x[i] == y[j]):
        result =  recursiveLCSWrapper(x,y,i-1,j-1)+1

    else:
        result = max(recursiveLCSWrapper(x,y,i-1,j),recursiveLCSWrapper(x,y,i,j-1))

    return result

def memoizedLCS(x,y):
    i = len(x) - 1
    j = len(y) - 1

    #This Columns then rows values.
    mvec = [[-1 for i in range(len(y))] for j in range(len(x))]
    return memoizedLCSWrapper(x, y, i, j,mvec,svec)

def memoizedLCSWrapper(x, y, i, j,mvec,svec):
    #Base case
    if (i == -1 or j == -1):
        return 0

    if (mvec[i][j] != -1):
        return mvec[i][j]

    if (x[i] == y[j]):
        svec.append(x[i])
        result = memoizedLCSWrapper(x,y,i-1,j-1,mvec,svec)+1
        # svec.append(x[i])
        #I believe so
    else:
        result = max(memoizedLCSWrapper(x,y,i-1,j,mvec,svec),memoizedLCSWrapper(x,y,i,j-1,mvec,svec))

    mvec[i][j] = result

    return result


def main():
    global svec
    svec = []
    n = [4, 5, 10]

    # SHOWING THAT THE TWO FUNCTIONS ARE WORKING AND GIVE THE SAME RESULT:
    # for values in n:
    #     x = generateFixedArray(values)
    #     y = generateFixedArray(values)
    #
    #     print("For size: ", values, "The first Array is: ", x)
    #     print("For size: ", values, "The second Array is: ", y)

    y = [1,5,5,3,6,12,69]
    x = [1,69]

    # zRecursive = recursiveLCS(x, y)
    zmemoized = memoizedLCS(x, y)

    # print("The recursive solution is: ", zRecursive)
    print("The memoized solution is: ", zmemoized)
    print(svec.reverse())

    # print("Are the results for both methods the same?: ", equals(zRecursive, zmemoized), "\n\n")

    # TIMING AND PLOTTING THE TIMINGS:
    #
    # memoizedTiming = []
    # recursiveTiming = []
    #
    #
    # n=[1,5,15,20,30,40]
    # exp = np.array([math.pow(2, values) for values in n])
    # squared = np.array([math.pow(values,2) for values in n ])
    #
    # for values in n:
    #     x = generateFixedArray(values)
    #     y = generateFixedArray(values)
    #
    #
    #     start_time = timer()
    #     zRecursive = recursiveLCL(x,y)
    #     end_time = timer()
    #     recursiveTiming.append(end_time - start_time)
    #
    #     start_time = timer()
    #     zmemoized = memoizedLCL(x,y)
    #     end_time = timer()
    #     memoizedTiming.append(end_time - start_time)
    #
    # recursiveScale = zRecursive[-1]/exp[-1]
    # memoizedScale = zmemoized[-1]/squared[-1]
    #
    # plt.figure(1)
    # plt.plot(n, recursiveTiming)
    # plt.plot(n, exp)
    # plt.ylabel("Time")
    # plt.xlabel("n")
    # plt.title("Recursive Timing")
    # plt.legend(["recursive", str(round(recursiveScale, 2)) + "*2^n"])
    #
    # plt.figure(2)
    # plt.plot(n, memoizedTiming)
    # plt.plot(n, squared)
    # plt.ylabel("Time")
    # plt.xlabel("n")
    # plt.title("Memoized Timing diagram")
    # plt.legend(["Memoized Timing", str(round(memoizedScale, 2)) + "*n^2"])
    #
    # plt.show()


if __name__ == '__main__':
    main()

