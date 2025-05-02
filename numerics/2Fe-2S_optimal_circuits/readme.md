This directory contains the data and scripts regarding the [2Fe-2S] results:

- The active space: the active space integrals are obtained from the data repository
    of the publication: https://pubs.acs.org/doi/abs/10.1021/acs.jctc.7b00270. The link to the repository is: 
    https://github.com/zhendongli2008/Active-space-model-for-Iron-Sulfur-Clusters/tree/main/Fe2S2_and_Fe4S4.

    The active space has 20 orbitals and 15 alpha and 15 beta electrons. We focus on the properties for the singlet eigenstates.

    NOTE: we work in the MO basis and not in the localized basis provided in the repository. We provide the script to transform from one to the other.

    The directory `/active_space_integrals` contains:
        
    - `/active_space_integrals/fe2s2_fcidump.txt`: integrals from the repository.
        
    - `/active_space_integrals/run_RHF.py`: script to run RHF and generate the 1- and 2-body integrals in the MO basis: `/active_space_integrals/h1e_Fe2S2_MO.npy` and `/active_space_integrals/h2e_Fe2S2_MO.npy` respectively.

- The optimized LUCJ circuit parameters with heavy-hex connectivity in the Jastrow: `/circuit_parameters/optimal_LUCJ_params.npy`. Additionally, we provide a script to load the parameters into `ffsim` https://github.com/qiskit-community/ffsim, which allows to construct the circuit: `/circuit_parameters/load_params_to_circuit.py`.

- The qiskit circuit: `/qiskit_circuit/circuit.qpy`. And an example on how to lead it in `/qiskit_circuit/load_circuit.py`.

- The 58644964 electronic configurations that we sampled from such circuit: `/samples_from_circuit/samples_58644964.npy`. The format of the configurations is a matrix where each row is a configuration represented by a an array of `bool` type. `False` means empty and `True` occupied. The first(last) half of the array is the alpha(beta) orbitals. A script showing how to load them is provided `/samples_from_circuit/load_samples.py`.
