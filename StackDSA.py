from collections import deque

class Stack:

    def __init__(self):
        self.stack = deque()
        
    def push(self,val):
        return self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# function to reverse any string provided to it
def reverse_string(string):
    stack = Stack()

    # iterating the string and putting the each character of the string in the stack
    for char in string:
        stack.push(char)  

    reversed_str = ''  
    while stack.size() != 0:
        reversed_str += stack.pop()    #taking out each charater from the stack and making a single string

    return reversed_str  # returnin the object of the reversed string

if __name__ == "__main__":
    reversed_string = reverse_string("My name is Bishal jaiswal")
    print(reversed_string)
