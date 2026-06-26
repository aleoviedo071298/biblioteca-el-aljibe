import json
import datetime
import os

fecha_de_hoy = datetime.date.today()
separador = "=============================="

#Funciones utiles.
#Limpiar pantalla
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Cargar datos y guardar datos
CARPETA_SCRIPT = os.path.dirname(os.path.abspath(__file__))
ARCHIVOS = {
    "catalogo":   os.path.join(CARPETA_SCRIPT, "catalogo.json"),
    "donaciones": os.path.join(CARPETA_SCRIPT, "donaciones.json"),
    "prestamos":  os.path.join(CARPETA_SCRIPT, "prestamos.json"),
    "reservas":   os.path.join(CARPETA_SCRIPT, "reservas.json"),
    "socios":     os.path.join(CARPETA_SCRIPT, "socios.json"),
}

def cargar_datos():
    datos = {}
    for clave, archivo in ARCHIVOS.items():
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos[clave] = json.load(f)
        except FileNotFoundError:
            print(f"'{archivo}' no encontrado. Inicializando vacío.")
            datos[clave] = []
    return datos

def guardar_datos(datos):
    for clave, archivo in ARCHIVOS.items():
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos[clave], f, indent=4)

#Generar el próximo ID
def siguiente_id(lista):
    if not lista:
        return 1
    return max(item["id"] for item in lista) + 1

#Buscar por ID
def buscar_por_id(lista, id_buscado):
    for item in lista:
        if item["id"] == id_buscado:
            return item
    return None

#Buscar por texto en cualquier lista.
def buscar_por_texto(lista, campo, texto):
    resultados = []
    for item in lista:
        if texto.lower() in item[campo].lower():
            resultados.append(item)
    return resultados

#Confirmar acción (s/n)
def confirmar(mensaje="¿Estás seguro? (s/n): "):
    return input(mensaje).lower() == "s"

#Mostrar menú y pedir opción
def mostrar_menu(titulo, opciones):
    print(f" {titulo} ")
    print(separador)
    for clave, texto in opciones.items():
        print(f"{clave}. {texto}")
    return input("Ingrese una opción: ").lower()

# Pide un número entero y repite hasta que el usuario ingrese solo dígitos.
def pedir_entero(mensaje):
  while True:
    valor = input(mensaje)
    if valor.isdigit():
      return int(valor)
    print("Tenes que ingresar un numero.")

# Pide una entrada de números y la devuelve como texto.
def pedir_digitos(mensaje):
  while True:
    valor = input(mensaje)
    if valor.isdigit():
      return valor
    print("Solo se aceptan numeros.")

# Pide un email y valida que tenga "@" o que este vacio.
def pedir_email(mensaje):
  while True:
    valor = input(mensaje)
    if "@" in valor or valor == "":
      return valor
    print("El email tiene que tener @.")

# Pausa hasta que se presione Enter.
def pausar(mensaje="Presione Enter para continuar..."):
    input(mensaje)

# Muestra en pantalla todos los datos de un préstamo.
def listar_prestamos(prestamo):
  print("ID del prestamo", prestamo["id"])
  print("ID del libro", prestamo["id_libro"])
  print("ID del socio", prestamo["id_socio"])
  print("Fecha de prestamo", prestamo["fecha_prestamo"])
  print("Fecha de devolucion pactada", prestamo["fecha_devolucion_pactada"])
  print("Fecha de devolucion real", prestamo["fecha_devolucion_real"])
  print("Estado", prestamo["estado"])

# Muestra en pantalla toda la información de un libro.
def listar_catalogo(libro):
  print("Numero de inventario: ", libro["id"])
  print("Titulo: ", libro["titulo"])
  print("Autor: ", libro["autor"])
  print("Genero: ", libro["genero"])
  print("Año de publicacion: ", libro["anio_publicacion"])
  print("Estado: ", libro["estado"])
  print("Como llego: ", libro["procedencia"])

# Muestra los datos de un socio y sus prestamos.
def listar_socio(socio):
  print("Numero de carnet:", socio["id"])
  print("DNI:", socio["dni"])
  print("Nombre completo:", socio["nombre_completo"])
  print("Telefono:", socio["telefono"])
  print("Email:", socio["email"])
  print("Fecha de alta:", socio["fecha_alta"])
  print("Categoria:", socio["categoria"])
  prestamos_socio = False
  for prestamo in prestamos:
    if prestamo["id_socio"] == socio["id"]:
      prestamos_socio = True
      print("Historial de prestamos:")
      print("ID del libro:", prestamo["id_libro"])
      libro = buscar_por_id(catalogo, prestamo["id_libro"])
      if libro:
        print("Nombre del libro:", libro["titulo"])
      print("Fecha de prestamo:", prestamo["fecha_prestamo"])
      print("Fecha de devolucion pactada:", prestamo["fecha_devolucion_pactada"])
      print("Fecha de devolucion real:", prestamo["fecha_devolucion_real"])
      print("Estado:", prestamo["estado"])
      print(separador)
  if not prestamos_socio:
    print("No tiene prestamos.")
    print(separador)

