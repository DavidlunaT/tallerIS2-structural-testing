# Tarea A.4: Clasificación de Nodos

A continuación se presenta la clasificación de los nodos en el grafo de flujo de control (CFG) de la función `analyzeString`:

## Tipos de Nodos en el CFG

1. **Nodo Fuente (Source Node)**
   - **[1]** Inicio de la función

2. **Nodo Sumidero (Sink Node)**
   - **[12]** Instrucción de retorno

3. **Nodos de Secuencia (Sequence Nodes)**
   - **[2]** Inicialización de variables
   - **[4]** Asignación `ch = s[i]`
   - **[5.1]** Incremento de `countUpper`
   - **[5.3]** Incremento de `countLower`
   - **[5.5]** Incremento de `countDigits`
   - **[5.6]** Incremento de `countSpecial`
   - **[6.4]** Incremento de `i`
   - **[7]** Inicialización de `category`
   - **[9]** Asignación `category = "More Uppercase"`
   - **[11]** Asignación `category = "More Lowercase"`
   - **[13]** Asignación `category = "Balanced"`

4. **Nodos de Decisión (Decision Nodes)**
   - **[3]** Condición del bucle `i < len(s)`
   - **[5]** Condición `'A' <= ch <= 'Z'`
   - **[5.2]** Condición `'a' <= ch <= 'z'`
   - **[5.4]** Condición `'0' <= ch <= '9'`
   - **[8]** Condición `countUpper > countLower`
   - **[10]** Condición `countLower > countUpper`

5. **Estructura if-then-else**
   - La cascada de condiciones con `ch` (nodos [5], [5.2], [5.4]) forma una estructura if-then-else anidada
   - Las condiciones para determinar la categoría (nodos [8], [10]) también forman una estructura if-then-else

6. **Estructura de Bucle (Loop Structure)**
   - El bucle `while` que itera sobre cada carácter de la cadena (nodos [3], [4], [5], etc.)

## Diagrama con Anotaciones

```
[1] Inicio (Nodo Fuente)
 |
 v
[2] Inicialización (Secuencia)
 |
 v
[3] ¿i < len(s)? (Decisión - Entrada de Bucle)
 |   |
 |   v (No)
 |  [7] category = "" (Secuencia)
 |   |
 |   v
 |  [8] ¿countUpper > countLower? (Decisión - if-then-else)
 |   |   |
 |   |   v (Sí)
 |   |  [9] category = "More Uppercase" (Secuencia - if-then)
 |   |   |
 |   |   v
 |   |  [12] Retornar (Nodo Sumidero)
 |   |
 |   v (No)
 |  [10] ¿countLower > countUpper? (Decisión - if-then-else)
 |   |   |
 |   |   v (Sí)
 |   |  [11] category = "More Lowercase" (Secuencia - if-then)
 |   |   |
 |   |   v
 |   |  [12] Retornar (Nodo Sumidero)
 |   |
 |   v (No)
 |  [13] category = "Balanced" (Secuencia - else)
 |   |
 |   v
 |  [12] Retornar (Nodo Sumidero)
 |
 v (Sí)
[4] ch = s[i] (Secuencia)
 |
 v
[5] ¿'A' <= ch <= 'Z'? (Decisión - if-then-else)
 |   |
 |   v (Sí)
 |  [5.1] countUpper = countUpper + 1 (Secuencia - if-then)
 |   |
 |   v
 |  [6.4] i = i + 1 (Secuencia)
 |   |
 |   v
 |  [3] (Regreso al bucle)
 |
 v (No)
[5.2] ¿'a' <= ch <= 'z'? (Decisión - if-then-else)
 |   |
 |   v (Sí)
 |  [5.3] countLower = countLower + 1 (Secuencia - if-then)
 |   |
 |   v
 |  [6.4] i = i + 1 (Secuencia)
 |   |
 |   v
 |  [3] (Regreso al bucle)
 |
 v (No)
[5.4] ¿'0' <= ch <= '9'? (Decisión - if-then-else)
 |   |
 |   v (Sí)
 |  [5.5] countDigits = countDigits + 1 (Secuencia - if-then)
 |   |
 |   v
 |  [6.4] i = i + 1 (Secuencia)
 |   |
 |   v
 |  [3] (Regreso al bucle)
 |
 v (No)
[5.6] countSpecial = countSpecial + 1 (Secuencia - else)
 |
 v
[6.4] i = i + 1 (Secuencia)
 |
 v
[3] (Regreso al bucle)
```

Para ejecutar las pruebas, simplemente ejecuta el archivo `test_analyze.py`:

```bash
python test_analyze.py
```

Esto ejecutará todas las pruebas definidas y te mostrará si todas pasaron correctamente.

### Conclusión

Hemos creado un proyecto en Python que implementa la función `analyzeString`, cubrimos pruebas unitarias, diseñamos un gráfico de flujo de control y clasificamos los nodos. Puedes ajustar la implementación y las pruebas según los requisitos específicos que tengas en mente.