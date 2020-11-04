#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:19:18 2019

@author: yan
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
plt.ion() 
import re
from scipy import stats

total_PRE_Ax_A = np.zeros(10)
total_DURANTE_Ax_A = np.zeros(10)
total_PRE_Ax_x = np.zeros(10)
total_DURANTE_Ax_x = np.zeros(10)

total_PRE_A_A = np.zeros(10)
total_DURANTE_A_A = np.zeros(10)
total_PRE_A_x = np.zeros(10)
total_DURANTE_A_x = np.zeros(10)

total_PRE_x_A = np.zeros(10)
total_DURANTE_x_A = np.zeros(10)
total_PRE_x_x = np.zeros(10)
total_DURANTE_x_x = np.zeros(10)

total_PRE_A2x_A = np.zeros(10)
total_DURANTE_A2x_A = np.zeros(10)
total_PRE_A2x_x = np.zeros(10)
total_DURANTE_A2x_x = np.zeros(10)

total_PRE_A4x_A = np.zeros(10)
total_DURANTE_A4x_A = np.zeros(10)
total_PRE_A4x_x = np.zeros(10)
total_DURANTE_A4x_x = np.zeros(10)

total_PRE_A8x_A = np.zeros(10)
total_DURANTE_A8x_A = np.zeros(10)
total_PRE_A8x_x = np.zeros(10)
total_DURANTE_A8x_x = np.zeros(10)

def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

#se obtiene una lista desordenada con todos los archivos que están en la carpeta datosRatas
contenido_Ax = sorted_aphanumeric(os.listdir("/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/Grupo_Ax/"))

carpetas = sorted_aphanumeric(os.listdir("/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/"))
print(carpetas)

k = 0
l = 0
m = 0
n = 0
o = 0
p = 0

