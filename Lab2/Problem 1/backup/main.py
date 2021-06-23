import sys
import matplotlib.pyplot as plt
import math

import numpy as np


def evaluaterecurrenc(myFunction,nvec):
    timings = []
    for value in nvec:
        print(value)
        timing = myFunction(value)
        timings.append(timing)
    return timings

#The recurrance relation for merge sort
def mergeSort(n):
    if(n<1):
        return 1
    else:
        value = n/2
        return 1+2*mergeSort(value)+n

#the recurrance relation for T3
def T3(n):
    if(n<1):
        return 1
    return 5*T3(n//3)+n

def Factorial(n):
    if(n<1):
        return 1
    return Factorial(n-1) + 1

def Hanoi(n):
    if (n <= 1):
        return 1
    return 2 * Hanoi(n-1) + 1

if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    # functionName = input("""Enter the name of the function for calculating the cost,Please choose of the following\n1)mergeSort\n2)TowerOfHanoi\n3)T3\n4)Special\n""") #for now dummy
    nvec = range(1,1100,100)
    mnvec = range(0,20,1)
    # cost1 = evaluaterecurrenc(eval(functionName),nvec)

    cost1 = evaluaterecurrenc(mergeSort,nvec)
    cost2 = evaluaterecurrenc(T3,nvec)
    cost3 = evaluaterecurrenc(Hanoi,mnvec)
    cost4 = evaluaterecurrenc(Factorial, nvec)

    loggedValues = [n * math.log(n) for n in nvec]
    loggedValues = np.array(loggedValues)
    expValues = [math.pow(2,n) for n in mnvec]
    expValues = np.array(expValues)
    nvec = np.array(nvec)

    mergeScaleFactor = cost1[-1] / loggedValues[-1];
    T3ScaleFactor = cost2[-1] / loggedValues[-1];
    HanoiScaleFactor = cost3[-1] / expValues[-1];
    FactorialScaleFactor = cost4[-1] / nvec[-1];

    plt.figure(1)
    plt.plot(nvec,cost1)
    plt.plot(nvec, mergeScaleFactor * loggedValues)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("mergeSort")
    plt.legend(["Dataset 1", str(rou) + "Dataset 2"])

    plt.figure(2)
    plt.plot(nvec,cost2)
    plt.plot(nvec, T3ScaleFactor * loggedValues)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("T3")

    plt.figure(3)
    plt.plot(mnvec,cost3)
    plt.plot(mnvec, HanoiScaleFactor * expValues)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("Hanoi")

    plt.figure(4)
    plt.plot(nvec,cost4)
    plt.plot(nvec, FactorialScaleFactor*nvec)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("Factorial")

    plt.show()


