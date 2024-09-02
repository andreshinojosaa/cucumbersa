Feature: Entrada y Salida de Productos

  Scenario: Reducir la cantidad de un producto existente
    Given que el inventario contiene un producto con registro 1 y cantidad 10
    When el usuario reduce la cantidad del producto con registro 1 en 5
    Then la cantidad del producto con registro 1 debería ser 5

  Scenario: Agregar cantidad a un producto existente
    Given que el inventario contiene un producto con registro 1 y cantidad 10
    When el usuario agrega 5 unidades al producto con registro 1
    Then la cantidad del producto con registro 1 debería ser 15

  Scenario: Intentar reducir cantidad de un producto no existente
    Given que el inventario está vacío
    When el usuario intenta reducir la cantidad del producto con registro 1 en 5
    Then se debería mostrar un mensaje de error indicando que el producto no existe

  Scenario: Intentar agregar cantidad a un producto no existente
    Given que el inventario está vacío
    When el usuario intenta agregar 5 unidades al producto con registro 1
    Then se debería mostrar un mensaje de error indicando que el producto no existe
