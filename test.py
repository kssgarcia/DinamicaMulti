import numpy as np
A = np.random.rand(1000,3,3)
def slow_inverse(A): 

    for i in range(900):
        a = np.linalg.inv(A[i])
    return 'listo'

def fast_inverse(A):
    identity = np.identity(A.shape[0], dtype=A.dtype)
    Ainv = np.zeros_like(A)

    for i in range(A.shape[3]):
        Ainv[i] = np.linalg.solve(A[i], identity)
    return Ainv

def fast_inverse2(A):
    identity = np.identity(A.shape[2], dtype=A.dtype)
    for i in range(900):
        a = np.linalg.solve(A[i], identity)
    return 'listo'

from numpy.linalg import lapack_lite
lapack_routine = lapack_lite

def faster_inverse(A):
    b = np.identity(A.shape[2], dtype=A.dtype)

    n_eq = A.shape[1]
    n_rhs = A.shape[2]
    pivots = zeros(n_eq, np.intc)
    identity  = np.eye(n_eq)
    def lapack_inverse(a):
        b = np.copy(identity)
        pivots = zeros(n_eq, np.intc)
        results = lapack_lite.dgesv(n_eq, n_rhs, a, n_eq, pivots, b, n_eq, 0)
        if results['info'] > 0:
            raise LinAlgError('Singular matrix')
        return b

    return array([lapack_inverse(a) for a in A])


B = np.array([[1,2,3],
            [1,2,7],
            [1,7,3]])
# print(np.linalg.inv(B))
# print(np.linalg.solve(B, np.identity(B.shape[0], dtype=A.dtype)))


# print(slow_inverse(A))
print(fast_inverse2(A))

