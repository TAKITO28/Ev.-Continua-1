class Usuario:
  def __init__(self, nombre: str, id_usuario: str, tarifa_multa_dia: float = 2.5):
    self._nombre = nombre
    self._id_usuario = id_usuario
    self._membresia_activa = True
    self._tarifa_multa = tarifa_multa_dia
    self._hisstorial_prestamos = []

  def get_nombre(self) -> str:
    return self._nombre

  def get_id(self) -> str:
    return self._id_usuario

  def is_membresia_activa(self) -> bool:
    return self._membresia_activa

#-------------------------------------------------------
# MÉTODOS PROPUESTOS
#-------------------------------------------------------

  def registrar_prestamos(self, prestamo):
    """
    Guarda un objeto de tipo Prestamo en la lista de historial del usuario.
    """
    self._historial_prestamos.append(prestamo)
    print(f"Préstamo registrado exitosamente en el historial de {self._nombre}.")

  def calcular_multa(self, dias_retraso: int) -> float:
    """
    Calcula el monto de la mullta bas{andose en los d{ias de retraso
    """
    if dias_retraso > 0:
      total_multa = dias_retraso*self._tarifa_multa
      return total_multa
    return 0.0

  def renovar_membresia(self):
    """
    Activa de nuevo la membresía del usuario.
    """
    self._membresia_activa = True
    print(f"La membresía del usuario {self._nombre} ha sido renovada con éxito.")

#----------------------------------------------
# MÉTODOS ADICIONALES (muestra de información)
#----------------------------------------------

  def mostrar_historial(self):
    """
    Muestra la cantidad de préstamos realizados por el usuario.
    """
    print(f"\nHistorial de préstamos realizados de {self._nombre}:")
    if not self._historial_prestamos:
      print(" Sin préstamos registraods.")
    else:
      print(f" Total de préstamos realizados: {len(self._historial_prestamos)}")

  def __str__(self):
    estado = "Activa" if self._membresia_activa else "Inactiva"
    return f"Usuario: {self._nombre} | ID: {self._id_usuario} | Membresía: {estado}"

