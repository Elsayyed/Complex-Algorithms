# Problem 1
import math
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import numpy as np


def recursiveFibonacci(n):
    if n < 0:
        print("Invalid Input, Fibonacci works for values greater than 0");
        return None

    if (n == 0 or n == 1):
        return 1

    return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);


def memoizedFibonacciBootstrap(n):
    if n < 0:
        print("Invalid Input, Fibonacci works for values greater than 0");
        return None

    memolist = [-1 for i in range(n + 1)];

    return memoizedFibonacci(n, memolist)


def memoizedFibonacci(n, memolist):

    if (memolist[n] != -1):
        return memolist[n];

    if (n == 0):
        memolist[n] = 1;
        return 1

    if (n == 1):
        memolist[n] = 1;
        return 1

    result = memoizedFibonacci(n - 1, memolist)\
             + memoizedFibonacci(n - 2, memolist);

    memolist[n] = result;

    return result

def  bottomupFibonacci(n):

    if (n == 0 or n == 1):
        return 1

    values = [1,1]
    counter = 2

    while counter <= n:
        values.append(values[counter-2]+values[counter-1]);
        counter = counter + 1

    return values[n]

def main():
    n = [0,5,10,15,20,25,30,35,40]
    nhigh = [0,50,150,200,250,300,400,450,450]
    # n = [20]
    recursiveFibonacciTiming = []   #A
    memoizedFibonacciTiming = []    #B
    bottomupFibonacciTiming = []    #C

    recursitveOn = [math.pow(2,value) for value in n]
    recursitveOn = np.array(recursitveOn);

    memoizedOn = n
    memoizedOn = np.array(memoizedOn);

    bottomupOn= n
    bottomupOn = np.array(bottomupOn);


    for values in n:

        # complexity 2^n.
        start_time = timer()
        result = recursiveFibonacci(values)
        # print(result)
        end_time = timer()
        recursiveFibonacciTiming.append(end_time - start_time)

    for values in nhigh:
        start_time = timer()
        result = memoizedFibonacciBootstrap(values)
        end_time = timer()
        # print(result)
        memoizedFibonacciTiming.append(end_time - start_time)

        start_time = timer()
        result = bottomupFibonacci(values)
        # print(result)
        end_time = timer()
        bottomupFibonacciTiming.append(end_time - start_time)

    recursiveScale = recursiveFibonacciTiming[-1]/recursitveOn[-1]
    memoizedScale = memoizedFibonacciTiming[-1]/memoizedOn[-1]
    bottomUpScale = bottomupFibonacciTiming[-1]/bottomupOn[-1]

    plt.subplot(3, 1, 1)
    plt.plot(n, recursiveFibonacciTiming)
    plt.plot(n,recursiveScale * recursitveOn)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("recursive Fibonacci Timing Diagram")
    plt.legend(["Recursive Fibonacci",str(round(recursiveScale,12))+"*2^n"])
    # plt.legend(["T(n) = 8T(n/2)+n^2", str(round(factor,5))+"*OurCodeTiming"])

    plt.subplot(3, 1, 2)
    plt.plot(nhigh, memoizedFibonacciTiming)
    plt.plot(nhigh, memoizedScale * memoizedOn)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("memoized Fibonacci Timing Diagram")
    plt.legend(["Memoized Fibonacci", str(round(memoizedScale,7))+"*n"])

    plt.subplot(3, 1, 3)
    plt.plot(nhigh, bottomupFibonacciTiming)
    plt.plot(nhigh, bottomUpScale*bottomupOn)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title(" bottomup Fibonacci Timing Diagram")
    plt.legend([" bottom up Fibonacci", str(round(bottomUpScale,7))+"*n"])

    plt.show()

if __name__ == '__main__':
    main()
