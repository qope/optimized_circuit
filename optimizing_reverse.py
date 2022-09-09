import numpy as np
from qutip import *

n = 4
matrices = []
for i in range(4):
    matrices.append(rand_unitary_haar(4, [[2, 2], [2, 2]]).data)

U = rand_unitary_haar(2)
V = matrices[0]@(np.kron(U, np.eye(2)))

P = np.kron(np.eye(2), np.array([[1], [0]]))
# print((P.conj().T)@matrices[0]@P)
psi = rand_ket(2).data.reshape([2, 1])

r = np.kron(psi, np.array([[1], [0]]))
print(r)
def calc(matrices, U, psi):
    C = matrices[0]
    for V in matrices[1:]:
        C = C @ ( (np.kron(U, np.eye(2)))@V )
    init_state = np.kron(psi, np.array([[1], [0]]))
    print(init_state.conj().T.shape)
    return (init_state.conj().T)@C@init_state

calc(matrices, U, psi)


