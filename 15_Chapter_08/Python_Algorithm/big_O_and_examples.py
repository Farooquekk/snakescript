
# O(1) --> Constant time
# Example --> Accessing an element in a list by its index

# def access_element(dog_name, idx):
#     return dog_name[idx]

# dog_name = ['GPT', 'Avan', 'X', 'Dogesh']

# print('Dog name : ',access_element(dog_name,3))

# ------------------------------------------------------------------

# O(n) --> Linear time
# Searching for a specific value in an unsortd list
# def linear_search(arr,target):
#     for f in arr:
#         if f == target:
#             return True
#     return False

# my_arr = [1,2,4,-1,8,-10]s
# my_target = 8
# print(f'Target : {my_target} is found ? {linear_search(my_arr,my_target)}')

# O(n^2) --> Quadratic time
# Example --> A simple sorting algorithm (Bubble Sort).
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     return arr
# arr = [1,2,3,10,-10,0]
# print(f'Sorted array : {bubble_sort(arr)}')

# O(log n) --> Logarithmic time
# Example --> Binary Search in a sorted list.
def binary_search(arr,target):
    left,right=0, len(arr)-1
    while left<=right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target :
            left = mid+1
        else:
            right = mid-1
    return -1
sorted_list = [1, 3, 5, 7, 9, 11, 13]
target = 9

result = binary_search(sorted_list, target)
print('Element found at index : ' , result)
