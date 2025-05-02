import numpy as np
import ffsim
from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit import qpy

p_flat = np.load("optimal_params.npy")

norb = 20

nelec = (15, 15)

pairs_aa = [(p, p + 1) for p in range(norb - 1)]
pairs_ab = [(0, 0), (4, 4), (8, 8), (12, 12), (16, 16)]
interaction_pairs = (pairs_aa, pairs_ab)

UCJ_object = ffsim.UCJOpSpinBalanced.from_parameters(
    params=p_flat,
    norb=norb,
    n_reps=1,
    interaction_pairs=interaction_pairs,
    with_final_orbital_rotation=True,
)

# Initialize qubits
qubits = QuantumRegister(2 * norb, name="q")

circuit = QuantumCircuit(qubits)
circuit.append(ffsim.qiskit.PrepareHartreeFockJW(norb, nelec), qubits)
circuit.append(ffsim.qiskit.UCJOpSpinBalancedJW(UCJ_object), qubits)


with open("../qiskit_circuit/circuit.qpy", "wb") as file:
    qpy.dump(circuit, file)
