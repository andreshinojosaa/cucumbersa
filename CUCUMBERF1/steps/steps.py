# features/steps/steps.py

from behave import given, when, then
from inventory import Producto, agregarProducto, buscarProductoPorRegistro, reducirCantidadProducto, mostrarInventario

@given('el sistema está inicializado')
def step_given_system_initialized(context):
    context.inventario = []

@when('el usuario inicia sesión con "{usuario}" y "{contrasena}"')
def step_when_user_logs_in(context, usuario, contrasena):
    context.sesion_iniciada = context.iniciar_sesion(usuario, contrasena)

@then('la sesión debe ser exitosa')
def step_then_login_successful(context):
    assert context.sesion_iniciada is True

@when('se agrega un producto con registro {registro}, nombre "{nombre}", cantidad {cantidad} y costo {costo}')
def step_when_add_product(context, registro, nombre, cantidad, costo):
    producto = Producto(int(registro), nombre, int(cantidad), float(costo))
    agregarProducto(context.inventario, producto)

@then('el producto con registro {registro} debe estar en el inventario')
def step_then_product_in_inventory(context, registro):
    producto = buscarProductoPorRegistro(context.inventario, int(registro))
    assert producto is not None

# Añadir más pasos para los otros escenarios según sea necesario
