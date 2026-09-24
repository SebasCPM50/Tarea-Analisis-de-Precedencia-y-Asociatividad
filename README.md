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
*(Sección en construcción para la siguiente fase...)*

## Pruebas
*(Sección en construcción para agrupar los resultados...)*

## Resultados
*(Sección en construcción...)*

## Conclusiones
*(Sección en construcción...)*
