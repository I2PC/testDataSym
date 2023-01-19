import numpy as np
import pyworkflow.tests as pwtests

import pwem.constants as emcts
import pwem.convert as emconv

#matrices = emconv.getSymmetryMatrices(emcts.SYM_CYCLIC, n=7)
# vectorsEdge, vectorsPlane = emconv.getUnitCell(sym=emcts.SYM_CYCLIC, n=7, center=(0, 0, 0), offset=None)
# vectorsEdge, vectorsPlane = emconv.getUnitCell(sym=emcts.SYM_DIHEDRAL, n=7, center=(0, 0, 0), offset=None)
vectorsEdge, vectorsPlane = emconv.getUnitCell(sym=emcts.SYM_TETRAHEDRAL_Z3, n=None, center=(0, 0, 0), offset=None)
