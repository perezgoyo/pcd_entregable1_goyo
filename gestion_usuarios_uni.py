# Sistema de gestión de usuarios de una Universidad

class Universidad:
    # Constructor de la clase
    def __init__(self, departamentos=None, profesores=None, estudiantes=None, asignaturas=None):
        self.departamentos = departamentos or []
        self.profesores = profesores or []
        self.estudiantes = estudiantes or []
        self.asignaturas = asignaturas or [] # Definición de las listas que queremos que formen parte de la Universidad

    def nuevo_estudiante(self, nuevo_estudiante):
        self.estudiantes.append(nuevo_estudiante) # Método que agrega un nuevo estudiante a la Universidad con append

    def eliminar_estudiante(self, antiguo_estudiante):
        if antiguo_estudiante in self.estudiantes:
            self.estudiantes.remove(antiguo_estudiante)
        else:
            raise ValueError("El estudiante no pertenece a la universidad") # Método que elimina un estudiante de la Universidad con remove, siempre y cuando el estudiante pertenezca a la misma

    def anadir_profesor(self, nuevo_profesor):
        self.profesores.append(nuevo_profesor) # Método que agrega un nuevo profesor a la Universidad con append

    def eliminar_profesor(self, antiguo_profesor):
        if antiguo_profesor in self.profesores:
            self.profesores.remove(antiguo_profesor)
        else:
            raise ValueError("El profesor no está registrado en la universidad.") # Método que elimina un profesor de la Universidad con remove, siempre y cuando el profesor pertenezca a la misma

    def agregar_asignatura(self, nueva_asignatura):
        if nueva_asignatura not in self.asignaturas:
            self.asignaturas.append(nueva_asignatura)
            for estudiante in self.estudiantes:
                estudiante.universidad = self
        else:
            raise ValueError("La asignatura ya está registrada en la universidad.") # Método que agrega una nueva asignatura a la Universidad con append

    def eliminar_asignatura(self, antigua_asignatura):
        if antigua_asignatura in self.asignaturas:
            self.asignaturas.remove(antigua_asignatura)
            for estudiante in self.estudiantes:
                estudiante.eliminar_asignatura_matriculada(antigua_asignatura)
            for profesor in self.profesores:
                profesor.eliminar_asignatura(antigua_asignatura)
        else:
            raise ValueError("La asignatura no está registrada en la universidad.") # Método que elimina una asignatura de la Universidad con remove, siempre y cuando la asignatura pertenezca a la misma

    def obtener_asignaturas_disponibles(self):
        return self.asignaturas # Método que llama a la lista de asignaturas que está actualizada al momento, con el fin de llevar un seguimiento de la misma
    
class Persona:
    # Constructor de la clase
    def __init__(self, nombre, dni, direccion, sexo):
        self._nombre = nombre
        self._dni = dni
        self._direccion = direccion
        self._sexo = sexo # Parámetros de la clase Persona

class AsignaturaNoEncontrada(Exception):
    pass # Excepción que se lanza cuando la asignatura que queremos añadir o eliminar no está dentro de la lista asignaturas de la clase Universidad

class Asignatura:
    # Constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre # Parámetro de la clase Asignatura

class Estudiante(Persona):
    # Constructor de la clase
    def __init__(self, nombre, dni, direccion, sexo): # Parámetros de la clase Estudiante
        super().__init__(nombre, dni, direccion, sexo) # Parámetros de la clase Estudiante que hereda de la clase Persona, ya que todos los estudiantes son personas
        self.asignaturas_matriculadas = [] # Listado de asignaturas en las que se matricula "x" estudiante, dentro de las asignaturas de las que dispone la Universidad

    def agregar_asignatura_matriculada(self, asignatura):
        if asignatura in self.universidad.obtener_asignaturas_disponibles():
            self.asignaturas_matriculadas.append(asignatura)
        else:
            raise AsignaturaNoEncontrada("La asignatura no está disponible en la universidad.") # Método que añade una asignatura a la lista de asignaturas matriculadas del Estudiante

    def eliminar_asignatura_matriculada(self, asignatura):
        if asignatura in self.asignaturas_matriculadas:
            self.asignaturas_matriculadas.remove(asignatura)
        else:
            raise AsignaturaNoEncontrada("No estás matriculado en esta asignatura.") # Método que elimina una asignatura a la lista de asignaturas matriculadas del Estudiante

