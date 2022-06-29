import numpy as np
from qiskit import QuantumCircuit as qc
from qiskit import QuantumRegister as qr
from qiskit import ClassicalRegister as cr
from qiskit import Aer, execute, IBMQ
from qiskit.visualization import plot_state_city
import matplotlib.pyplot as pyplot

IBMQ.load_account()

def real_map(value, leftMin, leftMax, rightMin, rightMax):
    # Maps one range to another
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def rngesus(a, b, qubits=2):
	q = qr(qubits, 'q')
	circ = qc(q)
	c0 = cr(2, 'c0')
	circ.add_register(c0)

	for i in range(qubits):
		circ.h(q[i])
	for i in range(qubits):
		circ.measure(q[i], c0)
	
	# look at what the Aer backends are / what they do
	backend = Aer.get_backend('statevector_simulator') # keeps track of state vectors of qubits ????
	job = execute(circ, backend) # 
	result = job.result()
	output = result.get_statevector(circ, decimals=5)

	n1=0
	n2=0
	n3=0
	for i in range(len(output)):
		if abs(output[i]) != 0 :
			n1 = 1
			n2 = np.real(output[i])
			n3 = np.imag(output[i])
	
	y = real_map(n1+n2+n3, -qubits, len(output)-1+qubits, a, b)
	plot_state_city(output)
	return y

x = []
y = []
for i in range(40):
	x.append(i)
	y.append(rngesus(0, 100, 3))
pyplot.plot(x, y)
pyplot.show()