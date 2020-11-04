#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:51:00 2019

@author: yancarlo
"""

#%%Importar librerias 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
plt.ion() 
import re
from scipy import stats

#%%Crear las matrices donde se guardarán los datos generales y las variables de sujetos y sesiones
sujetos = 10
sesiones = 10
total_respuestas_Ax = np.zeros((sujetos,sesiones))
total_respuestas_A = np.zeros((sujetos,sesiones))
total_respuestas_x = np.zeros((sujetos,sesiones))


#%%Ordenar carpetas
#Función que recibe un string, que es la dirección de la carpeta que se desea ordenar alfanumericamente
def orden_alfanumerico(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)


#%%Inicio de ciclos for, que leen cada una de los archivos en las carpetas correspondientes a cada grupo

#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_Ax = orden_alfanumerico(os.listdir("/home/yancarlo/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_Ax/"))


k = 0
l = 0
for elemento in contenido_Ax:
    ruta = "/home/yancarlo/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_Ax/"
    archivo = ruta + elemento
    print(elemento)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                       na_values=[' '])
    
    respuestas = pd.DataFrame(datos[9:10][:])
    respuestas.columns=['Numero','Dato']
    total_respuestas_Ax[k][l] = float(respuestas['Dato'])
    
    l += 1
    if l == 10:
        k +=1
        l = 0
        

#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_A = orden_alfanumerico(os.listdir("/home/yancarlo/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A/"))

k = 0
l = 0
for elemento in contenido_A:
    ruta = "/home/yancarlo/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_A/"
    archivo = ruta + elemento
    print(elemento)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                       na_values=[' '])
    
    respuestas = pd.DataFrame(datos[9:10][:])
    respuestas.columns=['Numero','Dato']
    total_respuestas_A[k][l] = float(respuestas['Dato'])
    
    l += 1
    if l == 10:
        k +=1
        l = 0


#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_x = orden_alfanumerico(os.listdir("/home/yancarlo/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_x/"))

k = 0
l = 0
for elemento in contenido_x:
    ruta = "/home/yancarlo/datos_ratas_tesis_doctorado/ENTRENAMIENTO/Grupo_x/"
    archivo = ruta + elemento
    print(elemento)
    datos = pd.read_csv(archivo, sep = ': ', engine='python', keep_default_na=False,
                       na_values=[' '])
    
    respuestas = pd.DataFrame(datos[9:10][:])
    respuestas.columns=['Numero','Dato']
    total_respuestas_x[k][l] = float(respuestas['Dato'])
    
    l += 1
    if l == 10:
        k +=1
        l = 0


#%%Promedios y error éstandar
#se obtiene el promedio por sesión de todas las respuestas de todos los sujetos por grupo, así como su 
#desviación éstandar 
respuestas_Ax_promedio = np.sum(total_respuestas_Ax, axis=0)/10
tasa_Ax = respuestas_Ax_promedio/34
error_respuestas_Ax = stats.sem(tasa_Ax, axis=0, ddof=0)

respuestas_A_promedio = np.sum(total_respuestas_A, axis=0)/10
tasa_A = respuestas_A_promedio/34
error_respuestas_A = stats.sem(tasa_A, axis=0, ddof=0)

respuestas_x_promedio = np.sum(total_respuestas_x, axis=0)/10
tasa_x = respuestas_x_promedio/34
error_respuestas_x = stats.sem(tasa_x, axis=0, ddof=0)


#%%Plot

#primero se establece el rango de valores para el eje x, en la variable "x"
x = np.arange(.99, 10.01)
#con plt.subplots, se declara que habrá más de un plot 
fig, ax = plt.subplots()
#el primer número representa las filas, el segundo las columnas y el tercero el plot que se hará  
#en este caso es una fila, tres columnas (o plots) y se comienza a crear el primer plot
plt.subplot(131)
#el primer parametro de la función .errorbar (que sirve para poner las barras de dispersión), es el eje  x,
#el segundo es los datos a plotear, el tercero es el error de esos datos, y los de marker y color son 
#estilos de línea (aquí la documentación: https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html) 
plt.errorbar(x, tasa_Ax, yerr=error_respuestas_Ax,  marker='s', color = 'k')
# gca = 'get current axis'
ax = plt.gca() 
# .spines['right'].set_color('none') pone en color none el spine derecho, es decir, lo borra
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
#la siguiente función pone la línea inferior del frame del plot en la posición indicada (en este caso 0)
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
#con lo siguiente se marcan los límites de los ejes
plt.ylim(0,10)
plt.xlim(0,11)
#título y tamaño de la letra del plot
plt.title(u'Ax+', fontsize = 20)
#tamaño de letra de los números de las escalas de cada eje
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
#título y tamaño de la letra de los ejes
plt.ylabel('TASA DE RESPUESTAS (R/min)', fontsize = 20)
plt.xlabel('SESIONES', fontsize = 20)

#comienza el segundo plot
plt.subplot(132) 
plt.errorbar(x, tasa_A, yerr=error_respuestas_A,  marker='s', color = 'k', label='DURANTE ECs')
plt.ylim(0,10)
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

#comienza el tercer plot
plt.subplot(133)
plt.errorbar(x, tasa_x, yerr=error_respuestas_x,  marker='s', color = 'k', label='DURANTE ECs')
plt.ylim(0,10)
plt.xlim(0,11)
plt.title(u'x+', fontsize = 20)
#plt.legend(fontsize = 15) 
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

#si se descomenta la siguiente línea, se guarda la gráfica con 300dpi (puntos por pulgada) automáticamente 
#en la ubicación donde está guardado este código, sino solo lo mostrará con plt.show()
#plt.savefig('adquisicionRatos', dpi = 300) 

plt.show()