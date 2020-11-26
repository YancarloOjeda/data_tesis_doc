# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 10:58:43 2020

@author: yanoj
"""

import pandas as pd
import numpy as np
from scipy import stats
import os
import re
import matplotlib.pyplot as plt
import matplotlib as mpl

#%%-----ubicación vía 1 (M"1-M')-----------------------------------------------
ubicacion_BD_M1 = "C:/Users/yanoj/OneDrive/Documentos/simulacion/con ITI/datos_filtrados_entrenamiento_PESOS/PROMEDIOS_total_Pre1.csv"

datos_M1 = pd.read_csv(ubicacion_BD_M1, sep = ',', engine='python', keep_default_na=False, na_values=[' '])

df_M1 = pd.DataFrame(datos_M1)

#%%-----ubicación vía 1 (M"2-M')-----------------------------------------------
ubicacion_BD_M2 = "C:/Users/yanoj/OneDrive/Documentos/simulacion/con ITI/datos_filtrados_entrenamiento_PESOS/PROMEDIOS_total_Pre2.csv"

datos_M2 = pd.read_csv(ubicacion_BD_M2, sep = ',', engine='python', keep_default_na=False, na_values=[' '])

df_M2 = pd.DataFrame(datos_M2)

#%%-----Graphs-----------------------------------------------------------------
x = np.arange(.99, 300)
fig, ax = plt.subplots()
plt.subplot(231)  
plt.errorbar(x, df_M1['Ax'], color = 'k', linestyle = '-', label='Ax')
plt.errorbar(x, df_M2['Ax'], color = 'k', linestyle = ':', label='Ax')
plt.ylim(0,1)
plt.xlim(0,300)
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
#ax.spines['left'].set_color('none')
# ax.set_yticklabels([])
plt.yticks(fontsize=20)
# ax.yaxis.set_ticks_position('none')
plt.title(u'Ax', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.yticks(fontsize=13, weight='bold') 
plt.xticks(fontsize=13, weight='bold')


plt.subplot(232)  
plt.errorbar(x, df_M1['ï»¿A'], color = 'k', linestyle = '-', label='A')
plt.errorbar(x, df_M2['ï»¿A'], color = 'k', linestyle = ':', label='A')
plt.ylim(0,1)
plt.xlim(0,300)
plt.title(u'A', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
# ax.spines['left'].set_color('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')


plt.subplot(233)
plt.errorbar(x, df_M1['x'], color = 'k', linestyle = '-', label=r'$M$"${}_{1}$' + "-$M'$")
plt.errorbar(x, df_M2['x'], color = 'k', linestyle = ':', label=r'$M$"${}_{2}$' + "-$M'$")
plt.ylim(0,1)
plt.xlim(0,300)
plt.title(u'x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.legend(fontsize = 15, loc = 'upper right') 
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
# ax.spines['left'].set_color('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')



plt.subplot(234)
plt.errorbar(x, df_M1['A(1)x'], color = 'k', linestyle = '-', label='A1x')
plt.errorbar(x, df_M2['A(1)x'], color = 'k', linestyle = ':', label='A1x')
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
plt.ylim(0,1)
plt.xlim(0,300)
plt.title(u'A1x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.yticks(fontsize=13, weight='bold') 
plt.xticks(fontsize=13, weight='bold')
plt.ylabel("Pesos promedio\n de conexiones", fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.xlabel('Ensayos', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})



plt.subplot(235)
plt.errorbar(x, df_M1['A(2)x'], color = 'k', linestyle = '-', label='A2x')
plt.errorbar(x, df_M2['A(2)x'], color = 'k', linestyle = ':', label='A2x')
plt.ylim(0,1)
plt.xlim(0,300)
plt.title(u'A2x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
# ax.spines['left'].set_color('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')



plt.subplot(236)
plt.errorbar(x, df_M1['A(4)x'], color = 'k', linestyle = '-', label='A4x')
plt.errorbar(x, df_M2['A(4)x'], color = 'k', linestyle = ':', label='A4x')
plt.ylim(0,1)
plt.xlim(0,300)
plt.title(u'A4x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
# ax.spines['left'].set_color('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')

#plt.savefig('adquisicionRatos', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)

plt.show()
