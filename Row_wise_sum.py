#For a given two-dimensional integer array/list of size (N x M), find and print the sum of each of the row elements in a single line, separated by a single space.
o = int(input())
for i in range(o):
  s = input().split()
  m = int(s[0])
  n = int(s[1])
  x = []
  if m >= 1 and n >= 1:
    l = []
    for i in range(m):
      ll = [int(i) for i in input().split()]
      l.append(ll)
    for i in range(m):
      a = 0
      for s in range(n):
        a = a+l[i][s]
      x.append(a)
    for i in x:
      print(i, end=' ')
    print()
  else:
    print('')
    