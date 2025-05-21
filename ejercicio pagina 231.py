class Persona:
    """
    Representa a una persona con nombre y dirección.
    """
    def __init__(self, nombre: str, direccion: str):
        """
        Constructor de la clase Persona.

        Args:
            nombre (str): El nombre de la persona.
            direccion (str): La dirección de la persona.
        """
        self.nombre: str = nombre  # Atributo público nombre
        self.direccion: str = direccion  # Atributo público dirección

    def get_nombre(self) -> str:
        """
        Retorna el nombre de la persona.
        """
        return self.nombre

    def get_direccion(self) -> str:
        """
        Retorna la dirección de la persona.
        """
        return self.direccion

    def set_nombre(self, nombre: str):
        """
        Establece el nombre de la persona.

        Args:
            nombre (str): El nuevo nombre.
        """
        self.nombre = nombre

    def set_direccion(self, direccion: str):
        """
        Establece la dirección de la persona.

        Args:
            direccion (str): La nueva dirección.
        """
        self.direccion = direccion

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Dirección: {self.direccion}"


class Estudiante(Persona):
    """
    Representa a un estudiante, que es un tipo de Persona,
    con carrera y semestre.
    """
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        """
        Constructor de la clase Estudiante.

        Args:
            nombre (str): El nombre del estudiante.
            direccion (str): La dirección del estudiante.
            carrera (str): La carrera del estudiante.
            semestre (int): El semestre actual del estudiante.
        """
        super().__init__(nombre, direccion)
        self.carrera: str = carrera  # Atributo público carrera
        self.semestre: int = semestre  # Atributo público semestre

    def get_carrera(self) -> str:
        """
        Retorna la carrera del estudiante.
        """
        return self.carrera

    def get_semestre(self) -> int:
        """
        Retorna el semestre del estudiante.
        """
        return self.semestre

    def set_carrera(self, carrera: str):
        """
        Establece la carrera del estudiante.

        Args:
            carrera (str): La nueva carrera.
        """
        self.carrera = carrera

    def set_semestre(self, semestre: int):
        """
        Establece el semestre del estudiante.

        Args:
            semestre (int): El nuevo semestre.
        """
        self.semestre = semestre

    def __str__(self) -> str:
        return f"{super().__str__()} - Carrera: {self.carrera}, Semestre: {self.semestre}"


class Profesor(Persona):
    """
    Representa a un profesor, que es un tipo de Persona,
    con departamento y categoría.
    """
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        """
        Constructor de la clase Profesor.

        Args:
            nombre (str): El nombre del profesor.
            direccion (str): La dirección del profesor.
            departamento (str): El departamento al que pertenece el profesor.
            categoria (str): La categoría del profesor.
        """
        super().__init__(nombre, direccion)
        self.departamento: str = departamento  # Atributo público departamento
        self.categoria: str = categoria      # Atributo público categoría

    def get_departamento(self) -> str:
        """
        Retorna el departamento del profesor.
        """
        return self.departamento

    def get_categoria(self) -> str:
        """
        Retorna la categoría del profesor.
        """
        return self.categoria

    def set_departamento(self, departamento: str):
        """
        Establece el departamento del profesor.

        Args:
            departamento (str): El nuevo departamento.
        """
        self.departamento = departamento

    def set_categoria(self, categoria: str):
        """
        Establece la categoría del profesor.

        Args:
            categoria (str): La nueva categoría.
        """
        self.categoria = categoria

    def __str__(self) -> str:
        return f"{super().__str__()} - Departamento: {self.departamento}, Categoría: {self.categoria}"

# Ejemplo de uso
if __name__ == "__main__":
    persona1 = Persona("Juan Pérez", "Calle  37 #97a-45")
    print(f"Persona: {persona1.get_nombre()}, Dirección: {persona1.get_direccion()}")
    print(persona1)

    print("\n" + "="*20 + "\n")

    estudiante1 = Estudiante("Ana Gómez", "Avenida Siempre Viva 742", "Ingeniería de Sistemas", 5)
    print(f"Estudiante: {estudiante1.get_nombre()}, Carrera: {estudiante1.get_carrera()}, Semestre: {estudiante1.get_semestre()}")
    estudiante1.set_semestre(6)
    print(f"Estudiante (semestre actualizado): {estudiante1.get_semestre()}")
    print(estudiante1)

    print("\n" + "="*20 + "\n")

    profesor1 = Profesor("Carlos López", "Boulevard de los Sueños Rotos 45", "Matemáticas", "Titular")
    print(f"Profesor: {profesor1.get_nombre()}, Departamento: {profesor1.get_departamento()}, Categoría: {profesor1.get_categoria()}")
    profesor1.set_categoria("Asociado")
    print(f"Profesor (categoría actualizada): {profesor1.get_categoria()}")
    print(profesor1)