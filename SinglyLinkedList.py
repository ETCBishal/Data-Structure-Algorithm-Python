'''
Singly Linked List - implemented using python
Name: Bishal jaiswal
'''


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty!")
            return

        itr = self.head
        list_str = ""
        while itr:
            list_str += str(itr.data)+"-->"
            itr = itr.next

        print(list_str)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next  # checking if we got None or not

        itr.next = Node(data, None)  # when we got None

    def insert_list_values(self, list_data):
        self.head = None
        for data in list_data:
            self.insert_at_end(data)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")

        if index == self.head:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, val):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")

        if index == 0:
            self.insert_at_begining(val)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                #node = Node(data,itr.next)
                #itr.next = node
                itr.next = Node(val, itr.next)
                break
            itr = itr.next
            count += 1

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            print("Linked List is Empty!")
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def remove_by_value(self,data_to_remove):
        if self.head is None:
            print("Linked List is Empty!")
            return
        itr = self.head
        count = 0
        found = False
        while itr:
            if itr.data == data_to_remove:
                self.remove_at(count)
                found = True
                break                
            itr = itr.next
            count+=1
        if found == False:
            print("Element not found!")


if __name__ == "__main__":
    
    ll = LinkedList()
    ll.insert_list_values(["Bishal", "Samir", "Sharad"])
    list_length = ll.get_length()
    print(f"<Node_length={list_length}>")
    ll.print()
    ll.insert_at(2, "Harry")
    ll.insert_after_value("Harry","PythonConda")
    ll.insert_after_value("PythonConda","C++")
    ll.print()
    ll.remove_by_value("A")
    ll.remove_by_value("C++")
    ll.print()
