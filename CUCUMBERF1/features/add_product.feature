Feature: Ingreso de Productos

  Scenario: Agregar un producto nuevo
    Given que el inventario está vacío
    When el usuario agrega un producto con registro 1, nombre "Producto1", cantidad 5 y costo 10.0
    Then el producto debería ser agregado al inventario

  Scenario: Intentar agregar un producto con registro existente
    Given que el inventario contiene un producto con registro 1
    When el usuario intenta agregar un producto con el mismo registro 1
    Then se debería mostrar un mensaje de error indicando que el registro ya existe
