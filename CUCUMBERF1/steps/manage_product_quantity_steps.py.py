from behave import given, when, then
from main import Producto, reducirCantidadProductoEnInventario, agregarCantidadProductoEnInventario

@given('que el inventario está vacío')
def step_given_empty_inventory(context):
    context.inventario = []

@given('que el inventario contiene un producto con registro {registro} y cantidad {cantidad}')
def step_given_inventory_contains_product_with_registration_and_quantity(context, registro, cantidad):
    registro = int(registro)
    cantidad = int(cantidad)
    producto = Producto(registro=registro, nombre="ProductoEjemplo", cantidad=cantidad, costo=0.0)
    context.inventario = [producto]

@when('el usuario reduce la cantidad del producto con registro {registro} en {cantidad}')
def step_when_reduce_product_quantity(context, registro, cantidad):
    reducirCantidadProductoEnInventario(context.inventario, int(registro), int(cantidad))

@when('el usuario agrega {cantidad} unidades al producto con registro {registro}')
def step_when_add_product_quantity(context, cantidad, registro):
    agregarCantidadProductoEnInventario(context.inventario, int(registro), int(cantidad))

@then('la cantidad del producto con registro {registro} debería ser {cantidad}')
def step_then_product_quantity(context, registro, cantidad):
    producto = next((p for p in context.inventario if p.registro == int(registro)), None)
    assert producto is not None
    assert producto.cantidad == int(cantidad)

@then('se debería mostrar un mensaje de error indicando que el producto no existe')
def step_then_error_message_product_not_found(context):
    pass
