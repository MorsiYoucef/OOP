class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
class Linked_list:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    def printf(self):
        if self.head is None:
            print("the linked list is empty")
        itr = self.head
        ls = ''
        while itr :
            ls += str(itr.data) + "-->"
            itr = itr.next
        print(ls)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
if __name__ == "__main__":
    ll = Linked_list()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(10)
    # ll.insert_at_beginning(15)
    ll.insert_at_end(12)
    ll.insert_at_beginning(15)
    ll.insert_at_end(14)
    ll.insert_at_end(18)
    ll.insert_at_beginning(18)
    print(ll.head)
    ll.printf()


