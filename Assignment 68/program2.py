# Input Feature Map
feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]


relu_output = [[max(0, val) for val in row] for row in feature_map]

print("ReLU Output:")
for row in relu_output:
    print(row)

pooled_output = [
    [max(relu_output[i][j], relu_output[i][j+1],
         relu_output[i+1][j], relu_output[i+1][j+1])
     for j in range(0, len(relu_output[0])-1, 2)]
    for i in range(0, len(relu_output)-1, 2)
]

print("\nMax Pooling Output:")
for row in pooled_output:
    print(row)
