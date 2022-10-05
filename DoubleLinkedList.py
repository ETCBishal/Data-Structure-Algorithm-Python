'''
Double Linked List -implemented using python
Name: Bishal jaiswal
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data)  # creating a node with data the given

        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node  # making the new_node as the head of the LinkeList

    def print(self):
        if self.head is None:
            print("DLL is Empty!")
            return

        itr = self.head
        DLL_str = ''
        while itr:
            DLL_str += str(itr.data)+'-->'
            itr = itr.next
        print(DLL_str)

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next  # searching for the node at the end pointing to None

        # when the node found pointing that node to new_node and new_node to that previous node
        itr.next = new_node
        new_node.pre = itr

    def get_length(self):
        length = 0
        itr = self.head
        while itr:  # iterating the linked list till the end
            itr = itr.next
            length += 1
        return length

    def find_index(self, data):
        if self.head is None:
            print("DLL is Empty!")
            return
        index = 0
        itr = self.head
        while itr:  # iterating throughout the list
            if itr.data == data:  # if we found the data provided to find the index then we return with its index
                return index
            itr = itr.next
            index += 1

    def insert_after(self, data_after, data):
        if self.head is None:
            print("DLL is Empty!")
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                new_node = Node(data)
                new_node.prev = itr.next
                itr.next = new_node
                new_node.next = itr.next.prev
                break
            itr = itr.next

    def insert_at(self,index,data):
        if index < 0 or index>=self.get_length():
            raise Exception("Index Out of Range!")

        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        new_node=Node(data)
        for _ in range(1,index-1):
            itr = itr.next

        new_node.prev = itr
        new_node.next = itr.next
        itr.next.prev = new_node
        itr.next = new_node       

    def insert_before(self, data_before, data_to_insert):
        if self.head is None:
            print("DLL is Empty!")
            return

        itr = self.head
        while itr:
            if itr.data == data_before:
                index = self.find_index(data_before)
                self.insert_at(int(index),data_to_insert)
                break

            itr = itr.next


    def insert_list_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_begining(data=data)

    
    def remove_at(self,index):
        if self.head is None:
            print("DLL is Empty!")
            return

        if index <0 or index >= self.get_length():
            raise Exception("Index Out Of Range!")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                    return
            itr = itr.next
            count += 1

    def print_forward(self):
        self.print()

    def print_backward(self):
        if self.head is None:
            print("DLL is Empty!")
            return

        itr = self.get_last_node()
        listStr = ''
        while itr:
            listStr += str(itr.data)+'-->'

            itr = itr.prev
        print(listStr)
            


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr




if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert_at_begining("Bishal")
    dll.insert_at_begining("Bikash")
    dll.insert_at_end("Samir")
    dll.insert_at_end("Sarad")
    print("DLL Length:", dll.get_length())
    print(dll.find_index("Sarad"))
    dll.print()
    dll.insert_after("Sarad", "Bimal")
    dll.print()
    dll.insert_before("Bimal", "Aaman")
    dll.print()
    dll.insert_at(3,"Conda")
    dll.print()
    dll.insert_before("Bishal","Harry")
    dll.print()
    dll.insert_list_values(["Harry","Bishal","Tech with Tim","Web Code"])
    dll.print()
    dll.remove_at(2)
    dll.print()
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(0,"BlackPanthor")
    dll.print()
    
    
