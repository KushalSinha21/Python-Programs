#Python program to check if a string has at least one letter and one number
def checkString(str):
    flag_l = False
    flag_n = False

    for i in str:
        if i.isalpha():
            flag_l = True
 
        if i.isdigit():
            flag_n = True

    return flag_l and flag_n

str = input()
print(checkString(str))