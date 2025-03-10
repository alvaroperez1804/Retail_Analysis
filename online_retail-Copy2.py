#!/usr/bin/env python
# coding: utf-8

# # Portfolio Project: Online Retail Exploratory Data Analysis with Python

# ## Overview
# 
# In this project, you will step into the shoes of an entry-level data analyst at an online retail company, helping interpret real-world data to help make a key business decision.

# ## Case Study
# In this project, you will be working with transactional data from an online retail store. The dataset contains information about customer purchases, including product details, quantities, prices, and timestamps. Your task is to explore and analyze this dataset to gain insights into the store's sales trends, customer behavior, and popular products. 
# 
# By conducting exploratory data analysis, you will identify patterns, outliers, and correlations in the data, allowing you to make data-driven decisions and recommendations to optimize the store's operations and improve customer satisfaction. Through visualizations and statistical analysis, you will uncover key trends, such as the busiest sales months, best-selling products, and the store's most valuable customers. Ultimately, this project aims to provide actionable insights that can drive strategic business decisions and enhance the store's overall performance in the competitive online retail market.
# 
# ## Prerequisites
# 
# Before starting this project, you should have some basic knowledge of Python programming and Pandas. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - numpy
# - seaborn
# - matplotlib
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`

# ## Project Objectives
# 1. Describe data to answer key questions to uncover insights
# 2. Gain valuable insights that will help improve online retail performance
# 3. Provide analytic insights and data-driven recommendations

# ## Dataset
# 
# The dataset you will be working with is the "Online Retail" dataset. It contains transactional data of an online retail store from 2010 to 2011. The dataset is available as a .xlsx file named `Online Retail.xlsx`. This data file is already included in the Coursera Jupyter Notebook environment, however if you are working off-platform it can also be downloaded [here](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx).
# 
# The dataset contains the following columns:
# 
# - InvoiceNo: Invoice number of the transaction
# - StockCode: Unique code of the product
# - Description: Description of the product
# - Quantity: Quantity of the product in the transaction
# - InvoiceDate: Date and time of the transaction
# - UnitPrice: Unit price of the product
# - CustomerID: Unique identifier of the customer
# - Country: Country where the transaction occurred

# # Tasks
# 
# You may explore this dataset in any way you would like - however if you'd like some help getting started, here are a few ideas:
# 
# 1. Load the dataset into a Pandas DataFrame and display the first few rows to get an overview of the data.
# 2. Perform data cleaning by handling missing values, if any, and removing any redundant or unnecessary columns.
# 3. Explore the basic statistics of the dataset, including measures of central tendency and dispersion.
# 4. Perform data visualization to gain insights into the dataset. Generate appropriate plots, such as histograms, scatter plots, or bar plots, to visualize different aspects of the data.
# 5. Analyze the sales trends over time. Identify the busiest months and days of the week in terms of sales.
# 6. Explore the top-selling products and countries based on the quantity sold.
# 7. Identify any outliers or anomalies in the dataset and discuss their potential impact on the analysis.
# 8. Draw conclusions and summarize your findings from the exploratory data analysis.

# ## Task 1: Load the Data

# In[1]:



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("Online Retail.xlsx")

df.head(100)
df.shape

print(df.dtypes)                                                                 #verificar si cada columna tiene el el formato correcto

ubicacion = np.where(df.values == "C536379")
print(ubicacion)

print(df.iloc[0,0])

print(df.iloc[141])    #simplemente estoy comprobando que es verdad que el "C536379" si existe en el invoice ID

numero_de_duplicated_rows = df[df.duplicated()]
print("numero de duplicados:", numero_de_duplicated_rows.shape)     #Tenemos 5268 filas duplicadas, vamos a eliminarlas

df = df.drop_duplicates()              #elimine las duplicadas 

numero_de_duplicated_rows = df[df.duplicated()]
print("numero de duplicados:", numero_de_duplicated_rows.shape) 

df.count()    #para saber cuantos valores REALES no NULOS hay en cada columna 

print(df.isnull().sum())

print((135037/536641)*100)        #vemos que el customerId tiene muchos valores nulos mas del 25% son nulos , debemos hacer algo 
#al respecto, en este caso opte por rellenar esos espacios con np.nan

df["CustomerID"] = df["CustomerID"].fillna(np.nan)   #rellenando los valores nulos en customerID por np.nan

df = df.dropna() 
print(df.count())                #eliminando los valores nulos

print(df.isnull().sum())   #confirmando que no hay valores nulos

#df.describe("unitprice","quantity") Esto es un error, para seleccionar columnas se usa el []

print("ver valores atipicos en la tabla:",df[["Quantity","UnitPrice"]].describe())   #nos damos cuenta que hay valores atipicos

indice = df[df["Quantity"] == -80995.000000	 ]     #me da los valores de ese datafram donde quantity es -80995, voy a eliminar esa fila
print(indice)


df = df.drop(df[df["Quantity"] == 80995.000000 ].index)  #siguen habiendo outliers, mejor usamos el metodo IQR para eliminarlos mas adelante
df.describe()

#sns.boxplot(x=df["Quantity"])  #               #graficamos el quantity usand seaborn nos damos cuenta que hay valores atipicos, esto no es bueno cuando vayamos a empezar a hacer calculos de 
#plt.show()#                                        #Me doy cuenta que tiene 5 outliers


Q1 = df["Quantity"].quantile(0.25)
Q3 = df["Quantity"].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5*(IQR)
limite_superior = Q3 + 1.5*(IQR) 
df = df[(df["Quantity"] >= limite_inferior)  & (df["Quantity"] <= limite_superior)]
print("nuevo quantity")
print(df["Quantity"].describe())    #nOTO QUE AUn hay valores en quantity que son negativos, tengo que eliminarlos

df = df[(df["Quantity"] >= 0)]
print("Quantity limpiado 100%")
print(df["Quantity"].describe())

plt.style.use('dark_background')

sns.boxplot(df["UnitPrice"], palette=["#00FFFF", "#FF00FF", "#00FF00", "#FF4500"])

plt.title("Buscando outliers en el UnitPrice", fontsize=16, color='white', fontweight='bold')

plt.show()      #veo muchos outliers debemos eliminarlos   ojo las graficas retrasan la lectura

Q1 = df["UnitPrice"].quantile(0.25)
Q3 = df["UnitPrice"].quantile(0.75)                                                        
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5*(IQR)
limite_superior = Q3 + 1.5*(IQR) 
df = df[(df["UnitPrice"] >= limite_inferior)  & (df["UnitPrice"] <= limite_superior)]
print("nuevos valores sin outliers de UnitPrice")
print(df["UnitPrice"].describe())
descripcion = df.describe()
print(descripcion)

sns.boxplot(df["UnitPrice"])
plt.title("UnitPrice sin outliers")      
plt.show()    #notese que los outliers que aparecen que estuvieran ahi no son significativos, y son outliers de la nueva muestra
print(df["CustomerID"].nunique())   #para saber cuantos clientes tiene la tienda osea cuantos valores unicos hay , ok tiene 4192
print(df["StockCode"].nunique())   #vamos a ver cuantos valores unicos tiene el stockcodem para saber si en verdad el codigo es unico o no, y filtramos el producto que mas se vendio por DESCRIPTION
print(df["StockCode"].count())     #aunque en realidad esto se podia comparar facilemente 
mas_vendidos = df["StockCode"].value_counts().head(15)  #vamos a ver cuantas veces se repite cada producto para ver cuales son los mas vendidos
print(mas_vendidos.head(15))
print("DIAGRAMA DE BARRAS PARA LOS PRODUCTOS MAS VENDIDOS")
df["ShortDescription"] = df["Description"].apply(lambda x: ' '.join(str(x).split()[:3]))
mas_vendidos = df["StockCode"].value_counts().head(15).reset_index()
mas_vendidos.columns = ["StockCode", "CantidadVendida"]

# Unimos con la descripción corta
mas_vendidos = mas_vendidos.merge(df[["StockCode", "ShortDescription"]].drop_duplicates(), on="StockCode", how="left")

# Graficamos usando la descripción corta en el eje X
plt.figure(figsize=(12,8))
plt.bar(mas_vendidos["ShortDescription"], mas_vendidos["CantidadVendida"], color="blue")
plt.xlabel("Producto (Descripción Corta)")
plt.ylabel("Cantidad Vendida")
plt.title("Top 15 Productos Más Vendidos")
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.show()

print(df["Country"].value_counts().head(15))
paises = df["Country"].value_counts().head(15)
plt.figure(figsize=(12,8))
paises.plot(kind="bar",color = "blue")
plt.title("paises mas vendidos")
plt.ylabel("Cantidad")
plt.xlabel("Stockcode", fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.show()    #ya tenemos la grafica de los paises con mas ventas, deifinitivamente UK es el que msa clientes tiene
#print(df["InvoiceDate"].sort_values(ascending=False).head(10))
#print(df["InvoiceDate"].sort_values(ascending=False).tail(10))   #NOS DAMOS CUENTA QUE LAS FECHAS VAN DE DEC DE 2010 HASTA DEC DE 2011
#como podemos representar en que meses se vendio mas? supongo que un histograma
print(df["InvoiceDate"].dtype)
df["month"] = df["InvoiceDate"].dt.month  #se crea para sacar solo el mes de esa clase
#print(df["month"].head(5))
print("veces que cada mes se repite")
meses = df["month"].value_counts()
print(meses)
# para darle nombre a las columnas se usa el .columns 
#queria darle nombre a las columnas para que se graficaran porque me piden mostrar que es lo que voy a graficar en cada eje, y para darle nombre a las columnas primero tienen que existir columnas y para que existan debe haber un datafrme
#vamos a graficar los meses usando el metodo predeterminado
# Convierte la Serie en DataFrame
import calendar
meses = meses.reset_index()   #convertimos la serie en un dataframe 
meses.columns = ["Meses","numero_de_ventas"]
meses["Meses"] = meses["Meses"].apply(lambda x: calendar.month_name[x])    #se usa para que los meses en vez de ser numeros sean nombre
plt.figure(figsize=(10,6))
plt.bar(meses["Meses"],meses["numero_de_ventas"])
plt.xlabel("Meses")
plt.ylabel("# VENTAS")
plt.xticks(rotation = 45)
plt.show()

#los clientes que mas compraron
clientes_masmas = df["CustomerID"].value_counts().reset_index().head(15)
clientes_masmas.columns = ["Cliente","numero_de_compras"]
clientes_masmas["Cliente"] = clientes_masmas["Cliente"].astype(str)
plt.figure(figsize=(10,6))
plt.bar(clientes_masmas["Cliente"],clientes_masmas["numero_de_compras"])
plt.xlabel("Cliente")
plt.ylabel("# compras")
plt.title("Numero de compras por clienteID")
plt.xticks(rotation = 45)
plt.show()

#vamos a hacer las correlaciones
df["month"] = df["InvoiceDate"].dt.month
df_analisis_corre = df[["Quantity","UnitPrice","CustomerID","month"]]   # Usa df[["columna"]] si necesitas que el resultado siga siendo un DataFrame.
print(df_analisis_corre.corr())   


plt.scatter(df['UnitPrice'], df['Quantity'])
plt.xlabel('UnitPrice')
plt.ylabel('Quantity')
plt.title('Scatter plot de UnitPrice vs Quantity')
plt.show()