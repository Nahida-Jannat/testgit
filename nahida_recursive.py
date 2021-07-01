#Python program for Recursive Binary search:

def binary_recursive(arr, low, high, search_value):

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == search_value:
            return mid
        elif arr[mid] > search_value:
            return binary_recursive(arr, low, mid - 1, search_value)
        else:
            return binary_recursive(arr, mid + 1, high, search_value)
    else:
        return -1
        
arr =[10, 15, 20, 44, 55, 60, 70, 77, 80]

print("Enter your search value: ")
search_value = int(input())

result = binary_recursive(arr, 0, len(arr) - 1, search_value)
if result != -1:
    print("Search value is finding at index: ", result)
else:
    print("Search value is not finding ")
