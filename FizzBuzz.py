#You have been provided with an integer value as input. Your task is to print "Fizz" and "Buzz" according to the below conditions.
#1. For multiples of three print "Fizz" instead of the number.
#2. For the multiples of five print "Buzz". 
#3. For numbers that are multiples of both three and five print "FizzBuzz".
n = int(input())
li = []
for fizzbuzz in range(1,n):
    if fizzbuzz % 5 ==0 and fizzbuzz % 3 == 0:
        li.append("fizzbuzz")  
        continue                                      
    elif fizzbuzz % 3 == 0:    
        li.append("fizz")  
        continue                                      
    elif fizzbuzz % 5 == 0:        
        li.append("buzz")
        continue
    li.append(fizzbuzz)

print(li)