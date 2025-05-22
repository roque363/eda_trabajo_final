class Producto:
  def __init__(self, codigo, nombre, categoria, cantidad):
    self.codigo = codigo
    self.nombre = nombre
    self.categoria = categoria
    self.cantidad = cantidad # stock
    self.salidas = 0 # salida de stock
  
  def mostrar(self):
    print(f"Código: {self.codigo} | Nombre: {self.nombre} | "
          f"Categoría: {self.categoria} | Cantidad: {self.cantidad} | "
          f"Salidas de producto: {self.salidas}")
    
  def registrar_entrada(self, cantidad):
    self.cantidad += cantidad

  def registrar_salida(self, cantidad):
    if cantidad <= self.cantidad:
      self.cantidad -= cantidad
      self.salidas += cantidad
      return True
    else:
      return False
    
