# X, Y, Z, W = 0, 1, 2, 3
from africanhead import vector
from africanhead.сonstants import *

"""
https://show.ntu.edu.sg/home/ehchua/programming/opengl/CG_BasicsTheory.html#zz-8.
"""
lightPoint = [lightSourceX, lightSourceY, lightSourceZ, 1]


def diffuse(normal, trianglePoint):
    lightVec = [lightPoint[0] - trianglePoint[0],
                lightPoint[1] - trianglePoint[1],
                lightPoint[2] - trianglePoint[2],
                lightPoint[3] - trianglePoint[3]]

    lightVec = vector.normalize(lightVec)
    normal = vector.normalize(normal)
    # print(lightVec[0],lightVec[1],lightVec[2])
    # print(vector.length(lightVec))
    return max(vector.dotProduct(lightVec, normal), 0)


def specular(normal, trianglePoint):
    eyeVector = [cameraX - trianglePoint[0],
                 cameraY - trianglePoint[1],
                 cameraZ - trianglePoint[2],
                 1.0 - trianglePoint[3]]

    eyeVector = vector.normalize(eyeVector)

    lightVec = [lightPoint[0] - trianglePoint[0],
                lightPoint[1] - trianglePoint[1],
                lightPoint[2] - trianglePoint[2],
                lightPoint[3] - trianglePoint[3]]

    lightVec = vector.normalize(lightVec)

    # H вектор
    H = [lightVec[0] + eyeVector[0],
         lightVec[1] + eyeVector[1],
         lightVec[2] + eyeVector[2],
         lightVec[3] + eyeVector[3]]

    H = vector.normalize(H)
    d = vector.dotProduct(normal, H)

    # блик альфа
    return Triangle.np.pow(max(d, 0), shininess)


def calculateColour(triangle):
    ambColour = [0.0, 0.0, 0.0]
    ambColour[R] = ambientMatR * ambientLightR
    ambColour[G] = ambientMatG * ambientLightG
    ambColour[B] = ambientMatB * ambientLightB

    diffuseColour = [0.0, 0.0, 0.0]
    diffuseFactor = diffuse(triangle.normal, triangle.averagePoint(triangle))
    # print(diffuseFactor)

    diffuseColour[R] = diffuseFactor * diffuseMatR * lightSourceR
    diffuseColour[G] = diffuseFactor * diffuseMatG * lightSourceG
    diffuseColour[B] = diffuseFactor * diffuseMatB * lightSourceB
    # print(diffuseColour[R],diffuseColour[G],diffuseColour[B])

    specularColour = [0.0, 0.0, 0.0]
    specularFactor = specular(triangle.normal, triangle.averagePoint(triangle))
    # print(specularFactor)

    specularColour[R] = specularFactor * specularMatR * lightSourceR
    specularColour[G] = specularFactor * specularMatG * lightSourceG
    specularColour[B] = specularFactor * specularMatB * lightSourceB
    # print(specularColour[R],specularColour[G],specularColour[B])

    endColour = [0.0, 0.0, 0.0]
    endColour[R] = ambColour[R] + diffuseColour[R] + specularColour[R]
    endColour[G] = ambColour[G] + diffuseColour[G] + specularColour[G]
    endColour[B] = ambColour[B] + diffuseColour[B] + specularColour[B]

    #
    if endColour[R] > 1.0:
        endColour[R] = 1.0

    if endColour[G] > 1.0:
        endColour[G] = 1.0

    if endColour[B] > 1.0:
        endColour[B] = 1.0

    return colour(endColour[R], endColour[G], endColour[B])
