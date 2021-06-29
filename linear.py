# Linear search 

def linear(arr, n, search):
    for i in range (0, n):
        if(arr[i] == search):
            return i
    return 0

arr = [10, 20, 30, 40, 60, 32]
n = len(arr)
search = 60

index = linear(arr, n, search)
if (index == 0):
    print('searching not found')
else:
    print('searching found at index =', index)

