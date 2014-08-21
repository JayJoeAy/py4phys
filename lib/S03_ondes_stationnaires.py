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
Mise en place d'ondes stationnaires par superposition d'ondes qui se propagent 
dans les deux sens
"""

import numpy as np              # Bo�te � outils num�riques
import matplotlib.pyplot as plt # Bo�te � outils graphiques
import film                     # Bo�te � outils vid�os

def source(x,t,x0=0,phi=0):
    '''La fonction repr�sentant notre source situ�e en x0.'''
    k,w = 5,1                        # Quelques constantes 
    r = np.sqrt((x-x0)**2)           # La distance � la source
    u = k*r - w*t + phi              # La variable de d�placement
    res =  np.sin(u)                 # Simple sinus
    res[u > 0] = 0.0                 # Pour s'assurer qu'� t<0, il n'y a pas d'onde
    return res

x2  = 5                    # Position de la deuxi�me source (premi�re en 0)
xmin,xmax = 0,x2           # Limites de la fen�tre d'�chantillonnage
nb_points = 1000           # Nombre de points d'�chantillonnage
phi = np.pi/2              # D�phasage de la deuxi�me source
tmin,tmax = 0,60           # L'intervalle de temps d'�tude
dt = 0.1                   # Incr�ment de temps

base_name = 'PNG/S03_ondes_stationnaires'

t = tmin
i = 0
while t < tmax:
    print(t)
    x = np.linspace(xmin,xmax,nb_points)
    S1 = source(x,t,0)
    S2 = source(x,t,x2,phi)
    S =  S1+S2
    plt.plot(x,S1,alpha=0.5)
    plt.plot(x,S2,alpha=0.5)
    plt.plot(x,S,'k',linewidth=2)
    plt.ylim(-2,2)
    plt.savefig(base_name + '_{:04d}.png'.format(i))
    plt.clf()
    i+= 1
    t+=dt

film.make_film(base_name)  # Fabrication du film � la fin



