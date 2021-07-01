#Binary Search Using Iterative method:

def binary_iterative(arr, search_value):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < search_value:  
            low = mid + 1
        elif arr[mid] > search_value:
            high = mid - 1
        else:
            return mid

arr =[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print("Enter your search value: ")
search_value = int(input())

result = binary_iterative(arr, search_value)
if result != -1:
    print("Search value is finding at index: ", result)
else:
    print("Search value is not finding ")
