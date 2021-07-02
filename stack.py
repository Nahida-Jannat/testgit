#Data Structure Stack Implementation with function:

def my_stack():
    stack = []
    return stack

def empty_stack(stack):
    if len(stack) == 0:
        return True
    else:
        return False

def push(stack, value):
    stack.append(value)

def pop(stack):
    if empty_stack(stack):
        return "Stack is empty"
    return stack.pop() 

Stack = my_stack()

#Add elements in a stack using push()
push(Stack, 1)
push(Stack, 2)
push(Stack, 3)
push(Stack, 4)
push(Stack, 5)
print("After Push: ", Stack)

#remove elements in a stack using pop()
pop(Stack)
pop(Stack)
print("after poping: ", Stack)

#print Top Value
print("Top Value: ", Stack[-1])

pop(Stack)
print("After poping again: ", Stack)
print("New top value: ", Stack[-1])