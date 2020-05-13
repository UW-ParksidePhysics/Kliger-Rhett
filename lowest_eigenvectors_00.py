#lowest_eigenvectors
#Return the eigenvalues and eigenvectors
def square_matrix():  # Generates a square matrix to test
    from numpy import zeros
    A = zeros([10, 10]) #Want a 10X10 matrix of zeros

    n = 0
    while n <= 9:
        A[n, n] = 2
        n = n + 1

    n = 0
    while n <= 8:
        A[n, n + 1] = 1
        A[n + 1, n] = 1
        n = n + 1

    H = (1 / (1 / 9)) * A
    return H


def lowest_eigenvectors(square_matrix, number_of_eigenvectors=3): #Default is 3
    from numpy import linalg, argsort

    M_rows = len(square_matrix)
    count = 0
    while count < M_rows:
        M_columns = len(square_matrix[count])
        if not M_rows == M_columns:
            return print("The matrix must be an M X M square matrix and M must be greater than 1.")
        count += 1

    (V, D) = linalg.eig(square_matrix)
    ordered_indices = argsort(V)
    eigenvalues = (V[ordered_indices[0:number_of_eigenvectors]])
    eigenvectors = (D[ordered_indices[0:number_of_eigenvectors]])
    return eigenvalues, eigenvectors