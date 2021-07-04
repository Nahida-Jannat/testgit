#Data Structure Queue Implementation with function:

def Queue():
   queue = []
   return queue

def is_empty(queue):
   if len(queue) == 0:
      return True
   else:
      return False

def enqueue(queue, value):
   queue.append(value)

def dequeue(queue):
   if len(queue) < 1:
      return None
   return queue.pop(0)

def front(queue):
   return queue[0]
    
def rear(queue):
   return queue[-1]

Q = Queue()

print("IsEmpty: ", is_empty(Q))
#Add elements in a stack using enqueue()
enqueue(Q ,50)
enqueue(Q ,100)
enqueue(Q ,150)
enqueue(Q ,200)
enqueue(Q ,250)

print("After Enqueue: ", Q)
print("Front: ", front(Q))
print("Rear: ", rear(Q))
print("IsEmpty: ", is_empty(Q))

#remove elements in a stack using pop()
dequeue(Q)
dequeue(Q)
dequeue(Q)
dequeue(Q)

print("after poping: ", Q)
print("Front: ", front(Q))
print("Rear: ", rear(Q))

dequeue(Q)
print("After Enqueue again: ", Q)
print("IsEmpty: ", is_empty(Q))
