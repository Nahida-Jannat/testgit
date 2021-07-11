# Bubble Sort Implementation
#n = 5

def bubble_sort(data_list):
    n = len(data_list)
    for i in range(n-1):
      print('Loop 1: i-%d\n-----' %i)

      swap = False
      
      for j in range(n-i-1):
         print('j-', j)

         if  data_list[j] > data_list[j+1]:
               temp = data_list[j]
               data_list[j] = data_list[j+1]
               data_list[j+1] = temp
               
               swap = True
      
      if not swap:
         break

if __name__ == '__main__':
    data_list = [5,7,6,4,2]
    bubble_sort(data_list)
    print(data_list)