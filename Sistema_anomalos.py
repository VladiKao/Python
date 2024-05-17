#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import xlrd 
from openpyxl import load_workbook 
import matplotlib.pyplot as plt
import math
import numpy as np
#leer excel, hoja stuck
fileName = 'Pruebas de BD.xlsx'
df_bd = pd.read_excel(fileName,sheet_name='LogNodo_12052021 (secciones)', usecols=["id","Hora", "temperatura"])
df = pd.DataFrame(df_bd)
#DATOS GENERALES
hora_ini = df['Hora'].head(1).item()
hora_fin = df['Hora'].values[25757]
tiempo = [hora_ini, hora_fin]
id_ini = df['id'].head(1).item()
id_fin = df['id'].values[25757]
id_limite = [id_ini, id_fin]
size_id = len(df['id'])
intervalo = '00:03' 

lapso = 3
size = len(df['Hora']) #Cantidad de datos a evaluar

print("El primer dato empieza en ", end="")
print(hora_ini, end="")
print(" y termina en: ", end="")
print(hora_fin)
print("Hay un total de datos de: ", end="")
print(size)
#print(df)
print(id_ini)
print(id_fin)


# In[2]:


from datetime import datetime
date = df['Hora'].head(1).item()
final = df.iloc[25760,1]#df['Hora'].tail(1).item()
formatted_date=date.strftime('%H:%M:%S')

print(formatted_date)
#print(final)

#print(df)
valorfinal= df['Hora'].values[25757]
print(valorfinal)


# In[2]:


#graficar    
      
import matplotlib.pyplot as plt
df_bd[['temperatura', 'Hora']].plot()
plt.show()


# In[3]:


pendientes = [0.0]
for i in range(size_id):
    if i > 0:
        primerdato = df['temperatura'][i]
        datoanterior = df['temperatura'][i - 1]
        m = abs((primerdato - datoanterior)//lapso)
        arcT = math.atan(m)
        grd = math.degrees(arcT)
        pendientes.append(grd)
        
    else:
        None
print(pendientes)


# In[ ]:





# In[4]:


#codigo por si se deasea leer todos los datos
print(size_id)
for i in range(size_id):
    intervalo = df['Hora'][i] 
   
    
    if i > 1 and i < 25759:
        if pendientes[i] >= 1:
            if (df['temperatura'][i] - df['temperatura'][i - 1]) >= 0 and (df['temperatura'][i] - df['temperatura'][i - 1]) < 1:
                None
            else:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Outlier")
        elif pendientes[i] >= 2 and pendientes[i] <= 44:
            if pendientes[i + 1] == pendientes[i + 2] == pendientes[i + 3] == pendientes[i + 4]:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Step")
            else:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Peak")
        elif pendientes[i] <= 45:
            if pendientes[i + 1] == pendientes[i + 2] == pendientes[i + 3] == pendientes[i + 4]:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Step Extreme")
            else:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Extreme")
        else:
            None
    else:
        None


# In[8]:


for i in range(size):
    intervalo = df['Hora'][i] 
    #intervalo2 = np.power(df['id'][i] dtype=np.float64)
    #intervalo3 = df['id'][i] dtype=np.float64
    if i > 0 and i < 25759:
        
        if pendientes[i] <= 45:
            if (df['temperatura'][i] - df['temperatura'][i - 1]) >= 0 and (df['temperatura'][i] - df['temperatura'][i - 1]) < 1:
                None
            else:
                print("Dato con id " + str(intervalo) + ": ", end="")
                print("Outlier")
        elif pendientes[i] <= 86:
            if pendientes[i + 1] == pendientes[i + 2] == pendientes[i + 3] == pendientes[i + 4]:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Step")
            else:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Peak")
        elif pendientes[i] >= 88:
            if pendientes[i + 1] == pendientes[i + 2] == pendientes[i + 3] == pendientes[i + 4]:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Step Extreme")
            else:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Extreme")
        else:
            None
    else:
        None


# In[5]:


contador=0
for i in range(size):
    if i > 0:
        if pendientes[i] >= 45:
            if (df['temperatura'][i] - df['temperatura'][i - 1]) > -1 and (df['temperatura'][i] - df['temperatura'][i - 1]) < 1:
                None
            else:
                if pendientes[i] == pendientes[i + 2] == pendientes[i + 4] == pendientes[i + 6]:
                    contador+=1
                else:
                    None
        else:
            None
    else:
        None
        
if contador >= 3:
    print("Noise detectado")
else:
    print("no es un noisy")


# In[6]:


#este bloque de codigo es por si el cliente desea unos valores exactos
print("Hola este es un software realizado para graficar datos anomalos e identificarlos")
print("Los datos totales son ", end="")
print(size)
nuevos_datos= input("Cuantos desea leer?:")
primer_num = int(input ("Escriba el primer numero a leer:"))
ultimo_num = int(input ("Escriba el ultimo numero a leer"))

for i in range(size):        
    intervalo = df['Hora'][i] 
    if i > primer_num and i < ultimo_num:
        if pendientes[i] >= 1:
            if (df['temperatura'][i] - df['temperatura'][i - 1]) >= 0 and (df['temperatura'][i] - df['temperatura'][i - 1]) < 1:
                None
            else:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Outlier")
        elif pendientes[i] >= 2 and pendientes[i] <= 44:
            if pendientes[i + 1] == pendientes[i + 2] == pendientes[i + 3] == pendientes[i + 4]:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Step")
            else:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Peak")
        elif pendientes[i] <= 45:
            if pendientes[i + 1] == pendientes[i + 2] == pendientes[i + 3] == pendientes[i + 4]:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Step Extreme")
            else:
                print("Dato sensado en el momento " + str(intervalo) + ": ", end="")
                print("Extreme")
        else:
            None
    else:
        None


# In[ ]:





# In[ ]:




