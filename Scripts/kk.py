import numpy as np
import pyworkflow.tests as pwtests

import pwem.constants as emcts
import pwem.convert as emconv

sym = emcts.SYM_TETRAHEDRAL_222
#sym = emcts.SYM_TETRAHEDRAL_Z3
#sym = emcts.SYM_TETRAHEDRAL_Z3R
matrices = emconv.getSymmetryMatrices(sym)
# vectorsEdge, vectorsPlane = emconv.getUnitCell(sym=emcts.SYM_CYCLIC, 
 #n=7, 
 #center=(0, 0, 0), 
 #offset=None)
#vectorsEdge, vectorsPlane = emconv.getUnitCell(
# sym=emcts.SYM_DIHEDRAL, 
# n=7, 
# center=(0, 0, 0), 
# offset=None)
vectorsEdge, vectorsPlane = emconv.getUnitCell(sym=sym, 
 n=None, 
 center=(0, 0, 0), 
 offset=None)
