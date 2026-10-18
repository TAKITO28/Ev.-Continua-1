from datetime import date, timedelta

#Creando la clase
class Prestamo:
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
#Creando los métodos
    def generar_ticket(self):
        print("=" * 30)
        print("      TICKET DE PRESTAMO")
        print("=" * 30)
        print("N° de prestamo:", self.id_prestamo)
        print("Usuario:", self.usuario.nombre)
        print("Libro:", self.libro.titulo)
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

#Añadiendo una clase hija, haciendo uso de la herencia
class PrestamoEstudiante(Prestamo):
    # Prestamo para estudiantes: mas dias de plazo y mas extensiones
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