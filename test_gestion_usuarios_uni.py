#Conjunto de test unitarios con pytest

import pytest
from gestion_usuarios_uni import Universidad, Estudiante, Asignatura, ProfesorTitular, ProfesorAsociado

@pytest.fixture
def universidad():
    return Universidad()

@pytest.fixture
def estudiante():
    return Estudiante("Juan Pedro", "36587342D", "Calle Juan La Mattina 12", "V")

@pytest.fixture
def profesor_titular():
    return ProfesorTitular("Damián", "87654321B", "Calle Abeelxo 3", "V","DIIC","Diétetica")

@pytest.fixture
def profesor_asociado():
    return ProfesorAsociado("Laura", "45678901E", "Calle Secundaria 5", "M", "DIITEC")

@pytest.fixture
def asignatura():
    return Asignatura("Matemáticas")

def test_nuevo_estudiante(universidad, estudiante):
    universidad.nuevo_estudiante(estudiante)
    assert estudiante in universidad.estudiantes

def test_eliminar_estudiante(universidad, estudiante):
    universidad.nuevo_estudiante(estudiante)
    universidad.eliminar_estudiante(estudiante)
    assert estudiante not in universidad.estudiantes

def test_anadir_profesor(universidad, profesor_titular, profesor_asociado):
    universidad.anadir_profesor(profesor_titular)
    universidad.anadir_profesor(profesor_asociado)
    assert profesor_titular in universidad.profesores
    assert profesor_asociado in universidad.profesores

def test_eliminar_profesor(universidad, profesor_titular, profesor_asociado):
    universidad.anadir_profesor(profesor_titular)
    universidad.anadir_profesor(profesor_asociado)
    universidad.eliminar_profesor(profesor_titular)
    universidad.eliminar_profesor(profesor_asociado)
    assert profesor_titular not in universidad.profesores
    assert profesor_asociado not in universidad.profesores


def test_agregar_asignatura(universidad, asignatura):
    universidad.agregar_asignatura(asignatura)
    assert asignatura in universidad.asignaturas

def test_eliminar_asignatura(universidad, asignatura):
    universidad.agregar_asignatura(asignatura)
    universidad.eliminar_asignatura(asignatura)
    assert asignatura not in universidad.asignaturas

def test_obtener_asignaturas_disponibles(universidad, asignatura):
    universidad.agregar_asignatura(asignatura)
    assert asignatura in universidad.obtener_asignaturas_disponibles()

def test_agregar_asignatura_matriculada(estudiante, asignatura):
    estudiante.asignaturas_matriculadas.append(asignatura)
    assert asignatura in estudiante.asignaturas_matriculadas

def test_eliminar_asignatura_matriculada(estudiante, asignatura):
    estudiante.asignaturas_matriculadas.append(asignatura)
    estudiante.eliminar_asignatura_matriculada(asignatura)
    assert asignatura not in estudiante.asignaturas_matriculadas

