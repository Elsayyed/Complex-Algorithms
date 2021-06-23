import random
from timeit import default_timer as timer
import math
# Note: this won't run unless you have matplotlib installed
import matplotlib.pyplot as plt


# def mergeList(randomList, lo, midPoint, hi):
#     mid = midPoint + 1
#
#     if (randomList[midPoint] <= randomList[mid]):
#         return;
#
#     while lo <= midPoint and mid <= hi:
#         if randomList[lo] < randomList[mid]:
#             lo += 1
#         else:
#             tempValue = randomList[mid]
#             index = mid
#
#             while index != lo:
#                 randomList[index] = randomList[index - 1];
#                 index -= 1;
#
#             randomList[lo] = tempValue;
#             lo += 1
#             midPoint += 1
#             mid += 1

# def mergeList(randomList, lo, midPoint, hi):
#     tempList =[0] * (hi-lo + 1)
#     start = lo
#     midStart = midPoint + 1
#     tempIndex = 0
#
#     #the reason it's hi-lo that we operate on the right half and left half,
#     #so we don't always operate from zero only the left side of the tree kinda.
#
#     while tempIndex < (hi-lo + 1):
#         if (midStart > hi) or (randomList[start] < randomList[midStart] and start <= midPoint):
#             tempList[tempIndex] = randomList[lo]
#             tempIndex += 1
#             lo += 1
#         else:
#             tempList[tempIndex] = randomList[midStart]
#             tempIndex += 1
#             midStart += 1
#
#     for i in range((hi-lo + 1)):
#         randomList[i + lo] = tempList[i]


def mergeList(A, p, q, r):
    left = q - p + 1
    right = r - q

    L = [0] * (left+1)  # considerr extra place later!
    R = [0] * (right+1)  # considerr extra place later!

    for i in range(left):
        L[i] = A[p + i]

    for j in range(right):
        R[j] = A[q + j + 1]

    L[left] = math.inf
    R[right] = math.inf

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSortAux(randomList, lo, hi):
    if lo < hi:  # incase of equality "size = 1" it'll stop // base case!
        midPoint = int((lo + hi - 1) / 2)
        mergeSortAux(randomList, lo, midPoint)
        mergeSortAux(randomList, midPoint + 1, hi)
        mergeList(randomList, lo, midPoint, hi)


def mergeSort(randomList, listSize):
    mergeSortAux(randomList, 0, listSize - 1)


def generateRandomArray(listSize):
    for i in range(listSize):
        n = random.randint(1, 1000)
        randomList.append(n)
    return randomList


def sortedAscending(A):
    for i in range(0, len(A) - 1):
        if A[i] > A[i + 1]:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    loop = True
    while loop:
        try:
            listSize = int(input("Enter the size of the array/list: "))
            loop = False
        except:
            print("Wrong input, please enter an integer!")

    randomList = []

    ####### In-place Merge Sort Library ########
    randomList = generateRandomArray(listSize)

    start_time = timer()
    Asorted = sorted(randomList)
    end_time = timer()

    print("\nPython Elapsed time= ", end_time - start_time)
    print("Is the List Sorted?: ", sortedAscending(Asorted))
    #############################

    ####### In-place Merge Sort ########
    startTime = timer()
    mergeSort(randomList, listSize)
    endTime = timer()
    print('\n')
    print(randomList)
    print(f"\nElapsed time of the Merge sort algorithm is {endTime - startTime}")
    print("Is the List Sorted?: ", sortedAscending(randomList))
    #############################

    ############## Validation and Data Collection #################
    n = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000]
    pythonTiming = []
    myTiming = []
    counter = 0

    for values in n:
        randomList = generateRandomArray(values)

        start_time = timer()
        Asorted = sorted(randomList)
        end_time = timer()
        pythonTiming.append(end_time - start_time)

        startTime = timer()
        mergeSort(randomList, listSize)
        endTime = timer()
        myTiming.append(endTime - start_time)

    # print(myTiming)
    # print("\n")
    # print(pythonTiming)

    plt.subplot(2, 1, 1)
    plt.plot(n, myTiming)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("My Timing Diagram")

    plt.subplot(2, 1, 2)
    plt.plot(n, pythonTiming)
    plt.ylabel("Time")
    plt.xlabel("n")
    plt.title("My Python Diagram")
    plt.show()

###############################################################
