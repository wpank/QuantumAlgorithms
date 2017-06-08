from sympy.physics.quantum.qubit import IntQubit
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.grover import OracleGate
from sympy.physics.quantum.qapply import qapply
from sympy.physics.quantum.gate import HadamardGate
from sympy.physics.quantum.grover import superposition_basis
from sympy.physics.quantum.grover import grover_iteration
from sympy.physics.quantum.grover import apply_grover

from Qubit import QubitString
from QubitCollection import QubitCollection

q1 = QubitString(Qubit(0), "one")
q2 = QubitString(Qubit(1,0), "two")
q3 = QubitString(Qubit(0,1,1), "three")
q4 = QubitString(Qubit(0,1,0,1), "four")
q5 = QubitString(Qubit(1,0,1,0,0), "five")
q6 = QubitString(Qubit(0,1,0,1,1,0), "six")
q7 = QubitString(Qubit(0,0,1,1,1,0,0), "seven")
q8 = QubitString(Qubit(0,0,1,0,1,0,1,0), "eight")

qcol = QubitCollection()
qcol.add(q1.qutuple)
qcol.add(q2.qutuple)
qcol.add(q3.qutuple)
qcol.add(q4.qutuple)
qcol.add(q5.qutuple)
qcol.add(q6.qutuple)
qcol.add(q7.qutuple)
qcol.add(q8.qutuple)


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

print("Applied Oracle Gates:")
print(qapply(v1*q1.qubit))
print(qapply(v2*q2.qubit))
print(qapply(v3*q3.qubit))
print(qapply(v4*q4.qubit))
print(qapply(v5*q5.qubit))
print(qapply(v6*q6.qubit))
print(qapply(v7*q7.qubit))
print(qapply(v8*q8.qubit))
print()

print("Superpositions:")
print("q1:")
print(q1.superposition())
print()

print("q2:")
print(q2.superposition())
print()

print("q3:")
print(q3.superposition())
print()

print("q4:")
print(q4.superposition())
print()

print("q5:")
print(q5.superposition())
print()

print("q6:")
print(q6.superposition())
print()

print("q7:")
print(q7.superposition())
print()

print("q8:")
print(q8.superposition())
print()

# Grover Iteration
print(qcol.allQubits[Qubit(qapply(grover_iteration(q2.superposition(), v2)))])
#print(qcol.allQubits[Qubit(
print(qapply(apply_grover(f5, q2.nQubits())))
#])
