li = [int(s) for s in input().split()]
my_result = [(val, pow(val, 2)) for val in li]
print(my_result)