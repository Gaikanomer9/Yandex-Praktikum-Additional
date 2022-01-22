class Node:
    def __init__(self, value):
        self.Next = None
        self.Value = value
    
    def __str__(self):
        return f'[{self.Value}]->{self.Next}'


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.Next = node2
node2.Next = node3

print(node1)

class LinkedList():
    def __init__(self, root: Node):
        self.root = root

    def __str__(self):
        return f'|{self.root}|'
    
    def append(self, node: Node):
        temp = self.root
        while temp.Next:
            temp = temp.Next
        temp.Next = node

    def length(self):
        raise NotImplementedError('Implement length function first')

list1 = LinkedList(node1)

print(list1)
list1.append(Node(4))
print(list1)
list1.length()