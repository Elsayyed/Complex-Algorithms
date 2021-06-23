import numpy as np
import sys
import math
import copy
import heapq
import operator  # for sorting lists of classes by attribute
import bitstring
from timeit import default_timer as timer
from datetime import timedelta
from bitarray import bitarray

class HuffmanNode:
    """Huffman encoding tree node"""
    character = -1  # the character represented
    index = -1  # index of character (integer)
    count = -1  # character frequency (count) in the file
    left = []  # left child node
    right = []  # right child node
    code = bitstring.BitString()  # bitstring code for the character

    # flag = bitstring.BitString('0b0')  #initially assume that all nodes are internal
    flag = 0

    # constructor
    def __init__(self, character):
        self.character = character;
        self.index = int.from_bytes(self.character, sys.byteorder)
        self.count = 0

    # for printing
    def __repr__(self):
        return str("Huffman Node") + str(self.__dict__)

    # for printing
    def __str__(self):
        return str("Huffman Node") + str(self.__dict__)

    # comparison operator required for heapq comparison
    def __lt__(self, other):
        return self.count < other.count

    # print function (non-recursive)
    def print(self):
        print("Huffman Node: ")
        print("\tCharacter = ", self.character)
        print("\tIndex = ", self.index)
        print("\tCount = ", self.count)
        has_left = (self.left != [])
        has_right = (self.right != [])
        print("\tHas left child = ", has_left)
        print("\tHas right child = ", has_right)
        print("\tCode = ", self.code)

        print("\tFlag= ",self.flag)


def isPrev1(index,headerData):
    if(index==0):
        return False

    if(index>1):
        return (headerData[index-1]=="1" and headerData[index-2]!="1")

    return(headerData[index-1]=="1")

def split(word):
    return [char for char in word]

def findCharacter(dataLines,counter):
    go = 8
    charByte = ""
    while(go!=0):
        charByte += dataLines[counter]
        del dataLines[counter]
        go -= 1
    return(int(charByte,2))


def fileEqual(data1,data2):
    for char1,char2 in zip(data1,data2):
        if(char1!=char2):
            return False
    return True

def getfilecharactercounts(filename):
    """ Read a file and count characters """

    f = open(filename, "rb")
    nodes = [];

    # for every character of interest (and then some) create a huffman node
    for i in range(0, 256):
        nodes.append(HuffmanNode(bytes([i])))  # works in python 3

    # loop over file reading a character at a time and increment the count
    # of that character in the list of huffman nodes
    while True:
        c = f.read(1)
        if c:
            index = int.from_bytes(c, sys.byteorder)
            nodes[index].count += 1
        else:
            # print("End of file")
            break

    f.close()

    #Traverse through the list, if count == 0, delete node.
    nodes = sorted(nodes, key=lambda value: (value.count))

    while (nodes[0].count == 0): #We pruned the tree
        del nodes[0]
    return nodes


def createhuffmantree(huffmannodes):
    """ Create the huffman tree
        Using heapq functionality to build the tree from a priority queue"""
    node_heap = copy.deepcopy(huffmannodes)  # first create a copy
    heapq.heapify(node_heap)  # create heap
    for i in range(1, len(node_heap)):
        leftNode = heapq.heappop(node_heap)
        rightNode = heapq.heappop(node_heap)

        parentNode = HuffmanNode(bytes())

        parentNode.left = leftNode
        parentNode.right = rightNode
        parentNode.count = leftNode.count + rightNode.count
        heapq.heappush(node_heap,parentNode)
    return heapq.heappop(node_heap)  # final node is the tree we want

def codehuffmantree(huffmantreenode, nodecode):
    """ Traverse Huffman Tree to produce Prefix Codes"""
    # print(huffmantreenode.character)
    # print("Nodecode = ", nodecode)

    if (huffmantreenode.left == [] and huffmantreenode.right == []):
        huffmantreenode.code = nodecode  # no children - assign code
    else:
        leftcode = copy.copy(nodecode)  # append 0 to left
        leftcode.append(bitstring.Bits('0b0'))
        codehuffmantree(huffmantreenode.left, leftcode)
        rightcode = copy.copy(nodecode)  # append 1 to right
        rightcode.append(bitstring.Bits('0b1'))
        codehuffmantree(huffmantreenode.right, rightcode)

def PreorderTraversal(huffmantreenode,queue):
    if(huffmantreenode!=[]):
        queue.append(huffmantreenode)
        PreorderTraversal(huffmantreenode.left,queue)
        PreorderTraversal(huffmantreenode.right,queue)


def listhuffmancodes(huffmantreenode, codelist):
    """ Create a list of Prefix Codes from the Huffman Tree"""
    if (huffmantreenode.left == [] and huffmantreenode.right == []):
        codelist[huffmantreenode.index] = huffmantreenode.code
        huffmantreenode.flag = 1
    else:
        listhuffmancodes(huffmantreenode.left, codelist)
        listhuffmancodes(huffmantreenode.right, codelist)


