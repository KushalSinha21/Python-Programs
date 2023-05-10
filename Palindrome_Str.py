#Given a string, determine if it is a palindrome, considering only alphanumeric characters.
def isPalindrome(s):
    return s == s[::-1]

s = input()
ans = isPalindrome(s)
  
if ans:
    print("true")
else:
    print("false")