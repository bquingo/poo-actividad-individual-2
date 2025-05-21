# tiendamascotas.py

class Mascota:
    """
    Clase raíz para todos los animales de la tienda.
    """
    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre: str = nombre
        self.edad: int = edad
        self.color: str = color

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Color: {self.color}"

# --- Jerarquía de Perros ---
class Perro(Mascota):
    """
    Clase base para todos los perros.
    """
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso: float = peso
        self.muerde: bool = muerde

    @staticmethod
    def sonido():
        """
        Método estático que imprime el sonido de los perros.
        """
        print("Los perros ladran")

    def __str__(self):
        return (f"{super().__str__()}, Peso: {self.peso}kg, "
                f"Muerde: {'Sí' if self.muerde else 'No'}")

# Categorías de Perros por tamaño
class PerroPequeno(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class PerroMediano(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class PerroGrande(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

# Razas de Perros Pequeños
class Caniche(PerroPequeno):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class YorkshireTerrier(PerroPequeno):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Schnauzer(PerroPequeno): # Schnauzer puede ser mediano también, pero aquí se pide como pequeño
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Chihuahua(PerroPequeno):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

# Razas de Perros Medianos
class Collie(PerroMediano):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Dalmata(PerroMediano):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Bulldog(PerroMediano):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Galgo(PerroMediano):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Sabueso(PerroMediano):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

# Razas de Perros Grandes
class PastorAleman(PerroGrande):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Doberman(PerroGrande): # Escrito como "do berman" en el enunciado
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)

class Rottweiler(PerroGrande): # Corregido "rotweiller"
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color, peso, muerde)


# --- Jerarquía de Gatos ---
class Gato(Mascota):
    """
    Clase base para todos los gatos.
    """
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self.altura_salto: float = altura_salto
        self.longitud_salto: float = longitud_salto

# Categorías de Gatos por tipo de pelo
class GatoSinPelo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class GatoPeloLargo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class GatoPeloCorto(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

# Razas de Gatos Sin Pelo
class Esfinge(GatoSinPelo): # Sphynx
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Elfo(GatoSinPelo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Donskoy(GatoSinPelo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

# Razas de Gatos de Pelo Largo
class Angora(GatoPeloLargo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Himalayo(GatoPeloLargo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Balines(GatoPeloLargo): # Balinese
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Somali(GatoPeloLargo):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

# Razas de Gatos de Pelo Corto
class AzulRuso(GatoPeloCorto):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Britanico(GatoPeloCorto):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class Manx(GatoPeloCorto):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)

class DevonRex(GatoPeloCorto):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)


# --- Ejemplo de uso ---
if __name__ == "__main__":
    print("--- Perros ---")
    mi_caniche = Caniche(nombre="Lulú", edad=3, color="Blanco", peso=4.5, muerde=False)
    mi_pastor = PastorAleman(nombre="Rex", edad=5, color="Negro y Fuego", peso=35.0, muerde=True)

    print("\nInformación del Caniche:")
    print(mi_caniche)
    print("Sonido del Caniche:")

    print("\nInformación del Pastor Alemán:")
    print(mi_pastor)
    print("\n--- Gatos ---")
    gato_esfinge = Esfinge(nombre="Anubis", edad=2, color="Piel Rosada", altura_salto=1.5, longitud_salto=2.0)
    gato_angora = Angora(nombre="Pelusa", edad=4, color="Blanco Nieve", altura_salto=1.2, longitud_salto=1.8)

    print("\nInformación del Esfinge:")
    print(gato_esfinge)


    print("\nInformación del Angora:")
    print(gato_angora)
