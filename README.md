# Online Retail Exploratory Data Analysis
Este proyecto analiza datos transaccionales de una tienda de retail en línea. A través de técnicas de análisis exploratorio de datos (EDA), se buscan patrones en las ventas, comportamiento de los clientes y productos más populares. El objetivo es obtener insights que puedan ayudar a mejorar la estrategia comercial del negocio.
📂 Dataset

El análisis se basa en el conjunto de datos "Online Retail", que contiene transacciones de una tienda de comercio electrónico desde 2010 hasta 2011. Las principales columnas del dataset son:

InvoiceNo: Número de factura.

StockCode: Código único del producto.

Description: Descripción del producto.

Quantity: Cantidad comprada.

InvoiceDate: Fecha y hora de la transacción.

UnitPrice: Precio unitario del producto.

CustomerID: Identificación del cliente.

Country: País de la compra.

📥 Puedes descargar el dataset desde: https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx

🛠️ Instalación y Requisitos

Para ejecutar el análisis, necesitas instalar las siguientes librerías de Python:

pip install pandas numpy seaborn matplotlib

También puedes instalarlas dentro de un notebook ejecutando:

!pip install pandas numpy seaborn matplotlib

🔍 Análisis Realizado

Se han realizado las siguientes tareas de análisis y limpieza de datos:

Carga del Dataset: Lectura del archivo y visualización de las primeras filas.

Limpieza de Datos: Eliminación de valores nulos y duplicados.

Detección y tratamiento de outliers: Se usó el método IQR para eliminar valores atípicos en Quantity y UnitPrice.

Análisis de ventas:

Identificación de los productos más vendidos.

Identificación de los países con más compras.

Análisis de estacionalidad en las ventas por mes.

Identificación de los clientes más frecuentes.

Visualización de datos: Gráficos de barras, boxplots y scatter plots para entender mejor las tendencias.

📊 Principales Hallazgos

Algunos de los insights obtenidos en este análisis son:

📈 El mes con mayor volumen de ventas fue Noviembre, lo que indica una fuerte tendencia de compras en la temporada de BlackFriday, y la temporada navideña.

🛒 El producto más vendido fue 85123A con la descripcion WHITE HANGING HEART, con un alto número de transacciones.

🌍 El país con más ventas fue el Reino Unido, lo que indica que la mayoría de los clientes son locales.

💰 Existen clientes que compran de forma recurrente, lo que puede ser aprovechado con estrategias de fidelización.

📷 Visualizaciones

Algunas de las visualizaciones generadas incluyen:

Productos más vendidos:
![Productos mas vendidos](https://github.com/alvaroperez1804/Retail_Analysis/blob/main/productos_mas_vendidos.png)
Ventas por país:

Ventas mensuales:

(Si deseas incluir imágenes en GitHub, súbelas a tu repositorio y coloca la URL correcta en ruta_a_la_imagenX.png.)

📌 Conclusión

Este análisis proporciona información valiosa sobre las tendencias de compra en una tienda online. Los hallazgos pueden ser utilizados para mejorar la gestión del inventario, optimizar campañas de marketing y aumentar la rentabilidad del negocio.

🔹 Próximos pasos: Se podría extender el análisis con modelos de predicción de demanda o segmentación de clientes usando técnicas de Machine Learning.

📜 Autor

Proyecto desarrollado por @alvaroperez1804. Puedes contactarme en LinkedIn o explorar más proyectos en mi GitHub.
