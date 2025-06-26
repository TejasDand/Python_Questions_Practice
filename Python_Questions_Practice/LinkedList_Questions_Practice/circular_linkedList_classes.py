# Circular Linked List by using only Classes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
         self.head = None

    # Add a node at the end
    def append(self, data):
        new_Node = Node(data)

        if not self.head:
            self.head = new_Node
            new_Node.next = self.head   # Point to itself to make it circular
        else:
            current = self.head
            while current.next != self.head:    # Loop until last node
                current = current.next
            current.next = new_Node     # Link last node to new node
            new_Node.next = self.head   # Make new node point back to head

    # Display the list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:    # Stop when we circle back to head
                break
        print("(Back to Head)")

print("Circular Linked List:")
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.display()