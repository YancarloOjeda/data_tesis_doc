# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:49:59 2021

@author: yanoj
"""

import pandas as pd
import numpy as np
from scipy import stats
import os
import re
import matplotlib.pyplot as plt

#%%-----Load DB from Pavlovbot-------------------------------------------------
datos_A = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A_activations.csv"
                    , sep =',', index_col=False)
df_A = pd.DataFrame(datos_A)
CA_A = df_A['CR'][0:9000]

datos_Ax = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/Ax_activations.csv"
                    , sep =',', index_col=False)
df_Ax = pd.DataFrame(datos_Ax)
CA_Ax = df_Ax['CR'][0:9000]

datos_x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/x_activations.csv"
                    , sep =',', index_col=False)
df_x = pd.DataFrame(datos_x)
CA_x = df_x['CR'][0:9000]

datos_A1x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A1x_2_activations.csv"
                    , sep =',', index_col=False)
df_A1x = pd.DataFrame(datos_A1x)
CA_A1x = df_A1x['CR'][0:9000]

datos_A2x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A2x_5_activations.csv"
                    , sep =',', index_col=False)
df_A2x = pd.DataFrame(datos_A2x)
CA_A2x = df_A2x['CR'][0:9000]

datos_A4x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A4x-5_activations.csv"
                    , sep =',', index_col=False)
df_A4x = pd.DataFrame(datos_A4x)
CA_A4x = df_A4x['CR'][0:9000]
#%%-----Graphs-----------------------------------------------------------------
x = np.arange(.99, 9000)
fig, ax = plt.subplots()
plt.subplot(231)  
plt.errorbar(x, CA_Ax, color = 'k', label='Ax')
plt.ylim(0,1)
plt.xlim(0,9000)
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
plt.errorbar(x, CA_A, color = 'k', label='A')
plt.ylim(0,1)
plt.xlim(0,9000)
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
plt.errorbar(x, CA_x, color = 'k', label='x')
plt.ylim(0,1)
plt.xlim(0,9000)
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
plt.errorbar(x, CA_A1x, color = 'k', label='A1x')
ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
plt.ylim(0,1)
plt.xlim(0,9000)
plt.title(u'A1x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.yticks(fontsize=13, weight='bold') 
plt.xticks(fontsize=13, weight='bold')
plt.ylabel("Activaciones condicionadas\n Unidad $M'$", fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.xlabel('Momentos temporales', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})



plt.subplot(235)
plt.errorbar(x, CA_A2x, color = 'k', label='A2x')
plt.ylim(0,1)
plt.xlim(0,9000)
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
plt.errorbar(x, CA_A4x, color = 'k', label='A4x')
plt.ylim(0,1)
plt.xlim(0,9000)
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
