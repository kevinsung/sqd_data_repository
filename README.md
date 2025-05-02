This is a data repository for the paper titled:



[**Chemistry Beyond the Scale of Exact Solutions on a Quantum-Centric Supercomputer.**](https://arxiv.org/abs/2405.05068)

This repository contains for all molecules considered in the study:

- Energy approximations (and exact when possible) obtained from classical many-body methods: ``/classical_reference_methods``.

- The electronic integrals for all molecules considered in ``fcidump`` format [link](https://pyscf.org/_modules/pyscf/tools/fcidump.html).

- The raw experiment data and results in ``/experiments``:
    - Raw dictionaries of samples together with a python script to lead them: ``/experiments/{molecule name}/experiment_data.zip``.
    - Energies (and variances when available) obtained from the quantum experiments using sqd: ``/experiments/{molecule name}/sqd_hardware_energetics``.
    - Template script to generate the ``qiskit`` circuits run on the experiments. The circuits were generated using the python package [ffsim](https://github.com/qiskit-community/ffsim).
    - Energies obtained by running SQD on samples obtained from the uniform distribution: ``/experiments/{molecule name}/sqd_on_uniform_distribution``.





