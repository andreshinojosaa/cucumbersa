# inventory.py

class Producto:
    def __init__(self, registro, nombre, cantidad, costo):
        self.registro = registro
        self.nombre = nombre
        self.cantidad = cantidad
        self.costo = costo

def agregarProducto(inventario, producto):
    inventario.append(producto)

def buscarProductoPorRegistro(inventario, registro):
    for producto in inventario:
        if producto.registro == registro:
            return producto
    return None

def reducirCantidadProducto(inventario, registro, cantidad):
    producto = buscarProductoPorRegistro(inventario, registro)
    if producto:
        if producto.cantidad >= cantidad:
            producto.cantidad -= cantidad
        else:
            raise ValueError("Cantidad a reducir mayor a la disponible")
    else:
        raise ValueError("Producto no encontrado")

def mostrarInventario(inventario):
    for producto in inventario:
        print(f"Registro: {producto.registro}")
        print(f"Nombre: {producto.nombre}")
        print(f"Cantidad: {producto.cantidad}")
        print(f"Costo: {producto.costo}")
        print("-----------------------------")
