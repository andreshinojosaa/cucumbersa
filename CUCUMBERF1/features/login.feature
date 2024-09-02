Feature: Inicio de Sesión

  Scenario: Inicio de sesión exitoso con credenciales correctas
    Given que el usuario ingresa el nombre de usuario "Admin" y la contraseña "fingsW2023"
    When el usuario intenta iniciar sesión
    Then el acceso debería ser concedido

  Scenario: Inicio de sesión fallido con credenciales incorrectas
    Given que el usuario ingresa el nombre de usuario "Admin" y la contraseña "incorrecta"
    When el usuario intenta iniciar sesión
    Then el acceso debería ser denegado
