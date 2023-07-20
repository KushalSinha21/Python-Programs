#Take an array with n elements with possibly duplicate elements as the input.
# The task is to find the index of the first occurrences of the element x in the array and, if it is not present, return -1.
def find_first_occurrence(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Read input
N = int(input())
arr = list(map(int, input().split()))
x = int(input())

# Find the index of the first occurrence
index = find_first_occurrence(arr, x)

# Print the result
print(index)