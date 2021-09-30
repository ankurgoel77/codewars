#https://www.codewars.com/kata/589d581680458f695200008e/train/python

class Node:
    def __init__(self, value, index):
        self.value = 0
        self.index = 0
        self.prod = None
        self.sum = None

def buildTree(arr,Node,index):
    if index == len(arr)-1 :
        return Node(arr[index])

def sum_or_product(arr):
    if len(arr) == 1:
        return arr[0]