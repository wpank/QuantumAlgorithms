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
v2 = OracleGate(q2.nQubits(), f2)
v3 = OracleGate(q3.nQubits(), f3)
v4 = OracleGate(q4.nQubits(), f4)
v5 = OracleGate(q5.nQubits(), f5)
v6 = OracleGate(q6.nQubits(), f6)
v7 = OracleGate(q7.nQubits(), f7)
v8 = OracleGate(q8.nQubits(), f8)


print(qapply(v1*q1.qubit))
print(qapply(v2*q2.qubit))
print(qapply(v3*q3.qubit))
print(qapply(v4*q4.qubit))
print(qapply(v5*q5.qubit))
print(qapply(v6*q6.qubit))
print(qapply(v7*q7.qubit))
print(qapply(v8*q8.qubit))

print(q1.superposition())
qapply(grover_iteration(q2.superposition(), v2))
