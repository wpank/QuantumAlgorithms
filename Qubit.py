from sympy.physics.quantum.qubit import IntQubit
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.grover import OracleGate
from sympy.physics.quantom.qapply import qapply
from sympy.physics.quantum.gate import HadamardGate
from sympy.physics.quantum.grover import superposition_basis

class QubitString:

    # Inputs:
    # Either a multi-qubit ket or a qubit ket that stores integer values as binary numbers
    # ex: |10> == |2>      |100> == |4>
    # A String to create a dictionary with an associated qubit.
    def __init__(self, qubit, qustring):
        self.qubit = qubit
        self.qustring = qustring
        self.qutuple = {qubit: qustring}

    # returns the number of dimensions of the given qubit
    def qubitDimension(self):
        return self.qubit.dimension



    def qubitToIntQubit(self):
        return IntQubit(self.qubit)

    def intQubitToQubit(self):
        return Qubit(self.qubit)

    def __str__(self):
        return self.qustring

    def __unicode__(self):
        return self.qustring





x = QubitString(Qubit(0,0,0), "Hello")
print(x)
