from datetime import date, timedelta


# =====================================================================
#  CLASE LIBRO
# =====================================================================
class Libro:
    """
    Representa un libro de la biblioteca y controla su disponibilidad.

    Atributos (privados, se acceden con getters):
        _titulo (str): título del libro.
        _autor (str): autor del libro.
        _codigo (str): código único del libro (por ejemplo, ISBN).
        _disponible (bool): True si el libro está en la biblioteca.
        _veces_prestado (int): cuántas veces se ha prestado.
    """

    def __init__(self, titulo: str, autor: str, codigo: str):
        if not titulo.strip() or not autor.strip() or not codigo.strip():
            raise ValueError("Título, autor y código no pueden estar vacíos.")
        self._titulo = titulo
        self._autor = autor
        self._codigo = codigo
        self._disponible = True
        self._veces_prestado = 0

    # ---------------------------- Getters ----------------------------
    def get_titulo(self) -> str:
        return self._titulo

    def get_autor(self) -> str:
        return self._autor

    def get_codigo(self) -> str:
        return self._codigo

    def get_veces_prestado(self) -> int:
        return self._veces_prestado

    # ------------------------ Métodos principales --------------------
    def verificar_disponibilidad(self) -> bool:
        """Devuelve True si el libro se puede prestar, False si ya está prestado."""
        return self._disponible

    def prestar_libro(self) -> bool:
        """
        Marca el libro como prestado.
        Devuelve True si el préstamo fue posible, False si ya estaba prestado.
        """
        if not self._disponible:
            print(f"El libro '{self._titulo}' no está disponible.")
            return False
        self._disponible = False
        self._veces_prestado += 1
        print(f"El libro '{self._titulo}' ha sido prestado.")
        return True

    def devolver_libro(self) -> bool:
        """
        Marca el libro como disponible otra vez.
        Devuelve True si se devolvió, False si el libro no estaba prestado.
        """
        if self._disponible:
            print(f"El libro '{self._titulo}' ya estaba en la biblioteca.")
            return False
        self._disponible = True
        print(f"El libro '{self._titulo}' ha sido devuelto.")
        return True

    def __str__(self) -> str:
        estado = "Disponible" if self._disponible else "Prestado"
        return f"Libro: {self._titulo} | Autor: {self._autor} | Código: {self._codigo} | {estado}"


# =====================================================================
#  CLASE USUARIO
# =====================================================================
class Usuario:
    """Representa a un usuario de la biblioteca."""

    def __init__(self, nombre: str, id_usuario: str, tarifa_multa_dia: float = 2.5):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._membresia_activa = True
        self._tarifa_multa = tarifa_multa_dia
        self._historial_prestamos = []

    # ---------------------------- Getters ----------------------------
    def get_nombre(self) -> str:
        return self._nombre

    def get_id(self) -> str:
        return self._id_usuario

    def is_membresia_activa(self) -> bool:
        return self._membresia_activa

    # ------------------------ Métodos principales --------------------
    def registrar_prestamos(self, prestamo):
        """Guarda un objeto de tipo Prestamo en el historial del usuario."""
        self._historial_prestamos.append(prestamo)
        print(f"Préstamo registrado exitosamente en el historial de {self._nombre}.")

    def calcular_multa(self, dias_retraso: int) -> float:
        """Calcula el monto de la multa según los días de retraso."""
        if dias_retraso > 0:
            total_multa = dias_retraso * self._tarifa_multa
            return total_multa
        return 0.0

    def renovar_membresia(self):
        """Activa de nuevo la membresía del usuario."""
        self._membresia_activa = True
        print(f"La membresía del usuario {self._nombre} ha sido renovada con éxito.")

    # ------------------------ Métodos adicionales --------------------
    def mostrar_historial(self):
        """Muestra la cantidad de préstamos realizados por el usuario."""
        print(f"\nHistorial de préstamos realizados de {self._nombre}:")
        if not self._historial_prestamos:
            print(" Sin préstamos registrados.")
        else:
            print(f" Total de préstamos realizados: {len(self._historial_prestamos)}")

    def __str__(self):
        estado = "Activa" if self._membresia_activa else "Inactiva"
        return f"Usuario: {self._nombre} | ID: {self._id_usuario} | Membresía: {estado}"


