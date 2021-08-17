# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 07:50:43 2021

@author: yanoj
"""

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
A_M1_R = df_A['M"1-R*'][0:9000]
A_M2_R = df_A['M"2-R*'][0:9000]

datos_Ax = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/Ax_weights.csv"
                    , sep =',', index_col=False)
df_Ax = pd.DataFrame(datos_Ax)
Ax_M1_R = df_Ax['M"1-R*'][0:9000]
Ax_M2_R = df_Ax['M"2-R*'][0:9000]

datos_x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/x_weights.csv"
                    , sep =',', index_col=False)
df_x = pd.DataFrame(datos_x)
x_M1_R = df_x['M"1-R*'][0:9000]
x_M2_R = df_x['M"2-R*'][0:9000]

datos_A1x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A1x_2_weights.csv"
                    , sep =',', index_col=False)
df_A1x = pd.DataFrame(datos_A1x)
A1x_M1_R = df_A1x['M"1-R*'][0:9000]
A1x_M2_R = df_A1x['M"2-R*'][0:9000]

datos_A2x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A2x_5_weights.csv"
                    , sep =',', index_col=False)
df_A2x = pd.DataFrame(datos_A2x)
A2x_M1_R = df_A2x['M"1-R*'][0:9000]
A2x_M2_R = df_A2x['M"2-R*'][0:9000]

datos_A4x = pd.read_csv("C:/Users/yanoj/OneDrive/Documentos/robot-implementation/Final experiments/A4x-5_weights.csv"
                    , sep =',', index_col=False)
df_A4x = pd.DataFrame(datos_A4x)
A4x_M1_R = df_A4x['M"1-R*'][0:9000]
A4x_M2_R = df_A4x['M"2-R*'][0:9000]
#%%-----Graphs-----------------------------------------------------------------
x = np.arange(.99, 9000)
fig, ax = plt.subplots()
plt.subplot(231)  
plt.errorbar(x, Ax_M1_R, color = 'K', linestyle = '-', label='Ax')
plt.errorbar(x, Ax_M2_R, color = 'K', linestyle = ':', label='Ax')
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
plt.errorbar(x, A_M1_R, color = 'K', linestyle = '-', label='A')
plt.errorbar(x, A_M2_R, color = 'K', linestyle = ':', label='A')
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
plt.errorbar(x, x_M1_R, color = 'K', linestyle = '-', label=r'$M$"${}_{1}$' + "-$M'$")
plt.errorbar(x, x_M2_R, color = 'K', linestyle = ':', label=r'$M$"${}_{2}$' + "-$M'$")
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
plt.errorbar(x, A1x_M1_R, color = 'K', linestyle = '-', label='A1x')
plt.errorbar(x, A1x_M2_R, color = 'K', linestyle = ':', label='A1x')
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
plt.errorbar(x, A2x_M1_R, color = 'K', linestyle = '-', label='A2x')
plt.errorbar(x, A2x_M2_R, color = 'K', linestyle = ':', label='A2x')
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
plt.errorbar(x, A4x_M1_R, color = 'K', linestyle = '-', label='A4x')
plt.errorbar(x, A4x_M2_R, color = 'K', linestyle = ':', label='A4x')
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
