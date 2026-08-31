class Estudiante1:
    
    def __init__(self, nombre, carrera, num_calif):
        self.Nombre = nombre
        self.Carrera = carrera
        self.calificaciones = [0] * num_calif

    def CapturaCalificacion(self, materia, calif):
        self.calificaciones[materia] = calif

    def getPromedio(self):
        suma = 0

        for i in range(len(self.calificaciones)):
            suma = suma + self.calificaciones[i]

        promedio = suma / len(self.calificaciones)

        return promedio

    def Esregular(self):
        for i in range(len(self.calificaciones)):
            if self.calificaciones[i] < 70:
                return False

        return True