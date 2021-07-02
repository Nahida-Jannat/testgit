#Stack using Class

class Stack():
    def __init__(self):
        self.item = []

    def push(self, value):
        self.item.append(value)
        return value

    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return len(self.item) == 0

    def peek(self):
        return self.item[-1]


    def size(self):
        return len(self.elements)

stack = Stack()
    
#checking isEmpty method
print("Stack Empty Status: ", stack.isEmpty())

#Add elements with push()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
stack.push(25)
stack.push(30)

print("after pushing: ", stack.item)

#printing top value
print("Top Value: ", stack.item[-1])
print("Stack empty status: ",stack.isEmpty())

#printing top value
print("New Top Value", stack.peek())

#pop Stack element    
stack.pop()

print("after poping: ", stack.item)
print("New Top Value: ",stack.peek())

# popping  all the element
stack.pop()
stack.pop()
stack.pop() 
stack.pop()
stack.pop() 
print("after poping all elements: ", stack.item)


    ## checking the isEmpty method for the last time -> true
print("Stack empty status: ",stack.isEmpty())





