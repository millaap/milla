

class Usuario:
    def __init__(self, nombre: str, rut: str, correo: str):
        self._nombre: str = nombre
        self._rut: str = rut
        self._correo: str = correo


class Estudiante:
    def __init__(self, notas: float, nombre: str):
        self._notas: float = notas
        self._nombre: str = nombre


class Asignatura:
    def __init__(self, codigo: str, nombre: str, estudiantes: str):
        self._codigo: str = codigo
        self._nombre: str = nombre
        self._estudiantes: str = estudiantes


class Docentes:
    def __init__(self, especialidad:str):
        self._especialidad: str = especialidad


class Administrativo:
    def __init__(self, area: str):
        self._area: str = area


class Reporte:
    def __init__(self, tipo: str, fecha: int):
        self._tipo: str = tipo
        self._fecha: int = fecha
