import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from hierarqcal import (
    Qhierarchy,
    Qcycle,
    Qpermute,
    Qmask,
    Qunmask,
    Qpivot,
    Qinit,
    Qmotif,
    Qmotifs,
    plot_motif,
    plot_circuit,
    Qunitary,
)

backend = "qiskit"

if backend == "qiskit":
    import qiskit
    from hierarqcal.qiskit.qiskit_circuits import V2, U2, V4

    def get_circuit(hierq):
        return hierq(backend="qiskit")

    def draw_circuit(circuit, **kwargs):
        return circuit.draw(output="mpl", **kwargs)

elif backend == "pennylane":
    import pennylane as qml
    from hierarqcal.pennylane.pennylane_circuits import V2, U2, V4

    def get_circuit(hierq):
        dev = qml.device("default.qubit", wires=hierq.tail.Q)

        @qml.qnode(dev)
        def circuit():
            if isinstance(next(hierq.get_symbols(), False), sp.Symbol):
                # Pennylane doesn't support symbolic parameters, so if no symbols were set (i.e. they are still symbolic), we initialize them randomly
                hierq.set_symbols(np.random.uniform(0, 2 * np.pi, hierq.n_symbols))
            hierq(backend="pennylane")  # This executes the compute graph in order
            return [qml.expval(qml.PauliZ(wire)) for wire in hierq.tail.Q]

        return circuit

    def draw_circuit(circuit, **kwargs):
        fig, ax = qml.draw_mpl(circuit)(**kwargs)


# backend = "pennylane"
# hierq = Qinit(8) + Qcycle(1,1,0, mapping = u2)
# circuit = get_circuit(hierq)
# fig = draw_circuit(circuit)
u2 = Qunitary(U2, 1, 2)
v2 = Qunitary(V2, 0, 2)
v4 = Qunitary(V4, 0, 4)
# ===== Demo =====
name = "demo_init"
hierq = Qinit(5)
fig, ax = plot_motif(hierq)
fig.savefig(f"./img/{name}.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle1"
hierq = Qinit(5) + Qcycle(stride=1, step=1, offset=0)
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle2"
hierq = Qinit(8) + Qcycle(stride=1, step=1, offset=0)
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle3"
hierq = Qinit(8) + Qcycle(stride=1, step=1, offset=0, boundary="open")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle4"
hierq = Qinit(8) + Qcycle(stride=2, step=1, offset=0, boundary="open")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle5"
hierq = Qinit(8) + Qcycle(stride=3, step=1, offset=0, boundary="open")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle6"
hierq = Qinit(8) + Qcycle(stride=1, step=2, offset=0, boundary="open")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle7"
hierq = Qinit(8) + Qcycle(stride=1, step=3, offset=0, boundary="open")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle8"
hierq = Qinit(8) + Qcycle(stride=1, step=3, offset=1, boundary="open")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_cycle9"
hierq = Qinit(8) + Qcycle(1, 1, 0, mapping=u2)
circuit = get_circuit(hierq)
# hierq(backend="qiskit")
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

# name = "demo_cycle10"
# backend = "pennylane"
# hierq = Qinit(8) + Qcycle(1,1,0, mapping = u2)
# hierq(backend="pennylane")
# circuit = get_circuit(hierq)
# fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
# fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_mask1"
hierq = Qinit(8) + Qmask("10100000")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_mask2"
hierq = Qinit(8) + Qmask("1*")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_mask3"
hierq = Qinit(8) + Qmask("!00")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_mask4"
hierq = Qinit(8) + Qmask("!*")
fig, ax = plot_motif(hierq[1])
fig.savefig(f"./img/{name}_motif.svg", transparent=True, bbox_inches="tight")
fig, ax = plot_circuit(hierq, plot_width=10)
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")


name = "demo_qcnn1"
hierq = (
    Qinit(8) + Qcycle(1, 1, 0, mapping=u2) + Qmask("*!") + Qcycle(1, 1, 0, mapping=u2)
)
circuit = get_circuit(hierq)
# hierq(backend="qiskit")
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")


name = "demo_qcnn2"
hierq = (
    Qinit(8)
    + Qcycle(1, 1, 0, mapping=u2)
    + Qmask("*!", mapping=v2)
    + Qcycle(1, 1, 0, mapping=u2)
)
circuit = get_circuit(hierq)
# hierq(backend="qiskit")
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_qcnn3"
cycle_mask = Qcycle(1, 1, 0, mapping=u2) + Qmask("*!", mapping=v2)
hierq = Qinit(8) + cycle_mask
circuit = get_circuit(hierq)
# hierq(backend="qiskit")
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_qcnn4"
cycle_mask = Qcycle(1, 1, 0, mapping=u2) + Qmask("*!", mapping=v2)
hierq = Qinit(8) + cycle_mask * 3
circuit = get_circuit(hierq)
# hierq(backend="qiskit")
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_qcnn5"
cycle_mask = Qcycle(1, 1, 0, mapping=u2) + Qmask("!*", mapping=v2)
hierq = Qinit(8) + cycle_mask * 3
circuit = get_circuit(hierq)
# hierq(backend="qiskit")
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")


name = "demo_qcnn6"
cycle_mask = Qcycle(1, 1, 0, mapping=u2) + Qmask("!*!", mapping=v2)
hierq = Qinit(8) + cycle_mask * 3
circuit = get_circuit(hierq)
# hierq(backend="qiskit")
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")

name = "demo_qcnn7"
cycle_mask = Qcycle(1, 1, 0, mapping=u2) + Qmask("*!*", mapping=v2)
hierq = Qinit(8) + cycle_mask * 3
circuit = get_circuit(hierq)
# hierq(backend="qiskit")
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}_circuit.svg", transparent=True, bbox_inches="tight")


# ===== Demo =====
name = "demo_right"
nq = 3
hierq = Qinit(2**nq) + (Qcycle(mapping=u2) + Qmask("!*", mapping=v2)) * nq
circuit = get_circuit(hierq)
fig = draw_circuit(circuit, style={"backgroundcolor": "none"})
fig.savefig(f"./img/{name}.svg", transparent=True, bbox_inches="tight")

print("debug")