# Muestra en pantalla todos los datos de una reserva.
def listar_reserva(reserva):
  print("ID reserva:", reserva["id"])
  print("Numero de inventario del Libro:", reserva["id_libro"])
  print("ID socio:", reserva["id_socio"])
  socio = buscar_por_id(socios, reserva["id_socio"])
  if socio:
    print(socio["nombre_completo"])
  print("Fecha de reserva:", reserva["fecha_reserva"])
  print("Estado", reserva["estado"])
  print(separador)

# Muestra en pantalla todos los datos de una donacion.
def listar_donacion(donacion):
  print("ID Donación:", donacion["id"])
  print("Donante:", donacion["nombre_donante"])
  print("Contacto:", donacion["contacto"])
  print("Fecha de recepción:", donacion["fecha_recepcion"])
  print("Cantidad de libros:", donacion["cantidad_libros"])
  print("Estado de procesamiento:", donacion["estado"])
  print("Observaciones:", donacion["observaciones"])

# Funciones del módulo Catálogo
def cargar_libro():
  limpiar_pantalla()
  print("Carga de libros.")
  print(separador)
  id = siguiente_id(catalogo)
  titulo = input("Ingrese titulo del libro: ")
  autor = input("Ingrese autor del libro: ")
  genero = input("Ingrese genero del libro: ")
  anio_publicacion = pedir_entero("Ingrese año de publicacion del libro: ")
  procedencia_check = False
  while not procedencia_check:
    procedencia = pedir_entero("Ingrese como llego el libro: (1.Compra 2.Donacion): ")
    if procedencia == 1:
      procedencia = "compra"
      procedencia_check = True
    elif procedencia == 2:
      procedencia = "donacion"
      procedencia_check = True
    else:
      print("Inserte una opcion valida")
  libro = {
      "id": id,
      "titulo": titulo,
      "autor": autor,
      "genero": genero,
      "anio_publicacion": anio_publicacion,
      "estado": "disponible",
      "procedencia": procedencia
  }
  catalogo.append(libro)
  print("Libro cargado correctamente.")
  print(separador)
  pausar()

def listar_libros():
  limpiar_pantalla()
  if len(catalogo) == 0:
    print("No hay libros cargados.")
    print(separador)
  else:
    print("Listado de libros.")
    print("1. Todos")
    print("2. Disponible")
    print("3. Prestado")
    print("4. En reparacion")
    print("5. Dado de baja")
    opcion_filtro = input("Elija filtro a aplicar: ")
    print(separador)
    if opcion_filtro == "2":
      estado_filtro = "disponible"
    elif opcion_filtro == "3":
      estado_filtro = "prestado"
    elif opcion_filtro == "4":
      estado_filtro = "en reparacion"
    elif opcion_filtro == "5":
      estado_filtro = "dado de baja"
    else:
      estado_filtro = None
    hay_libros = False
    for libro in catalogo:
      if estado_filtro is None or libro["estado"] == estado_filtro:
        listar_catalogo(libro)
        print(separador)
        hay_libros = True
    if not hay_libros:
      print("No hay libros con ese estado.")
      print(separador)
  pausar()

def buscar_libro():
  limpiar_pantalla()
  opcion_buscador = mostrar_menu("Buscador de libros", {
      "a": "Busqueda por titulo",
      "b": "Busqueda por autor",
      "c": "Busqueda por numero de inventario",
      "d": "Salir"
  })
  match opcion_buscador:
    case "a":
      limpiar_pantalla()
      titulo_busqueda = input("Ingrese el titulo: ")
      resultados = buscar_por_texto(catalogo, "titulo", titulo_busqueda)
      if resultados:
        for libro in resultados:
          listar_catalogo(libro)
          print(separador)
      else:
        print("No se encontro el libro.")
        print(separador)
    case "b":
      limpiar_pantalla()
      autor_busqueda = input("Ingrese el autor: ")
      resultados = buscar_por_texto(catalogo, "autor", autor_busqueda)
      if resultados:
        for libro in resultados:
          listar_catalogo(libro)
          print(separador)
      else:
        print("No se encontro el libro.")
        print(separador)
    case "c":
      limpiar_pantalla()
      id_busqueda = pedir_entero("Ingrese numero de inventario: ")
      libro = buscar_por_id(catalogo, id_busqueda)
      if libro:
        listar_catalogo(libro)
        print(separador)
      else:
        print("No se encontro el libro.")
        print(separador)
    case "d":
      print("Volviendo al menu...")
    case _:
      print("Opcion invalida.")
  pausar()

