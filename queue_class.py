# Queue implementation in Python

class Queue():
    def __init__(self):
        self.queue = []

# enqueue() : add an element from the end of the Queue
    def enqueue(self, value):
        self.queue.append(value)

# dequeue() : remove an element from the front of the Queue
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)
        
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]

    def display(self):
        return self.queue



Q = Queue()

print("IsEmpty: ", Q.isEmpty())     #Check if the Queeue is empty

Q.enqueue(11)   # add elements
Q.enqueue(22)
Q.enqueue(33)
Q.enqueue(44)
Q.enqueue(55)

print("After Enqueue: ", Q.display() )    #display the Queue
print("After Enqueue: ", Q.front())
print("After Enqueue: ", Q.rear())
Q.dequeue()     #remove an element from the front of the Queue
Q.dequeue()

print("After Dequeue: ", Q.display())
print("After Dequeue: ", Q.front())
print("After Dequeue: ", Q.rear())

print("IsEmpty: ", Q.isEmpty())
