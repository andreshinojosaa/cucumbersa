from behave import given, when, then
from main import Producto, mostrarInventarioDeInventario

@given('que el inventario está vacío')
def step_given_empty_inventory(context):
    context.inventario = []

@given('que el inventario contiene los siguientes productos:')
def step_given_inventory_with_products(context):
    context.inventario = []
    for row in context.table:
        producto = Producto(int(row['registro']), row['nombre'], int(row['cantidad']), float(row['costo']))
        context.inventario.append(producto)

@when('el usuario solicita ver el inventario')
def step_when_view_inventory(context):
    context.inventory_output = []
    def mock_print(*args):
        context.inventory_output.append(args)
    import builtins
    builtins.print = mock_print
    mostrarInventarioDeInventario(context.inventario)

@then('el inventario debería estar vacío')
def step_then_inventory_empty(context):
    assert not context.inventory_output

@then('el inventario debería mostrar los productos correctamente')
def step_then_inventory_shows_products(context):
    expected_output = [
        ('\nRegistro: 1',),
        ('Producto: ProductoA',),
        ('Cantidad: 10',),
        ('Costo: 5.0',),
        ('-----------------------------',),
        ('\nRegistro: 2',),
        ('Producto: ProductoB',),
        ('Cantidad: 20',),
        ('Costo: 15.0',),
        ('-----------------------------',),
    ]
    assert context.inventory_output == expected_output
