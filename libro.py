class Libro:
    """
    Representa un libro de la biblioteca y controla su disponibilidad.

    Atributos (privados, se acceden con getters):
        _titulo (str): título del libro.
        _autor (str): autor del libro.
        _codigo (str): código único del libro (por ejemplo, ISBN).
        _disponible (bool): True si el libro está en la biblioteca.
        _veces_prestado (int): cuántas veces se ha prestado (valor añadido).
    """

    def __init__(self, titulo: str, autor: str, codigo: str):
        if not titulo.strip() or not autor.strip() or not codigo.strip():
            raise ValueError("Título, autor y código no pueden estar vacíos.")
        self._titulo = titulo
        self._autor = autor
        self._codigo = codigo
        self._disponible = True
        self._veces_prestado = 0

    # ------------------------------------------------------------------
    # Getters (encapsulamiento)
    # ------------------------------------------------------------------
    def get_titulo(self) -> str:
        return self._titulo

    def get_autor(self) -> str:
        return self._autor

    def get_codigo(self) -> str:
        return self._codigo

    def get_veces_prestado(self) -> int:
        return self._veces_prestado

    # ------------------------------------------------------------------
    # Métodos principales
    # ------------------------------------------------------------------
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


# Prueba rápida: solo se ejecuta si corres este archivo directamente
if __name__ == "__main__":
    libro = Libro("Cien años de soledad", "Gabriel García Márquez", "LIB-001")
    print(libro)
    print("¿Disponible?", libro.verificar_disponibilidad())
    libro.prestar_libro()
    libro.prestar_libro()      # intento repetido: debe fallar
    print(libro)
    libro.devolver_libro()
    libro.devolver_libro()     # intento repetido: debe avisar
    print(libro)
    print("Veces prestado:", libro.get_veces_prestado())
