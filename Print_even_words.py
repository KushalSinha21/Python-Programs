#Given a string as input, your task is to print all the words which have even lengths
n = input()
#splitting the words in a given string
s=n.split(" ")
for i in s:
  #checking the length of words
  if len(i)%2==0:
    print(i)