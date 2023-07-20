#In Little Flowers Public School, there are many students with same first names. 
#You are given a task to find the students with same names. 
#You will be given a string comprising of all the names of students and you have to tell the name and count of those students having same. If all the names are unique, print -1 instead.
#Note: We don't have to mention names whose frequency is 1.
import collections

s = input()
s += ' '
word = ""
m = collections.defaultdict(int)
for i in s:
    if i == ' ':
        m[word] += 1
        word = ""
    else:
        word += i

exist = 0
for i in m:
    if m[i] > 1:
        print(i, m[i])
        exist += 1

if not exist:
    print("-1")
