# Sistema de Gestión de Biblioteca

Evaluación Grupal 1 – Lenguaje de Programación II (2026-2) – UNALM  
**Grupo 2**

## Integrantes

| Usuario de GitHub | Nombres y apellidos |
|---|---|
| TAKITO28 | Cielo Stephany Azaldi Pinchi |
| Carlosacee | Carlos Alejandro Carpio Espichan |
| gatoUNALM | Eduardo Daniel Suero Peqqueña |
| fabri1803 | Fabrizzio Andree Torres Montesinos |

## Descripción

Simulación de una biblioteca con las clases `Libro`, `Usuario`, `Prestamo`,
`PrestamoEstudiante` (herencia) y `Biblioteca` (menú interactivo en consola).

## Cómo ejecutar

Requiere Python 3 (no usa librerías externas).

    python menu1.py            # sistema completo con menú interactivo
    python prueba_multas.py    # prueba automática del cálculo de multas

## Contenido del repositorio

- `menu1.py`: código fuente del sistema (todas las clases y el menú interactivo), documentado.
- `informe.md`: informe con el escenario, el diagrama de clases, los atributos y métodos de cada clase y la ejecución de prueba.
- `prueba_multas.py`: script que comprueba las multas de un préstamo normal y de uno de estudiante.
- `ejecucion_prueba.txt`: registro real de una sesión del menú (préstamos, extensiones, ticket, multa, historial y devoluciones).

> Las versiones anteriores de las clases en archivos separados (`libro.py`, `usuario.py`, `prestamo.py` y `main.py`) se conservan en el historial del repositorio, en el commit `33385e0`.