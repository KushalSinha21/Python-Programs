#You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is present at least once. 
#That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these, there is a single integer value that is present twice. 
#You need to find and return that duplicate number present in the array.
import sys

def duplicatenum(arr, size):
    for i in range(size -1):
        for j in range((i+1), size):
            if arr[i] == arr[j]:
                return arr[i]
    return sys.maxsize

def takeinput():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(),0
    arr = list(map(int,sys.stdin.readline().strip().split()))
    return arr,n


t = int(sys.stdin.readline().strip())
while t>0:
    arr,n = takeinput()
    print(duplicatenum(arr,n))
    t -= 1