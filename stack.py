

class Stack:
    
    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push_back(self, value):
        node = self.Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.len +=1
    
    def pop_node(self):
        value = self.head.value
        if self.len == 1:
            self.head = None
            self.tail = None
            self.len-=1
        elif self.head != None:
            current_node = self.head
            while current_node.next:
                previous_node = current_node
                current_node = current_node.next
            value = current_node.value
            previous_node.next = None
            self.tail = previous_node
            self.len -= 1
        return value