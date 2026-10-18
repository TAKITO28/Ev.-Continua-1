"""
Sistema de gestión de biblioteca: clases y menú interactivo en un solo archivo.

Clases:
    Libro, Usuario, Prestamo, PrestamoEstudiante (herencia) y Biblioteca (menú).

Ejecutar con:  python menu1.py
"""
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
    """
    Representa a un usuario de la biblioteca.

    Atributos (privados, se acceden con getters):
        _nombre (str), _id_usuario (str), _membresia_activa (bool),
        _tarifa_multa (float, por día de retraso), _historial_prestamos (list).
    """

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
            return dias_retraso * self._tarifa_multa
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
    """
    Transacción que une un Usuario con un Libro durante un plazo de días.

    Atributos (privados, se acceden con getters):
        _id_prestamo, _usuario, _libro, _fecha_prestamo, _dias_plazo,
        _fecha_limite, _fecha_devolucion, _extensiones, _max_extensiones, _activo.
    """

    def __init__(self, id_prestamo, usuario, libro, dias_plazo=7):
        self._id_prestamo = id_prestamo
        self._usuario = usuario
        self._libro = libro
        self._fecha_prestamo = date.today()
        self._dias_plazo = dias_plazo
        self._fecha_limite = self._fecha_prestamo + timedelta(days=dias_plazo)
        self._fecha_devolucion = None
        self._extensiones = 0
        self._max_extensiones = 2
        self._activo = True

    # ---------------------------- Getters ----------------------------
    def get_id(self):
        return self._id_prestamo

    def get_usuario(self) -> Usuario:
        return self._usuario

    def get_libro(self) -> Libro:
        return self._libro

    def get_fecha_limite(self) -> date:
        return self._fecha_limite

    def get_dias_plazo(self) -> int:
        return self._dias_plazo

    def is_activo(self) -> bool:
        return self._activo

    # ------------------------ Métodos principales --------------------
    def generar_ticket(self):
        """Imprime el comprobante del préstamo."""
        print("=" * 30)
        print("      TICKET DE PRESTAMO")
        print("=" * 30)
        print("N° de prestamo:", self._id_prestamo)
        print("Usuario:", self._usuario.get_nombre())
        print("Libro:", self._libro.get_titulo())
        print("Fecha de prestamo:", self._fecha_prestamo)
        print("Fecha limite:", self._fecha_limite)
        print("Estado: Activo" if self._activo else "Estado: Finalizado")
        print("=" * 30)

    def extender_plazo(self, dias_extra: int) -> bool:
        """Suma días a la fecha límite. Devuelve False si no se puede extender."""
        if not self._activo:
            print("No se puede extender, el prestamo ya finalizo.")
            return False
        if dias_extra <= 0:
            print("Los dias extra deben ser mayor a 0.")
            return False
        if self._extensiones >= self._max_extensiones:
            print("Ya no puedes extender mas este prestamo.")
            return False

        self._fecha_limite = self._fecha_limite + timedelta(days=dias_extra)
        self._extensiones += 1
        print("Plazo extendido. Nueva fecha limite:", self._fecha_limite)
        return True

    def finalizar_prestamo(self) -> float:
        """
        Cierra el préstamo, devuelve el libro y calcula la multa por retraso.
        Devuelve el monto de la multa (0 si no hubo retraso).
        """
        if not self._activo:
            print("Este prestamo ya estaba finalizado.")
            return 0

        self._fecha_devolucion = date.today()
        self._activo = False

        dias_retraso = (self._fecha_devolucion - self._fecha_limite).days
        if dias_retraso < 0:
            dias_retraso = 0

        self._libro.devolver_libro()

        multa = 0
        if dias_retraso > 0:
            multa = self._usuario.calcular_multa(dias_retraso)
            print("Devolucion con", dias_retraso, "dia(s) de retraso.")
            print("Multa a pagar:", multa)
        else:
            print("Libro devuelto a tiempo, sin multa.")
        return multa


# =====================================================================
#  CLASE HIJA (HERENCIA): PRESTAMO ESTUDIANTE
# =====================================================================
class PrestamoEstudiante(Prestamo):
    """Préstamo para estudiantes: 14 días de plazo, 3 extensiones y multa a la mitad."""

    def __init__(self, id_prestamo, usuario, libro, carrera):
        super().__init__(id_prestamo, usuario, libro, dias_plazo=14)
        self._carrera = carrera
        self._max_extensiones = 3

    def generar_ticket(self):
        super().generar_ticket()
        print("Tipo: Prestamo de estudiante")
        print("Carrera:", self._carrera)

    def finalizar_prestamo(self) -> float:
        multa = super().finalizar_prestamo()
        if multa > 0:
            multa = multa / 2
            print("Descuento de estudiante aplicado. Multa final:", multa)
        return multa


