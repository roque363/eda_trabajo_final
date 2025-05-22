from producto import Producto

class Inventario:
  def __init__(self):
    self.productos = []

    p1 = Producto("101", "Rodamiento", "Repuestos Mecanicos", 10)
    p2 = Producto("102", "Sensor de proximidad", "Repuestos Electricos", 5)
    p3 = Producto("103", "Casco SteelPro", "Equipo de Protección Personal", 8)
    p4 = Producto("104", "Cinta aislante", "Otros", 15)
    p5 = Producto("105", "Dispersor de calor", "Repuestos Mecanicos", 6)
    p6 = Producto("106", "Bomba de aceite de moto", "Repuestos Mecanicos", 4)
    p7 = Producto("107", "PanelBoards", "Repuestos Electricos", 26)
    p8 = Producto("108", "Cable LSOH-90", "Repuestos Electricos", 30)
    p9 = Producto("109", "Tapon de oido", "Equipo de Protección Personal", 24)

    self.productos.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9])

  def buscar_por_codigo(self, codigo):
    for producto in self.productos:
      if producto.codigo == codigo:
        return producto
    return None
  
  def seleccionar_categoria(self):
    print("\nSeleccione la categoría:")
    print("1. Repuestos Mecánicos")
    print("2. Repuestos Eléctricos")
    print("3. Equipo de Protección Personal")
    print("4. Otros")

    opcion = input("Ingrese el número de categoría: ").strip()
    categorias = {
      "1": "Repuestos Mecánicos",
      "2": "Repuestos Eléctricos",
      "3": "Equipo de Protección Personal",
      "4": "Otros"
    }
    return categorias.get(opcion, "Otros")
  

  def agregar_producto(self):
    codigo = input("Código: ").strip()
    if self.buscar_por_codigo(codigo) is not None:
      print("Error: Ya existe un producto con ese código.")
      return

    nombre = input("Nombre: ").strip()
    categoria = self.seleccionar_categoria()
    cantidad = int(input("Cantidad inicial: "))

    nuevo = Producto(codigo, nombre, categoria, cantidad)
    self.productos.append(nuevo)
    print("Producto agregado correctamente.")


  def editar_producto(self):
    codigo = input("Código del producto a editar: ").strip()
    producto = self.buscar_por_codigo(codigo)

    if not producto:
      print("Producto no encontrado.")
      return
    
    nuevo_nombre = input(f"Nombre ({producto.nombre}): ").strip()
    nueva_categoria = input(f"Categoría ({producto.categoria}): ").strip()
    nueva_cantidad = input(f"Cantidad actual ({producto.cantidad}): ").strip()
    
    if nuevo_nombre: producto.nombre = nuevo_nombre
    if nueva_categoria: producto.categoria = nueva_categoria
    if nueva_cantidad.isdigit(): producto.cantidad = int(nueva_cantidad)

    print("Producto actualizado.")

  
  def modificar_stock(self):
    codigo = input("Código del producto: ").strip()
    producto = self.buscar_por_codigo(codigo)

    if not producto:
      print("Producto no encontrado.")
      return
    
    print("\n")
    producto.mostrar()
    
    print("\n1. Ingresar stock")
    print("2. Retirar stock")
    print("3. Volver")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
      cantidad = int(input("Cantidad a ingresar: "))
      producto.registrar_entrada(cantidad)
      print("Stock actualizado.")
    elif opcion == "2":
      cantidad = int(input("Cantidad a retirar: "))
      if producto.registrar_salida(cantidad):
        print("Stock actualizado.")
      else:
        print("Error: stock insuficiente.")
    elif opcion == "3":
      print("Volviendo...")
      return
    else:
      print("Opción inválida.")


  def listar_productos(self):
    if not self.productos:
      print("Inventario vacío.")
      return
    for p in self.productos:
      p.mostrar()


  def reporte_por_categoria(self):
    categorias = {}
    for p in self.productos:
      categorias.setdefault(p.categoria, []).append(p)

    for categoria, items in categorias.items():
      print(f"\nCategoría: {categoria}")
      for p in items:
        p.mostrar()


  def reporte_por_salidas(self, orden="desc"):
    if orden == "desc":
      ordenados = sorted(self.productos, key=lambda p: p.salidas, reverse=True)
      print("\nProductos más utilizados:")
    else:
      ordenados = sorted(self.productos, key=lambda p: p.salidas)
      print("\nProductos menos utilizados:")

    for p in ordenados:
      p.mostrar()


  def reporte_por_stock(self, orden="desc"):
    if orden == "desc":
      ordenados = sorted(self.productos, key=lambda p: p.cantidad, reverse=True)
      print("\nProductos con mayor stock:")
    else:
      ordenados = sorted(self.productos, key=lambda p: p.cantidad)
      print("\nProductos con menor stock:")

    for p in ordenados:
      p.mostrar()

