

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        Grupo.asignarNombre("Grado 12")
        
    def __str__(self):
        cadena = "Grupo de estudiantes: grupo predeterminado"
        return cadena

    def listadoAsignaturas(self,  **kwargs):
        self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if(lista is None):
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = lista + [alumno] 

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
