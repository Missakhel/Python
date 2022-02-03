import sys

class Vector:
    origin = [0.0, 0.0]
    direction = [0.0, 0.0]
    absoluteOrigin = [0.0, 0.0]
    absoluteDirection = [0.0, 0.0]
    color = (0,0,0)
    magnitude = 0.0
    tag = ""

    def __init__(self, aPos, bPos, unitSize, midScreen, color, tag):
        self.origin = aPos
        self.direction = bPos
        self.color = color
        self.tag = tag
        for index in range(0, 2):
            self.absoluteDirection[index] = bPos[index]*unitSize+midScreen
            self.absoluteOrigin[index] = aPos[index]*unitSize+midScreen

        sqrtMagnitude = (self.direction[0] ** 2 + self.direction[1] ** 2)
        # Si la magnitud de tu vector resultante resulta ser 0, cuando quieras normalizar o proyectar
        # el programa fallará porque no puedes dividir entre 0, para evitarlo, hacemos lo siguiente:
        if(sqrtMagnitude <= sys.float_info.epsilon):
            self.sqrtMagnitude = 0.0001
            self.magnitude = self.sqrtMagnitude ** 0.5
            return

        self.magnitude = (self.direction[0] ** 2 + self.direction[1] ** 2) ** 0.5
        self.sqrtMagnitude = sqrtMagnitude

    def normalize(self, unitSize, midScreen):
        vector = Vector(self.origin, [self.direction[0]/self.magnitude, self.direction[1]/self.magnitude], unitSize, midScreen, (0, 255, 0))    
        return vector

    def add(self, vector, unitSize, midScreen):
        vector = Vector(self.origin, vector.direction, unitSize, midScreen, (0, 255, 0), "R")
        return vector

    def substract(self, vector, unitSize, midScreen):
        vector = Vector(vector.direction, self.direction, unitSize, midScreen, (0, 255, 0),  "R")
        return vector

    def project(self, vector, unitSize, midScreen):
        dotProduct = self.direction[0] * vector.direction[0] + self.direction[1] * vector.direction[1]
        multiplier = dotProduct / vector.sqrtMagnitude
        # pero el vector B debería normalizarse antes de multiplicar
        endX = vector.direction[0] * multiplier
        endY = vector.direction[1] * multiplier
        # El truco para evitarlo (y de paso optimizar) es dividir entre la magnitud cuadrada al inicio
        projectedVector = Vector(self.origin, [endX, endY], unitSize, midScreen, (0, 255, 0), "R")
        axis = Vector(self.direction, projectedVector.direction,unitSize, midScreen, (255, 255, 0), "Axis")
        return projectedVector,axis