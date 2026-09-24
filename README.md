# Taller de Asociatividad y Precedencia con ANTLR4

## Descripción
Esta tarea tiene como propósito comprobar experimentalmente cómo funcionan las reglas de asociatividad y precedencia en el diseño de un lenguaje. Para ello, se utiliza una gramática de calculadora básica construida con ANTLR4. La calculadora es únicamente el medio de comprobación; el objetivo real es observar cómo los cambios en las reglas de la gramática afectan la forma en que se agrupan y evalúan las expresiones. Toda la tarea se ejecuta utilizando Python.

## Objetivos
* Demostrar la asociatividad por la izquierda mediante la estructura predeterminada de la gramática.
* Demostrar la asociatividad por la derecha modificando las reglas de ANTLR4.
* Comprobar el cambio en la interpretación de una expresión al alterar la precedencia (prioridad) entre multiplicación/división y suma/resta.

## Estructura de la tarea
* `Calculadora.g4`: Archivo principal que contiene la gramática (reglas léxicas y sintácticas).
* `calculadora.py`: Script en Python que toma los archivos generados por ANTLR4, lee la expresión, recorre el árbol y evalúa el resultado matemático.
* Archivos autogenerados por ANTLR4 (Lexer, Parser, Visitor)
* `README.md`: Documentación y análisis de la tarea.

## Requerimientos
* ANTLR4 instalado en el sistema (disponible mediante el comando `antlr4`).
* Python 3.
* Paquete `antlr4-python3-runtime` para ejecutar el código generado. No se utiliza Java para la ejecución del proyecto.

## Instalación y configuración
Para preparar el entorno, basta con instalar el runtime de ANTLR4 para Python mediante el gestor de paquetes de Python (pip):
```bash
pip install antlr4-python3-runtime
```

## Ejecución
1. Generar los archivos Python a partir de la gramática:
   ```bash
   antlr4 -Dlanguage=Python3 -visitor Calculadora.g4
   ```
2. Ejecutar la prueba:
   ```bash
   python3 calculadora.py
   ```
   
## Asociatividad

### Asociatividad por la izquierda
Por defecto, si una gramática en ANTLR4 no tiene instrucciones adicionales, asocia las operaciones del mismo nivel (como múltiples restas) de izquierda a derecha.

* **Expresión analizada:** `10 - 3 - 2`
* **Forma en que se agrupa:** `(10 - 3) - 2`
* **Resultado obtenido:** `5`

**Explicación y Árbol Sintáctico:**
La gramática interpreta esta expresión construyendo el árbol desde el extremo izquierdo. Las operaciones que quedan más abajo (más profundas) en el árbol se resuelven primero.

Representación del árbol generado por el parser:
```text
         Resta (-)  Última operación en resolverse
         /       \
   Resta (-)      2
    /     \
  10       3 Primer operación en resolverse
```
Como se observa en el árbol, el parser agrupa primero el `10` y el `3`. Python evalúa ese sub-árbol inferior (dando 7) y luego utiliza ese resultado para restarle el `2` del nivel superior, dando el resultado final de `5`.

**Prueba:**
<img width="1497" height="620" alt="image" src="https://github.com/user-attachments/assets/ed40a96a-c130-4cae-a762-24e9f912eca2" />


### Asociatividad por la derecha
**Objetivo:** Demostrar que al modificar la gramática, podemos forzar a que los operadores del mismo tipo se agrupen de derecha a izquierda.

Para lograr esto, modificamos la regla de la resta en nuestro archivo `Calculadora.g4` añadiendo la directiva `<assoc=right>`:
`| <assoc=right> expr '-' expr     # Resta`

*   **Expresión analizada:** `10 - 3 - 2`
*   **Forma en que se agrupa lógicamente:** `10 - (3 - 2)`
*   **Resultado obtenido:** `9`

**Por qué la gramática produce esta agrupación:**
Al indicar explícitamente `<assoc=right>`, el parser altera su comportamiento predeterminado. Cuando encuentra operadores compitiendo en el mismo nivel jerárquico, prioriza resolver primero el lado derecho. 

Esto se refleja en el árbol de análisis sintáctico, donde la operación de la derecha queda más profunda y, por lo tanto, se resuelve primero:
```text
      - (Raíz. Operación final: 10 - 1 = 9)
    /   \
  10      - (Sub-árbol derecho. Se resuelve primero: 3 - 2 = 1)
        /   \
       3     2
```
**Prueba:**
<img width="1491" height="617" alt="image" src="https://github.com/user-attachments/assets/a9e94a97-be66-4c9a-ad01-2d1b3693d568" />


## Precedencia

### Precedencia de multiplicación y división

**Objetivo:** Comprobar que en la gramática, los operadores de multiplicación (`*`) y división (`/`) tienen mayor prioridad (se ejecutan primero) que la suma (`+`) y la resta (`-`).

