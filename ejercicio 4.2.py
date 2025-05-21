from enum import Enum

# Clase: Inmueble
class Inmueble:
    """
    Esta clase denominada Inmueble modela un inmueble que posee
    como atributos un identificador, un área, una dirección y un precio
    de venta. Es la clase raíz de una jerarquía de herencia.
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str):
        """
        Constructor de la clase Inmueble
        :param identificador_inmobiliario: Parámetro que define el identificador de un inmueble
        :param area: Parámetro que define el área de un inmueble
        :param direccion: Parámetro que define la dirección donde se encuentra localizado un inmueble
        """
        self._identificador_inmobiliario: int = identificador_inmobiliario
        self._area: int = area
        self._direccion: str = direccion
        self._precio_venta: float = 0.0

    def calcular_precio_venta(self, valor_area: float) -> float:
        """
        Método que a partir del valor del área de un inmueble, calcula su
        precio de venta.
        :param valor_area: El valor unitario por área de un determinado inmueble
        :return: Precio de venta del inmueble
        """
        self._precio_venta = self._area * valor_area
        return self._precio_venta

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de un inmueble
        """
        print(f"Identificador inmobiliario = {self._identificador_inmobiliario}")
        print(f"Área = {self._area} m2")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = ${self._precio_venta:,.2f}")

# Clase: InmuebleVivienda
class InmuebleVivienda(Inmueble):
    """
    Esta clase denominada InmuebleVivienda modela un inmueble
    destinado para la vivienda con atributos como el número de
    habitaciones y el número de baños que posee.
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int):
        """
        Constructor de la clase InmuebleVivienda
        :param identificador_inmobiliario: Identificador inmobiliario del inmueble
        :param area: Área del inmueble
        :param direccion: Dirección del inmueble
        :param numero_habitaciones: Número de habitaciones del inmueble
        :param numero_banos: Número de baños del inmueble
        """
        super().__init__(identificador_inmobiliario, area, direccion)
        self._numero_habitaciones: int = numero_habitaciones
        self._numero_banos: int = numero_banos

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de un inmueble para la vivienda
        """
        super().imprimir()
        print(f"Número de habitaciones = {self._numero_habitaciones}")
        print(f"Número de baños = {self._numero_banos}")

# Clase: Casa
class Casa(InmuebleVivienda):
    """
    Esta clase denominada Casa modela un tipo específico de inmueble
    destinado para la vivienda con atributos como el número de pisos
    que tiene una casa.
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)
        self._numero_pisos: int = numero_pisos

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de una casa
        """
        super().imprimir()
        print(f"Número de pisos = {self._numero_pisos}")

# Clase: Apartamento
class Apartamento(InmuebleVivienda):
    """
    Esta clase denominada Apartamento modela un tipo de inmueble
    específico destinado para la vivienda.
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de un apartamento
        """
        super().imprimir()
        # No hay atributos adicionales específicos de Apartamento base para imprimir aquí

# Clase: CasaRural
class CasaRural(Casa):
    """
    Esta clase denominada CasaRural modela un tipo específico de casa
    ubicada en el sector rural.
    """
    _valor_area: float = 1500000.0  # Atributo de clase (equivalente a static en Java)

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int,
                 distancia_cabecera: int, altitud: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self._distancia_cabecera: int = distancia_cabecera
        self._altitud: int = altitud

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de una casa rural.
        """
        super().imprimir()
        # Corrección: se imprimía _numero_habitaciones en lugar de _distancia_cabecera
        print(f"Distancia a la cabecera municipal = {self._distancia_cabecera} km.")
        print(f"Altitud sobre el nivel del mar = {self._altitud} metros.")
        print()

# Clase: CasaUrbana
class CasaUrbana(Casa):
    """
    Esta clase denominada CasaUrbana modela un tipo específico de casa
    destinada para la vivienda localizada en el sector urbano.
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de una casa urbana.
        """
        super().imprimir()
        # No hay atributos adicionales específicos de CasaUrbana base para imprimir aquí

# Clase: ApartamentoFamiliar
class ApartamentoFamiliar(Apartamento):
    """
    Esta clase denominada ApartamentoFamiliar modela un tipo
    específico de apartamento con atributos como el valor por área y el
    valor de la administración.
    """
    _valor_area: float = 2000000.0

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, valor_administracion: int):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)
        # Corrección: 'valor Administración' en Java, unificado a 'valor_administracion'
        self._valor_administracion: int = valor_administracion

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de un apartamento familiar.
        """
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administracion:,.2f}")
        print()

