from behave import given, when, then
import io
import sys

# Suponiendo que la función `iniciarSesion` está en el archivo `main.py`
from main import iniciarSesion  

@given('que el usuario ingresa el nombre de usuario "{usuario}" y la contraseña "{contrasena}"')
def step_given_user_credentials(context, usuario, contrasena):
    context.usuario = usuario
    context.contrasena = contrasena

@when('el usuario intenta iniciar sesión')
def step_when_attempt_login(context):
    # Redirigir la entrada estándar para simular la entrada del usuario
    input_backup = sys.stdin
    sys.stdin = io.StringIO(f"{context.usuario}\n{context.contrasena}\n")
    
    # Llamar a la función de inicio de sesión
    context.result = iniciarSesion()

    # Restaurar la entrada estándar
    sys.stdin = input_backup

@then('el acceso debería ser concedido')
def step_then_access_granted(context):
    assert context.result is True

@then('el acceso debería ser denegado')
def step_then_access_denied(context):
    assert context.result is False
