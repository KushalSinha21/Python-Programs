#Given an N*N matrix. The task is to find the index of the column with the maximum sum. That is the column whose sum of elements is maximum.
N = int(input())
rows = N
columns = N
matrix = []
for _ in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)
max_sum = float('-inf')

for i in range(columns):
    row_sum  = 0
    for j in range(rows):
        row_sum += matrix[j][i]
    max_sum = max(row_sum, max_sum)
print(max_sum)
 