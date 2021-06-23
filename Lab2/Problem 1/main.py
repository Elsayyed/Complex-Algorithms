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

def problem2(n):
    if(n<1):
        return 1
    else:
        value = n/2
        return 8*mergeSort(value)+(n*n)

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
        return 2
    return Factorial(n-1) + 1

def Hanoi(n):
    if (n <= 1):
        return 1
    return 2 * Hanoi(n-1) + 1

if __name__ == '__main__':
    sys.setrecursionlimit(15000)
    # functionName = input("""Enter the name of the function for calculating the cost,Please choose of the following\n1)mergeSort\n2)TowerOfHanoi\n3)T3\n4)Special\n""") #for now dummy
    nvec = range(1,2500,50)
    nvec = np.array(nvec)
    mnvec = range(0,20,1)

    problem2list = [50,100,200,400,800,1000]

    # cost1 = evaluaterecurrenc(eval(functionName),nvec)

    cost1 = evaluaterecurrenc(mergeSort,nvec)
    cost2 = evaluaterecurrenc(T3,nvec)
    cost3 = evaluaterecurrenc(Hanoi,mnvec)
    cost4 = evaluaterecurrenc(Factorial, nvec)

    cost5 = evaluaterecurrenc(problem2, problem2list)
    print("The cost array for problem 2 is: \n")
    print(cost5)

    loggedValues = [n * (math.log(n)) for n in nvec]
    loggedValues = np.array(loggedValues)

    expValues = [math.pow(2,n) for n in mnvec]
    expValues = np.array(expValues)


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
    plt.legend(["T(n) = 1+2T(n/2)+n",str(round(mergeScaleFactor,2))+"*nlog(n)"])

    plt.figure(2)
    plt.plot(nvec,cost2)
    plt.plot(nvec,  T3ScaleFactor * loggedValues)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("T3")
    plt.legend(["T(n) = 5T(n/3)+n",str(round(T3ScaleFactor,2))+"*nlog(n)"])

    plt.figure(3)
    plt.plot(mnvec,cost3)
    plt.plot(mnvec, HanoiScaleFactor * expValues)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("Hanoi")
    plt.legend(["T(n) = 2T(n-1) +1 ",str(round(HanoiScaleFactor,2))+"*2^n"])

    plt.figure(4)
    plt.plot(nvec,cost4)
    plt.plot(nvec, FactorialScaleFactor*nvec)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("Factorial")
    plt.legend(["T(n) = T(n-1) + 1", str(round(FactorialScaleFactor, 2)) + "*n"])
    #
    plt.show()


