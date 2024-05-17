class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def ZigZagTranversal(root):
    if root is None:
        return

    currentStack = []
    nextStack = []

    ltr = True

    # append root to current stack
    currentStack.append(root)

    while len(currentStack)>0:
        # pop from stack
        temp = currentStack.pop(-1)
        print(temp.data, end = " ")

        if ltr:
            # if ltr is true push left  before right
            if temp.left:
                nextStack.append(temp.left)
            if temp.right:
                nextStack.append(temp.right)
        else:
            # else push right before left
            if temp.right:
                nextStack.append(temp.right)
            if temp.left:
                nextStack.append(temp.left)

        if len(currentStack)==0:
            # reverse ltr to push node in opposite order
            ltr = not(ltr)
            # swapping of stacks
            currentStack , nextStack = nextStack , currentStack

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    ZigZagTranversal(root)