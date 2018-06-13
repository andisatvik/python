
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
                                                       
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
                                                                                                                                         
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next


# Populate Linked List

length = int(input("Enter size of LL: "))

a_ll = linked_list.LinkedList()
# print(a_ll)

i=1
while (i<=length):
    data = int(input("Enter data: "))
    a_ll.append(data)
    i+=1

# Reverse the list:Wq
# 1. Set prev = None, curr = head, follow = head.next

a_ll.display()