for elemento in carpetas: 
    ruta = "/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/"
    archivo = ruta + elemento +'/'
    print('archivo', archivo)
    grupos = sorted_aphanumeric(os.listdir(archivo))
    print(grupos)
    
    for sesion in grupos:
        archivo1 = archivo + sesion
        print(archivo)
        
        if archivo == '/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/Grupo_Ax/':
            datos = pd.read_csv(archivo1, sep = ': ', engine='python', keep_default_na=False,
                               na_values=[' '])
            
            datos.columns=['Numero','Dato']
            datos_Ax = pd.DataFrame(datos)
            
            datos_PRE_Ax_A = pd.to_numeric(datos_Ax[40:45]['Dato'])
            datos_DURANTE_Ax_A = pd.to_numeric(datos_Ax[46:50]['Dato'])
            datos_PRE_Ax_x = pd.to_numeric(datos_Ax[52:56]['Dato'])
            datos_DURANTE_Ax_x = pd.to_numeric(datos_Ax[58:62]['Dato'])
            
            suma_PRE_Ax_A = np.sum(datos_PRE_Ax_A)
            suma_DURANTE_Ax_A = np.sum(datos_DURANTE_Ax_A)
            suma_PRE_Ax_x = np.sum(datos_PRE_Ax_x)
            suma_DURANTE_Ax_x = np.sum(datos_DURANTE_Ax_x)
         
            total_PRE_Ax_A[k] = suma_PRE_Ax_A
            total_DURANTE_Ax_A[k] = suma_DURANTE_Ax_A
            total_PRE_Ax_x[k] = suma_PRE_Ax_x
            total_DURANTE_Ax_x[k] = suma_DURANTE_Ax_x
            
            k += 1
            
        if archivo == '/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/Grupo_A/':
            datos = pd.read_csv(archivo1, sep = ': ', engine='python', keep_default_na=False,
                               na_values=[' '])
            
            datos.columns=['Numero','Dato']
            datos_A = pd.DataFrame(datos)
            
            datos_PRE_A_A = pd.to_numeric(datos_A[40:45]['Dato'])
            datos_DURANTE_A_A = pd.to_numeric(datos_A[46:50]['Dato'])
            datos_PRE_A_x = pd.to_numeric(datos_A[52:56]['Dato'])
            datos_DURANTE_A_x = pd.to_numeric(datos_A[58:62]['Dato'])
            
            suma_PRE_A_A = np.sum(datos_PRE_A_A)
            suma_DURANTE_A_A = np.sum(datos_DURANTE_A_A)
            suma_PRE_A_x = np.sum(datos_PRE_A_x)
            suma_DURANTE_A_x = np.sum(datos_DURANTE_A_x)
         
            total_PRE_A_A[l] = suma_PRE_A_A
            total_DURANTE_A_A[l] = suma_DURANTE_A_A
            total_PRE_A_x[l] = suma_PRE_A_x
            total_DURANTE_A_x[l] = suma_DURANTE_A_x
            
            l += 1
        
        if archivo == '/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/Grupo_x/':
            datos = pd.read_csv(archivo1, sep = ': ', engine='python', keep_default_na=False,
                               na_values=[' '])
            
            datos.columns=['Numero','Dato']
            datos_x = pd.DataFrame(datos)
            
            datos_PRE_x_A = pd.to_numeric(datos_x[40:45]['Dato'])
            datos_DURANTE_x_A = pd.to_numeric(datos_x[46:50]['Dato'])
            datos_PRE_x_x = pd.to_numeric(datos_x[52:56]['Dato'])
            datos_DURANTE_x_x = pd.to_numeric(datos_x[58:62]['Dato'])
            
            suma_PRE_x_A = np.sum(datos_PRE_x_A)
            suma_DURANTE_x_A = np.sum(datos_DURANTE_x_A)
            suma_PRE_x_x = np.sum(datos_PRE_x_x)
            suma_DURANTE_x_x = np.sum(datos_DURANTE_x_x)
         
            total_PRE_x_A[m] = suma_PRE_x_A
            total_DURANTE_x_A[m] = suma_DURANTE_x_A
            total_PRE_x_x[m] = suma_PRE_x_x
            total_DURANTE_x_x[m] = suma_DURANTE_x_x
            
            m += 1
        
        if archivo == '/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/Grupo_A(2)x/':
            datos = pd.read_csv(archivo1, sep = ': ', engine='python', keep_default_na=False,
                               na_values=[' '])
            
            datos.columns=['Numero','Dato']
            datos_A2x = pd.DataFrame(datos)
            
            datos_PRE_A2x_A = pd.to_numeric(datos_A2x[39:43]['Dato'])
            datos_DURANTE_A2x_A = pd.to_numeric(datos_A2x[45:49]['Dato'])
            datos_PRE_A2x_x = pd.to_numeric(datos_A2x[51:55]['Dato'])
            datos_DURANTE_A2x_x = pd.to_numeric(datos_A2x[57:61]['Dato'])
            
            suma_PRE_A2x_A = np.sum(datos_PRE_A2x_A)
            suma_DURANTE_A2x_A = np.sum(datos_DURANTE_A2x_A)
            suma_PRE_A2x_x = np.sum(datos_PRE_A2x_x)
            suma_DURANTE_A2x_x = np.sum(datos_DURANTE_A2x_x)
         
            total_PRE_A2x_A[n] = suma_PRE_A2x_A
            total_DURANTE_A2x_A[n] = suma_DURANTE_A2x_A
            total_PRE_A2x_x[n] = suma_PRE_A2x_x
            total_DURANTE_A2x_x[n] = suma_DURANTE_A2x_x
            
            n += 1
        
        if archivo == '/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/Grupo_A(4)x/':
            datos = pd.read_csv(archivo1, sep = ': ', engine='python', keep_default_na=False,
                               na_values=[' '])
            
            datos.columns=['Numero','Dato']
            datos_A4x = pd.DataFrame(datos)
            
            datos_PRE_A4x_A = pd.to_numeric(datos_A4x[39:44]['Dato'])
            datos_DURANTE_A4x_A = pd.to_numeric(datos_A4x[45:49]['Dato'])
            datos_PRE_A4x_x = pd.to_numeric(datos_A4x[51:55]['Dato'])
            datos_DURANTE_A4x_x = pd.to_numeric(datos_A4x[57:61]['Dato'])
            
            suma_PRE_A4x_A = np.sum(datos_PRE_A4x_A)
            suma_DURANTE_A4x_A = np.sum(datos_DURANTE_A4x_A)
            suma_PRE_A4x_x = np.sum(datos_PRE_A4x_x)
            suma_DURANTE_A4x_x = np.sum(datos_DURANTE_A4x_x)
         
            total_PRE_A4x_A[o] = suma_PRE_A4x_A
            total_DURANTE_A4x_A[o] = suma_DURANTE_A4x_A
            total_PRE_A4x_x[o] = suma_PRE_A4x_x
            total_DURANTE_A4x_x[o] = suma_DURANTE_A4x_x
            
            o += 1
            
        if archivo == '/home/yan/datos_ratas_tesis_doctorado/PRUEBAS/Grupo_A(8)x/':
            datos = pd.read_csv(archivo1, sep = ': ', engine='python', keep_default_na=False,
                               na_values=[' '])
            
            datos.columns=['Numero','Dato']
            datos_A8x = pd.DataFrame(datos)
            
            datos_PRE_A8x_A = pd.to_numeric(datos_A8x[39:44]['Dato'])
            datos_DURANTE_A8x_A = pd.to_numeric(datos_A8x[45:49]['Dato'])
            datos_PRE_A8x_x = pd.to_numeric(datos_A8x[51:55]['Dato'])
            datos_DURANTE_A8x_x = pd.to_numeric(datos_A8x[57:61]['Dato'])
            
            suma_PRE_A8x_A = np.sum(datos_PRE_A8x_A)
            suma_DURANTE_A8x_A = np.sum(datos_DURANTE_A8x_A)
            suma_PRE_A8x_x = np.sum(datos_PRE_A8x_x)
            suma_DURANTE_A8x_x = np.sum(datos_DURANTE_A8x_x)
         
            total_PRE_A8x_A[p] = suma_PRE_A8x_A
            total_DURANTE_A8x_A[p] = suma_DURANTE_A8x_A
            total_PRE_A8x_x[p] = suma_PRE_A8x_x
            total_DURANTE_A8x_x[p] = suma_DURANTE_A8x_x
            
            p += 1
  
