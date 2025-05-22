from inventario import Inventario

inv = Inventario()

def menu():
  while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Modificar stock")
    print("4. Listar productos")
    print("5. Reportes")
    print("6. Salir")

    opcion = input("Seleccione una opción: ").strip()
    print("\n")

    if opcion == "1":
      inv.agregar_producto()
    elif opcion == "2":
      inv.editar_producto()
    elif opcion == "3":
      inv.modificar_stock()
    elif opcion == "4":
      inv.listar_productos()
    elif opcion == "5":
      sub_menu_reportes()
    elif opcion == "6":
      print("Saliendo de la aplicación.")
      break
    else:
      print("Opción no válida.")

def sub_menu_reportes():
  print("\n--- MENÚ DE REPORTES ---")
  print("1. Por categoría")
  print("2. Más utilizados (por salidas de stock)")
  print("3. Menos utilizados (por salidas de stock)")
  print("4. Mayor stock")
  print("5. Menor stock")

  opcion = input("Seleccione una opción: ").strip()
  print("\n")

  if opcion == "1":
    inv.reporte_por_categoria()
  elif opcion == "2":
    inv.reporte_por_salidas(orden="desc")
  elif opcion == "3":
    inv.reporte_por_salidas(orden="asc")
  elif opcion == "4":
    inv.reporte_por_stock(orden="desc")
  elif opcion == "5":
    inv.reporte_por_stock(orden="asc")
  else:
    print("Opción no válida.")

menu()
