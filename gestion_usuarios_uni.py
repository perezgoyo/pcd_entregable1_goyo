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

# Crear una universidad(instancia de la clase Universidad)
mi_universidad = Universidad()

# Crear algunas asignaturas
asig1 = Asignatura('BDI')
asig2 = Asignatura('BDII')
asig3 = Asignatura('PCD')

# Agregar asignaturas a la universidad
mi_universidad.agregar_asignatura(asig1)
mi_universidad.agregar_asignatura(asig2)

# Crear estudiantes
estudiante1 = Estudiante('Juan', '12343478A', 'Calle Abeelxo 12', 'V')
estudiante2 = Estudiante('Pedro', '98565432B', 'Calle Cypher 14', 'V')

# Asignar la universidad a los estudiantes
estudiante1.universidad = mi_universidad
estudiante2.universidad = mi_universidad

# Matricular al estudiante de algunas de las asignaturas disponibles
estudiante1.agregar_asignatura_matriculada(asig1)
estudiante1.agregar_asignatura_matriculada(asig2)

#Matricular al estudiante en  una asignatura no disponible(No ha sido agregada aún a mi_universidad)
#estudiante1.agregar_asignatura_matriculada(asig3)  # Esta asignatura no está disponible

# Ver las asignaturas matriculadas por el estudiante
print("Listado de asignaturas matriculadas por el estudiante 1:", [asig.nombre for asig in estudiante1.asignaturas_matriculadas])

# Crear un profesor
profesor1 = Profesor('Pedro', '23477789C', 'Calle Bumbum 6', 'V', 'DIIC')

# Asignar la universidad al profesor
profesor1.universidad = mi_universidad

# Agregar asignaturas al profesor
profesor1.agregar_asignatura(asig1)
profesor1.agregar_asignatura(asig2)

#Matricular al profesor  en una asignatura no  disponible(No ha sido agregada aún a mi_universidad)
#profesor1.agregar_asignatura(asig3)  # Esta asignatura no está disponible

# Ver las asignaturas impartidas por el profesor
print("Listado de asignaturas impartidas por el profesor 1:", [asig.nombre for asig in profesor1.asignaturas])

# Eliminar una asignatura de la universidad
mi_universidad.eliminar_asignatura(asig2)

# Ver las asignaturas disponibles en la universidad
print("Listado de asignaturas disponibles en la universidad:", [asig.nombre for asig in mi_universidad.obtener_asignaturas_disponibles()])

# Crear un departamento
departamento_DITEC = Departamento("Departamento DITEC")

# Crear un miembro de departamento
profesor_titular = ProfesorTitular("Carlos", "34567890D", "Calle Valentino 8", "M", departamento_DITEC, "Inteligencia Artificial")

# Asignar la universidad al profesor titular
profesor_titular.universidad = mi_universidad

# Agregar el profesor titular como miembro del departamento
departamento_DITEC.anadir_miembro(profesor_titular)

# Ver los miembros del departamento de informática
print("Miembros del Departamento DITEC:", [miembro._nombre for miembro in departamento_DITEC.miembros])

# Crear un profesor asociado
profesor_asociado = ProfesorAsociado("Paula", "32374141E", "Calle Nairobi 2", "M", departamento_DITEC)

# Asignar la universidad al profesor asociado
profesor_asociado.universidad = mi_universidad

# Agregar el profesor asociado como miembro del departamento
departamento_DITEC.anadir_miembro(profesor_asociado)

# Ver los miembros del departamento de informática después de agregar el profesor asociado
print("Miembros del Departamento DITEC:", [miembro._nombre for miembro in departamento_DITEC.miembros])

# Crear una universidad
mi_universidad = Universidad()

# Crear asignaturas
asignatura_1 = Asignatura("Computadores")
asignatura_2 = Asignatura("Fundamentos de Redes")
asignatura_3 = Asignatura("ML")

# Agregar asignaturas a la universidad
mi_universidad.agregar_asignatura(asignatura_1)
mi_universidad.agregar_asignatura(asignatura_2)
mi_universidad.agregar_asignatura(asignatura_3)

# Crear un departamento
departamento_DIS = Departamento("Departamento DIS")

# Crear miembros del departamento
profesor_titular = ProfesorTitular("Carlos", "34567890D", "Calle Principal 4", "M", departamento_DIS, "Inteligencia Artificial")
profesor_asociado = ProfesorAsociado("Laura", "45678901E", "Calle Secundaria 5", "F", departamento_DIS)
investigador = Investigador("Eva", "56789012F", "Calle Terciaria 6", "F", departamento_DIS, "Redes Neuronales")

# Agregar miembros al departamento
departamento_DIS.anadir_miembro(profesor_titular)
departamento_DIS.anadir_miembro(profesor_asociado)
departamento_DIS.anadir_miembro(investigador)

# Crear estudiantes
estudiante_1 = Estudiante("Evaristo", "12345328A", "Calle Príncipe de Asturias 22", "V")
estudiante_2 = Estudiante("Juana", "23456879B", "Calle José Barnés 36", "M")

# Asignar la universidad a los estudiantes
estudiante_1.universidad = mi_universidad
estudiante_2.universidad = mi_universidad

# Matricular estudiantes en asignaturas
estudiante_1.agregar_asignatura_matriculada(asignatura_1)
estudiante_1.agregar_asignatura_matriculada(asignatura_3)
estudiante_2.agregar_asignatura_matriculada(asignatura_2)

# Crear el departamento que aún no hemos creado
departamento_DIIC = Departamento('DIIC')

# Crear miembros de departamento
profesor_titular = ProfesorTitular('Pedro', '666554321B', 'Calle Grenheir 456', 'V', departamento_DIIC, 'Ciencias de la Computación')
profesor_asociado = ProfesorAsociado('Ana', '736535837C', 'Calle Iván 456', 'M', departamento_DITEC)
investigador = Investigador('Elena', '83635645D', 'Calle Aléx 789', 'M', departamento_DIS, 'Inteligencia Artificial')

# Crear un miembro de departamento y agregarlo
miembro_departamento = Miembro_Departamento(departamento_DIIC)
miembro_departamento.anadir_miembro(profesor_titular)
miembro_departamento.anadir_miembro(profesor_asociado)
miembro_departamento.anadir_miembro(investigador)

print("Miembros de DIIC:", [miembro._nombre for miembro in departamento_DIIC.miembros])

# Cambiar a un nuevo departamento
miembro_departamento.cambiar_departamento(departamento_DIS, profesor_asociado, departamento_DIS)

print("Miembros de DIIC después del cambio:", [miembro._nombre for miembro in departamento_DIIC.miembros])
print("Miembros de DITEC después del cambio:", [miembro._nombre for miembro in departamento_DITEC.miembros])
print("Miembros de DIS después del cambio:", [miembro._nombre for miembro in departamento_DIS.miembros])

# Intentar cambiar un miembro que no está en el departamento actual
try:
    miembro_departamento.cambiar_departamento(departamento_DIS, profesor_titular, departamento_DIS)
except ValueError as e:
    print(e)