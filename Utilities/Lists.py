from enum import Enum, auto

class LinkedListTypes(Enum):
    SINGLY_LINKED_LIST = auto
    DOUBLY_LINKED_LIST = auto

class DistinctNull:
    pass
dict()
class Node:


    def __init__(self, content, next=None):
        self.content = content # Data value 
        self.next:Node = next # The link to next node

    
    def __str__(self):
        return f"Node Data = {self.content}"

class LinkedList:

    def __init__(self, list_type: LinkedListTypes = LinkedListTypes.SINGLY_LINKED_LIST):
        pass
        self.size:int = 0
        self.head:Node = None
        self.tail:Node = None

    pass



    def append(self, node_content):
        '''
        Appends a node to the end of the list
        
        '''
        
        if self.head is not None and self.tail is not None and self.size != 0:
            '''Case when the list is not empty'''
            self.tail.next = Node(node_content, None)
            self.tail = self.tail.next
            
        else:
            self.head = Node(node_content, None)
        self.size = self.size + 1
        new_node = None
        pass

    def remove(self, index:int)->Node:
        ''''''
        pass

    def prepend(self, node_content):
        '''insert object at the beginning of the list'''
        self.insert(node_content, 0)
        pass

    def insert(self, node_content, index: int):
        '''Insert a node before the index'''
        prev:Node = None
        curr:Node = self.head
        
        if not index >= 0:
            raise IOError("The index must be at least 0")
        elif index > self.size:

            raise IOError(f"The list size is not large enough to insert the node at the {index} index" )

        elif index == 0:
            temp = self.head
            self.head = Node(node_content, temp)
            
        iter_index = 0

        while iter_index < index:
            curr = curr.next
            iter_index = iter_index

        self.size = self.size + 1
        print(self.head.content)

    def _get_node_by_index(self, index):
        '''Returns the node at the index if'''
        if self.size < index:
            raise IOError("The index is not present in the linkedlist")
        elif index < 0 or isinstance(index, int):
            raise IOError("The index provided must be a non negative integer")
        
        curr:Node = self.head
        iter_index = 0

        while iter_index < index:
            curr = curr.next
            iter_index = iter_index

        return curr

        
        
        pass
    def _add_first(node_content):
        pass
    
    def pop(self, index:int):
        '''Remove and return the node at the specific index in the list'''
        
        
        pass

    def find(self, index:int) -> Node:
        curr = self.head
        while index > 0:
            curr = curr.next
            index = index - 1
        return curr
        
    def prepend(self, node_content):
        pass

    
    def __str__(self):
        curr = self.head
        output_str = "["
        counter = 0
        while curr is not None:
            
            output_str = output_str + f"{curr.content}, "
            curr = curr.next
        
        output_str = output_str + "]"
        return output_str
        pass




    
class DoublyLinkedNode(Node):
    next: Node
    prev: Node
    pass

    def __init__(self, content, next, prev):
        super().__init__(content)
        self.next = next
        self.prev = prev

class SinglyLinkedNode(Node):
    next: Node
    def __init__(self, content, next):
        
        super().__init__(content)
        self.next = next
    pass


def main():
    li = LinkedList()
    li.insert("A", 0)
    li.insert("B", 0)
    li.insert("C", 0)
    curr = li.head
    while curr is not None:
        print(curr)
        curr = curr.next

    
    pass
    print(li)
main()

my_list = list()
