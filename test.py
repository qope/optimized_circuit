import numpy as np
from qutip import *

U = rand_unitary_haar(2).data
V = rand_unitary_haar(2).data
a = np.array([[1.0], [0]])

print(U@V@a)