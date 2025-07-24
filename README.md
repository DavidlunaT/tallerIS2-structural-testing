# tallerIS2-structural-testing

Este repositorio contiene el código para pruebas estructurales de software.

## Sección A: Análisis de Cadenas

Esta sección implementa y prueba una función `analyzeString` que analiza una cadena y cuenta:
- Caracteres en mayúscula
- Caracteres en minúscula
- Dígitos
- Caracteres especiales

Además, clasifica la cadena según tenga más caracteres en mayúscula, minúscula o si están equilibrados.

### Estructura del Proyecto

```
pruebas-estructurales/
├── src/
│   ├── __init__.py
│   └── analyze_string.py      # Implementación de la función analyzeString
├── tests/
│   ├── __init__.py
│   └── test_analyze_string.py # Pruebas unitarias con cobertura de declaraciones
├── docs/
│   ├── control_flow_graph.md  # Grafo de flujo de control (CFG)
│   └── node_classification.md # Clasificación de nodos del CFG
└── requirements.txt           # Dependencias del proyecto
```

### Tareas Completadas

- **Tarea A.1**: Implementación del código `analyzeString` en Python
- **Tarea A.2**: Diseño de casos de prueba con 100% de cobertura de declaraciones
- **Tarea A.3**: Creación del grafo de flujo de control (CFG)
- **Tarea A.4**: Clasificación de nodos en el grafo