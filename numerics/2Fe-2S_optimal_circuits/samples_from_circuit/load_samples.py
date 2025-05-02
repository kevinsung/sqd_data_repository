import numpy as np

bit_arrays = np.zeros((0, 40))

for i in range(40):
    bit_arrays = np.concatenate(
        (
            bit_arrays,
            np.load(f"../samples_from_circuit/samples_58644964_partition_{i}.npy"),
        ),
        axis=0,
    )

print(bit_arrays)

print("Hartree Fock string:")

print(bit_arrays[0])
