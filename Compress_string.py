#Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
s=input()
res=[]
i=0
while i<len(s):
    count = 1
    j=i+1

    while j<len(s):
        if s[i]==s[j]:
            count+=1
            j+=1
        else:break
    if count>1:
        res.append(s[i]+str(count))
    else:
        res.append(s[i])

    i=i+count
for i in range(0,len(res)):
    print(res[i],end="")