def huffmanencodefile(filename):
    """ Read and Encode a File using Huffman Codes"""

    counts = getfilecharactercounts(filename)  # get the counts from the file

    huffmantree = createhuffmantree(counts)  # create and encode the characters
    codehuffmantree(huffmantree, bitstring.BitString())

    codelist = [None] * 256
    listhuffmancodes(huffmantree, codelist)  # get the codes for each character



    for i in range(0, 256):
        if codelist[i] != None:
            print("character ", chr(i), " maps to code ", codelist[i].bin)

    # # # encode the file
    with open(filename, 'rb') as f:
        filecode = bitstring.BitString()
        while True:
            c = f.read(1)
            index = int.from_bytes(c, sys.byteorder)
            if c:
                filecode.append(codelist[index])
            else:
                break  #eof

    with open(filename,'r') as f:
        data = f.readlines()
    dataRead = ""
    for line in data:
        dataRead = dataRead+line

    print("\nNumber of bits(each character is 8 bits) in the original file: ",len(dataRead)*8)
    print("Size of orginal in Kbytes: ",len(dataRead)/1000,"\n")

    queue = []
    headerData =""
    PreorderTraversal(huffmantree, queue)
    for node in queue:
        headerData = headerData + (str(node.flag)) #adding the 0s or 1s
        if(node.flag==1):
            headerData = headerData + (str(node.character.decode("utf-8"))) #if its a 1--> leaf --> print its char


    headerArray = bitarray()
        #Create a bit array for the header
    for i in range(len(headerData)):
        if((headerData[i]!='0' and headerData[i]!='1')):
            headerArray.frombytes(bytes([ord(headerData[i])]))
        else:
            if(headerData[i]=='0'):
                if(isPrev1(i, headerData)):
                    headerArray.frombytes(bytes([ord(headerData[i])]))
                else:
                    headerArray.append(False)
            else:
                if(isPrev1(i, headerData)):
                    headerArray.frombytes(bytes([ord(headerData[i])]))
                else:
                    headerArray.append(True)
    #Indicate end of header
    headerArray.append(True)
    headerArray.frombytes(bytes([ord('\n')]))

    #Create a bit array for the file Body
    string = filecode.bin
    bodyArray = bitarray()
    for character in string:
        if(character == '1'):
            bodyArray.append(True)
        else:
            bodyArray.append(False)

    headerArray.extend(bodyArray)

    #write the headerData + Body into the file
    with open(filename + ".huf", 'wb') as header:
        headerArray.tofile(header)

    return dataRead

def findHeader(dataLines):
    found = 0
    dataList = split(dataLines)
    header=""
    while(found!=2):
        if(dataList[0]=='0'):
            header+=dataList[0]
            del dataList[0]
        elif(dataList[0]=='1'):
            del dataList[0]
            current = chr(findCharacter(dataList,0))
            if(current=='\n'):
                found += 1
                if(found==2):
                    return [header,dataList]
            header += "1"
            header+= current
    return [header,dataList]


def recreateTree(headerData):
    stack = []
    # 0121;1N1b1i
    # i , b ,N, ; , 2
    #i see a 0 --> pop 2 , ; (subtree)
    # i , b ,N , subtree, { , 0
    headerData = headerData.strip()
    counter = len(headerData)-1
    while(counter >=0):
        s = headerData[counter]
        if(headerData[counter] != '0' ):
            child = HuffmanNode(bytes(s, 'utf-8'))
            counter = counter-2
            stack.append(child)
        else:
            if(isPrev1(counter,headerData) ):
                child = HuffmanNode(bytes(s, 'utf-8'))
                counter = counter - 2
                stack.append(child)
            else:
                parent = HuffmanNode(bytes())
                leftChild = stack.pop()
                rightChild = stack.pop()
                parent.left = leftChild
                parent.right = rightChild
                stack.append(parent)
                counter = counter-1
    return stack[0]

def decryptcode(root, dataLines):
    '''
    Traverse left given "0"...Traverse right given "1" **
    for each node we're traversing, **
    check if it's leaf node or not  **
    True: concatenate that corresponding node "letter" in the variable
    and reset the traversing process.
    False: keep reading/traversing
    '''
    array = split(dataLines)
    current = root
    dataDecoded ='' #.write(dataDecoded) && accumlate the strings.
    counter = 0
    letterCounter = 0
    while(counter < len(dataLines)):
        if (current.left == [] and current.right == []):
            found = str(current.character.decode("utf-8"))
            dataDecoded = dataDecoded + found
            letterCounter = letterCounter + 1
            current = root
        elif (array[counter] == '0'): #left
            current = current.left
            counter = counter + 1
        else:#right
            current = current.right
            counter = counter + 1

    found = str(current.character.decode("utf-8"))
    dataDecoded = dataDecoded + found
    return dataDecoded

def huffmandecodefile(filename):
    """ Decode a Huffman-Coded File"""

    dataLines = bitarray() #created object
    with open(filename , 'rb') as headerRead:
        dataLines.fromfile(headerRead) #change a t the file as a bitarray

    dataLines = dataLines.to01() #convert to string

    print("Number of bits in the encoded File: ",len(dataLines))
    print("Size of encoded in Kbytes: ", len(dataLines) / 8000,"\n")

    data= findHeader(dataLines)
    dataLines = data[1]
    headerData = data[0]

    root = recreateTree(headerData)

    data = decryptcode(root,dataLines) #Data decoded

    print("Data Compression rate: ", len(data)*8/len(dataLines),"\n")

    with open("./LoremIpsumLongDecoded.rtf", 'w') as decodedFile:
        decodedFile.write(data)

    return data
# main
filename = "./LoremIpsumLong.rtf"
readFile = huffmanencodefile(filename)
decodeFile = huffmandecodefile(filename + ".huf") #uncomment once this file is written

print("Are the two files equal (the original file and the decoded file):",fileEqual(readFile,decodeFile))
