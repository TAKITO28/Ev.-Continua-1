"""
Prueba automática del cálculo de multas (préstamo normal y de estudiante).

El menú no permite esperar días reales, así que aquí se simula el paso del
tiempo moviendo la fecha límite 6 días hacia atrás y luego se devuelve el libro.

Ejecutar con:  python prueba_multas.py
"""
from datetime import date, timedelta

from menu1 import Libro, Usuario, Prestamo, PrestamoEstudiante

DIAS_RETRASO = 6
TARIFA = 2.5


def simular_retraso(prestamo, dias):
    """Mueve la fecha límite al pasado para simular una devolución tardía."""
    prestamo._fecha_limite = date.today() - timedelta(days=dias)


def main():
    usuario = Usuario("Ana", "U1", tarifa_multa_dia=TARIFA)

    print("--- Préstamo normal ---")
    libro1 = Libro("Don Quijote", "Cervantes", "L1")
    libro1.prestar_libro()
    normal = Prestamo("P001", usuario, libro1)
    simular_retraso(normal, DIAS_RETRASO)
    multa_normal = normal.finalizar_prestamo()
    assert multa_normal == DIAS_RETRASO * TARIFA, "Multa normal incorrecta"

    print("\n--- Préstamo de estudiante ---")
    libro2 = Libro("Ilíada", "Homero", "L2")
    libro2.prestar_libro()
    estudiante = PrestamoEstudiante("P002", usuario, libro2, "Ingeniería")
    simular_retraso(estudiante, DIAS_RETRASO)
    multa_estudiante = estudiante.finalizar_prestamo()
    assert multa_estudiante == DIAS_RETRASO * TARIFA / 2, "Multa de estudiante incorrecta"

    print("\n--- Sin retraso ---")
    libro3 = Libro("Hamlet", "Shakespeare", "L3")
    libro3.prestar_libro()
    a_tiempo = Prestamo("P003", usuario, libro3)
    assert a_tiempo.finalizar_prestamo() == 0, "No debería haber multa"

    print("\nResultado: todas las pruebas de multas pasaron.")
    print(f"  Normal:     {DIAS_RETRASO} x S/ {TARIFA:.2f} = S/ {multa_normal:.2f}")
    print(f"  Estudiante: {multa_normal:.2f} / 2 = S/ {multa_estudiante:.2f}")


if __name__ == "__main__":
    main()
