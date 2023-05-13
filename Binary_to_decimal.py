#Given a binary number as an integer N, convert it into decimal and print.
b_num = list(input())
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print(value)