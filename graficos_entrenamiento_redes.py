# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 20:08:15 2020

@author: yanoj
"""

import pandas as pd
import numpy as np
from scipy import stats
import os
import re
import matplotlib.pyplot as plt

#%%-----Load DB----------------------------------------------------------------
ubicacion_BD = "C:/Users/yanoj/OneDrive/Documentos/simulacion/con ITI/datos_filtrados_entrenamiento/PROMEDIOS_total_.csv"

datos = pd.read_csv(ubicacion_BD, sep = ',', engine='python', keep_default_na=False, na_values=[' '])

df = pd.DataFrame(datos)

#%%-----Graphs-----------------------------------------------------------------
x = np.arange(.99, 299)
fig, ax = plt.subplots()
plt.subplot(231)  
plt.errorbar(x, df['Ax'], color = 'k', label='Ax')
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
plt.errorbar(x, df['ï»¿A'], color = 'k', label='A')
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
plt.errorbar(x, df['x'], color = 'k', label='x')
plt.ylim(0,1)
plt.xlim(0,300)
plt.title(u'x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
# plt.legend(fontsize = 15) 
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
plt.errorbar(x, df['A(1)x'], color = 'k', label='A1x')
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
plt.ylabel('Activaciones\n promedio', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 24})
plt.xlabel('Ensayos', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})



plt.subplot(235)
plt.errorbar(x, df['A(2)x'], color = 'k', label='A2x')
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
plt.errorbar(x, df['A(4)x'], color = 'k', label='A4x')
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
