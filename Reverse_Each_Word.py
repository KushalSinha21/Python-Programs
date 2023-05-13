#You have been provided with a sentence in the form of a string as a function parameter. 
#The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.
s=list(map(str,input().split()))
s1=[]
for i in range(len(s)):
    s1.append(s[i][::-1])

print(" ".join(s1))