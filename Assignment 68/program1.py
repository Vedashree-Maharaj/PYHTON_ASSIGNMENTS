image = [
  [0,0,0,0,0],
  [0,0,0,0,0],
  [1,1,1,1,1],
  [0,0,0,0,0],
  [0,0,0,0,0],
]

kernel = [
  [-1,-1,-1],
  [0 , 0, 0],
  [1 , 1, 1]
]

image_size = len(image)
kernel_size = len(kernel)
output_size = image_size - kernel_size + 1

feature_map = [[0]*output_size for _ in range(output_size)]

for i in range(output_size):
    for j in range(output_size):
        feature_map[i][j] = sum(
            image[i+m][j+n] * kernel[m][n]
            for m in range(kernel_size)
            for n in range(kernel_size)
        )

print("Feature Map:")
for row in feature_map:
    print(row)
