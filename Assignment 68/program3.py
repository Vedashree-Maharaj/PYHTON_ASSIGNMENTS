matrix = [
  [6,4],
  [8,6]
]

print("Original matrix:")
print(matrix)

for row in matrix:
  print(row)

flatten = [val for row in matrix for val in row]

print("flattend output")
print(flatten)