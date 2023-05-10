#Given a string, replace every occurrence of 'a' with 'b' in that string and print the replaced string.
str = input()
 
# declaring an empty string variable for storing modified string
modified_str = ''
 
# iterating over the string
for char in range(0, len(str)):
    # checking if the character at char index is equivalent to 'a'
    if(str[char] == 'a') :
        # append $ to modified string
        modified_str += 'b'
    else:
        # append original string character
        modified_str += str[char]
 
print("")
print(modified_str)