Investigación: Limpieza y consolidación de datos con Pandas
1. Función rename()

La función rename() de Pandas se utiliza para cambiar el nombre de las columnas o índices de un DataFrame.

Es útil cuando diferentes archivos tienen nombres de columnas diferentes para representar el mismo tipo de información. Al cambiar los nombres, se puede lograr que todos los archivos tengan una estructura uniforme antes de consolidarlos.

Ejemplo:
df = df.rename(columns={
    "Nombre": "nombre",
    "Precio": "precio"
})

En este ejemplo, la columna Nombre pasa a llamarse nombre y la columna Precio pasa a llamarse precio.

2. Función drop_duplicates()

La función drop_duplicates() de Pandas sirve para eliminar filas que están repetidas dentro de un DataFrame.

Los datos duplicados pueden provocar que la información se cuente más de una vez y afectar los resultados del análisis. Por esta razón, eliminar duplicados es una parte importante de la limpieza de datos.

Ejemplo:
df = df.drop_duplicates()

También podemos conocer cuántas filas había antes y después:

filas_antes = len(df)

df = df.drop_duplicates()

filas_despues = len(df)

print("Filas antes:", filas_antes)
print("Filas después:", filas_despues)

La diferencia entre las dos cantidades permite conocer cuántas filas duplicadas fueron eliminadas.

3. Función isnull().sum()

La función isnull() permite identificar los valores que están vacíos o son NaN dentro de un DataFrame.

Al combinarla con sum(), podemos contar cuántos valores vacíos existen en cada columna.

Ejemplo:
df.isnull().sum()

El resultado muestra la cantidad de valores vacíos que tiene cada columna.

Por ejemplo:

producto     0
cantidad     2
precio       1
vendedor     0

Esto significa que cantidad tiene 2 valores vacíos y precio tiene 1.

Esta función permite identificar qué columnas necesitan ser tratadas durante el proceso de limpieza.

4. Función fillna()

La función fillna() de Pandas sirve para reemplazar valores vacíos o NaN por un valor determinado.

El valor utilizado depende del tipo de información de la columna y de lo que tenga sentido para los datos.

Ejemplo con un promedio:
df["precio"] = df["precio"].fillna(df["precio"].mean())

En este caso, los valores vacíos de la columna precio se reemplazan por el promedio de los precios existentes.

Ejemplo con texto:
df["vendedor"] = df["vendedor"].fillna("Desconocido")

En este caso, los valores vacíos de la columna vendedor se reemplazan por "Desconocido".

Por lo tanto, antes de utilizar fillna() es importante analizar qué representa cada columna y elegir un valor adecuado para reemplazar los datos faltantes.

5. Importancia de estas funciones en la limpieza de datos

Estas funciones permiten preparar los datos antes de realizar un análisis:

rename() → permite unificar los nombres de las columnas.
drop_duplicates() → elimina registros repetidos.
isnull().sum() → permite detectar y contar valores vacíos.
fillna() → permite reemplazar los valores vacíos por valores adecuados.

Estas herramientas ayudan a obtener un conjunto de datos más organizado y consistente para realizar posteriormente el análisis.