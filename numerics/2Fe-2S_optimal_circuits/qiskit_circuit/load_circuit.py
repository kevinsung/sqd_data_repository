from qiskit.circuit import QuantumCircuit, QuantumRegister
from qiskit import qpy

with open("circuit.qpy", "rb") as handle:
    qc = qpy.load(handle)[0]

qc.draw()
