#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:31:56 2020

@author: Yancarlo Ojeda

Rescorla-Wagner model of conditioning 
07/07/2021
Make a difference respect the simulation show in the thesis. This is that I add a CTX stimulus 
In the simulation showed in thesis, I only put two stimulus, but I add this other to be what happen 
whit a CTX stimulus. The results are very similar, so I don't used CTX simulation. 
"""

import numpy as np
import matplotlib.pyplot as plt

VA = 0
VX = 0
VCTX = 0
VTot = 0
DVA = 0
DVX = 0
DVCTX = 0
DVTot = 0
AlphaA = 0
AlphaX = .4
AlphaCTX = 0.2
Lambda = 0
Beta = 0.5
trial = 100
replica = 4 
auxReinforcer = 0
auxA = 0
tsReinforcer = 4
tsA = tsReinforcer - 0

A = np.zeros((replica,trial))
X = np.zeros((replica,trial))
CTX = np.zeros((replica,trial))
V = np.zeros((replica,trial))

    
#Microtrials simulation
for i in range(replica):
    tsA = tsReinforcer - i
    VA = 0
    VX = 0
    VCTX = 0
    VTot = 0
    DVA = 0
    DVX = 0
    DVCTX = 0
    DVTot = 0
    
    for j in range(trial):
    
        if auxReinforcer < tsReinforcer:
            
            if auxA <= tsA: 
                AlphaA = 0.5
                Lambda = 0
                DVA = AlphaA * Beta * (Lambda - VTot)
                DVX = AlphaX * Beta * (Lambda - VTot)
                # DVCTX = AlphaCTX * Beta * (Lambda - VTot)
                DVTot = DVA + DVX #+ DVCTX 
                
                VA = VA + DVA
                VX = VX + DVX
                # VCTX = VCTX + DVCTX 
                VTot = DVTot + VTot
                
                A[i][j] = VA
                X[i][j] = VX
                # CTX[i][j] = VCTX
                V[i][j] = VTot
                
                auxA += 1
                # print('1')
                
            else:
                AlphaA = 0
                Lambda = 0
                DVA = AlphaA * Beta * (Lambda - VTot)
                DVX = AlphaX * Beta * (Lambda - VTot)
                # DVCTX = AlphaCTX * Beta * (Lambda - VTot)
                DVTot = DVA + DVX #+ DVCTX 
                
                VA = VA + DVA
                VX = VX + DVX
                # VCTX = VCTX + DVCTX
                VTot = DVTot + VTot 
                
                A[i][j] = VA
                X[i][j] = VX
                # CTX[i][j] = VCTX
                V[i][j] = VTot
                
                auxA += 1
            
            auxReinforcer += 1
                    
        else:
            Lambda = 1
            
            if auxA <= tsA:
                AlphaA = 0.5
                DVA = AlphaA * Beta * (Lambda - VTot)
                DVX = AlphaX * Beta * (Lambda - VTot)
                # DVCTX = AlphaCTX * Beta * (Lambda - VTot)
                DVTot = DVA + DVX # + DVCTX
                
                VA = VA + DVA
                VX = VX + DVX
                # VCTX = VCTX + DVCTX
                VTot = DVTot + VTot
                
                A[i][j] = VA
                X[i][j] = VX
                # CTX[i][j] = VCTX
                V[i][j] = VTot
                
                auxA = 0
                auxReinforcer = 0
            
            else:
                Lambda = 1
                AlphaA = 0
                DVA = AlphaA * Beta * (Lambda - VTot)
                DVX = AlphaX * Beta * (Lambda - VTot)
                # DVCTX = AlphaCTX * Beta * (Lambda - VTot)
                DVTot = DVA + DVX #+ DVCTX
                
                VA = VA + DVA
                VX = VX + DVX
                # VCTX = VCTX + DVCTX
                VTot = DVTot + VTot
                
                A[i][j] = VA
                X[i][j] = VX
                # CTX[i][j] = VCTX
                V[i][j] = VTot
                
                auxA = 0
                auxReinforcer = 0
                
            
            
        # print(i, auxA, AlphaA, AlphaX, Lambda)
        print(i, VTot, VA, VX) 

print(A)

x = np.arange(.99, trial)
fig, ax = plt.subplots()
plt.subplot(224)  
plt.errorbar(x, V[0][0:], color = 'K', label=r'$V_T$')
plt.errorbar(x, A[0][0:], color = 'K', linestyle=':', label=r'$V_A (\alpha_A = 0.5)$')
plt.errorbar(x, X[0][0:], color = 'K', linestyle='--', label=r'$V_X (\alpha_X = 0.4)$')
plt.ylim(-2,2)
plt.xlim(0,trial)
plt.legend(fontsize = 15)
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
plt.title(u'Ax', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',-2))
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')




plt.subplot(221)  
plt.errorbar(x, V[1][0:], color = 'K', label=r'$V_T$')
plt.errorbar(x, A[1][0:], color = 'K', linestyle=':', label=r'$V_A (\alpha_A = 0.5)$')
plt.errorbar(x, X[1][0:], color = 'K', linestyle='--', label=r'$V_X (\alpha_X = 0.4)$')
plt.ylim(-2,2)
plt.xlim(0,trial)
# plt.legend(fontsize = 15)
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
plt.title(u'A1x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',-2))
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')


plt.subplot(222)  
plt.errorbar(x, V[2][0:], color = 'K', label=r'$V_T$')
plt.errorbar(x, A[2][0:], color = 'K', linestyle=':', label=r'$V_A (\alpha_A = 0.5)$')
plt.errorbar(x, X[2][0:], color = 'K', linestyle='--', label=r'$V_X (\alpha_X = 0.4)$')
plt.ylim(-2,2)
plt.xlim(0,trial)
# plt.legend(fontsize = 15)
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
plt.title(u'A2x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',-2))
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')


plt.subplot(223)  
plt.errorbar(x, V[3][0:], color = 'K', label=r'$V_T$')
plt.errorbar(x, A[3][0:], color = 'K', linestyle=':', label=r'$V_A (\alpha_A = 0.5)$')
plt.errorbar(x, X[3][0:], color = 'K', linestyle='--', label=r'$V_X (\alpha_X = 0.4)$')
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',-2))
ax.yaxis.set_ticks_position('left')
plt.ylim(-2,2)
plt.xlim(0,trial)
# plt.legend(fontsize = 15)
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
plt.title(u'A3x', position=(0.15, 0.8),
          fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.yticks(fontsize=15, weight='bold') 
plt.xticks(fontsize=15, weight='bold')
plt.ylabel('Fuerza asociativa', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.xlabel('Microensayos', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})