elevacion_Ax_A = total_DURANTE_Ax_A - total_PRE_Ax_A # 21.5
elevacion_Ax_x = total_DURANTE_Ax_x - total_PRE_Ax_x # 4
elevacion_A_A = total_DURANTE_A_A - total_PRE_A_A 
elevacion_A_x = total_DURANTE_A_x - total_PRE_A_x
elevacion_x_A = total_DURANTE_x_A - total_PRE_x_A 
elevacion_x_x = total_DURANTE_x_x - total_PRE_x_x
elevacion_A2x_A = total_DURANTE_A2x_A - total_PRE_A2x_A 
elevacion_A2x_x = total_DURANTE_A2x_x - total_PRE_A2x_x
elevacion_A4x_A = total_DURANTE_A4x_A - total_PRE_A4x_A 
elevacion_A4x_x = total_DURANTE_A4x_x - total_PRE_A4x_x
elevacion_A8x_A = total_DURANTE_A8x_A - total_PRE_A8x_A 
elevacion_A8x_x = total_DURANTE_A8x_x - total_PRE_A8x_x

print(total_PRE_Ax_A)
print(total_DURANTE_Ax_A)
print(total_PRE_Ax_x)
print(total_DURANTE_Ax_x)
print('elevacion_Ax_A',elevacion_Ax_A)
print('elevacion_Ax_x',elevacion_Ax_x)

print(total_PRE_A_A)
print(total_DURANTE_A_A)
print(total_PRE_A_x)
print(total_DURANTE_A_x)
print('elevacion_A_A',elevacion_A_A)
print('elevacion_A_x',elevacion_A_x)

print(total_PRE_x_A)
print(total_DURANTE_x_A)
print(total_PRE_x_x)
print(total_DURANTE_x_x)
print('elevacion_x_A',elevacion_x_A)
print('elevacion_x_x',elevacion_x_x)

print(total_PRE_A2x_A)
print(total_DURANTE_A2x_A)
print(total_PRE_A2x_x)
print(total_DURANTE_A2x_x)
print('elevacion_A(2)x_A',elevacion_A2x_A)
print('elevacion_A(2)x_x',elevacion_A2x_x)

