from sympy.physics.quantum.qubit import IntQubit
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.grover import OracleGate
from sympy.physics.quantom.qapply import qapply
from sympy.physics.quantum.gate import HadamardGate
from sympy.physics.quantum.grover import superposition_basis
from sympy.physics.quantum.grover import grover_iteration

q1 = QubitString((0), "one")
q2 = QubitString((0,0), "two")
q3 = QubitString((0,0,0), "three")
q4 = QubitString((0,0,0,0), "four")
q5 = QubitString((0,0,0,0,0), "five")
q6 = QubitString((0,0,0,0,0,0), "six")
q7 = QubitString((0,0,0,0,0,0,0), "seven")
q8 = QubitString((0,0,0,0,0,0,0,0), "eight")

f1 = lambda qubits: qubits == IntQubits(1)
f2 = lambda qubits: qubits == IntQubits(2)
f3 = lambda qubits: qubits == IntQubits(3)
f4 = lambda qubits: qubits == IntQubits(4)
f5 = lambda qubits: qubits == IntQubits(5)
f6 = lambda qubits: qubits == IntQubits(6)
f7 = lambda qubits: qubits == IntQubits(7)
f8 = lambda qubits: qubits == IntQubits(8)
