#Given a string as input, your task is to print all the words which have even lengths.
#Input : It is a python program
#Output :
#It
#is
#python
n = input()
#splitting the words in a given string
s=n.split(" ")
for i in s:
  #checking the length of words
  if len(i)%2==0:
    print(i)