print(total_PRE_A4x_A)
print(total_DURANTE_A4x_A)
print(total_PRE_A4x_x)
print(total_DURANTE_A4x_x)
print('elevacion_A(4)x_A',elevacion_A4x_A)
print('elevacion_A(4)x_x',elevacion_A4x_x)

print(total_PRE_A8x_A)
print(total_DURANTE_A8x_A)
print(total_PRE_A8x_x)
print(total_DURANTE_A8x_x)
print('elevacion_A(8)x_A',elevacion_A8x_A)
print('elevacion_A(8)x_x',elevacion_A8x_x)

promedio_elevacion_Ax_A = np.mean(elevacion_Ax_A)
promedio_elevacion_Ax_x = np.mean(elevacion_Ax_x)
promedio_elevacion_A_A = np.mean(elevacion_A_A)
promedio_elevacion_A_x = np.mean(elevacion_A_x)
promedio_elevacion_x_A = np.mean(elevacion_x_A)
promedio_elevacion_x_x = np.mean(elevacion_x_x)
promedio_elevacion_A2x_A = np.mean(elevacion_A2x_A)
promedio_elevacion_A2x_x = np.mean(elevacion_A2x_x)
promedio_elevacion_A4x_A = np.mean(elevacion_A4x_A)
promedio_elevacion_A4x_x = np.mean(elevacion_A4x_x)
promedio_elevacion_A8x_A = np.mean(elevacion_A8x_A)
promedio_elevacion_A8x_x = np.mean(elevacion_A8x_x)

error_elevacion_Ax_A = stats.sem(elevacion_Ax_A, axis=0, ddof=0) #4#
error_elevacion_Ax_x = stats.sem(elevacion_Ax_x, axis=0, ddof=0) #2#
error_elevacion_A_A = stats.sem(elevacion_A_A, axis=0, ddof=0)
error_elevacion_A_x = stats.sem(elevacion_A_x, axis=0, ddof=0)
error_elevacion_x_A = stats.sem(elevacion_x_A, axis=0, ddof=0)
error_elevacion_x_x = stats.sem(elevacion_x_x, axis=0, ddof=0)
error_elevacion_A2x_A = stats.sem(elevacion_A2x_A, axis=0, ddof=0) 
error_elevacion_A2x_x = stats.sem(elevacion_A2x_x, axis=0, ddof=0)
error_elevacion_A4x_A = stats.sem(elevacion_A4x_A, axis=0, ddof=0) 
error_elevacion_A4x_x = stats.sem(elevacion_A4x_x, axis=0, ddof=0)
error_elevacion_A8x_A = stats.sem(elevacion_A8x_A, axis=0, ddof=0) 
error_elevacion_A8x_x = stats.sem(elevacion_A8x_x, axis=0, ddof=0)


men_means, men_std = (promedio_elevacion_Ax_A,promedio_elevacion_A2x_A, promedio_elevacion_A4x_A, 
                      promedio_elevacion_A8x_A, promedio_elevacion_A_A, promedio_elevacion_x_A), (error_elevacion_Ax_A, error_elevacion_A2x_A, error_elevacion_A4x_A, error_elevacion_A8x_A, error_elevacion_A_A, error_elevacion_x_A)
women_means, women_std = (promedio_elevacion_Ax_x, promedio_elevacion_A2x_x, promedio_elevacion_A4x_x, 
                          promedio_elevacion_A8x_x, promedio_elevacion_A_x, promedio_elevacion_x_x), (error_elevacion_Ax_x, error_elevacion_A2x_x, error_elevacion_A4x_x, error_elevacion_A8x_x, error_elevacion_A_x, error_elevacion_x_x)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                color='gray', label='A')
rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
                color='lightgrey', label='x')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('ELEVACIÓN', fontsize = 30)
ax.set_xlabel('GRUPOS', fontsize = 30)
#ax.set_title('GRUPOS CONTROL', fontsize = 20)
ax.set_xticks(ind)
ax.set_xticklabels(('Ax', 'A(2)x', 'A(4)x', 'A(8)x', 'A', 'x'), fontsize = 15)
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',-5))
ax.yaxis.set_ticks_position('left')
plt.legend(fontsize = 15)
plt.yticks(fontsize=25) 
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
ax.legend(fontsize = 15)


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()
