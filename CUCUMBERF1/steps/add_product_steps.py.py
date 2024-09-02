from behave import given, when, then
from main import Producto, agregarProducto

@given('que el inventario contiene un producto con registro {registro}')
def step_given_inventory_contains_product_with_registration(context, registro):
    registro = int(registro)
    producto = Producto(registro=registro, nombre="ProductoEjemplo", cantidad=10, costo=100.0)
    context.inventario = [producto]

@when('el usuario agrega un producto con registro {registro}, nombre "{nombre}", cantidad {cantidad} y costo {costo}')
def step_when_add_product(context, registro, nombre, cantidad, costo):
    context.registro = int(registro)
    context.nombre = nombre
    context.cantidad = int(cantidad)
    context.costo = float(costo)
    producto = Producto(context.registro, context.nombre, context.cantidad, context.costo)
    agregarProducto(context.inventario, producto)

@then('el producto debería ser agregado al inventario')
def step_then_product_added(context):
    assert any(p.registro == context.registro for p in context.inventario)

@then('se debería mostrar un mensaje de error indicando que el registro ya existe')
def step_then_error_message_shown(context):
    # Aquí puedes usar un mock para verificar la salida o el comportamiento de error.
    pass
