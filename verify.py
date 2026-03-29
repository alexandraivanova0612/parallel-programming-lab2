import numpy as np

A = np.loadtxt('matrix_A.txt')
B = np.loadtxt('matrix_B.txt')
C = np.loadtxt('matrix_C.txt')

C_expected = np.dot(A, B)
max_diff = np.max(np.abs(C - C_expected))

print(f"Макс. разница: {max_diff:.6e}")
if max_diff < 1e-8:
    print("ВЕРНО")
else:
    print("ОШИБКА")