def cambiar_estado_libro():
  limpiar_pantalla()
  print("Cambio de estado de libro.")
  id_cambio = pedir_entero("Ingrese numero de inventario: ")
  libro = buscar_por_id(catalogo, id_cambio)
  if not libro:
    print("No se encontro el libro.")
    print(separador)
  else:
    print(f"Estado actual: {libro['estado']}")
    print("Seleccione el nuevo estado:")
    print("1. disponible")
    print("2. prestado")
    print("3. en reparación")
    print("4. dado de baja")
    nueva_opcion_estado = input("Opción: ")
    if nueva_opcion_estado == "1":
      libro["estado"] = "disponible"
      print("Estado cambiado correctamente.")
      print(separador)
    elif nueva_opcion_estado == "2":
      libro["estado"] = "prestado"
      print("Estado cambiado correctamente.")
      print(separador)
    elif nueva_opcion_estado == "3":
      libro["estado"] = "en reparación"
      print("Estado cambiado correctamente.")
      print(separador)
    elif nueva_opcion_estado == "4":
      libro["estado"] = "dado de baja"
      print("Estado cambiado correctamente.")
      print(separador)
    else:
      print("Opción inválida. El estado no fue modificado.")
      print(separador)
  pausar()

def baja_libro():
  limpiar_pantalla()
  print("Baja de libro.")
  id_baja = pedir_entero("Ingrese numero de inventario: ")
  libro = buscar_por_id(catalogo, id_baja)
  if not libro:
    print("No se encontro el libro.")
    print(separador)
  else:
    if confirmar("Estas seguro?(s/n)"):
      libro["estado"] = "dado de baja"
      print("Libro dado de baja correctamente.")
      print(separador)
    else:
      print("No se dio de baja el libro")
  pausar()


# Funciones del módulo Socios
def registrar_socio():
  limpiar_pantalla()
  id = siguiente_id(socios)
  dni = pedir_digitos("Ingrese DNI: ")
  nombre_completo = input("Ingrese nombre completo: ")
  telefono = pedir_digitos("Ingrese telefono: ")
  email = pedir_email("Ingrese email: ").lower()
  fecha_alta = fecha_de_hoy
  categoria_check = False
  while not categoria_check:
      categoria = pedir_entero("Ingrese categoría del socio: 1.General 2.Jubilado 3.Estudiante 4.Infantil: ")
      if categoria == 1:
          categoria = "general"
          categoria_check = True
      elif categoria == 2:
          categoria = "jubilado"
          categoria_check = True
      elif categoria == 3:
          categoria = "estudiante"
          categoria_check = True
      elif categoria == 4:
          categoria = "infantil"
          categoria_check = True
      else:
          print("Inserte una opción válida")
  nuevo_socio = {
      "id" : id,
      "dni" : dni,
      "nombre_completo" : nombre_completo,
      "telefono" : telefono,
      "email" : email,
      "fecha_alta" : str(fecha_alta),
      "categoria" : categoria
  }
  socios.append(nuevo_socio)
  print("Socio registrado en la base de datos")
  print(separador)
  pausar()

def listar_socios():
  limpiar_pantalla()
  print("Listado de socios.")
  print(separador)
  if len(socios) <= 0:
    print("No hay socios registrados.")
  else:
    for socio in socios:
      listar_socio(socio)
  pausar()

def buscar_socio():
  limpiar_pantalla()
  opcion_buscador = mostrar_menu("Busqueda de socios", {
      "a": "Por numero de carnet",
      "b": "Por DNI",
      "c": "Por nombre completo"
  })
  print(separador)
  if opcion_buscador == "a":
    limpiar_pantalla()
    numero_carnet = pedir_entero("Ingrese numero de carnet: ")
    socio = buscar_por_id(socios, numero_carnet)
    if socio:
      listar_socio(socio)
    else:
      print("No se encontro el socio.")
  elif opcion_buscador == "b":
    limpiar_pantalla()
    dni = pedir_digitos("Ingrese DNI: ")
    encontrado = False
    for socio in socios:
      if socio["dni"] == dni:
        encontrado = True
        listar_socio(socio)
        break
    if not encontrado:
      print("No se encontro el socio.")
  elif opcion_buscador == "c":
    limpiar_pantalla()
    nombre_completo = input("Ingrese nombre completo: ")
    resultados = buscar_por_texto(socios, "nombre_completo", nombre_completo)
    if resultados:
      for socio in resultados:
        listar_socio(socio)
    else:
      print("No se encontro el socio.")
  pausar()

