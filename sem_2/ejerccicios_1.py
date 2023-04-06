import pandas as pd
import numpy as np


data = pd.read_csv('data/global_internet_users_Final.csv')

#mostrar los primeros 10 registros
data.head(10)
#muestra dimensiones
data.shape
#muestra información sobre los tipos de datos y valores faltantes en cada columna
data.info()
#selecciona una columna de interes
data['Year']
#filtrar por pais
mask = (data['Entity'] == 'Colombia') & (data['No. of Internet Users'] > 0)
data[mask]
#ordernar por una columna
data.sort_values(by='No. of Internet Users', ascending=False)

#detectar filas duplicadas
data.duplicated().sum()
#detectar valores nulos
data.isnull().sum()
#detectar valores faltantes
data.isna().sum()
#renombrar columnas
data.rename(columns={'No. of Internet Users': 'Internet Users'}, inplace=True)
#crear nuevas columnas a partir de otras, calculando la poblacion total con base en el porcentaje de usuarios de internet
data['Total Population'] = round(data['Internet Users'] / data['Internet Users(%)'] * 100, 0).astype(int)

