import numpy as np
import sys
import math
import copy
import heapq
import operator  # for sorting lists of classes by attribute
import bitstring
from timeit import default_timer as timer
from datetime import timedelta


class HuffmanNode:
    """Huffman encoding tree node"""

    character = -1  # the character represented
    index = -1  # index of character (integer)
    count = -1  # character frequency (count) in the file
    left = []  # left child node
    right = []  # right child node
    code = bitstring.BitString()  # bitstring code for the character

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

    # Code Missing: mark and delete any characters that don't occur in the file
    # i.e., nodes should be as long as the number of unique characters in the file (not 256 things long)
    # Hint: Eliminate zero counts, sorting may help.

    # Traverse through the list, if count == 0, delete node.
    nodes = sorted(nodes, key=lambda value: (value.count))

    while (nodes[0].count == 0):  # We pruned the tree
        del nodes[0]
    # print("dummy")

    return nodes


def createhuffmantree(huffmannodes):
    """ Create the huffman tree
        Using heapq functionality to build the tree from a priority queue"""
    node_heap = copy.deepcopy(huffmannodes)  # first create a copy
    heapq.heapify(node_heap)  # create heap
    # Code Missing: Create the Huffman Node Tree using the Min Priority Queue (heap)
    for i in range(1, len(node_heap)):
        leftNode = heapq.heappop(node_heap)
        rightNode = heapq.heappop(node_heap)

        # suspicious!!
        parentNode = HuffmanNode(bytes())

        parentNode.left = leftNode
        parentNode.right = rightNode
        parentNode.count = leftNode.count + rightNode.count
        heapq.heappush(node_heap, parentNode)

    return heapq.heappop(node_heap)  # final node is the tree we want


def codehuffmantree(huffmantreenode, nodecode):
    """ Traverse Huffman Tree to produce Prefix Codes"""
    # huffmantreenode.print()
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


# Pre-order traversal
def listhuffmancodes(huffmantreenode, codelist):
    """ Create a list of Prefix Codes from the Huffman Tree"""
    if (huffmantreenode.left == [] and huffmantreenode.right == []):
        codelist[huffmantreenode.index] = huffmantreenode.code
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
        # consider getting rid of the nones with proper hashmapping.

        if codelist[i] != None:
            print(len(codelist[i].bin))
            print("character ", chr(i), " maps to code ", codelist[i].bin)

    ###encode the file###
    with open(filename, 'rb') as f:
        filecode = bitstring.BitString()
        while True:
            c = f.read(1)
            index = int.from_bytes(c, sys.byteorder)
            if c:
                filecode.append(codelist[index])
            else:
                break  # eof
    # header.write(str(len(codelist[i].bin))) I left it here for convenience.

    # Writing the header in the file
    with open(filename + ".huf", 'w') as header: #Header represent the upcoming codes lengths to decrypt.
        # Header got the length! Ex. (930176) edge case if 0 is presented
        for i in range(0, 256):
            if codelist[i] != None:
                if (len(codelist[i].bin) < 10):
                    header.write(str(len(codelist[i].bin)))
                else:  # I can make it more robust
                    header.write('0')
                    header.write(str(len(codelist[i].bin)))
        header.write("\n")  # for readability
        header.write("\n")  # for readability
    # Writing the codes in the file
    with open(filename + ".huf", 'a') as charCodes:
        for i in range(0, 256):
            if codelist[i] != None:
                charCodes.write(codelist[i].bin)
                print(codelist[i].bin, end="")
        charCodes.write("\n")  # for readability
        charCodes.write("\n")  # for readability

    # Writing the encrypted file
    with open(filename + ".huf", 'a') as body:
        body.write(filecode)

        # # header.write("Header\n")
        # #Body of the file writing
        # for i in range(0, 256):
        #     # consider getting rid of the nones with proper hashmapping.
        #     if codelist[i] != None:
        #         header.write(codelist[i].bin)

        # for i in range(0, 256):
        #     if codelist[i] != None:
        #         current = str(chr(i)) + "\t"+str(codelist[i].count)
        #         print(current)
        #
    # write the file
    # with open(filename + ".huf", 'a') as coded_file:


#
#
# # Code Missing: Write the bitstring (and any additional information necessary) to file
#
#
# def huffmandecodefile(filename):
#     """ Decode a Huffman-Coded File"""
#     # Code Missing:
#
#
# # main
filename = "./LoremIpsumLong.rtf"
huffmanencodefile(filename)

# huffmandecodefile(filename + ".huf") #uncomment once this file is written
