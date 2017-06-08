from sympy.physics.quantum.qubit import IntQubit
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.grover import OracleGate
from sympy.physics.quantum.qapply import qapply
from sympy.physics.quantum.gate import HadamardGate
from sympy.physics.quantum.grover import superposition_basis
from sympy.physics.quantum.grover import grover_iteration

from Qubit import QubitString

q1 = QubitString(Qubit(0), "one")
q2 = QubitString(Qubit(0,0), "two")
q3 = QubitString(Qubit(0,0,0), "three")
q4 = QubitString(Qubit(0,0,0,0), "four")
q5 = QubitString(Qubit(0,0,0,0,0), "five")
q6 = QubitString(Qubit(0,0,0,0,0,0), "six")
q7 = QubitString(Qubit(0,0,0,0,0,0,0), "seven")
q8 = QubitString(Qubit(0,0,0,0,0,0,0,0), "eight")

f1 = lambda qubits: qubits == IntQubit(1)
f2 = lambda qubits: qubits == IntQubit(2)
f3 = lambda qubits: qubits == IntQubit(3)
f4 = lambda qubits: qubits == IntQubit(4)
f5 = lambda qubits: qubits == IntQubit(5)
f6 = lambda qubits: qubits == IntQubit(6)
f7 = lambda qubits: qubits == IntQubit(7)
f8 = lambda qubits: qubits == IntQubit(8)



v1 = OracleGate(q1.nQubits(), f1)

print(qapply(v1*IntQubit(1)))
