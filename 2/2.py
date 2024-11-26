import numpy as np
import  os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

matrix = np.load(f"{BASE_DIR}/second_task.npy")
print(matrix)
x = []
y = []
z = []

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i][j] > 586:
            x.append(i)
            y.append(j)
            z.append(matrix[i][j])

np.savez(f"{BASE_DIR}/second_task.npz", x=x, y=y, z=z)
#print(np.load("second_task.npz"))

np.savez_compressed(f"{BASE_DIR}/second_task_compress.npz", x=x, y=y, z=z)

first_size = os.path.getsize(f'{BASE_DIR}/second_task.npz')
second_size = os.path.getsize(f'{BASE_DIR}/second_task_compress.npz')

print(f"savez = {first_size}")
print(f"savez_compressed = {second_size}")
print(f"diff = {first_size - second_size}")