def actualizar_socio():
  limpiar_pantalla()
  print("Actualizar datos.")
  print(separador)
  numero_carnet = pedir_entero("Ingrese numero de carnet:")
  socio = buscar_por_id(socios, numero_carnet)
  if not socio:
    print("No se encontro el socio.")
  else:
    socio["telefono"] = pedir_digitos("Ingrese telefono: ")
    socio["email"] = pedir_email("Ingrese email: ")
    categoria_check = False
    while not categoria_check:
        categoria = pedir_entero("Ingrese categoría del socio: 1.General 2.Jubilado 3.Estudiante 4.Infantil: ")
        if categoria == 1:
            categoria = "general"
            categoria_check = True
        elif categoria == 2:
            categoria = "jubilado"
            categoria_check = True
        elif categoria == 3:
            categoria = "estudiante"
            categoria_check = True
        elif categoria == 4:
            categoria = "infantil"
            categoria_check = True
        else:
            print("Inserte una opción válida")
    socio["categoria"] = categoria
    print("Datos actualizados.")
    print(separador)
  pausar()

def baja_socio():
  limpiar_pantalla()
  print("Dar de baja a socios.")
  print(separador)
  numero_carnet = pedir_entero("Ingrese numero de carnet: ")
  socio = buscar_por_id(socios, numero_carnet)
  if not socio:
    print("No se encontro el socio.")
  else:
    if confirmar("Estas seguro?(s/n)"):
      socios.remove(socio)
      print("Socio dado de baja.")
      print(separador)
    else:
      print("No se dio de baja el socio.")
  pausar()

def socios_inactivos():
  limpiar_pantalla()
  print("Socios inactivos (mas de 2 años.)")
  print(separador)
  limite = fecha_de_hoy - datetime.timedelta(days=365*2)
  hay_inactivos = False
  for socio in socios:
    ultima_fecha_convertida = datetime.datetime.strptime(socio["fecha_alta"], "%Y-%m-%d").date()
    for prestamo in prestamos:
      if prestamo["id_socio"] == socio["id"]:
        prestamo_fecha_convertida = datetime.datetime.strptime(prestamo["fecha_prestamo"], "%Y-%m-%d").date()
        if prestamo_fecha_convertida > ultima_fecha_convertida:
          ultima_fecha_convertida = prestamo_fecha_convertida
    if ultima_fecha_convertida < limite:
      hay_inactivos = True
      print("Carnet", socio["id"], "//", socio["nombre_completo"], "// ultima actividad:", ultima_fecha_convertida)
  if not hay_inactivos:
    print("No hay socios inactivos.")
  print(separador)
  pausar()

#Funciones del módulo Préstamos
def registrar_prestamo():
  limpiar_pantalla()
  print("Registrar un prestamo nuevo.")
  print(separador)
  id = siguiente_id(prestamos)
  id_libro = pedir_entero("Ingrese ID del libro: ")
  libro_a_prestar = buscar_por_id(catalogo, id_libro)
  if not libro_a_prestar:
    print("No existe un libro con el ID ingresado. Por favor, intente de nuevo.")
    print(separador)
    pausar()
    return
  if libro_a_prestar["estado"] != "disponible":
    print(f" El libro con ID {id_libro} no está disponible para préstamo. Estado actual: {libro_a_prestar['estado']}.")
    print(separador)
    pausar()
    return
  id_socio = pedir_entero("Ingrese ID del socio: ")
  if not buscar_por_id(socios, id_socio):
    print("No existe un socio con el ID ingresado. Por favor, intente de nuevo.")
    print(separador)
    pausar()
    return
  fecha_prestamo = fecha_de_hoy
  fecha_devolucion_pactada = fecha_prestamo + datetime.timedelta(days=15)
  fecha_devolucion_real = None
  estado = "activo"
  nuevo_prestamo = {
      "id" : id,
      "id_libro" : id_libro,
      "id_socio" : id_socio,
      "fecha_prestamo" : str(fecha_prestamo),
      "fecha_devolucion_pactada" : str(fecha_devolucion_pactada),
      "fecha_devolucion_real" : fecha_devolucion_real,
      "estado" : estado
  }
  prestamos.append(nuevo_prestamo)
  libro_a_prestar["estado"] = "prestado"
  print("Prestamo registrado.")
  print(separador)
  pausar()

