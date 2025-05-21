# Clase: Profesor
class Profesor:
    def _imprimir(self):
        print("Es un profesor.")

# Clase: ProfesorTitular
class ProfesorTitular(Profesor):

    def _imprimir(self):
        print("Es un profesor titular.")

# Clase: Prueba (convertida a script)
if __name__ == "__main__":
    profesor1 = ProfesorTitular()
    profesor1._imprimir()