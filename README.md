# Taller de Asociatividad y Precedencia con ANTLR4

## Descripción
Este taller tiene como propósito comprobar experimentalmente cómo funcionan las reglas de asociatividad y precedencia en el diseño de un lenguaje. Para ello, se utiliza una gramática de calculadora básica construida con ANTLR4. La calculadora es únicamente el medio de comprobación; el objetivo real es observar cómo los cambios en las reglas de la gramática afectan la forma en que se agrupan y evalúan las expresiones. Todo el proyecto se ejecuta utilizando Python.

## Objetivos
* Demostrar la asociatividad por la izquierda mediante la estructura predeterminada de la gramática.
* Demostrar la asociatividad por la derecha modificando las reglas de ANTLR4.
* Comprobar el cambio en la interpretación de una expresión al alterar la precedencia (prioridad) entre multiplicación/división y suma/resta.

## Estructura del proyecto
* `Calculadora.g4`: Archivo principal que contiene la gramática (reglas léxicas y sintácticas).
* `calculadora.py`: Script en Python que toma los archivos generados por ANTLR4, lee la expresión, recorre el árbol y evalúa el resultado matemático.
* Archivos autogenerados por ANTLR4 (Lexer, Parser, Visitor): Son el puente entre nuestra gramática y el código Python.
* `README.md`: Documentación y análisis del taller.

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
         Resta (-)  <-- Operación principal (última en resolverse)
         /       \
   Resta (-)      2 <-- Lado derecho de la operación principal
    /     \
  10       3 <-- Esta resta está más profunda, se resuelve primero (10 - 3 = 7)
```
Como se observa en el árbol, el parser agrupa primero el `10` y el `3`. Python evalúa ese sub-árbol inferior (dando 7) y luego utiliza ese resultado para restarle el `2` del nivel superior, dando el resultado final de `5`.

### Asociatividad por la derecha
*(Sección en construcción para la siguiente fase...)*

## Precedencia
*(Sección en construcción para la siguiente fase...)*

## Pruebas
*(Sección en construcción para agrupar los resultados...)*

## Resultados
*(Sección en construcción...)*

## Conclusiones
*(Sección en construcción...)*