# Clase: Apartaestudio
class Apartaestudio(Apartamento):
    """
    Esta clase denominada Apartaestudio modela un tipo específico de
    apartamento que tiene una sola habitación.
    """
    _valor_area: float = 1500000.0

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str):
        # Los apartaestudios tienen una sola habitación y un solo baño por defecto
        super().__init__(identificador_inmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de un apartaestudio.
        """
        super().imprimir()
        print() # Solo para mantener la misma salida que el original Java si imprimía una línea vacía

# Clase: CasaConjuntoCerrado
class CasaConjuntoCerrado(CasaUrbana):
    """
    Esta clase denominada CasaConjuntoCerrado modela un tipo
    específico de casa urbana que se encuentra en un conjunto cerrado.
    """
    _valor_area: float = 2500000.0

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int,
                 valor_administracion: int, tiene_piscina: bool, tiene_campos_deportivos: bool):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self._valor_administracion: int = valor_administracion
        self._tiene_piscina: bool = tiene_piscina
        self._tiene_campos_deportivos: bool = tiene_campos_deportivos

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de una casa en conjunto cerrado.
        """
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administracion:,.2f}")
        print(f"Tiene piscina? = {'Sí' if self._tiene_piscina else 'No'}")
        print(f"Tiene campos deportivos? = {'Sí' if self._tiene_campos_deportivos else 'No'}")
        print()

# Clase: CasaIndependiente
class CasaIndependiente(CasaUrbana):
    """
    Esta clase denominada CasaIndependiente modela un tipo específico
    de casa urbana que no está en conjunto cerrado.
    """
    _valor_area: float = 3000000.0

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de una casa independiente.
        """
        super().imprimir()
        print() # Solo para mantener la misma salida que el original Java

# Definición del Enum para Local
class TipoLocal(Enum):
    INTERNO = "INTERNO"
    CALLE = "CALLE"

# Clase: Local
class Local(Inmueble):
    """
    Esta clase denominada Local modela un tipo específico de inmueble
    que no está destinado para la vivienda.
    """
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 tipo_local: TipoLocal):
        super().__init__(identificador_inmobiliario, area, direccion)
        self._tipo_local: TipoLocal = tipo_local

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de un local.
        """
        super().imprimir()
        print(f"Tipo de local = {self._tipo_local.value}")

# Clase: LocalComercial
class LocalComercial(Local):
    """
    Esta clase denominada LocalComercial modela un tipo específico de
    Local destinado para un uso comercial.
    """
    _valor_area: float = 3000000.0

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 tipo_local: TipoLocal, centro_comercial: str):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self._centro_comercial: str = centro_comercial

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de un local comercial.
        """
        super().imprimir()
        print(f"Centro comercial = {self._centro_comercial}")
        print()

# Clase: Oficina
class Oficina(Local):
    """
    Esta clase denominada Oficina modela un tipo específico de local.
    """
    _valor_area: float = 3500000.0

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 tipo_local: TipoLocal, es_gobierno: bool):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self._es_gobierno: bool = es_gobierno

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de una oficina.
        """
        super().imprimir()
        print(f"Es oficina gubernamental = {'Sí' if self._es_gobierno else 'No'}")
        print()

# Clase: Prueba (se convierte en un script/función principal)
def main_prueba_inmuebles():
    """
    Método main que crea dos inmuebles, calcula su precio de
    acuerdo al área y se muestran sus datos en pantalla.
    """
    apto1 = ApartamentoFamiliar(identificador_inmobiliario=103067, area=120,
                                direccion="Avenida Santander 45-45", numero_habitaciones=3,
                                numero_banos=2, valor_administracion=200000)
    print("--- Datos apartamento familiar ---")
    # Usamos el _valor_area de la clase específica
    apto1.calcular_precio_venta(ApartamentoFamiliar._valor_area)
    apto1.imprimir()

    print("--- Datos apartaestudio ---")
    # El constructor de Apartaestudio no toma numero_habitaciones ni numero_banos explícitamente
    aptestudio1 = Apartaestudio(identificador_inmobiliario=12354, area=50,
                                direccion="Avenida Caracas 30-15")
    aptestudio1.calcular_precio_venta(Apartaestudio._valor_area)
    aptestudio1.imprimir()

    # Ejemplo adicional para probar otra clase, por ejemplo CasaRural
    print("--- Datos Casa Rural ---")
    casa_r = CasaRural(identificador_inmobiliario=78901, area=250, direccion="Vereda El Pinar Lote 3",
                       numero_habitaciones=4, numero_banos=3, numero_pisos=2,
                       distancia_cabecera=15, altitud=2100)
    casa_r.calcular_precio_venta(CasaRural._valor_area) # Usa el _valor_area de CasaRural
    casa_r.imprimir()

    print("--- Datos Local Comercial ---")
    local_c = LocalComercial(identificador_inmobiliario=45678, area=80, direccion="Calle Falsa 123",
                             tipo_local=TipoLocal.CALLE, centro_comercial="Centro Mayor")
    local_c.calcular_precio_venta(LocalComercial._valor_area)
    local_c.imprimir()


if __name__ == "__main__":
    main_prueba_inmuebles()