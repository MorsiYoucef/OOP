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
        def insert_values(self,data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)
    def get_length(self):
        s = 0
        itr = self.head
        while itr.next:
            s+=1
            itr=itr.next
        return s
    def remove_at(self,index):
        if index<0 and index>=self.get_length():
            raise Exception("invalide index")
        if index == 0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            while itr.next:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                count+=1
                itr = itr.next
    def insert_at(self,index,data):
        if index<0 and index>=self.get_length():
            raise Exception("invalide index")
        if index == 0:
            self.insert_at_beginning(data)
        else:
            count = 0
            itr = self.head
            while itr.next:
                if count == index:
                    itr2 = Node(data,None)
                    itr3 = itr.next
                    itr.next = itr2
                    itr2.next = itr3
                    break
                count+=1
                itr = itr.next
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
    #########################################
    ls = Linked_list()
    a = [1 , 2 , 3, 4,5,6,7,8,9]
    ls.insert_values(a)
    ls.remove_at(0)
    # ls.insert_at(0,5)
    ls.printf()



