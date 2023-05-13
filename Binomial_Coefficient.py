def fact(k):
  f = i = 1
  while i<=k:
    f = i*f
    i += 1
  return f

def findcomb(x, y):
  num = fact(x)
  den = fact(x - y)
  den = fact(y) * den
  comb = num / den
  return comb

n, r = input().split()

print(findcomb(n, r))