class Profesor(Persona):
    # Constructor de la clase
    def __init__(self, nombre, dni, direccion, sexo, departamento):# Parámetros de la clase Profesor
        super().__init__(nombre, dni, direccion, sexo) # Parámetros de la clase Profesor que hereda de la clase Persona, ya que todos los profesores son personas
        self.asignaturas = [] # Listado de asignaturas que va a impartir o dejar de impartir el profesor
        self.departamento = departamento 

    def agregar_asignatura(self, asignatura):
        if asignatura not in self.universidad.obtener_asignaturas_disponibles():
            raise ValueError("La asignatura no está disponible en esta universidad.")
        self.asignaturas.append(asignatura) # Método que añade una asignatura a la lista de asignaturas que imparte el Profesor

    def eliminar_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
        else:
            raise ValueError("No da clase de esta asignatura.") # Método que elimina una asignatura a la lista de asignaturas que imparte el Profesor

class ProfesorTitular(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion): # Parámetros de la clase ProfesorTitular
        super().__init__(nombre, dni, direccion, sexo, departamento) # Parámetros de la clase ProfesorTitular que hereda de Profesor, ya que todos los profesores titulares son profesores
        self.area_investigacion = area_investigacion # Parámetro que relaciona ProfesorTitular con Investigador

    def convertirse_en_investigador(self):
        self.investigador = True # Método para verificar que el profesor titular es también investigador

class ProfesorAsociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, departamento): # Parámetros de la clase ProfesorAsociado
        super().__init__(nombre, dni, direccion, sexo, departamento) # Parámetros de la clase ProfesorAsociado que hereda de Profesor, ya que todos los profesores asociados son profesores
        self.universidad = None  

class Investigador(ProfesorTitular):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area_investigacion): # Parámetros de la clase Investigador 
        super().__init__(nombre, dni, direccion, sexo, departamento, area_investigacion) # Parámetros de la clase Investigador que hereda de ProfesorTitular, ya que todos los investigadores son profesores titulares

class Miembro_Departamento():
    def __init__(self, departamento, miembros=None): #Parámetros de la clase Miembro_Departamento
        self.departamento = departamento
        self.miembros = miembros if miembros is not None else []

    def anadir_miembro(self, nuevo_miembro):
        if isinstance(nuevo_miembro, Persona):
            self.miembros.append(nuevo_miembro)
        else:
            raise ValueError("Aquí solo se aceptan Personas") # Método que añade miembros a la lista de miembros de la clase, siempre y cuando esos miembros pertenezcan a la clase Persona, para evitar la posibilidad de que se añada por ejemplo una asignatura como miembro

    def eliminar_miembro(self, nombre_miembro):
        self.miembros.remove(nombre_miembro) # Método que elimina miembros de la lista miembros de la clase

    def cambiar_departamento(self, nuevo_departamento, nombre_miembro, nuevo_departamento_objeto):
        if nombre_miembro in self.miembros:
            # Eliminar el miembro del departamento actual
            self.miembros.remove(nombre_miembro)
            # Agregar el miembro al nuevo departamento
            if nuevo_departamento == self.departamento:
                raise ValueError("El miembro ya pertenece a este departamento")
            else:
                nuevo_departamento_objeto.anadir_miembro(nombre_miembro)
                print(f"El miembro {nombre_miembro._nombre} ha cambiado de departamento {nuevo_departamento}.")
                return True
        else:
            print("El miembro no está en este departamento")
            return False # Método que cambia el departamento del miembro, primero elimina al miembro del departamento al que pertenezca, para luego añadirlo a otro departamento, para así evitar una colisión y que en algún momento un miembro pertenezca a 2 departamentos

class Departamento:
    def __init__(self, nombre): # Parámetros de la clase Departamento
        self.nombre = nombre
        self.miembros = []

    def anadir_miembro(self, nuevo_miembro):
        self.miembros.append(nuevo_miembro)

    def eliminar_miembro(self, nombre_miembro):
        self.miembros.remove(nombre_miembro)

    def obtener_nombre(self, nombre):
        self.nombre = self.nombre # Método para obtener el nombre del departamento al que pertenezca un miembro