def ver_prestamos():
  limpiar_pantalla()
  print("Prestamos")
  print("1.Prestamos activos")
  print("2.Historial de prestamos")
  opcion_prestamos = pedir_entero("Ingrese una opcion: ")
  if opcion_prestamos == 1:
    print("Prestamos activos.")
    print(separador)
    hay_activos = False
    for prestamo in prestamos:
      if prestamo["estado"] == "activo":
        hay_activos = True
        print("ID del prestamo", prestamo["id"])
        print("ID del libro", prestamo["id_libro"])
        print("ID del socio", prestamo["id_socio"])
        print("Fecha de prestamo", prestamo["fecha_prestamo"])
        print("Fecha de devolucion pactada", prestamo["fecha_devolucion_pactada"])
        print(separador)
    if not hay_activos:
      print("No hay prestamos activos.")
      print(separador)
  elif opcion_prestamos == 2:
    print("Historial de prestamos.")
    print(separador)
    hay_historial = False
    for prestamo in prestamos:
      if prestamo["estado"] != "activo":
        hay_historial = True
        print("ID del prestamo", prestamo["id"])
        print("ID del libro", prestamo["id_libro"])
        print("ID del socio", prestamo["id_socio"])
        print("Fecha de prestamo", prestamo["fecha_prestamo"])
        print("Fecha de devolucion real", prestamo["fecha_devolucion_real"])
        print("Estado", prestamo["estado"])
        print(separador)
    if not hay_historial:
      print("Sin historial.")
      print(separador)
  else:
    print("Opcion invalida")
  pausar()

def buscar_prestamo():
  limpiar_pantalla()
  opcion_buscador = mostrar_menu("Buscar un prestamo", {
      "a": "Por numero de inventario del libro",
      "b": "Por DNI del socio"
  })
  print(separador)
  if opcion_buscador == "a":
    limpiar_pantalla()
    id_libro = pedir_entero("Ingrese numero de inventario del libro: ")
    encontrado = False
    for prestamo in prestamos:
      if prestamo["id_libro"] == id_libro:
        encontrado = True
        listar_prestamos(prestamo)
        print(separador)
    if not encontrado:
      print("No se encontro el prestamo.")
      print(separador)
  elif opcion_buscador == "b":
    limpiar_pantalla()
    dni_busqueda = input("Ingrese DNI del socio: ")
    id_socio = ""
    for socio in socios:
      if socio["dni"] == dni_busqueda:
        id_socio = socio["id"]
        break
    encontrado = False
    for prestamo in prestamos:
      if prestamo["id_socio"] == id_socio:
        encontrado = True
        listar_prestamos(prestamo)
        print(separador)
    if not encontrado:
      print("No se encontro el prestamo.")
      print(separador)
  pausar()

def registrar_devolucion():
  limpiar_pantalla()
  print("Registrar una devolucion.")
  print(separador)
  id_prestamo = pedir_entero("Ingrese ID del prestamo: ")
  prestamo = buscar_por_id(prestamos, id_prestamo)
  if not prestamo:
    print("No se encontro el prestamo.")
    print(separador)
  else:
    prestamo["estado"] = "devuelto"
    prestamo["fecha_devolucion_real"] = str(fecha_de_hoy)
    print("Devolucion registrada.")
    print(separador)
    libro = buscar_por_id(catalogo, prestamo["id_libro"])
    if libro:
      libro["estado"] = "disponible"
    for reserva in reservas:
      if reserva["id_libro"] == prestamo["id_libro"] and reserva["estado"] == "en espera":
        reserva["estado"] = "lista para retirar"
        print("Este libro tiene una reserva pendiente del socio con ID: ", reserva["id_socio"])
        print("La reserva", reserva["id"], "esta lista para ser retirada por el socio")
        print(separador)
        break
  pausar()

def eliminar_prestamo():
  limpiar_pantalla()
  print("Eliminar un prestamo mal cargado.")
  print(separador)
  id_prestamo = pedir_entero("Ingrese ID del prestamo: ")
  prestamo = buscar_por_id(prestamos, id_prestamo)
  if not prestamo:
    print("No se encontro el prestamo.")
    print(separador)
  else:
    if confirmar("Estas seguro?(s/n)"):
      prestamos.remove(prestamo)
      libro = buscar_por_id(catalogo, prestamo["id_libro"])
      if libro:
        libro["estado"] = "disponible"
      print("Prestamo eliminado.")
      print(separador)
    else:
      print("No se elimino el prestamo.")
  pausar()

