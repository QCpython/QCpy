import numpy as np

from qcpy.quantumgate import identity


def test_qg_01():
    assert (identity() == np.array([[1 + 0j, 0 + 0j], [0 + 0j, 1 + 0j]], "F")).all(), "test_qg_01 Failed on Identity"