En ANTLR4, la precedencia se establece **por el orden en que se declaran las alternativas dentro de una regla**. Las reglas que están más arriba tienen mayor prioridad.

Nuestra gramática está estructurada así:
```antlr
expr: expr '*' expr                   # Multiplicacion (Mayor prioridad)
    | expr '/' expr                   # Division
    | expr '+' expr                   # Suma
    | <assoc=right> expr '-' expr     # Resta (Menor prioridad)
    | INT                             # Numero
    ;
```
Expresión analizada: 2 + 3 * 4

Forma en que se agrupa lógicamente: 2 + (3 * 4)

Resultado obtenido: 14

**Por qué la gramática produce esta agrupación:**
Al analizar la expresión 2 + 3 * 4, el parser detecta dos operadores compitiendo: + y *. Como la regla de la multiplicación está declarada antes que la regla de la suma en el archivo .g4, ANTLR4 le asigna mayor precedencia.

Por lo tanto, el parser construye el árbol sintáctico agrupando primero el 3 * 4 en un nivel inferior (para que se evalúe primero), y el resultado de eso se suma con el 2 en la raíz del árbol.
```text
      + (Raíz. Operación final: 2 + 12 = 14)
    /   \
  2      * (Sub-árbol derecho. Se resuelve primero: 3 * 4 = 12)
        /   \
       3     4
```
**Prueba:**
<img width="1490" height="617" alt="image" src="https://github.com/user-attachments/assets/7aa807d4-4368-46aa-9c3b-4e5119d915c8" />

Aquí tienes exclusivamente las tres secciones finales para que las agregues a tu README.md:

## Precedencia de suma y resta

**Objetivo:** Demostrar que al alterar el orden de las reglas en la gramática, podemos invertir las reglas matemáticas tradicionales, dándole mayor prioridad a la suma (`+`) y a la resta (`-`) sobre la multiplicación (`*`) y la división (`/`).

Para lograr esto, modificamos el archivo `Calculadora.g4` moviendo las reglas de suma y resta hacia arriba:
```antlr
expr: expr '+' expr                   # Suma (Mayor prioridad)
    | <assoc=right> expr '-' expr     # Resta 
    | expr '*' expr                   # Multiplicacion (Menor prioridad)
    | expr '/' expr                   # Division
    | INT                             # Numero
    ;
```
Expresión analizada: 2 + 3 * 4

Forma en que se agrupa lógicamente: (2 + 3) * 4

Resultado obtenido: 20

**Por qué la gramática produce esta agrupación:**
Al colocar la suma por encima de la multiplicación en el archivo de la gramática, ANTLR4 le otorga mayor precedencia. El parser lee la expresión y, al encontrar la competencia entre + y *, decide resolver primero la suma.

En el árbol sintáctico, esto se refleja empujando la suma hacia el fondo del árbol (para que se calcule primero) y dejando la multiplicación en la raíz:
```text
      * (Raíz. Operación final: 5 * 4 = 20)
    /   \
  4      + (Sub-árbol. Se resuelve primero: 2 + 3 = 5)
        /   \
       2     3
```

**Prueba:**
<img width="1492" height="618" alt="image" src="https://github.com/user-attachments/assets/9de45d83-1f17-4ceb-a864-e7190b060cba" />

## Resultados
A lo largo de esta tarea, utilizamos la gramática de una calculadora básica no para construir una herramienta funcional, sino como un medio experimental para observar el comportamiento de ANTLR4.

Mediante pruebas controladas, logramos evidenciar que:
- La asociatividad se maneja por defecto hacia la izquierda, pero puede ser forzada hacia la derecha utilizando comandos específicos como <assoc=right>, lo cual cambia completamente la forma en que se agrupan operadores idénticos.
- La precedencia de los operadores no está predefinida por las leyes matemáticas, sino por el orden estricto en que se declaran las reglas dentro del archivo .g4. La regla escrita más arriba siempre se resolverá primero en el árbol de análisis sintáctico.

## Conclusiones
- El control está en la sintaxis: El análisis sintáctico (Parser) es el responsable de darle estructura y jerarquía a una expresión plana generada por el Lexer.

- Semántica mínima: La evaluación en Python (Visitor) se mantuvo estrictamente básica, calculando únicamente los nodos del árbol para poder comprobar matemáticamente que la gramática estaba agrupando los valores en el orden esperado.

- Independencia del lenguaje: ANTLR4 permite definir las reglas del lenguaje de forma abstracta en su propio formato (.g4), delegando la ejecución final al entorno de preferencia, en este caso, utilizando antlr4-python3-runtime para ejecutar el código generado 100% en Python.

## Integrantes
Alejandro Poveda Sandoval - Juan
