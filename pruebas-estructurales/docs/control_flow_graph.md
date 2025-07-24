# Tarea A.3: Control Flow Graph (CFG)

El siguiente es el Control Flow Graph (CFG) para la función `analyzeString`.

```
[1] Inicio
 |
 v
[2] Inicialización: 
    countUpper = 0
    countLower = 0
    countDigits = 0
    countSpecial = 0
    i = 0
 |
 v
[3] ¿i < len(s)?
 |   |
 |   v (No)
 |  [7] category = ""
 |   |
 |   v
 |  [8] ¿countUpper > countLower?
 |   |   |
 |   |   v (Sí)
 |   |  [9] category = "More Uppercase"
 |   |   |
 |   |   v
 |   |  [12] Retornar (countUpper, countLower, countDigits, countSpecial, category)
 |   |
 |   v (No)
 |  [10] ¿countLower > countUpper?
 |   |   |
 |   |   v (Sí)
 |   |  [11] category = "More Lowercase"
 |   |   |
 |   |   v
 |   |  [12] Retornar (countUpper, countLower, countDigits, countSpecial, category)
 |   |
 |   v (No)
 |  [13] category = "Balanced"
 |   |
 |   v
 |  [12] Retornar (countUpper, countLower, countDigits, countSpecial, category)
 |
 v (Sí)
[4] ch = s[i]
 |
 v
[5] ¿'A' <= ch <= 'Z'?
 |   |
 |   v (Sí)
 |  [5.1] countUpper = countUpper + 1
 |   |
 |   v
 |  [6.4] i = i + 1
 |   |
 |   v
 |  [3] ¿i < len(s)? (Volver al principio del bucle)
 |
 v (No)
[5.2] ¿'a' <= ch <= 'z'?
 |   |
 |   v (Sí)
 |  [5.3] countLower = countLower + 1
 |   |
 |   v
 |  [6.4] i = i + 1
 |   |
 |   v
 |  [3] ¿i < len(s)? (Volver al principio del bucle)
 |
 v (No)
[5.4] ¿'0' <= ch <= '9'?
 |   |
 |   v (Sí)
 |  [5.5] countDigits = countDigits + 1
 |   |
 |   v
 |  [6.4] i = i + 1
 |   |
 |   v
 |  [3] ¿i < len(s)? (Volver al principio del bucle)
 |
 v (No)
[5.6] countSpecial = countSpecial + 1
 |
 v
[6.4] i = i + 1
 |
 v
[3] ¿i < len(s)? (Volver al principio del bucle)

    def test_multiple_words(self):
        result = analyzeString("Hello world")
        self.assertEqual(result, {'num_chars': 11, 'num_words': 2, 'num_lines': 1})

    def test_new_lines(self):
        result = analyzeString("Hello\nworld")
        self.assertEqual(result, {'num_chars': 12, 'num_words': 2, 'num_lines': 2})

    def test_multiple_lines(self):
        result = analyzeString("Hello\nworld\nthis is a test")
        self.assertEqual(result, {'num_chars': 30, 'num_words': 6, 'num_lines': 3})

if __name__ == '__main__':
    unittest.main()
```

### Paso 3: Gráfico de flujo de control

El gráfico de flujo de control para la función `analyzeString` es bastante simple. Aquí hay una descripción textual:

1. **Inicio**
2. **Recibir `input_string`**
3. **Calcular `num_chars`**: Longitud de `input_string`
4. **Calcular `num_words`**: Número de palabras en `input_string`
5. **Calcular `num_lines`**: Número de líneas en `input_string`
6. **Devolver el diccionario con los resultados**
7. **Fin**

### Paso 4: Clasificación de nodos

La clasificación de nodos en el gráfico de flujo de control podría ser la siguiente:

- **Nodos de entrada**: `input_string`
- **Nodos de procesamiento**: Cálculo de `num_chars`, `num_words`, `num_lines`
- **Nodos de salida**: Devolución del diccionario con los resultados

### Paso 5: Estructura del proyecto

La estructura del proyecto podría ser la siguiente:

```
analyze_string_project/
│
├── analyze_string.py        # Contiene la función analyzeString
├── test_analyze_string.py   # Contiene las pruebas unitarias
└── README.md                # Documentación del proyecto
```

### Paso 6: Ejecución de pruebas

Para ejecutar las pruebas, simplemente ejecuta el archivo `test_analyze_string.py`:

```bash
python test_analyze_string.py
```

Esto ejecutará todas las pruebas definidas y te informará si alguna de ellas falla.

### Conclusión

Hemos creado un proyecto básico en Python que implementa la función `analyzeString`, junto con pruebas unitarias, un gráfico de flujo de control y una clasificación de nodos. Puedes expandir la funcionalidad de `analyzeString` según sea necesario, dependiendo de los requisitos específicos que tengas.