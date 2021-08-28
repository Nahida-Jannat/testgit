# implementation of BFS using Python

def bfs(graph, node, visited, queue, level):
   visited.append(node)
   queue.append(node)
   level[node] = 0

   while queue:
      parent = queue.pop(0)
      print(parent, end=" ")

      for child in graph[parent]:
         if child not in visited:
               visited.append(child)
               queue.append(child)
               level[child] = level[parent] + 1


if __name__ == '__main__':

   visited = []
   queue = []
   level = {}

   graph = {
      'A' : ['B', 'C'],
      'B' : ['D', 'E'],
      'C' : ['F', 'G'],
      'D' : [],
      'E' : ['F'],
      'F' : [],
      'G' : ['I', 'J'],
      'I' : ['K', 'L'],
      'J' : [],
      'K' : ['M', 'N'],
      'L' : [],
      'M' : [],
      'N' : ['O'],
      'O' : ['P', 'Q'],
      'P' : [],
      'Q' : ['R'],
      'R' : ['S', 'T'],
      'S' : [],
      'T' : ['U'],
      'U' : ['V', 'W', 'X'],
      'V' : [],
      'W' : [],
      'X' : ['Y', 'Z'],
      'Y' : [],
      'Z' : []
   }

   bfs(graph, 'A', visited, queue, level)
   print()
   print(level)






   