import numpy as np
from qutip import *

def calc(matrices, U, psi):
    C = matrices[0]@(np.kron(U, np.eye(2)))
    for V in matrices[:-1]:
        C = V@(np.kron(U, np.eye(2)))@C
    C = matrices[-1]@C
    init_state = np.kron(psi, np.array([[1], [0]]))
    return np.abs(((init_state.conj().T)@C@init_state)[0][0])
def make_matrices():
    matrices = []
    for _ in range(4):
        matrices.append(rand_unitary_haar(4, [[2, 2], [2, 2]]).data)
    return matrices


n = 4
U = rand_unitary_haar(2)
psi = np.array(rand_ket(2))
matrices = make_matrices()

print(calc(matrices, U, psi))


