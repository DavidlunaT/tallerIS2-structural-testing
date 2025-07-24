# Pruebas Estructurales

## Sección A: Análisis de Cadenas

### Tarea A.1: Implementación de la función `analyzeString`

La función `analyzeString` analiza una cadena y cuenta distintos tipos de caracteres:

```python
def analyzeString(s):
    """
    Analiza una cadena de texto y devuelve el conteo de caracteres en mayúscula, 
    minúscula, dígitos y caracteres especiales, así como una categoría basada 
    en la comparación entre mayúsculas y minúsculas.
    
    Args:
    s (str): La cadena de texto a analizar.
    
    Returns:
    tuple: (countUpper, countLower, countDigits, countSpecial, category)
        countUpper (int): Número de caracteres en mayúscula.
        countLower (int): Número de caracteres en minúscula.
        countDigits (int): Número de dígitos.
        countSpecial (int): Número de caracteres especiales.
        category (str): Categoría de la cadena ("More Uppercase", "More Lowercase", o "Balanced").
    """
    countUpper = 0
    countLower = 0
    countDigits = 0
    countSpecial = 0
    i = 0
    
    while i < len(s):
        ch = s[i]
        if 'A' <= ch <= 'Z':
            countUpper = countUpper + 1
        elif 'a' <= ch <= 'z':
            countLower = countLower + 1
        elif '0' <= ch <= '9':
            countDigits = countDigits + 1
        else:
            countSpecial = countSpecial + 1
        i = i + 1
    
    category = ""
    if countUpper > countLower:
        category = "More Uppercase"
    elif countLower > countUpper:
        category = "More Lowercase"
    else:
        category = "Balanced"
    
    return countUpper, countLower, countDigits, countSpecial, category

### Tarea A.2: Cobertura de Declaraciones (Statement Coverage)

Diseño de una suite de pruebas que logra 100% de cobertura de declaraciones con el mínimo número posible de casos de prueba:

```python
import unittest
import sys
import os

# Añadir el directorio src al path para poder importar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.analyze_string import analyzeString

class TestAnalyzeString(unittest.TestCase):
    """
    Pruebas para la función analyzeString.
    Task A.2: Statement Coverage - Diseñar una suite de pruebas que logre una 
    cobertura del 100% con el mínimo número de casos de prueba posible.
    """
    
    def test_more_uppercase(self):
        """
        Test para el caso donde hay más caracteres en mayúscula.
        Este test cubre:
        - Conteo de mayúsculas, minúsculas, dígitos y caracteres especiales
        - La condición countUpper > countLower es verdadera
        """
        result = analyzeString("ABCDef12!")
        self.assertEqual(result, (4, 2, 2, 1, "More Uppercase"))
    
    def test_more_lowercase(self):
        """
        Test para el caso donde hay más caracteres en minúscula.
        Este test cubre:
        - La condición countLower > countUpper es verdadera
        """
        result = analyzeString("ABcdef123!@#")
        self.assertEqual(result, (2, 4, 3, 3, "More Lowercase"))
    
    def test_balanced(self):
        """
        Test para el caso donde hay igual número de caracteres en mayúscula y minúscula.
        Este test cubre:
        - La condición else cuando countUpper == countLower
        """
        result = analyzeString("ABcd12!@")
        self.assertEqual(result, (2, 2, 2, 2, "Balanced"))
```

#### Explicación de cobertura:

1. **test_more_uppercase**: 
   - Cubre el caso donde `countUpper > countLower` es verdadero
   - Cubre el procesamiento de caracteres en mayúscula, minúscula, dígitos y especiales

2. **test_more_lowercase**: 
   - Cubre el caso donde `countLower > countUpper` es verdadero

3. **test_balanced**: 
   - Cubre el caso donde `countUpper == countLower` es verdadero

Con estos tres casos de prueba, se logra una cobertura del 100% de todas las declaraciones del código.

### Tarea A.3: Grafo de Flujo de Control (CFG)

Ver el archivo `control_flow_graph.md` para el CFG detallado de la función `analyzeString`.

### Tarea A.4: Clasificación de Nodos

Ver el archivo `node_classification.md` para la clasificación detallada de los nodos del CFG.

Un archivo README básico podría incluir:

```markdown
# Proyecto de Análisis de Cadenas

Este proyecto implementa una función en Python que analiza una cadena de texto y cuenta el número de caracteres, palabras y líneas.

## Instalación

No se requieren dependencias externas. Solo necesitas Python instalado.

## Ejecución de pruebas

Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
python -m unittest test_analyze_string.py
```

## Uso

Importa la función `analyzeString` desde `analyze_string.py` y úsala como se muestra a continuación:

```python
from analyze_string import analyzeString

result = analyzeString("Tu cadena aquí")
print(result)
```
```

Con esto, tienes un proyecto básico en Python que implementa la función `analyzeString`, incluye pruebas, un gráfico de flujo de control y una clasificación de nodos. Puedes ajustar la implementación y las pruebas según los requisitos específicos que tengas.