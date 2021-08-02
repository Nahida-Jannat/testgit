# Merge Sort Implementation
# merge data in ascending order

def merge_sort(data_list):

   if len(data_list) > 1:

      mid = len(data_list) // 2     #Splitting
      left = data_list[:mid]
      right = data_list[mid:]

      merge_sort(left)
      merge_sort(right)

      
      a, b, c = 0, 0, 0     #Initialize

      # Merging
      while a < len(left) and b < len(right):
         if left[a] < right[b]:
               data_list[c] = left[a]
               a += 1
         else:
               data_list[c] = right[b]
               b += 1
         c += 1

      # Insert remaining elements from left side list
      while a < len(left):
         data_list[c] = left[a]
         a += 1
         c += 1

      # Insert remaining elements from right side list
      while b < len(right):
         data_list[c] = right[b]
         b += 1
         c += 1


if __name__ == '__main__':

   data_list = [13, 7, 1, 44, 10, 55, 8, 61]  # Unsorted
   print('Before Merge Sort:', data_list)
   merge_sort(data_list)
   print('After Merge Sort:', data_list)