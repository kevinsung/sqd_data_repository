import numpy as np
from pyscf import ao2mo, tools, cc
import ffsim
from qiskit import QuantumCircuit, QuantumRegister


fcidump_filename = ""  # file name to fcidump file
num_orb = 0  # replace with number of orbitals
num_elec_a = 0  # replace with spin-up electron number
num_elec_b = 0  # replace with spin-down electron number

mf_as = tools.fcidump.to_scf(fcidump_filename)
h1e = mf_as.get_hcore()
h2e = ao2mo.restore(1, mf_as._eri, num_orb)


ccsd = cc.CCSD(mf_as).run()
t1 = ccsd.t1
t2 = ccsd.t2


n_reps = 1
alpha_alpha_indices = [(p, p + 1) for p in range(num_orb - 1)]
alpha_beta_indices = [(p, p) for p in range(0, num_orb, 4)]

ucj_op = ffsim.UCJOpSpinBalanced.from_t_amplitudes(
    t2=t2,
    t1=t1,
    n_reps=n_reps,
    interaction_pairs=(alpha_alpha_indices, alpha_beta_indices),
)

nelec = (num_elec_a, num_elec_b)

# create an empty quantum circuit
qubits = QuantumRegister(2 * num_orb, name="q")
circuit = QuantumCircuit(qubits)

# prepare Hartree-Fock state as the reference state and append it to the quantum circuit
circuit.append(ffsim.qiskit.PrepareHartreeFockJW(num_orb, nelec), qubits)

# apply the UCJ operator to the reference state
circuit.append(ffsim.qiskit.UCJOpSpinBalancedJW(ucj_op), qubits)
circuit.measure_all()
