# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:18:08 2024

@author: edi_a
"""

#******************************************************************************
#             APLICACIÓN ANALÍTICA SOBRE PRECIOS DE CASAS
#******************************************************************************

# Importar las librerías
import streamlit as st
import joblib
import numpy as np 
import pandas as pd
from PIL import Image
import sklearn


# Poner título en la página web
st.set_page_config(page_title='Calculo de precios de casas')


# Cargar el modelo desde el archivo
model_filename = 'precios_casas.pkl'
loaded_model = joblib.load(model_filename)
print("Modelo cargado")


# Poner imagen
st.title('TU PRIMERA CASA')
st.image('imagen_casa.jpg',width=500)
st.header("¡Has tu sueño realidad!")
st.subheader("Conoce el precio de tu casa $,$$")
st.text('Llama ya a tu asesor inmobilario, ubícanos en www.midulcecasa.com')



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
if sidebar.button("Calcular precio"):
    
  try:
      lot_area=float(superficie_terreno)
      year_built=float(año_construccion)
      garage_cars=int(numero_garajes)
      if (lot_area<=0 or year_built<=0 or garage_cars<0):
         st.warning('Ingrese un número mayor a cero')
      else:
              new_data={'LotArea':[lot_area],
                         'YearBuilt':[year_built],
                         'GarageCars':[garage_cars]
                         }
              new_data=pd.DataFrame(new_data)

              prediction= loaded_model.predict(new_data)
              print('Ejecutando calculo...')
              st.success(f' PRECIO CALCULADO:  {prediction}')
   
  except ValueError:
     st.error('Ingrese solo números')
 
else:
      st.info(f' EL PRECIO CALCULADO ES: ')     



