#You are given an array of integers that contain numbers in random order. Write a program to find and return the number which occurs the maximum times in the given input.
#If two or more elements are having the maximum frequency, return the element which occurs in the array first.
def maxfreq(arr):
    
    d = {}
    
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        #d[i] = d.get(0,i) + 1
        
    max_freq = arr[0]
    for i in arr:
        if d[i] > d[max_freq]:
            max_freq = i
            
    return max_freq
        

n = int(input())
arr = [int(x) for x in input().split()]
ans = maxfreq(arr)
print(ans)