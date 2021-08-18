# Tree implementation in-order

"""
            6
         /   \
         5     9
      /  \      \
      3   11      10
         / \    /  \
         7   2  4    8
"""

class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

   def add_left(self, node):
      self.left = node

   def add_right(self, node):
      self.right = node


def create_tree():
   six = Node(6)
   five = Node(5)
   nine = Node(9)
   six.add_left(five)
   six.add_right(nine)
   
   three = Node(3)
   eleven = Node(11)
   five.add_left(three)
   five.add_right(eleven)

   seven = Node(7)
   two = Node(2)
   eleven.add_left(seven)
   eleven.add_right(two)

   ten = Node(10)
   nine.add_right(ten)

   four = Node(4)
   eight = Node(8)
   ten.add_left(four)
   ten.add_right(eight)
   # return root node
   return six

def in_order(node):
    if node.left:
        in_order(node.left)
    print(node.data, end=' ')
    if node.right:
        in_order(node.right)

if __name__ == "__main__":
    tree = create_tree()
    print(tree.data)
    print('\n')

    in_order(tree)
    print('\n')