#Take an array with N elements with possibly duplicate elements as the input. 
# The task is to find the index of the last occurrences of the element x in the array and, if it is not present, return -1.
def findElem(find,list):
    if find not in list:
        return -1
    else:
        for i in range(len(list)):
            if(list[-i]==find):
                return((len(list))-i)

n=int(input())
list=[int(i) for i in input().split()]
find=int(input())

print(findElem(find,list))