# =====================================================================
#  CLASE PRESTAMO
# =====================================================================
class Prestamo:
    """Representa el préstamo de un libro a un usuario."""

    def __init__(self, id_prestamo, usuario, libro, dias_plazo=7):
        self.id_prestamo = id_prestamo
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.dias_plazo = dias_plazo
        self.fecha_limite = self.fecha_prestamo + timedelta(days=dias_plazo)
        self.fecha_devolucion = None
        self.extensiones = 0
        self.max_extensiones = 2
        self.activo = True

    # ------------------------ Métodos principales --------------------
    def generar_ticket(self):
        print("=" * 30)
        print("      TICKET DE PRESTAMO")
        print("=" * 30)
        print("N° de prestamo:", self.id_prestamo)
        print("Usuario:", self.usuario.get_nombre())
        print("Libro:", self.libro.get_titulo())
        print("Fecha de prestamo:", self.fecha_prestamo)
        print("Fecha limite:", self.fecha_limite)
        if self.activo:
            print("Estado: Activo")
        else:
            print("Estado: Finalizado")
        print("=" * 30)

    def extender_plazo(self, dias_extra):
        if not self.activo:
            print("No se puede extender, el prestamo ya finalizo.")
            return False

        if dias_extra <= 0:
            print("Los dias extra deben ser mayor a 0.")
            return False

        if self.extensiones >= self.max_extensiones:
            print("Ya no puedes extender mas este prestamo.")
            return False

        self.fecha_limite = self.fecha_limite + timedelta(days=dias_extra)
        self.extensiones += 1
        print("Plazo extendido. Nueva fecha limite:", self.fecha_limite)
        return True

    def finalizar_prestamo(self):
        if not self.activo:
            print("Este prestamo ya estaba finalizado.")
            return 0

        self.fecha_devolucion = date.today()
        self.activo = False

        # vemos si se paso de la fecha limite
        dias_retraso = (self.fecha_devolucion - self.fecha_limite).days
        if dias_retraso < 0:
            dias_retraso = 0

        # el libro vuelve a estar disponible
        self.libro.devolver_libro()

        multa = 0
        if dias_retraso > 0:
            multa = self.usuario.calcular_multa(dias_retraso)
            print("Devolucion con", dias_retraso, "dia(s) de retraso.")
            print("Multa a pagar:", multa)
        else:
            print("Libro devuelto a tiempo, sin multa.")

        return multa


# =====================================================================
#  CLASE HIJA (HERENCIA): PRESTAMO ESTUDIANTE
# =====================================================================
class PrestamoEstudiante(Prestamo):
    """Préstamo para estudiantes: más días de plazo y más extensiones."""

    def __init__(self, id_prestamo, usuario, libro, carrera):
        super().__init__(id_prestamo, usuario, libro, dias_plazo=14)
        self.carrera = carrera
        self.max_extensiones = 3

    def generar_ticket(self):
        # reutilizamos el ticket normal y le agregamos la carrera
        super().generar_ticket()
        print("Tipo: Prestamo de estudiante")
        print("Carrera:", self.carrera)

    def finalizar_prestamo(self):
        multa = super().finalizar_prestamo()
        # los estudiantes pagan la mitad de la multa
        if multa > 0:
            multa = multa / 2
            print("Descuento de estudiante aplicado. Multa final:", multa)
        return multa


# =====================================================================
#  EJEMPLO DE USO (solo se ejecuta si corres este archivo directamente)
# =====================================================================
def titulo(texto):
    print("\n" + "#" * 50)
    print("  " + texto)
    print("#" * 50)


def demo():
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "LIB-001")
    libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "LIB-002")
    ana = Usuario("Ana Torres", "U-001")

    print(libro1)
    print(libro2)
    print(ana)

    titulo("1. Préstamo normal, con extensión y devolución a tiempo")
    if libro1.verificar_disponibilidad():
        libro1.prestar_libro()
        p1 = Prestamo(1, ana, libro1)
        ana.registrar_prestamos(p1)
        p1.generar_ticket()
        p1.extender_plazo(3)
        p1.finalizar_prestamo()

    titulo("2. Préstamo con retraso (se simulan 4 días de atraso)")
    libro1.prestar_libro()
    p2 = Prestamo(2, ana, libro1)
    ana.registrar_prestamos(p2)
    p2.fecha_limite = date.today() - timedelta(days=4)   # simulamos el atraso
    p2.finalizar_prestamo()

    titulo("3. Préstamo de estudiante (retraso de 4 días, multa a la mitad)")
    libro2.prestar_libro()
    p3 = PrestamoEstudiante(3, ana, libro2, "Ingeniería de Sistemas")
    ana.registrar_prestamos(p3)
    p3.generar_ticket()

    print("\nIntento de prestar el mismo libro otra vez:")
    libro2.prestar_libro()

    p3.fecha_limite = date.today() - timedelta(days=4)   # simulamos el atraso
    p3.finalizar_prestamo()

    titulo("4. Resumen final")
    ana.mostrar_historial()
    print(libro1)
    print(libro2)
    print("Veces prestado (libro1):", libro1.get_veces_prestado())


if __name__ == "__main__":
    demo()

    