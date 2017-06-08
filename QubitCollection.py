from sympy.physics.quantum.qubit import IntQubit
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.grover import OracleGate
from sympy.physics.quantum.qapply import qapply
from sympy.physics.quantum.gate import HadamardGate

from Qubit import QubitString



class QubitCollection:


    def __init__(self):
        self.allQubits = {}


    def add(self, qubitString):
        self.allQubits = {**self.allQubits, **qubitString}


    def size(self):
        return len(self.allQubits)

    def test(self):
        x = QubitCollection()
        y = QubitString(Qubit(0,0,0), "one")
        z = QubitString(Qubit(1, 0 , 0), "two")
        x.add(y.qutuple)
        x.add(z.qutuple)
        print(x.size())