# Funciones del módulo Reservas
def registrar_reserva():
  limpiar_pantalla()
  print("Registrar una reserva nueva.")
  print(separador)
  id = siguiente_id(reservas)
  id_libro = pedir_entero("Ingrese numero de inventario del libro: ")
  libro_a_reservar = buscar_por_id(catalogo, id_libro)
  if not libro_a_reservar:
    print("No existe un libro con el ID ingresado. Por favor, intente de nuevo.")
    print(separador)
    pausar()
    return
  if libro_a_reservar["estado"] == "disponible":
    print("El libro esta disponible. Puede retirarlo directamente sin reserva.")
    print(separador)
    pausar()
    return
  if libro_a_reservar["estado"] == "dado de baja":
    print("No se puede reservar un libro dado de baja.")
    print(separador)
    pausar()
    return
  id_socio = pedir_entero("Ingrese ID del socio: ")
  if not buscar_por_id(socios, id_socio):
    print("No existe un socio con el ID ingresado. Por favor, intente de nuevo.")
    print(separador)
    pausar()
    return
  fecha_reserva = fecha_de_hoy
  estado = "en espera"
  nueva_reserva = {
      "id" : id,
      "id_libro" : id_libro,
      "id_socio" : id_socio,
      "fecha_reserva" : str(fecha_reserva),
      "estado" : estado
  }
  reservas.append(nueva_reserva)
  print("Reserva registrada correctamente.")
  print(separador)
  pausar()

def listar_reservas():
  limpiar_pantalla()
  print("Listado de reservas activas.")
  print(separador)
  hay_reservas = False
  for reserva in reservas:
    if reserva["estado"] == "en espera" or reserva["estado"] == "lista para retirar":
      hay_reservas = True
      listar_reserva(reserva)
  if not hay_reservas:
    print("No hay reservas activas.")
    print(separador)
  pausar()

def buscar_reserva():
  limpiar_pantalla()
  buscador_reserva = mostrar_menu("Buscador de reservas", {
      "a": "Buscar por libro",
      "b": "Buscar por socio"
  })
  print(separador)
  if buscador_reserva == "a":
    limpiar_pantalla()
    id_libro_busqueda = pedir_entero("Ingrese numero de inventario de libro: ")
    encontrado = False
    for reserva in reservas:
      if reserva["id_libro"] == id_libro_busqueda:
        listar_reserva(reserva)
        encontrado = True
    if not encontrado:
      print("No se encontro ninguna reserva.")
      print(separador)
  elif buscador_reserva == "b":
    limpiar_pantalla()
    id_socio_busqueda = pedir_entero("Ingrese ID socio: ")
    print(separador)
    encontrado = False
    for reserva in reservas:
      if reserva["id_socio"] == id_socio_busqueda:
        listar_reserva(reserva)
        encontrado = True
    if not encontrado:
      print("No se encontro ninguna reserva.")
      print(separador)
  else:
    print("Opcion invalida.")
    print(separador)
  pausar()

def cumplir_reserva():
  limpiar_pantalla()
  print("Marcar reserva como cumplida.")
  print(separador)
  id_reserva = pedir_entero("Ingrese ID de la reserva: ")
  reserva = buscar_por_id(reservas, id_reserva)
  if not reserva:
    print("Reserva no encontrada")
    print(separador)
  else:
    reserva["estado"] = "cumplida"
    print("Reserva marcada como cumplida.")
    print(separador)
    libro = buscar_por_id(catalogo, reserva["id_libro"])
    if libro:
      libro["estado"] = "prestado"
    nuevo_prestamo = {
        "id" : siguiente_id(prestamos),
        "id_libro" : reserva["id_libro"],
        "id_socio" : reserva["id_socio"],
        "fecha_prestamo" : str(fecha_de_hoy),
        "fecha_devolucion_pactada" : str(fecha_de_hoy + datetime.timedelta(days=15)),
        "fecha_devolucion_real" : None,
        "estado" : "activo"
    }
    prestamos.append(nuevo_prestamo)
  pausar()

def cancelar_reserva():
  limpiar_pantalla()
  print("Cancelar reserva")
  print(separador)
  id_cancelar = pedir_entero("Ingrese ID de la reserva a cancelar: ")
  reserva = buscar_por_id(reservas, id_cancelar)
  if not reserva:
    print("Reserva no encontrada")
    print(separador)
  else:
    if confirmar("Estas seguro?(s/n)"):
      reserva["estado"] = "cancelada"
      print("Reserva cancelada correctamente.")
      print(separador)
    else:
      print("No se cancelo la reserva.")
      print(separador)
  pausar()

