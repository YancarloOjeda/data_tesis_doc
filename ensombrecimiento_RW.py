# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:10:51 2021

@author: yanoj
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
AlphaA = .5
AlphaX = .5
AlphaCTX = 0.2
Lambda = 1
Beta = 0.5
trial = 100
replica = 4 
auxReinforcer = 0
auxA = 0
tsReinforcer = 4
tsA = tsReinforcer - 0

A = np.zeros(trial)
X = np.zeros(trial)
CTX = np.zeros(trial)
V = np.zeros(trial)

#%% First simulation: AlphaA = .5 AlphaX = .5   
#Microtrials simulation
for i in range(trial):
    DVA = AlphaA * Beta * (Lambda - VTot)
    DVX = AlphaX * Beta * (Lambda - VTot)
    # DVCTX = AlphaCTX * Beta * (Lambda - VTot)
    DVTot = DVA + DVX # + DVCTX
    
    VA = VA + DVA
    VX = VX + DVX
    # VCTX = VCTX + DVCTX
    VTot = DVTot + VTot
    
    A[i] = VA
    X[i] = VX
    # CTX[i][j] = VCTX
    V[i] = VTot
 
x = np.arange(.99, trial)
fig, ax = plt.subplots()
plt.subplot(131)  
plt.errorbar(x, V, color = 'K', label=r'$V_T$')
plt.errorbar(x, A, color = 'K', linestyle=':', label=r'$V_A (\alpha_A = 0.5)$')
plt.errorbar(x, X, color = 'K', linestyle='--', label=r'$V_X (\alpha_X = 0.5)$')
plt.ylim(0,1)
plt.xlim(0,trial)
plt.legend(fontsize = 15, loc="upper right")
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_ticks_position('left')
# ax.set_xticklabels([])
# ax.xaxis.set_ticks_position('none')
# ax.set_yticklabels([])
# ax.yaxis.set_ticks_position('none')
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
plt.yticks(fontsize=15, weight='bold') 
plt.xticks(fontsize=15, weight='bold')
plt.ylabel('Fuerza asociativa', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})
plt.xlabel('Ensayos', fontdict={'family': 'Arial', 
                    'color' : 'k',
                    'weight': 'bold',
                    'size': 20})

#%% Second simulation: AlphaA = .5 AlphaX = .4  
AlphaX = .4
VA = 0
VX = 0
VCTX = 0
VTot = 0
DVA = 0
DVX = 0
DVCTX = 0
DVTot = 0
A = np.zeros(trial)
X = np.zeros(trial)
CTX = np.zeros(trial)
V = np.zeros(trial)
#Microtrials simulation
for i in range(trial):
    DVA = AlphaA * Beta * (Lambda - VTot)
    DVX = AlphaX * Beta * (Lambda - VTot)
    # DVCTX = AlphaCTX * Beta * (Lambda - VTot)
    DVTot = DVA + DVX # + DVCTX
    
    VA = VA + DVA
    VX = VX + DVX
    # VCTX = VCTX + DVCTX
    VTot = DVTot + VTot
    
    A[i] = VA
    X[i] = VX
    # CTX[i][j] = VCTX
    V[i] = VTot

plt.subplot(132)  
plt.errorbar(x, V, color = 'K', label=r'$V_T$')
plt.errorbar(x, A, color = 'K', linestyle=':', label=r'$V_A (\alpha_A = 0.5)$')
plt.errorbar(x, X, color = 'K', linestyle='--', label=r'$V_X (\alpha_X = 0.4)$')
plt.ylim(0,1)
plt.xlim(0,trial)
plt.legend(fontsize = 15, loc="upper right")
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')


#%% Third simulation: AlphaA = .5 AlphaX = .1  
AlphaX = .1
VA = 0
VX = 0
VCTX = 0
VTot = 0
DVA = 0
DVX = 0
DVCTX = 0
DVTot = 0
A = np.zeros(trial)
X = np.zeros(trial)
CTX = np.zeros(trial)
V = np.zeros(trial)
#Microtrials simulation
for i in range(trial):
    DVA = AlphaA * Beta * (Lambda - VTot)
    DVX = AlphaX * Beta * (Lambda - VTot)
    # DVCTX = AlphaCTX * Beta * (Lambda - VTot)
    DVTot = DVA + DVX # + DVCTX
    
    VA = VA + DVA
    VX = VX + DVX
    # VCTX = VCTX + DVCTX
    VTot = DVTot + VTot
    
    A[i] = VA
    X[i] = VX
    # CTX[i][j] = VCTX
    V[i] = VTot

plt.subplot(133)  
plt.errorbar(x, V, color = 'K', label=r'$V_T$')
plt.errorbar(x, A, color = 'K', linestyle=':', label=r'$V_A (\alpha_A = 0.5)$')
plt.errorbar(x, X, color = 'K', linestyle='--', label=r'$V_X (\alpha_X = 0.1)$')
plt.ylim(0,1)
plt.xlim(0,trial)
plt.legend(fontsize = 15, loc="upper right")
plt.yticks(fontsize=20) 
plt.xticks(fontsize=20)
ax = plt.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([])
ax.xaxis.set_ticks_position('none')
ax.set_yticklabels([])
ax.yaxis.set_ticks_position('none')