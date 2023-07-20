#You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
#Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
#You need to find and return that number which is unique in the array/list

def firstNonRepeating(arr, n):
    for i in range(n):
        j = 0
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        if (j == n):
            return arr[i]
 
    return -1
 
 
t = int(input())
while(t>0):
    n1 = int(input())
    arr = [int(s) for s in input().split()]
    n = len(arr)
    print(firstNonRepeating(arr, n))
    t-=1