# Funciones del módulo Donaciones
def registrar_donacion():
  limpiar_pantalla()
  print("Registrar una donacion nueva.")
  print(separador)
  id = siguiente_id(donaciones)
  donante = input("Nombre del donante (o anonima): ")
  contacto = input("Ingrese telefono o email de contacto: ")
  fecha_recepcion = fecha_de_hoy
  estado = "recibida"
  cantidad_libros = pedir_entero("Ingrese cantidad de libros: ")
  observaciones = input("Ingrese alguna observacion: ")
  nuevo_donacion = {
      "id" : id,
      "nombre_donante" : donante,
      "contacto" : contacto,
      "fecha_recepcion" : str(fecha_recepcion),
      "cantidad_libros" : cantidad_libros,
      "estado" : estado,
      "observaciones" : observaciones
  }
  donaciones.append(nuevo_donacion)
  print("Donacion registrada con exito")
  print(separador)
  pausar()

def listar_donaciones():
  limpiar_pantalla()
  if len(donaciones) == 0:
    print("No hay donaciones registradas")
    print(separador)
  else:
    print("Lista de donaciones")
    print(separador)
    for i in donaciones:
      listar_donacion(i)
      print(separador)
  pausar()

def buscar_donacion():
  limpiar_pantalla()
  opcion_busqueda = mostrar_menu("Buscador de donaciones", {
      "a": "Buscar por nombre de donante",
      "b": "Buscar por fecha (AAAA-MM-DD)"
  })
  print(separador)
  if opcion_busqueda == "a":
    limpiar_pantalla()
    busqueda = input("Ingrese nombre del donante: ")
    resultados = buscar_por_texto(donaciones, "nombre_donante", busqueda)
    if resultados:
      for donacion in resultados:
        listar_donacion(donacion)
        print(separador)
    else:
      print("No se encontro el nombre del donante")
      print(separador)
  elif opcion_busqueda == "b":
    limpiar_pantalla()
    busqueda = input("Ingrese la fecha (AAAA-MM-DD): ")
    encontrado = False
    for i in donaciones:
      if str(i["fecha_recepcion"]) == busqueda:
        listar_donacion(i)
        print(separador)
        encontrado = True
    if not encontrado:
      print("No se encontro la donacion con esa fecha")
      print(separador)
  else:
    print("Opcion invalida.")
    print(separador)
  pausar()

def actualizar_estado_donacion():
  limpiar_pantalla()
  print("Actualizar estado")
  print(separador)
  id_buscar = pedir_entero("Ingrese el id de la donacion: ")
  donacion = buscar_por_id(donaciones, id_buscar)
  if not donacion:
    print("No se encontro id de donacion")
    print(separador)
  else:
    print("estado actual:", donacion["estado"])
    print("Seleccione un nuevo estado")
    print("1.Recibida")
    print("2.Catalogada")
    print("3.Integrada")
    estado_opcion = input("opcion: ")
    if estado_opcion == "1":
      donacion["estado"] = "recibida"
      print("Estado actualizado")
    elif estado_opcion == "2":
      donacion["estado"] = "catalogada"
      print("Estado actualizado")
    elif estado_opcion == "3":
      donacion["estado"] = "integrada"
      print("Estado actualizado")
    else:
      print("Opcion invalida")
    print(separador)
  pausar()

def eliminar_donacion():
  limpiar_pantalla()
  print("Eliminar donacion mal cargada.")
  print(separador)
  id_baja = pedir_entero("Ingrese ID de la donacion: ")
  donacion = buscar_por_id(donaciones, id_baja)
  if not donacion:
    print("No se encontro la donacion.")
    print(separador)
  else:
    if confirmar("Estas seguro?(s/n)"):
      donaciones.remove(donacion)
      print("Donacion eliminada.")
      print(separador)
    else:
      print("No se elimino la donacion.")
      print(separador)
  pausar()

datos = cargar_datos()
catalogo = datos["catalogo"]
socios = datos["socios"]
prestamos = datos["prestamos"]
reservas = datos["reservas"]
donaciones = datos["donaciones"]

#Menu principal del sistema.
opcion_principal = ""

