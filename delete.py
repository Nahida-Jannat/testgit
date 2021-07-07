#linked list implementation
#Add values at begenning in linked list
#Node --> Data | Next

class Node:
   def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

class LinkedList:
   def __init__(self):
      self.head = Node()
      
   def display(self):
      if self.head is None:
         print("Linked list is empty")
         return
      current_node = self.head
      info_str =''
      while current_node:
         info_str = info_str + str(current_node.data) + '-->'
         current_node = current_node.next
      print(info_str)

   def append_at_beginning(self, data):
      node = Node(data, self.head.next)
      self.head.next = node

   def remove(self, remove_item):
      pre = self.head
      if pre is not None:
         if pre.data == remove_item:
            self.head = pre.next
            pre = None
            return

      # while pre is not None:
      #    if pre.data == remove_item:
      #       break
      prev = pre
      pre = pre.next
      if pre == None:
         return
      prev.next = pre.next
      pre = None
   
if __name__ == '__main__':
   ll = LinkedList()

   #item added at beginning
   ll.append_at_beginning(1)
   ll.append_at_beginning(2)
   ll.append_at_beginning(3)

   ll.display()
   ll.remove(2)
   ll.display()