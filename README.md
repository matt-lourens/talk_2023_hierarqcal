### Hierarchical quantum circuit representations presentation

Slides made with [revealjs!](https://revealjs.com/)

Quantum circuit algorithms often require architectural design choices analogous to those made in constructing neural and tensor networks. These tend to be hierarchical, modular and exhibit repeating patterns. Neural Architecture Search (NAS) attempts to automate neural network design through learning network architecture and achieves state-of-the-art performance. We propose a framework for representing quantum circuit architectures using techniques from NAS, which enables search space design and architecture search. We use this framework to justify the importance of circuit architecture in quantum machine learning by generating a family of Quantum Convolutional Neural Networks (QCNNs) and evaluating them on a music genre classification dataset, GTZAN. Furthermore, we employ a genetic algorithm to perform Quantum Phase Recognition (QPR) as an example of architecture search with our representation. Finally, we implement the framework as an open-source Python package to enable dynamic circuit creation and facilitate circuit search space design for NAS.

Here's links to the [presentation](https://matt-lourens.github.io/talk_2023_hierarqcal/),  [paper](https://www.nature.com/articles/s41534-023-00747-z) and [package](https://github.com/matt-lourens/hierarqcal)!