# =====================================================================
#  CLASE BIBLIOTECA: GUARDA LOS DATOS Y MUESTRA EL MENÚ
# =====================================================================
class Biblioteca:
    """Guarda libros, usuarios y préstamos, y ofrece el menú de consola."""

    def __init__(self):
        self._libros = {}      # código -> Libro
        self._usuarios = {}    # id -> Usuario
        self._prestamos = []   # lista de Prestamo
        self._contador_prestamos = 0

    # ------------------------ Utilidades de entrada ------------------
    @staticmethod
    def _leer_entero(mensaje: str) -> int:
        """Pide un entero hasta que el usuario escriba uno válido."""
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("  Ingresa un número entero válido.")

    def _elegir_usuario(self):
        id_usuario = input("ID del usuario: ").strip()
        usuario = self._usuarios.get(id_usuario)
        if usuario is None:
            print("  No existe un usuario con ese ID.")
        return usuario

    def _elegir_libro(self):
        codigo = input("Código del libro: ").strip()
        libro = self._libros.get(codigo)
        if libro is None:
            print("  No existe un libro con ese código.")
        return libro

    def _elegir_prestamo(self, solo_activos: bool = False):
        """Muestra los préstamos (o solo los activos) y devuelve el elegido o None."""
        lista = [p for p in self._prestamos if p.is_activo() or not solo_activos]
        if not lista:
            print("  No hay préstamos para mostrar.")
            return None
        for i, p in enumerate(lista, 1):
            print(f"  {i}. [{p.get_id()}] {p.get_libro().get_titulo()} -> {p.get_usuario().get_nombre()}")
        n = self._leer_entero("Número de préstamo: ")
        if not 1 <= n <= len(lista):
            print("  Opción fuera de rango.")
            return None
        return lista[n - 1]

    # ------------------------ Opciones del menú ----------------------
    def registrar_libro(self):
        try:
            libro = Libro(input("Título: "), input("Autor: "), input("Código: ").strip())
        except ValueError as e:
            print(f"  Error: {e}")
            return
        if libro.get_codigo() in self._libros:
            print("  Ya existe un libro con ese código.")
            return
        self._libros[libro.get_codigo()] = libro
        print("  Libro registrado.")

    def registrar_usuario(self):
        nombre = input("Nombre: ").strip()
        id_usuario = input("ID: ").strip()
        if not nombre or not id_usuario:
            print("  Nombre e ID no pueden estar vacíos.")
        elif id_usuario in self._usuarios:
            print("  Ya existe un usuario con ese ID.")
        else:
            self._usuarios[id_usuario] = Usuario(nombre, id_usuario)
            print("  Usuario registrado.")

    def listar_libros(self):
        if not self._libros:
            print("  No hay libros registrados.")
        for libro in self._libros.values():
            print(" ", libro)

    def listar_usuarios(self):
        if not self._usuarios:
            print("  No hay usuarios registrados.")
        for usuario in self._usuarios.values():
            print(" ", usuario)

    def verificar_disponibilidad(self):
        libro = self._elegir_libro()
        if libro:
            estado = "disponible" if libro.verificar_disponibilidad() else "prestado"
            print(f"  '{libro.get_titulo()}' está {estado}.")

    def prestar(self):
        usuario = self._elegir_usuario()
        if usuario is None:
            return
        if not usuario.is_membresia_activa():
            print("  La membresía está inactiva. Renuévala primero.")
            return
        libro = self._elegir_libro()
        if libro is None or not libro.prestar_libro():
            return

        self._contador_prestamos += 1
        id_prestamo = f"P{self._contador_prestamos:03d}"
        if input("¿Es estudiante? (s/n): ").strip().lower() == "s":
            carrera = input("Carrera: ").strip()
            prestamo = PrestamoEstudiante(id_prestamo, usuario, libro, carrera)
        else:
            prestamo = Prestamo(id_prestamo, usuario, libro)

        usuario.registrar_prestamos(prestamo)
        self._prestamos.append(prestamo)
        prestamo.generar_ticket()

    def devolver(self):
        prestamo = self._elegir_prestamo(solo_activos=True)
        if prestamo is not None:
            prestamo.finalizar_prestamo()

    def extender(self):
        prestamo = self._elegir_prestamo(solo_activos=True)
        if prestamo is not None:
            prestamo.extender_plazo(self._leer_entero("Días extra: "))

    def ver_ticket(self):
        prestamo = self._elegir_prestamo()
        if prestamo is not None:
            prestamo.generar_ticket()

    def historial_usuario(self):
        usuario = self._elegir_usuario()
        if usuario:
            usuario.mostrar_historial()

    def renovar_membresia(self):
        usuario = self._elegir_usuario()
        if usuario:
            usuario.renovar_membresia()

    def calcular_multa(self):
        usuario = self._elegir_usuario()
        if usuario:
            dias = self._leer_entero("Días de retraso: ")
            print(f"  Multa: S/ {usuario.calcular_multa(dias):.2f}")

    # ------------------------ Bucle principal ------------------------
    def ejecutar(self):
        opciones = {
            "1": ("Registrar libro", self.registrar_libro),
            "2": ("Registrar usuario", self.registrar_usuario),
            "3": ("Listar libros", self.listar_libros),
            "4": ("Listar usuarios", self.listar_usuarios),
            "5": ("Verificar disponibilidad de un libro", self.verificar_disponibilidad),
            "6": ("Prestar libro", self.prestar),
            "7": ("Devolver libro (finalizar préstamo)", self.devolver),
            "8": ("Extender plazo de un préstamo", self.extender),
            "9": ("Ver ticket de un préstamo", self.ver_ticket),
            "10": ("Historial de un usuario", self.historial_usuario),
            "11": ("Calcular multa", self.calcular_multa),
            "12": ("Renovar membresía", self.renovar_membresia),
            "0": ("Salir", None),
        }
        while True:
            print("\n===== BIBLIOTECA =====")
            for clave, (texto, _) in opciones.items():
                print(f" {clave:>2}. {texto}")
            eleccion = input("Elige una opción: ").strip()
            if eleccion == "0":
                print("¡Hasta luego!")
                break
            if eleccion in opciones:
                opciones[eleccion][1]()
            else:
                print("  Opción no válida.")


if __name__ == "__main__":
    Biblioteca().ejecutar()
