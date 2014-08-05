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




''' 
Simple r�solution num�rique de l'�quation d'un oscillateur harmonique pour 
illustrer l'isochronisme des oscillations quelle que soit l'amplitude de d�part.
'''

import numpy as np               # Pour np.linspace
import scipy as sp               # Simple alias usuel
import scipy.integrate           # Pour l'int�gration
import matplotlib.pyplot as plt  # Pour les dessins

omega0 = 1   # On d�finit la pulsation propre

def equadiff(y,t):
    '''Renvoie l'action du syst�me dx/dt = vx et dvx/dt = -omega0**2 * x 
    soit bien l'oscillateur harmonique x'' + omega0**2 * x = 0'''
    x,vx = y                     # y contient position et vitesse
    return [vx,- omega0**2 * x]  # On renvoie un doublet pour [dx/dt,dvx/dt]

nb_CI = 10 # Nombre de conditions initiales explor�es

t = np.linspace(0,10,1000)       # Le temps total d'int�gration
x0= np.linspace(-5,5,nb_CI)      # Les positions initiales choisies
v0= [0]*nb_CI                    # Les vitesses  initiales choisies
    
for i in range(nb_CI):           # Pour chaque condition initiale
                                 # L'int�gration proprement dite
    sol = sp.integrate.odeint(equadiff,[x0[i],v0[i]],t)
    x = sol[:,0]                 # R�cup�ration de la position
    plt.plot(t,x)                # et affichage

# Il ne reste que le traitement cosm�tique

plt.title('Oscillateur harmonique pour differentes amplitudes initiales')
plt.ylabel('Position (unite arbitraire)')
plt.xlabel('Temps (unite arbitraire)')
plt.savefig('PNG/S01_oscillateur_harmonique_periode.png')



