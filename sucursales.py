import glob
import pandas as pd

# --------------------------------------------
# PARTE 1: Buscar y leer los archivos de sucursales
# --------------------------------------------
# Usamos "sucursal_*" para NO leer titanic_limpio.csv
archivos_csv = glob.glob("sucursal_*.csv")
archivos_xlsx = glob.glob("sucursal_*.xlsx")

lista_informes = []

for archivo in archivos_csv:
  df = pd.read_csv(archivo)
  lista_informes.append(df)
  print(f"Leído: {archivo} - {len(df)} filas")

for archivo in archivos_xlsx:
  df = pd.read_excel(archivo, engine='openpyxl')
  lista_informes.append(df)
  print(f"Leído: {archivo} - {len(df)} filas")


# --------------------------------------------
# PARTE 2 y 3: Identificar y Renombrar columnas
# --------------------------------------------
# Mostramos las columnas de cada archivo para detectar cuál tiene nombres diferentes
print("\n--- Columnas de cada archivo ---")
for i, df in enumerate(lista_informes):
  print(f"Archivo {i+1}: {list(df.columns)}")

# Reemplaza 'columna_diferente' y 'columna_correcta' con los nombres reales
# que veas en la terminal al ejecutar el bloque anterior:
for i, df in enumerate(lista_informes):
  if 'columna_diferente' in df.columns:
    lista_informes[i] = df.rename(
        columns={'columna_diferente': 'columna_correcta'}
    )

# Consolidamos las tablas corregidas
df_consolidado = pd.concat(lista_informes, ignore_index=True)
print(f"\nTotal columnas consolidadas: {len(df_consolidado.columns)}")


# --------------------------------------------
# PARTE 4: Limpieza de datos
# --------------------------------------------

# 4a. Eliminar filas duplicadas
filas_antes = len(df_consolidado)
df_consolidado = df_consolidado.drop_duplicates()
filas_despues = len(df_consolidado)

print(
    f"\nFilas antes: {filas_antes} | Filas después de eliminar duplicados:"
    f" {filas_despues}"
)

# 4b. Explorar valores vacíos
print("\nValores vacíos por columna:")
print(df_consolidado.isnull().sum())

# 4c. Rellenar valores vacíos con fillna()
for col in df_consolidado.columns:
  if df_consolidado[col].dtype in ['float64', 'int64']:
    df_consolidado[col] = df_consolidado[col].fillna(0)
  else:
    df_consolidado[col] = df_consolidado[col].fillna('Sin Registro')


# --------------------------------------------
# PARTE 5: Guardar el resultado
# --------------------------------------------
df_consolidado.to_excel('consolidado_limpio.xlsx', index=False)
print("\n¡Archivo 'consolidado_limpio.xlsx' generado con éxito!")