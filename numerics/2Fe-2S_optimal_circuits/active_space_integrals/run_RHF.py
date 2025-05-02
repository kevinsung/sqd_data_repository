import numpy as np
from pyscf import ao2mo, tools


norb = 20
nela = 15

mf_as = tools.fcidump.to_scf("fe2s2_fcidump.txt")
mf_as.mol.verbose = 1

# Run HF to make sure we have good MOs
mf_as.kernel()
for i in range(10):
    moi, moe, si, se = mf_as.stability(return_status=True)
    E = mf_as.kernel(mf_as.make_rdm1(moi, mf_as.mo_occ))

# Extract integrals
h0e = mf_as.mol.energy_nuc()
h1e = mf_as.get_hcore()
h2e = ao2mo.restore(1, mf_as._eri, norb)

# Extract integrals
h0e = mf_as.mol.energy_nuc()
h1e = mf_as.get_hcore()
h2e = ao2mo.restore(1, mf_as._eri, norb)


h1e = mf_as.mo_coeff.T.dot(mf_as.get_hcore()).dot(mf_as.mo_coeff)
h2e = np.einsum(
    "pqrs,pi,qj,rk,sl->ijkl",
    ao2mo.restore(1, mf_as._eri, norb),
    mf_as.mo_coeff,
    mf_as.mo_coeff,
    mf_as.mo_coeff,
    mf_as.mo_coeff,
    optimize=True,
)

np.save("h1e_Fe2S2_MO.npy", h1e)
np.save("h2e_Fe2S2_MO.npy", h2e)
