# coding: latin1

# Sauf mention explicite du contraire par la suite, ce travail a �t� fait par 
# Jean-Julien Fleck, professeur de physique/IPT en PCSI1 au lyc�e Kl�ber. 
# Vous �tes libres de le r�utiliser et de le modifier selon vos besoins.
# 
# Si l'encodage vous pose probl�me, vous pouvez r�encoder le fichier � l'aide 
# de la commande
# 
# recode l1..utf8 monfichier.py
# 
# Il faudra alors modifier la premi�re ligne en # coding: utf8
# pour que Python s'y retrouve.



""" 
Encore une illustration tir�e du livre "Dieu joue-t-il aux d�s ?" de Ian 
Stewart pour illustrer les doublements de p�riodes successifs dans les cycles 
limites de suites r�cursives � partir de l'application logistique 
x -> k*x*(1-x).
"""

import numpy as np
import matplotlib.pyplot as plt
import film

kmin,kmax = 2.9,4
ylim = None
# � essayer aussi:
# kmin = 3.9055
# kmax = 3.9068
# ylim = (0.48,0.52)

nb_points = 1000
k_list = np.linspace(kmin,kmax,nb_points)
iterations_avant_cycle = 1000
iterations_dans_cycle  = 100
u0 = 0.1



def f(x,k):
    return k*x*(1-x)

def get_cycle(k,u0):
    avant = np.zeros(iterations_avant_cycle)
    dans  = np.zeros(iterations_dans_cycle)
    tot = np.zeros(iterations_avant_cycle + iterations_dans_cycle)
    tot[0] = u0
    for i in range(1,len(tot)):
        tot[i] = f(tot[i-1],k)
    return tot[:iterations_avant_cycle],tot[iterations_avant_cycle:]

fig = plt.figure()
feigenbaum = fig.gca()

for k in k_list:
    avant,dans = get_cycle(k,u0)
    feigenbaum.plot([k]*len(dans),dans,'.k',markersize=1)

if ylim: feigenbaum.set_ylim(ylim)
feigenbaum.set_xlim(kmin,kmax)
fig.savefig('PNG/misc_feigenbaum.png')