#Opciones del menu principal
while opcion_principal != "0":
  limpiar_pantalla()
  print(separador)
  print("BIBLIOTECA POPULAR EL ALJIBE — Sistema v1.0")
  print(separador)
  print("1.Catalogo de libros")
  print("2.Socios")
  print("3.Prestamos")
  print("4.Las Reservas")
  print("5.Donaciones")
  print("0.Salir")
  print(separador)
  opcion_principal = pedir_digitos("Ingrese una opcion: ")
  print(separador)

  if opcion_principal == "1":
    opcion = ""
    while opcion != "x":
        limpiar_pantalla()
        opcion = mostrar_menu("Libros", {
            "a": "Cargar libro",
            "b": "Ver listado de libros",
            "c": "Buscar un libro",
            "d": "Cambiar estado de libro",
            "e": "Dar de baja libro",
            "x": "Volver a la pantalla principal"
        })
        print(separador)

        if opcion == "a":
          cargar_libro()
        elif opcion == "b":
          listar_libros()
        elif opcion == "c":
          buscar_libro()
        elif opcion == "d":
          cambiar_estado_libro()
        elif opcion == "e":
          baja_libro()
        elif opcion == "x":
          print("Volver a la pantalla principal.")
          print(separador)
        else:
          print("Opcion invalida.")
          pausar()
          print(separador)

  elif opcion_principal == "2":
    opcion = ""
    while opcion != "x":
      limpiar_pantalla()
      opcion = mostrar_menu("Socios", {
          "a": "Registrar socio nuevo",
          "b": "Listar socios",
          "c": "Buscar socio",
          "d": "Actualizar datos",
          "e": "Dar de baja a socios",
          "f": "Ver socios inactivos (2 años)",
          "x": "Volver a la pantalla principal"
      })
      print(separador)

      if opcion == "a":
        registrar_socio()
      elif opcion == "b":
        listar_socios()
      elif opcion == "c":
        buscar_socio()
      elif opcion == "d":
        actualizar_socio()
      elif opcion == "e":
        baja_socio()
      elif opcion == "f":
        socios_inactivos()
      elif opcion == "x":
        print("Volver a la pantalla principal.")
        print(separador)
      else:
        print("Opcion invalida.")
        pausar()
        print(separador)

  elif opcion_principal == "3":
    opcion = ""
    while opcion != "x":
      limpiar_pantalla()
      opcion = mostrar_menu("Prestamos", {
          "a": "Registrar un prestamo nuevo",
          "b": "Ver prestamos activos/historial",
          "c": "Buscar un prestamo",
          "d": "Registrar una devolucion",
          "e": "Eliminar un prestamo mal cargado",
          "x": "Volver a la pantalla principal"
      })
      print(separador)

      if opcion == "a":
        registrar_prestamo()
      elif opcion == "b":
        ver_prestamos()
      elif opcion == "c":
        buscar_prestamo()
      elif opcion == "d":
        registrar_devolucion()
      elif opcion == "e":
        eliminar_prestamo()
      elif opcion == "x":
        print("Volver a la pantalla principal.")
        print(separador)
      else:
        print("Opcion invalida.")
        pausar()
        print(separador)

  elif opcion_principal == "4":
    opcion=""
    while opcion != "x":
      limpiar_pantalla()
      opcion = mostrar_menu("Las Reservas", {
          "a": "Registrar reserva",
          "b": "Listar reservas",
          "c": "Buscar reservas (libro o socio)",
          "d": "Marcar reserva cumplida (Socio retira libro reservado)",
          "e": "Cancelar una reserva",
          "x": "Volver a la pantalla principal"
      })
      print(separador)

      if opcion == "a":
        registrar_reserva()
      elif opcion == "b":
        listar_reservas()
      elif opcion == "c":
        buscar_reserva()
      elif opcion == "d":
        cumplir_reserva()
      elif opcion == "e":
        cancelar_reserva()
      elif opcion == "x":
        print("Volver a la pantalla principal.")
        print(separador)
      else:
        print("Opcion invalida.")
        pausar()
        print(separador)

  elif opcion_principal == "5":
    opcion = ""
    while opcion != "x" :
            limpiar_pantalla()
            opcion = mostrar_menu("Donaciones", {
                "a": "Registrar una donacion",
                "b": "Listar donaciones",
                "c": "Buscar una donacion",
                "d": "Actualizar estado",
                "e": "Eliminar una donacion mal cargada",
                "x": "Volver a la pantalla principal"
            })
            print(separador)

            if opcion == "a":
              registrar_donacion()
            elif opcion == "b":
              listar_donaciones()
            elif opcion == "c":
              buscar_donacion()
            elif opcion == "d":
              actualizar_estado_donacion()
            elif opcion == "e":
              eliminar_donacion()
            elif opcion == "x":
              print("Volver a la pantalla principal.")
              print(separador)
            else:
              print("Opcion invalida.")
              pausar()
              print(separador)
#Salir del sistema
  elif opcion_principal == "0":
    #guardar los cambios.
    guardar_datos(datos)
    print("Gracias por usar el sistema.")
    print(separador)

#Por si pone cualquier cosa el usuario
  else:
    print("Opcion invalida.")
    print(separador)