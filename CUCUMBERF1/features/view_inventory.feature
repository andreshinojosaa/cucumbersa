Feature: Visualización del Inventario

  Scenario: Mostrar inventario vacío
    Given que el inventario está vacío
    When el usuario solicita ver el inventario
    Then el inventario debería estar vacío

  Scenario: Mostrar inventario con productos
    Given que el inventario contiene los siguientes productos:
      | registro | nombre     | cantidad | costo |
      | 1        | ProductoA  | 10       | 5.0   |
      | 2        | ProductoB  | 20       | 15.0  |
    When el usuario solicita ver el inventario
    Then el inventario debería mostrar los productos correctamente
