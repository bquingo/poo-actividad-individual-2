# Clase: Cuenta
class Cuenta:
    """
    Esta clase denominada Cuenta modela una cuenta bancaria con los
    atributos saldo, número de consignaciones, número de retiros, tasa
    anual de interés y comisión mensual.
    """

    def __init__(self, saldo: float, tasa_anual: float):
        """
        Constructor de la clase Cuenta
        :param saldo: Parámetro que define el saldo de la cuenta
        :param tasa_anual: Parámetro que define la tasa anual de interés de la cuenta
        """
        self._saldo: float = saldo
        self._tasa_anual: float = tasa_anual
        self._numero_consignaciones: int = 0
        self._numero_retiros: int = 0
        self._comision_mensual: float = 0.0

    def consignar(self, cantidad: float):
        """
        Método que recibe una cantidad de dinero a consignar y actualiza
        el saldo de la cuenta.
        :param cantidad: Parámetro que define la cantidad de dinero a
        consignar en la cuenta.
        """
        if cantidad > 0:
            self._saldo += cantidad
            self._numero_consignaciones += 1
        else:
            print("La cantidad a consignar debe ser mayor que cero.")

    def retirar(self, cantidad: float):
        """
        Método que recibe una cantidad de dinero a retirar y actualiza
        el saldo de la cuenta.
        :param cantidad: Parámetro que define la cantidad de dinero a retirar
        de la cuenta.
        """
        if cantidad > 0:
            if self._saldo >= cantidad:
                self._saldo -= cantidad
                self._numero_retiros += 1
            else:
                print("Saldo insuficiente para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")

    def calcular_interes_mensual(self):
        """
        Calcula y añade el interés mensual al saldo.
        """
        tasa_mensual = self._tasa_anual / 12 / 100  # Asumiendo que la tasa anual está en porcentaje
        interes_mensual_generado = self._saldo * tasa_mensual
        self._saldo += interes_mensual_generado

    def extracto_mensual(self):
        """
        Realiza las operaciones de fin de mes: cobra comisión y calcula interés.
        """
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()

    def imprimir_detalle(self):
        """
        Método para imprimir los detalles básicos de la cuenta.
        """
        print(f"Saldo: ${self._saldo:,.2f}")
        print(f"Comisión mensual: ${self._comision_mensual:,.2f}")
        print(f"Tasa anual de interés: {self._tasa_anual:.2f}%")
        print(f"Número de consignaciones: {self._numero_consignaciones}")
        print(f"Número de retiros: {self._numero_retiros}")
        print(f"Número total de transacciones: {self._numero_consignaciones + self._numero_retiros}")

