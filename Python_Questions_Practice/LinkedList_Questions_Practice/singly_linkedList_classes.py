# Singly Linked List by using only Classes

# Node class represents a single element in the list
class Node:
    def __init__(self, data):
        self.data = data    # Store the value
        self.next = None    # Initialize next as None

# Singly Linked List class to manage the list
class SinglyLinkedList:
    def __init__(self):
        self.head = None    # Initially the list is empty
    
    # Add a node at the end of the list
    def append(self, data):
        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node    # If list is empty, make new node the head
        else:
            current = self.head
            while current.next:     # Traverse to the last node
                current = current.next
            current.next = new_Node     # Link the last node to the new node
    
    # Display all elements in the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")   # End of List


print("Singly Linked List:")
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()