# Proyecto de Clasificación de Sitios Web de Phishing

## Aplicación
Link a la aplicación: https://juan-angel-cepeda-phishing-dataset-app-m9djx5.streamlit.app/

## Descripción

Este proyecto tiene como objetivo clasificar los sitios web como seguros o inseguros, donde los sitios seguros son aquellos que no representan riesgo de phishing, y los sitios inseguros tienen una alta probabilidad de ser sitios de phishing. El proyecto utiliza tres modelos de aprendizaje automático - "Support Vector Machine", "Random Forest Classifier" y "Extra Trees" - los cuales se entrenan utilizando un conjunto de datos de sitios web de phishing para su clasificación.

## Objetivo

El objetivo de este proyecto es desplegar una aplicación funcional utilizando Streamlit que pueda clasificar los sitios web como seguros o inseguros utilizando tres modelos diferentes: "Support Vector Machine", "Random Forest Classifier" y "Extra Trees". La aplicación debe obtener los datos necesarios para las características de predicción casi automáticamente mediante web scraping pasando como parametro el link de la pagina. En este caso, las características solicitadas al usuarion fueron aquellas en donde se neceistaba el API de Alexa y RankWebsites.

## Conjunto de datos

El conjunto de datos utilizado en este proyecto contiene 11.055 muestras y 30 características. Una descripción de las características se puede encontrar en `docs/Phishing Websites Features.docx`, junto con el conjunto de datos en sí.

## Tecnologías

Se utilizaron las siguientes tecnologías en este proyecto:

- Python
- Scikit-learn
- Streamlit
- Pandas
- NumPy
- Requests
- BeautifulSoup
- Sockets
- DNS
- Whois
- Selenium

## Conclusiones

Los tres modelos de aprendizaje automático alcanzaron métricas superiores al 85% en exactitud, puntuación F1, precisión, recuperación y AUC. Sin embargo, durante las pruebas con enlaces reales, se observó que el modelo Random Forest Classifier siempre daba resultados incorrectos con sitios web legítimos. Esto sugiere un error en el proceso de entrenamiento que no fue detectado a tiempo. Por otro lado, los otros dos modelos tuvieron un buen desempeño en las pruebas con sitios web legítimos, clasificándolos correctamente, mientras que los sitios maliciosos fallaron en las pruebas de web scraping, ya que carecían de sellos de tiempo, no estaban registrados en DNS, o bloqueaban la recuperación de datos necesarios para el análisis.

En un proyecto relacionado en Kaggle, se utilizaron 10 características, y las métricas de los modelos oscilaron entre el 75% y el 90%. El proyecto se puede encontrar en https://www.kaggle.com/code/emilia11/analysisphishingdataset.

