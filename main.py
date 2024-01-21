# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:10:53 2024

@author: edi_a
"""

#******************************************************************************
#              APLICACIÓN ANALÍTICA SOBRE PRECIOS DE CASAS
#******************************************************************************

# Importar las librerías
# Instalar las librerías en ‘CMD.exe Prompt 0.1.1’
import streamlit as st
import joblib
import numpy as np 
import pandas as pd
from PIL import Image
import sklearn


# Poner título en la página web
st.set_page_config(page_title='Cotizador de casas')


# Cargar el modelo desde el archivo
model_filename = 'precios_casas.pkl'
loaded_model = joblib.load(model_filename)
print("Modelo cargado")



# Poner imagen
st.title('COTIZADOR DE CASAS')
st.image('imagen_casa.jpg',width=500)
st.header("Has tu sueño realidad...!")
st.subheader('Llama ya a tu asesor inmobilario: MR.HOUSE') #, icon="✅"
st.text('Para mayor información ingresa al código QR') #, icon="ℹ"
st.image('imagen_codigo_qr.jpeg',width=250)


# Poner barra lateral
sidebar = st.sidebar
# Añadir un título a la barra lateral
sidebar.title("Calcula el precio de tu casa")

# Añadir en la barra lateral una celda de entrada de texto
superficie_terreno = sidebar.text_input("Superficie del terreno (m2)", value=0)

# Añadir en la barra lateral una celda de entrada de texto
año_construccion = sidebar.text_input("Año de construcción (aaaa)", value=0)

# Añadir en la barra lateral una barra de deslizamiento para valores numéricos
#numero_garajes = sidebar.slider("Número de garajes para carros", min_value=0, max_value=10, value=0)

# Añadir en la barra lateral una celda de entrada de texto
numero_garajes = sidebar.text_input("Número de garajes para carros", value=0)




# Ingresar los datos
if sidebar.button("Cotizar casa"):
    try:
        
        lot_area=float(superficie_terreno)
        year_built=float(año_construccion)
        garage_cars=int(numero_garajes)
        
        new_data={'LotArea':[lot_area],
                  'YearBuilt':[year_built],
                  'GarageCars':[garage_cars]
                  }
        
        new_data=pd.DataFrame(new_data)
        
        prediction= loaded_model.predict(new_data)
        print('Ejecutando calculo...')
        st.success(f' Cotización de tu casa:  {prediction}')
    
    except ValueError:
        "Error incorrecto de datos"