# Clase: CuentaAhorros
class CuentaAhorros(Cuenta):
    """
    Esta clase denominada CuentaAhorros modela una cuenta de ahorros
    que es una subclase de Cuenta. Tiene un nuevo atributo: activa.
    """

    def __init__(self, saldo: float, tasa_anual: float):
        """
        Constructor de la clase CuentaAhorros
        :param saldo: Parámetro que define el saldo de la cuenta de ahorros
        :param tasa_anual: Parámetro que define la tasa anual de interés de la
        cuenta de ahorros
        """
        super().__init__(saldo, tasa_anual)
        # Atributo que identifica si una cuenta está activa; lo está si su saldo
        # es superior a 10000
        self._activa: bool = self._saldo >= 10000

    def retirar(self, cantidad: float):
        """
        Método que recibe una cantidad de dinero a retirar y actualiza
        el saldo de la cuenta.
        :param cantidad: Parámetro que define la cantidad a retirar de una
        cuenta de ahorros.
        """
        if self._activa:
            super().retirar(cantidad)
        else:
            print("La cuenta no está activa. No se pueden realizar retiros.")

    def consignar(self, cantidad: float):
        """
        Método que recibe una cantidad de dinero a consignar y actualiza
        el saldo de la cuenta.
        :param cantidad: Parámetro que define la cantidad a consignar en
        una cuenta de ahorros.
        """
        if self._activa:
            super().consignar(cantidad)
            # Se podría reactivar la cuenta si el saldo supera el mínimo tras consignar
            # if self._saldo >= 10000:
            #     self._activa = True
        else:
            # Permitir consignar incluso si no está activa, para poder reactivarla
            # Si se consigna y supera los 10000, se activa
            if cantidad > 0:
                self._saldo += cantidad # Consignación directa para evitar el chequeo de activa en super().consignar
                self._numero_consignaciones += 1
                if self._saldo >= 10000:
                    self._activa = True
                    print("Cuenta reactivada tras la consignación.")
                else:
                    print("Consignación realizada, pero la cuenta sigue inactiva (saldo menor a $10,000).")
            else:
                print("La cantidad a consignar debe ser mayor que cero.")


    def extracto_mensual(self):
        """
        Método que genera el extracto mensual de una cuenta de ahorros.
        """
        # Si la cantidad de retiros es superior a cuatro, se genera una
        # comisión mensual adicional.
        if self._numero_retiros > 4:
            # La comisión mensual de la clase base se suma a esta comisión adicional
            self._comision_mensual += (self._numero_retiros - 4) * 1000

        super().extracto_mensual()
        # Si el saldo actualizado de la cuenta es menor a 10000, la
        # cuenta no se activa (o se desactiva)
        if self._saldo < 10000:
            self._activa = False

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de una cuenta de ahorros.
        """
        print("--- Cuenta de Ahorros ---")
        super().imprimir_detalle() # Llama al método de la clase base para info común
        print(f"Cuenta activa: {'Sí' if self._activa else 'No'}")
        print("-" * 25)


# Clase: CuentaCorriente
class CuentaCorriente(Cuenta):
    """
    Esta clase denominada CuentaCorriente modela una cuenta bancaria
    que es una subclase de Cuenta. Tiene un nuevo atributo: sobregiro.
    """

    def __init__(self, saldo: float, tasa_anual: float):
        """
        Constructor de la clase CuentaCorriente
        :param saldo: Parámetro que define el saldo de la cuenta corriente
        :param tasa_anual: Parámetro que define la tasa anual de interés de la
        cuenta corriente
        """
        super().__init__(saldo, tasa_anual)
        self._sobregiro: float = 0.0  # Inicialmente no hay sobregiro

    def retirar(self, cantidad: float):
        """
        Método que recibe una cantidad de dinero a retirar y actualiza
        el saldo de la cuenta.
        :param cantidad: Parámetro que define la cantidad de dinero a
        retirar de la cuenta corriente.
        """
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
            return

        resultado_temporal = self._saldo - cantidad
        # Si el valor a retirar supera el saldo de la cuenta, el valor
        # excedente se convierte en sobregiro y el saldo es cero.
        if resultado_temporal < 0:
            self._sobregiro -= resultado_temporal  # resultado_temporal es negativo, por eso se resta para sumar al sobregiro
            self._saldo = 0
            self._numero_retiros += 1 # Contabilizar el retiro
        else:
            # Si no hay sobregiro (o el retiro no lo causa), se realiza un retiro normal
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        """
        Método que recibe una cantidad de dinero a consignar y actualiza
        el saldo de la cuenta.
        :param cantidad: Parámetro que define la cantidad de dinero a
        consignar en la cuenta corriente.
        """
        if cantidad <= 0:
            print("La cantidad a consignar debe ser mayor que cero.")
            return

        # Si existe sobregiro, la cantidad consignada se aplica primero a cubrirlo.
        if self._sobregiro > 0:
            residuo_sobregiro = self._sobregiro - cantidad
            if residuo_sobregiro > 0: # La consignación no cubre todo el sobregiro
                self._sobregiro = residuo_sobregiro
                # El saldo sigue siendo 0
            else: # La consignación cubre el sobregiro y puede haber sobrante para el saldo
                self._saldo = -residuo_sobregiro # -residuo_sobregiro es la cantidad que sobra
                self._sobregiro = 0
            self._numero_consignaciones += 1 # Contabilizar la consignación
        else:
            # Si no hay sobregiro, se realiza una consignación normal
            super().consignar(cantidad)

    def extracto_mensual(self):
        """
        Método que genera el extracto mensual de la cuenta.
        (En este caso, solo llama al de la clase padre, pero podría tener lógica específica)
        """
        super().extracto_mensual()
        # La lógica de interés sobre sobregiro no está especificada,
        # pero podría ir aquí si fuera necesario.

    def imprimir(self):
        """
        Método que muestra en pantalla los datos de una cuenta corriente.
        """
        print("--- Cuenta Corriente ---")
        super().imprimir_detalle() # Llama al método de la clase base para info común
        print(f"Valor de sobregiro: ${self._sobregiro:,.2f}")
        print("-" * 25)


# Clase: PruebaCuenta (equivalente al main de Java)
def main_prueba_cuenta():
    """
    Esta función prueba diferentes acciones realizadas por cuentas bancarias
    de tipo Cuenta de ahorros y Cuenta corriente.
    """
    print("--- Configuración Cuenta de Ahorros ---")
    try:
        saldo_inicial_ahorros = float(input("Ingrese saldo inicial para la cuenta de ahorros = $: "))
        tasa_ahorros = float(input("Ingrese tasa de interés anual para la cuenta de ahorros (ej. 4.5 para 4.5%) = "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números.")
        return

    cuenta1 = CuentaAhorros(saldo_inicial_ahorros, tasa_ahorros)
    cuenta1.imprimir()

    print("\n--- Operaciones Cuenta de Ahorros ---")
    try:
        cantidad_depositar = float(input("Ingresar cantidad a consignar: $"))
        cuenta1.consignar(cantidad_depositar)
    except ValueError:
        print("Cantidad inválida.")

    try:
        cantidad_retirar = float(input("Ingresar cantidad a retirar: $"))
        cuenta1.retirar(cantidad_retirar)
    except ValueError:
        print("Cantidad inválida.")

    cuenta1.extracto_mensual()
    cuenta1.imprimir()

    print("\n\n--- Configuración Cuenta Corriente ---")
    try:
        saldo_inicial_corriente = float(input("Ingrese saldo inicial para la cuenta corriente = $: "))
        tasa_corriente = float(input("Ingrese tasa de interés anual para la cuenta corriente (ej. 2.0 para 2.0%) = "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números.")
        return

    cuenta2 = CuentaCorriente(saldo_inicial_corriente, tasa_corriente)
    cuenta2.imprimir()

    print("\n--- Operaciones Cuenta Corriente ---")
    try:
        cantidad_depositar_cc = float(input("Ingresar cantidad a consignar en cuenta corriente: $"))
        cuenta2.consignar(cantidad_depositar_cc)
    except ValueError:
        print("Cantidad inválida.")

    try:
        cantidad_retirar_cc = float(input("Ingresar cantidad a retirar de cuenta corriente: $"))
        cuenta2.retirar(cantidad_retirar_cc)
    except ValueError:
        print("Cantidad inválida.")

    cuenta2.extracto_mensual()
    cuenta2.imprimir()

if __name__ == "__main__":
    main_prueba_cuenta()