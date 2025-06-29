# Doubly Linked List by using only Classes

class Node:
    def __init__(self, data):
        self.data = data    # The actual data (value) stored in the node
        self.next = None    # Pointer to the previous node (starts as None)
        self.prev = None    # Pointer to the next node (starts as None)

class DoublyLinkedList:
    def __init__(self):
        self.head = None    # Start of the list

    def append(self, data):
        new_Node = Node(data)   # Create a new node with the given data

        if self.head is None:
            self.head = new_Node    # If list is empty, new node becomes the head
            return
        
        current = self.head
        while current.next:
            current = current.next  # Move to the last node

        current.next = new_Node     # Set current node’s next to new node
        new_Node.prev = current     # Set new node’s prev to current node

    def display_forward(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    def display_backward(self):
        current = self.head
        if current is None:
            print("List is empty")
            return
        
        # Move to the last node
        while current.next:
            current = current.next

        # Now go backward
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


# Example usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()