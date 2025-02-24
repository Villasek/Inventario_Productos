
def agregar (inventario, nombre, cantidad):
    if nombre in inventario:
        inventario[nombre] += cantidad
    else: 
        inventario [nombre] = cantidad

def consultar(inventario,nombre):
    return inventario.get(nombre, "El producto no ha sido encontrado")     

def eliminar(inventario,nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"El producto '{nombre}'ha sido eliminado")
    else:
        print("El producto no existe")



inventario = {} #productos/cantidades 

while True: #bucle principal# 
    opciones = input(" a) agregar un producto / b) consultar cantidad de productos / c)Eliminar producto  : ")

    if opciones == 'a':
        nombre = input("Nombre del producto : ")
        cantidad = int(input("Agregue cantidad de productos: "))
        agregar(inventario, nombre, cantidad)
        print("el producto ha sido agregado correctamente")

    elif opciones == 'b':
        nombre = input("Nombre del producto : ")
        print ("Cantidad: ", consultar(inventario, nombre))

    elif opciones =='c':
        nombre = input("Ingrese el nombre del producto que desea eliminar: ")
        eliminar(inventario, nombre)

    else:
        print("Opcion no valida ")



