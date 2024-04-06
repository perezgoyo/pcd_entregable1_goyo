#Conjunto de test unitarios y de integración con pytest

import pytest
from gestion_usuarios_uni import Universidad, Estudiante, Asignatura, ProfesorTitular, ProfesorAsociado , Investigador, Miembro_Departamento, Departamento

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

@pytest.fixture
def departamento():
    return Departamento("DIIC")

@pytest.fixture
def miembro_departamento(departamento):
    return Miembro_Departamento(departamento)

@pytest.fixture
def investigador(departamento):
    return Investigador("Elena", "98765432D", "Calle Terciaria 789", "M", departamento, "Inteligencia Artificial")

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

def test_anadir_miembro_departamento(departamento, profesor_titular, miembro_departamento):
    miembro_departamento.anadir_miembro(profesor_titular)
    assert profesor_titular in miembro_departamento.miembros

def test_eliminar_miembro_departamento(departamento, profesor_titular, miembro_departamento):
    miembro_departamento.anadir_miembro(profesor_titular)
    miembro_departamento.eliminar_miembro(profesor_titular)
    assert profesor_titular not in miembro_departamento.miembros

def test_cambiar_departamento(departamento, profesor_titular, miembro_departamento):
    nuevo_departamento = Departamento("DITEC")
    miembro_departamento.anadir_miembro(profesor_titular)
    miembro_departamento.cambiar_departamento(nuevo_departamento, profesor_titular, nuevo_departamento)
    assert profesor_titular not in departamento.miembros
    assert profesor_titular in nuevo_departamento.miembros

def test_convertirse_en_investigador(profesor_titular):
    profesor_titular.convertirse_en_investigador()
    assert profesor_titular.investigador