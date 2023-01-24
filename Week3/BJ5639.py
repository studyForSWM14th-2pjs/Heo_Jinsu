import sys
sys.setrecursionlimit(10**6)
'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def insert(self, key):
        if self.key > key:
            if self.left: self.left.insert(key)
            else: self.left = Node(key)
        elif self.key < key:
            if self.right: self.right.insert(key)
            else: self.right = Node(key)
        else: raise KeyError(f"Key {key} is already exist")
    
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.key)

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root:
            self.root.insert(key)
        else:
            self.root = Node(key)

inform = BinaryTree()

while True:
    try:
        key = int(input())
    except:
        break
    inform.insert(key)

inform.root.postOrder()
'''
inform = [0]*(10001)

def insertKey(key):
    global inform

    currentIdx = 1
    while inform[currentIdx] != 0:
        if inform[currentIdx] < key:
            currentIdx = currentIdx*2+1
        elif inform[currentIdx] > key:
            currentIdx = currentIdx*2
    inform[currentIdx] = key

def postOrder():
    global inform

    result = list()

    stack = list()
    stack.append(1)
    while stack:
        idx = stack.pop()
        result.append(inform[idx])
        if inform[idx*2]:
            stack.append(idx*2)
        if inform[idx*2+1]:
            stack.append(idx*2+1)
    
    for i in range(len(result)-1,-1,-1):
        print(result[i])

while True:
    try:
        key = int(input())
    except:
        break
    insertKey(key)

postOrder()

# Runtime Error (Index Error) -> Node가 한 쪽으로 치우친 경우...