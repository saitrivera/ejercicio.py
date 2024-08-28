import pandas as pd

# 1. Crear el DataFrame
data = {'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
        'Edad': [15, 14, 16, 15],
        'Nota': [8.5, 9.0, 7.5, 8.0]}

df = pd.DataFrame(data)

# 2. Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame:")
print(df.head())

# 3. Añadir la columna 'Ciudad'
df['Ciudad'] = ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']

# 4. Mostrar el DataFrame actualizado
print("\nDataFrame actualizado:")
print(df)
