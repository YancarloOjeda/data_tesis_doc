# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:42:06 2021

@author: yanoj
"""

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

#%%-----Load DB from Pavlovbot-------------------------------------------------
datos_A = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A_weights.csv"
                    , sep =',', index_col=False)
df_A = pd.DataFrame(datos_A)
A_A_S1 = df_A['A-S"1'][0:9000]
A_CTX_S1 = df_A['CTX-S"1'][0:9000]
A_x_S2 = df_A['x-S"2'][0:9000]
A_CTX_S2 = df_A['CTX-S"2'][0:9000]

datos_Ax = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/Ax_weights.csv"
                    , sep =',', index_col=False)
df_Ax = pd.DataFrame(datos_Ax)
Ax_A_S1 = df_Ax['A-S"1'][0:9000]
Ax_CTX_S1 = df_Ax['CTX-S"1'][0:9000]
Ax_x_S2 = df_Ax['x-S"2'][0:9000]
Ax_CTX_S2 = df_Ax['CTX-S"2'][0:9000]

datos_x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/x_weights.csv"
                    , sep =',', index_col=False)
df_x = pd.DataFrame(datos_x)
x_A_S1 = df_x['A-S"1'][0:9000]
x_CTX_S1 = df_x['CTX-S"1'][0:9000]
x_x_S2 = df_x['x-S"2'][0:9000]
x_CTX_S2 = df_x['CTX-S"2'][0:9000]

datos_A1x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A1x_2_weights.csv"
                    , sep =',', index_col=False)
df_A1x = pd.DataFrame(datos_A1x)
A1x_A_S1 = df_A1x['A-S"1'][0:9000]
A1x_CTX_S1 = df_A1x['CTX-S"1'][0:9000]
A1x_x_S2 = df_A1x['x-S"2'][0:9000]
A1x_CTX_S2 = df_A1x['CTX-S"2'][0:9000]

datos_A2x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A2x_5_weights.csv"
                    , sep =',', index_col=False)
df_A2x = pd.DataFrame(datos_A2x)
A2x_A_S1 = df_A2x['A-S"1'][0:9000]
A2x_CTX_S1 = df_A2x['CTX-S"1'][0:9000]
A2x_x_S2 = df_A2x['x-S"2'][0:9000]
A2x_CTX_S2 = df_A2x['CTX-S"2'][0:9000]

datos_A4x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A4x-5_weights.csv"
                    , sep =',', index_col=False)
df_A4x = pd.DataFrame(datos_A4x)
A4x_A_S1 = df_A4x['A-S"1'][0:9000]
A4x_CTX_S1 = df_A4x['CTX-S"1'][0:9000]
A4x_x_S2 = df_A4x['x-S"2'][0:9000]
A4x_CTX_S2 = df_A4x['CTX-S"2'][0:9000]
#%%-----Graphs-----------------------------------------------------------------
x = np.arange(.99, 9000)
fig, ax = plt.subplots()
plt.subplot(231)  
plt.errorbar(x, Ax_A_S1, color = 'grey', linestyle = '-', label='Ax')
plt.errorbar(x, Ax_CTX_S1, color = 'grey', linestyle = ':', label='Ax')
plt.errorbar(x, Ax_x_S2, color = 'k', linestyle = '-', label='Ax')
plt.errorbar(x, Ax_CTX_S2, color = 'k', linestyle = ':', label='Ax')
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
plt.errorbar(x, A_A_S1, color = 'grey', linestyle = '-', label='A')
plt.errorbar(x, A_CTX_S1, color = 'grey', linestyle = ':', label='A')
plt.errorbar(x, A_x_S2, color = 'k', linestyle = '-', label='A')
plt.errorbar(x, A_CTX_S2, color = 'k', linestyle = ':', label='A')
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
plt.errorbar(x, x_A_S1, color = 'grey', linestyle = '-', label=r"A" + '-$S$"${}_{1}$')
plt.errorbar(x, x_CTX_S1, color = 'grey', linestyle = ':', label=r"CTX" + '-$S$"${}_{1}$')
plt.errorbar(x, x_x_S2, color = 'k', linestyle = '-', label=r"x" + '-$S$"${}_{2}$')
plt.errorbar(x, x_CTX_S2, color = 'k', linestyle = ':', label=r"CTX" + '-$S$"${}_{2}$')
plt.ylim(0,1)
plt.xlim(0,9000)
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
plt.errorbar(x, A1x_A_S1, color = 'grey', linestyle = '-', label='A1x')
plt.errorbar(x, A1x_CTX_S1, color = 'grey', linestyle = ':', label='A1x')
plt.errorbar(x, A1x_x_S2, color = 'k', linestyle = '-', label='A1x')
plt.errorbar(x, A1x_CTX_S2, color = 'k', linestyle = ':', label='A1x')
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
plt.ylabel("Pesos entre conexiones", fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.xlabel('Momentos temporales', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})



plt.subplot(235)
plt.errorbar(x, A2x_A_S1, color = 'grey', linestyle = '-', label='A2x')
plt.errorbar(x, A2x_CTX_S1, color = 'grey', linestyle = ':', label='A2x')
plt.errorbar(x, A2x_x_S2, color = 'k', linestyle = '-', label='A2x')
plt.errorbar(x, A2x_CTX_S2, color = 'k', linestyle = ':', label='A2x')
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
plt.errorbar(x, A4x_A_S1, color = 'grey', linestyle = '-', label='A4x')
plt.errorbar(x, A4x_CTX_S1, color = 'grey', linestyle = ':', label='A4x')
plt.errorbar(x, A4x_x_S2, color = 'k', linestyle = '-', label='A4x')
plt.errorbar(x, A4x_CTX_S2, color = 'k', linestyle = ':', label='A4x')
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
