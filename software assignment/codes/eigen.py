import cmath
import time
def matmul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]  # Create matrix C nxn
    for i in range(n):
        for j in range(n):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return C

def gramschmidt(A):
    n = len(A)
    Q = [[0] * n for _ in range(n)]  # Initialize Q and R as nxn matrices
    R = [[0] * n for _ in range(n)]
    for j in range(n):
        v = [A[i][j] for i in range(n)]  # j-th column of A
        for k in range(j):
            R[k][j] = sum(Q[i][k].conjugate() * v[i] for i in range(n)) #projection of the current vector with the vector we are orthogalizing
            for i in range(n):
                v[i] -= R[k][j] * Q[i][k]
        norm = sum(v[i].conjugate() * v[i] for i in range(n))
        if abs(norm) < 1e-12:  #if column is linearly independent of other column
            R[j][j] = 0
            for i in range(n):
                Q[i][j] = 0
        else:
            R[j][j] = cmath.sqrt(norm)
            for i in range(n):
                Q[i][j] = v[i] / R[j][j]
    return Q, R
def check(temp):
    k = 0
    n=len(temp)
    eigenvalues = [0 + 0j] * n
    while k < n:
        if k < n - 1 and abs(temp[k + 1][k]) > 1e-10:
            a11 = temp[k][k]  #solving eigne using quadratic
            a12 = temp[k + 1][k]
            a21= temp[k][k + 1]
            a22= temp[k + 1][k + 1]
            
            b = -1.0 * (a11+a22)
            c = (a11*a22-a21*a12)
            D= b*b-4*c

            eigenvalues[k] = (-1*b + cmath.sqrt(D)) / 2.0
            eigenvalues[k + 1] = (-1*b- cmath.sqrt(D)) / 2.0
            temp[k + 1][k] = 0
            k += 2
        else:
            eigenvalues[k] = temp[k][k]
            k += 1
    return eigenvalues

def qr_algorithm_with_shift(matrix, Max_iterations=1000, Tolerance=1e-10):
    n = len(matrix)
    for iter in range(Max_iterations):
        if n > 1:
            d = (matrix[n-2][n-2] - matrix[n-1][n-1])/2.0
            if d.real>=0:
                sign=1.0
            else:
                sign=-1.0
            shift = matrix[n-1][n-1] - sign * cmath.sqrt(d * d + matrix[n-1][n-2] * matrix[n-2][n-1])
        else:
            shift = matrix[n-1][n-1]
        
        for i in range(n):
            matrix[i][i] -= shift
        Q, R = gramschmidt(matrix)
        matrix = matmul(R, Q)
        for i in range(n):
            matrix[i][i] += shift
        flag=0
        if(all(abs(matrix[i+1][i])<=Tolerance for i in range(n-1))):
            break
    return check(matrix)

if __name__ == "__main__":
    matrix = [
    [0,1],[-1,0]#inputing matrix
]
    st=time.time()
    eigenvalues = qr_algorithm_with_shift(matrix)
    et=time.time()
    print("Eigen Values are:",eigenvalues)
    print("Runtime:",et-st,"seconds")
