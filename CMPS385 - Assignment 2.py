class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def DoublyLinkedListInsert(node, data):
    if node is None:
        return
    newNode = Node(data)
    newNode.prev = node
    newNode.next = node.next

    if node.next:
        node.next.prev = newNode
    
    node.next = newNode

def DoublyLinkedListDelete(head, position):
    if head is None:
        return None
    
    if position < 0:
        return head
    
    if position == 0:
        if head.next:
            head.next.prev - None
        return head.next
    
    current = head
    count = 0
    while current and count < position:
        current = current.next
        count += 1
    
    if current is None:
        return head
    
    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next

    del current
    return head

def Display(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next

#Create doubly linked list and add values
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2

#Doubly linked list before insertion
Display(head)
print("")

#Insert a node
DoublyLinkedListInsert(node2, 4)

#Doubly linked list after insertion
Display(head)
print("")

#Delete a node
DoublyLinkedListDelete(head, 1)

#Doubly linked list after deletion
Display(head)