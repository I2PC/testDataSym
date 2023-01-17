import pwem.protocols as emprot
import pwem.constants as emcts
import pwem.convert as emconv

import pwem.objects as emobj
import numpy as np

"""
radius_marker = 2
radius_sphere = 55.

sym = emcts.SYM_I222r
icosahedron = emconv.Icosahedron(orientation=emcts.SCIPION_SYM_NAME[sym][1:])
f = open("test.bild", "w")
f.write(".color red\n")
for i, vertice in enumerate(icosahedron.getVertices()):
    vertice = radius_sphere * vertice
    x =  vertice[0];    y =  vertice[1];    z =  vertice[2]
    f.write(f".sphere {x} {y} {z} {radius_marker}\n")

f.write(".color green\n")
for _3fold in icosahedron.get3foldAxis():
    x = radius_sphere * _3fold[0]
    y = radius_sphere * _3fold[1]
    z = radius_sphere * _3fold[2]
    f.write(f".sphere {x} {y} {z} {radius_marker}\n")

f.write(".color blue\n")
for _2fold in icosahedron.get2foldAxis():
    x = radius_sphere * _2fold[0]
    y = radius_sphere * _2fold[1]
    z = radius_sphere * _2fold[2]
    f.write(f".sphere {x} {y} {z} {radius_marker}\n")
"""

"""
.color 1 1 0
.sphere -28.915211166552346 0.0 46.785794459362194 2
.sphere 28.915211166552343 0.0 46.785794459362194 2
.color green
.sphere -3.0531133177191805e-15 15.595264819787397 40.82893336175892 2
"""
_5fold1 = np.array([-28.915211166552346, 0.0, 46.785794459362194])
_5fold2 = np.array([28.915211166552343, 0.0, 46.785794459362194])
_3fold = np.array([0.0, 15.595264819787397, 40.82893336175892])

u = np.cross(_5fold1, _5fold2)
u = u / np.linalg.norm(u)
v = np.cross(_5fold2, _3fold)
v = v / np.linalg.norm(v)
w = np.cross(_3fold, _5fold1)
w = w / np.linalg.norm(w)


def readParticles(fileName):
    " Read particles from file."
    parSet = emobj.SetOfParticles(filename=fileName)
    return parSet

def extractProjectionDirection(parSet):
    """ Extract projection direction from particles.
    :param parSet: SetOfParticles
    :return: list of projection direction
    For test purposes only
    """
    projDir = []
    for par in parSet:
        projDir.append(par.getTransform().getMatrix()[:, 2])
    # f = open("test3697.bild", "w")
    # f.write(".color red\n")
    # for par in projDir:
    #     f.write(f".sphere {par[0]*55} {par[1]*55} {par[2]*55} 2\n")
    # f.close()
    return projDir

def getSymmetryMatrices(sym):
    icosahedron = emconv.Icosahedron(orientation=emcts.SCIPION_SYM_NAME[sym][1:])
    return icosahedron.icosahedralSymmetryMatrices()

def filterParticles(parSet, matrixSet):
    projDirIn = []
    projDirOut = []
    for par in parSet:
        column = par.getTransform().getMatrix()[0:3, 2]
        if (np.dot(column, u)>0) and \
           (np.dot(column, v)>0) and \
           (np.dot(column, w)>0):
            projDirIn.append(column)
        else:
            projDirOut.append(column)
    f = open("dotIn.bild", "w")
    f.write(".color green\n")
    for par in projDirIn:
        f.write(f".sphere {par[0]*55} {par[1]*55} {par[2]*55} 2\n")
    f.close()
    f = open("dotOut.bild", "w")
    f.write(".color red\n")
    for par in projDirOut:
        f.write(f".sphere {par[0]*55} {par[1]*55} {par[2]*55} 2\n")
    f.close()


# read particles
parSet = readParticles("particles_3542.sqlite")
# extract projection direction
# projDir = extractProjectionDirection(parSet)
# get symmetry matrices
matrixSet = getSymmetryMatrices(emcts.SYM_I222r)
# Multiply by base
# If all positive, then add particle
filterParticles(parSet, matrixSet)
# If not multiply by symmetry matrix and retry
