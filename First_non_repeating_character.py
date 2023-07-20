#In a given string, find the first non-repeating character .You are given a string, that can contain repeating characters. Your task is to return the first character in this string that does not repeat. i.e., occurs exactly once. 
#The string will contain characters only from English alphabet set, i.e., ('A' - 'Z') and ('a' - 'z'). 
#If there is no non-repeating character print the first character of string.
from collections import Counter

def repeatFunc(myStr):
    freq = Counter(myStr)
    # Traverse the string
    for i in myStr:
	    if(freq[i] == 1):
		    print(i)
            break
    
string = input()
repeatFunc(string)