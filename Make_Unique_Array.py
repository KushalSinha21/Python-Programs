#Find number of elements to be removed to make an array of all distinct elements.
def Repeat(arr):
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)

    return len(arr) - len(unique)
 
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print (Repeat(arr))