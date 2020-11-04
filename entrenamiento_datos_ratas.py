#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:43:43 2019

@author: yan
"""
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
plt.ion() 
import re
from scipy import stats

#%%-- Variables 
sujetos = 10 
sesiones = 10
total_PRE_Ax = np.zeros((sujetos, sesiones))
total_DURANTE_Ax = np.zeros((sujetos, sesiones))

total_PRE_A = np.zeros((sujetos, sesiones))
total_DURANTE_A = np.zeros((sujetos, sesiones))

total_PRE_x = np.zeros((sujetos, sesiones))
total_DURANTE_x = np.zeros((sujetos, sesiones))

total_PRE_A2x = np.zeros((sujetos, sesiones))
total_DURANTE_A2x = np.zeros((sujetos, sesiones))

total_PRE_A4x = np.zeros((sujetos, sesiones))
total_DURANTE_A4x = np.zeros((sujetos, sesiones))

total_PRE_A8x = np.zeros((sujetos, sesiones))
total_DURANTE_A8x = np.zeros((sujetos, sesiones))


#%%
def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_Ax = sorted_aphanumeric(os.listdir("/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_Ax/"))


k = 0
l = 0
for elemento in contenido_Ax:
    ruta = "/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_Ax/"
    archivo = ruta + elemento
    print(archivo)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                       na_values=[' '])
    
    datos_PRE = pd.DataFrame(datos[34:37][:])
    datos_PRE.columns=['Numero','Dato']
    concatena_datos_PRE = np.sum(datos_PRE)
    suma_datos_PRE = concatena_datos_PRE['Dato']
    
    
    datos_DURANTE = pd.DataFrame(datos[38:41][:])
    datos_DURANTE.columns=['Numero','Dato']
    concatena_datos_DURANTE = np.sum(datos_DURANTE)
    suma_datos_DURANTE = concatena_datos_DURANTE['Dato']
    
    j = 0
    h = 0
    array_PRE = np.arange(44)
    array_DURANTE = np.arange(44)
    for i in suma_datos_PRE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_PRE[j] = float(i)
            j += 1
    
    for i in suma_datos_DURANTE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_DURANTE[h] = float(i)
            h += 1
    
    total_PRE_Ax[k][l] = sum(array_PRE)
    total_DURANTE_Ax[k][l] = sum(array_DURANTE)
    
    l += 1
    if l == 10:
        k +=1
        l = 0

#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_A = sorted_aphanumeric(os.listdir("/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A/"))

k = 0
l = 0
for elemento in contenido_A:
    ruta = "/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A/"
    archivo = ruta + elemento
    print(archivo)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                      na_values=[' '])
    
    datos_PRE = pd.DataFrame(datos[34:37][:])
    datos_PRE.columns=['Numero','Dato']
    concatena_datos_PRE = np.sum(datos_PRE)
    suma_datos_PRE = concatena_datos_PRE['Dato']
    
    datos_DURANTE = pd.DataFrame(datos[38:41][:])
    datos_DURANTE.columns=['Numero','Dato']
    concatena_datos_DURANTE = np.sum(datos_DURANTE)
    suma_datos_DURANTE = concatena_datos_DURANTE['Dato']
    
    j = 0
    h = 0
    array_PRE = np.arange(44)
    array_DURANTE = np.arange(44)
    for i in suma_datos_PRE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_PRE[j] = float(i)
            j += 1
    
    for i in suma_datos_DURANTE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_DURANTE[h] = float(i)
            h += 1
    
    total_PRE_A[k][l] = sum(array_PRE)
    total_DURANTE_A[k][l] = sum(array_DURANTE)
    
    l += 1
    if l == 10:
        k +=1
        l = 0


#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_x = sorted_aphanumeric(os.listdir("/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_x/"))

k = 0
l = 0
for elemento in contenido_x:
    ruta = "/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_x/"
    archivo = ruta + elemento
    print(archivo)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                      na_values=[' '])
    
    datos_PRE = pd.DataFrame(datos[34:37][:])
    datos_PRE.columns=['Numero','Dato']
    concatena_datos_PRE = np.sum(datos_PRE)
    suma_datos_PRE = concatena_datos_PRE['Dato']
    
    datos_DURANTE = pd.DataFrame(datos[38:41][:])
    datos_DURANTE.columns=['Numero','Dato']
    concatena_datos_DURANTE = np.sum(datos_DURANTE)
    suma_datos_DURANTE = concatena_datos_DURANTE['Dato']
    
    j = 0
    h = 0
    array_PRE = np.arange(44)
    array_DURANTE = np.arange(44)
    for i in suma_datos_PRE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_PRE[j] = float(i)
            j += 1
    
    for i in suma_datos_DURANTE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_DURANTE[h] = float(i)
            h += 1
    
    total_PRE_x[k][l] = sum(array_PRE)
    total_DURANTE_x[k][l] = sum(array_DURANTE)
    
    l += 1
    if l == 10:
        k +=1
        l = 0


#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_A2x = sorted_aphanumeric(os.listdir("/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A(2)x/"))

k = 0
l = 0
for elemento in contenido_A2x:
    ruta = "/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A(2)x/"
    archivo = ruta + elemento
    print(archivo)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                      na_values=[' '])
    
    datos_PRE = pd.DataFrame(datos[34:37][:])
    datos_PRE.columns=['Numero','Dato']
    concatena_datos_PRE = np.sum(datos_PRE)
    suma_datos_PRE = concatena_datos_PRE['Dato']
    
    datos_DURANTE = pd.DataFrame(datos[38:41][:])
    datos_DURANTE.columns=['Numero','Dato']
    concatena_datos_DURANTE = np.sum(datos_DURANTE)
    suma_datos_DURANTE = concatena_datos_DURANTE['Dato']
    
    j = 0
    h = 0
    array_PRE = np.arange(44)
    array_DURANTE = np.arange(44)
    for i in suma_datos_PRE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_PRE[j] = float(i)
            j += 1
    
    for i in suma_datos_DURANTE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_DURANTE[h] = float(i)
            h += 1
    
    total_PRE_A2x[k][l] = sum(array_PRE)
    total_DURANTE_A2x[k][l] = sum(array_DURANTE)
    
    l += 1
    if l == 10:
        k +=1
        l = 0



#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_A4x = sorted_aphanumeric(os.listdir("/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A(4)x/"))

k = 0
l = 0
for elemento in contenido_A4x:
    ruta = "/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A(4)x/"
    archivo = ruta + elemento
    print(archivo)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                      na_values=[' '])
    
    datos_PRE = pd.DataFrame(datos[34:37][:])
    datos_PRE.columns=['Numero','Dato']
    concatena_datos_PRE = np.sum(datos_PRE)
    suma_datos_PRE = concatena_datos_PRE['Dato']
    
    datos_DURANTE = pd.DataFrame(datos[38:41][:])
    datos_DURANTE.columns=['Numero','Dato']
    concatena_datos_DURANTE = np.sum(datos_DURANTE)
    suma_datos_DURANTE = concatena_datos_DURANTE['Dato']
    
    j = 0
    h = 0
    array_PRE = np.arange(44)
    array_DURANTE = np.arange(44)
    for i in suma_datos_PRE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_PRE[j] = float(i)
            j += 1
    
    for i in suma_datos_DURANTE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_DURANTE[h] = float(i)
            h += 1
    
    total_PRE_A4x[k][l] = sum(array_PRE)
    total_DURANTE_A4x[k][l] = sum(array_DURANTE)
    
    l += 1
    if l == 10:
        k +=1
        l = 0
        

#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_A8x = sorted_aphanumeric(os.listdir("/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A(8)x/"))

k = 0
l = 0
for elemento in contenido_A8x:
    ruta = "/home/yan/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A(8)x/"
    archivo = ruta + elemento
    print(archivo)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                      na_values=[' '])
    
    datos_PRE = pd.DataFrame(datos[34:37][:])
    datos_PRE.columns=['Numero','Dato']
    concatena_datos_PRE = np.sum(datos_PRE)
    suma_datos_PRE = concatena_datos_PRE['Dato']
    
    datos_DURANTE = pd.DataFrame(datos[38:41][:])
    datos_DURANTE.columns=['Numero','Dato']
    concatena_datos_DURANTE = np.sum(datos_DURANTE)
    suma_datos_DURANTE = concatena_datos_DURANTE['Dato']
    
    j = 0
    h = 0
    array_PRE = np.arange(44)
    array_DURANTE = np.arange(44)
    for i in suma_datos_PRE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_PRE[j] = float(i)
            j += 1
    
    for i in suma_datos_DURANTE:
        if i == ' ' or i == '.':
            array = i
        else:
            array_DURANTE[h] = float(i)
            h += 1
    
    total_PRE_A8x[k][l] = sum(array_PRE)
    total_DURANTE_A8x[k][l] = sum(array_DURANTE)
    
    l += 1
    if l == 10:
        k +=1
        l = 0
        
        
#%%----Análisis de datos----------------------------------------
        
print(total_PRE_A2x)
print(total_DURANTE_A2x)
#####################---- Ax -------############################ 
################################################################       
PRE_Ax_promedio = np.sum(total_PRE_Ax, axis=0)/10
error_PRE_Ax = stats.sem(total_PRE_Ax, axis=0, ddof=0) 

DURANTE_Ax_promedio = np.sum(total_DURANTE_Ax, axis=0)/10
error_DURANTE_Ax = stats.sem(total_DURANTE_Ax, axis=0, ddof=0) 

elevacion_Ax = total_DURANTE_Ax - total_PRE_Ax
elevacion_Ax_promedio = np.sum(elevacion_Ax, axis=0)/10
error_elevacion_Ax = stats.sem(elevacion_Ax, axis=0, ddof=0)       

#####################---- A -------############################# 
################################################################ 
PRE_A_promedio = np.sum(total_PRE_A, axis=0)/10
error_PRE_A = stats.sem(total_PRE_A, axis=0, ddof=0)

DURANTE_A_promedio = np.sum(total_DURANTE_A, axis=0)/10
error_DURANTE_A = stats.sem(total_DURANTE_A, axis=0, ddof=0)

elevacion_A = total_DURANTE_A - total_PRE_A
elevacion_A_promedio = np.sum(elevacion_A, axis=0)/10
error_elevacion_A = stats.sem(elevacion_A, axis=0, ddof=0) 

#####################---- x -------############################# 
################################################################ 
PRE_x_promedio = np.sum(total_PRE_x, axis=0)/10
error_PRE_x = stats.sem(total_PRE_x, axis=0, ddof=0)

DURANTE_x_promedio = np.sum(total_DURANTE_x, axis=0)/10
error_DURANTE_x = stats.sem(total_DURANTE_x, axis=0, ddof=0) 

elevacion_x = total_DURANTE_x - total_PRE_x
elevacion_x_promedio = np.sum(elevacion_x, axis=0)/10
error_elevacion_x = stats.sem(elevacion_x, axis=0, ddof=0)

#####################---- A(2)x ---############################# 
################################################################ 
PRE_A2x_promedio = np.sum(total_PRE_A2x, axis=0)/10
error_PRE_A2x = stats.sem(total_PRE_A2x, axis=0, ddof=0)

DURANTE_A2x_promedio = np.sum(total_DURANTE_A2x, axis=0)/10
error_DURANTE_A2x = stats.sem(total_DURANTE_A2x, axis=0, ddof=0) 

elevacion_A2x = total_DURANTE_A2x - total_PRE_A2x
elevacion_A2x_promedio = np.sum(elevacion_A2x, axis=0)/10
error_elevacion_A2x = stats.sem(elevacion_A2x, axis=0, ddof=0)

#####################---- A(4)x ---############################# 
################################################################ 
PRE_A4x_promedio = np.sum(total_PRE_A4x, axis=0)/10
error_PRE_A4x = stats.sem(total_PRE_A4x, axis=0, ddof=0)

DURANTE_A4x_promedio = np.sum(total_DURANTE_A4x, axis=0)/10
error_DURANTE_A4x = stats.sem(total_DURANTE_A4x, axis=0, ddof=0) 

elevacion_A4x = total_DURANTE_A4x - total_PRE_A4x
elevacion_A4x_promedio = np.sum(elevacion_A4x, axis=0)/10
error_elevacion_A4x = stats.sem(elevacion_A4x, axis=0, ddof=0)

#####################---- A(8)x ---############################# 
################################################################ 
PRE_A8x_promedio = np.sum(total_PRE_A8x, axis=0)/10
error_PRE_A8x = stats.sem(total_PRE_A8x, axis=0, ddof=0)

DURANTE_A8x_promedio = np.sum(total_DURANTE_A8x, axis=0)/10
error_DURANTE_A8x = stats.sem(total_DURANTE_A8x, axis=0, ddof=0) 

elevacion_A8x = total_DURANTE_A8x - total_PRE_A8x
elevacion_A8x_promedio = np.sum(elevacion_A8x, axis=0)/10
error_elevacion_A8x = stats.sem(elevacion_A8x, axis=0, ddof=0)

#%%------Gráficos-------------------------------------------------

x = np.arange(.99, 10.01)
fig, ax = plt.subplots()
plt.subplot(231)  
plt.errorbar(x, PRE_Ax_promedio, yerr=error_PRE_Ax,  marker='o', color = 'k', linestyle='--', label='PRE ECs')
plt.errorbar(x, DURANTE_Ax_promedio, yerr=error_DURANTE_Ax,  marker='s', color = 'k', label='DURANTE ECs')
plt.errorbar(x, elevacion_Ax_promedio, yerr=error_elevacion_Ax,  marker='^', color = 'k', linestyle=':', label='ELEVACION')
plt.ylim(-5,75)
plt.xlim(0,11)
plt.title(u'Ax+', fontsize = 20)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
#ax.spines['left'].set_color('none')
#ax.set_yticklabels([])
plt.yticks(fontsize=20)
ax.yaxis.set_ticks_position('none')


plt.subplot(232)  
plt.errorbar(x, PRE_A_promedio, yerr=error_PRE_A,  marker='o', color = 'k', linestyle='--', label='PRE ECs')
plt.errorbar(x, DURANTE_A_promedio, yerr=error_DURANTE_A,  marker='s', color = 'k', label='DURANTE ECs')
plt.errorbar(x, elevacion_A_promedio, yerr=error_elevacion_A,  marker='^', color = 'k', linestyle=':', label='ELEVACION')
plt.ylim(-5,75)
plt.xlim(0,11)
plt.title(u'A+', fontsize = 20) 
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.spines['left'].set_color('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')


plt.subplot(233)
plt.errorbar(x, PRE_x_promedio, yerr=error_PRE_x,  marker='o', color = 'k', linestyle='--', label='PRE ECs')
plt.errorbar(x, DURANTE_x_promedio, yerr=error_DURANTE_x,  marker='s', color = 'k', label='DURANTE ECs')
plt.errorbar(x, elevacion_x_promedio, yerr=error_elevacion_x,  marker='^', color = 'k', linestyle=':', label='ELEVACION')
plt.ylim(-5,75)
plt.xlim(0,11)
plt.title(u'x+', fontsize = 20)
plt.legend(fontsize = 15) 
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.spines['left'].set_color('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')



plt.subplot(234)
plt.errorbar(x, PRE_A2x_promedio, yerr=error_PRE_A2x,  marker='o', color = 'k', linestyle='--', label='PRE ECs')
plt.errorbar(x, DURANTE_A2x_promedio, yerr=error_DURANTE_A2x,  marker='s', color = 'k', label='DURANTE ECs')
plt.errorbar(x, elevacion_A2x_promedio, yerr=error_elevacion_A2x,  marker='^', color = 'k', linestyle=':', label='ELEVACION')
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
plt.ylim(-5,75)
plt.xlim(0,11)
plt.title(u'A(2)x+', fontsize = 20)
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
plt.ylabel('PROMEDIO', fontsize = 20)
plt.xlabel('SESIONES', fontsize = 20)



plt.subplot(235)
plt.errorbar(x, PRE_A4x_promedio, yerr=error_PRE_A4x,  marker='o', color = 'k', linestyle='--', label='PRE ECs')
plt.errorbar(x, DURANTE_A4x_promedio, yerr=error_DURANTE_A4x,  marker='s', color = 'k', label='DURANTE ECs')
plt.errorbar(x, elevacion_A4x_promedio, yerr=error_elevacion_A4x,  marker='^', color = 'k', linestyle=':', label='ELEVACION')
plt.ylim(-5,75)
plt.xlim(0,11)
plt.title(u'A(4)x+', fontsize = 20)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.spines['left'].set_color('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')



plt.subplot(236)
plt.errorbar(x, PRE_A8x_promedio, yerr=error_PRE_A8x,  marker='o', color = 'k', linestyle='--', label='PRE ECs')
plt.errorbar(x, DURANTE_A8x_promedio, yerr=error_DURANTE_A8x,  marker='s', color = 'k', label='DURANTE ECs')
plt.errorbar(x, elevacion_A8x_promedio, yerr=error_elevacion_A8x,  marker='^', color = 'k', linestyle=':', label='ELEVACION')
plt.ylim(-5,75)
plt.xlim(0,11)
plt.title(u'A(8)x+', fontsize = 20)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.spines['left'].set_color('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')

#plt.savefig('adquisicionRatos', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)

plt.show()