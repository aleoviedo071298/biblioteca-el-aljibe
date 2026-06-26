# Biblioteca Popular "El Aljibe" — Sistema de Gestion

Sistema de gestion integral para la Biblioteca Popular "El Aljibe", desarrollado como **Trabajo Final Integrador** de la asignatura **Programacion 1** de la **Tecnicatura Universitaria en Desarrollo Web** (UNER - Facultad de Ciencias de la Administracion, 1er cuatrimestre 2026).

## Sobre la asignatura

**Programacion 1** es la materia introductoria de programacion de la carrera. Cubre los fundamentos del desarrollo de software en Python: variables, estructuras de control, funciones, estructuras de datos (listas, diccionarios, tuplas), manejo de archivos JSON y modularizacion del codigo.

El trabajo final integrador busca que el alumno:
- Ponga en practica todos los conocimientos adquiridos durante el cursado.
- Tenga una experiencia cercana a desarrollar un programa real con requerimientos establecidos por un usuario.
- Tome decisiones de diseno de un programa.

## Contexto del proyecto

La Biblioteca Popular "El Aljibe" es una biblioteca comunitaria fundada en 1962 en un pueblo de Entre Rios, a 40 km de Concordia. Con 3.200 libros y 480 socios activos, necesitaba reemplazar su sistema manual de cuadernos por una aplicacion digital que corriera localmente en la computadora de la biblioteca.

El sistema fue desarrollado a partir de un **documento de requerimientos** redactado por la presidenta de la comision de la biblioteca, simulando un escenario real de desarrollo con un cliente.

## Funcionalidades

El sistema gestiona cinco modulos principales a traves de una interfaz de consola con menus interactivos:

### 1. Catalogo de libros
- Alta, listado (con filtros por estado), busqueda (por titulo, autor o numero de inventario), cambio de estado y baja de libros.
- Estados: disponible, prestado, en reparacion, dado de baja.

### 2. Socios
- Registro, listado, busqueda (por carnet, DNI o nombre), actualizacion de datos y baja.
- Categorias: general, jubilado, estudiante, infantil.
- Deteccion de socios inactivos (sin actividad en mas de 2 anios).
- Al consultar un socio se muestra su historial de prestamos.

### 3. Prestamos
- Registro de prestamos con cambio automatico del estado del libro a "prestado".
- Visualizacion de prestamos activos e historial.
- Busqueda por numero de inventario del libro o DNI del socio.
- Registro de devolucion con cambio automatico del estado del libro a "disponible".
- Al devolver, el sistema notifica si el libro tiene reservas pendientes.

### 4. Reservas
- Registro de reservas para libros que no estan disponibles.
- Listado de reservas activas, busqueda por libro o socio.
- Marcado de reserva como cumplida (genera automaticamente un nuevo prestamo).
- Cancelacion de reservas.

### 5. Donaciones
- Registro, listado, busqueda (por donante o fecha) y actualizacion de estado de procesamiento.
- Estados: recibida, catalogada, integrada.

## Aspectos tecnicos

| Aspecto | Detalle |
|---|---|
| **Lenguaje** | Python 3 |
| **Persistencia** | Archivos JSON (catalogo, socios, prestamos, reservas, donaciones) |
| **Interfaz** | Consola (CLI) con menus interactivos |
| **Dependencias externas** | Ninguna (solo libreria estandar: `json`, `datetime`, `os`) |

### Estructura del proyecto

```
biblioteca-el-aljibe/
├── biblioteca.py        # Codigo fuente principal
├── catalogo.json        # Datos del catalogo de libros
├── socios.json          # Datos de socios registrados
├── prestamos.json       # Datos de prestamos
├── reservas.json        # Datos de reservas
├── donaciones.json      # Datos de donaciones
└── README.md
```

### Decisiones de diseno

- **Funciones utilitarias reutilizables**: `buscar_por_id()`, `buscar_por_texto()`, `siguiente_id()`, `confirmar()`, `pedir_entero()`, `pedir_email()` evitan duplicacion de logica.
- **Validacion de entrada**: los campos numericos solo aceptan digitos, los emails requieren `@`, y las acciones destructivas piden confirmacion.
- **IDs autoincrementales**: cada entidad genera su proximo ID a partir del maximo existente.
- **Integridad referencial automatica**: registrar un prestamo cambia el libro a "prestado"; devolver lo cambia a "disponible"; cumplir una reserva genera un prestamo automatico.
- **Persistencia al salir**: los datos se guardan en archivos JSON al cerrar el sistema.

## Como ejecutar

```bash
python biblioteca.py
```

Requiere **Python 3.10+** (usa `match/case`).

## Pautas de evaluacion

Segun las condiciones del trabajo integrador, se valoran:
- **Exactitud**: que el programa cumpla con los requerimientos del documento.
- **Eficiencia**: que las soluciones sean optimas y no redundantes.
- **Prolijidad**: indentacion consistente y buenas practicas de codigo.
- **Calidad de exposicion**: defensa oral del trabajo en coloquio.

---

*Trabajo realizado para la Tecnicatura Universitaria en Desarrollo Web — UNER, Facultad de Ciencias de la Administracion (2026).*
