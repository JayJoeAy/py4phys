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
Illustration du ph�nom�ne de propagation vers la droite d'une onde de forme 
quelconque � la fois au cours du temps dans un profil spatial, et spatialement 
dans un profil temporel.
'''

import numpy as np               # Pour np.linspace, np.exp et np.cos
import matplotlib.pyplot as plt  # Pour les dessins


def f(u,k=10):
    '''Le profil de l'onde � propager: une gaussienne multipli�e par un cosinus.'''
    return np.exp(-3*u**2) * np.cos(k*u-5)

nb_points  = 1000   # Le nombre de points d'�chantillonnage du graphe
nb_courbes = 3      # Le nombre de courbes � repr�senter

# Tout d'abord la visualisation spatiale

x = np.linspace(-2,2,nb_points)   # Echantillonnage en position
t = np.linspace(0,5,nb_courbes)  # On regarde le profil � diff�rents temps
c = 0.2 # Vitesse de propagation de l'onde

for ti in t:
    fi = f(x-c*ti) # Echantillonnage du profil pour les diff�rents x
    plt.plot(x,fi,label='$t={}$'.format(round(ti,1))) # Affichage

# La cosm�tique

plt.title('Profil spatial pour differents temps')
plt.xlabel('Position $x$')
plt.ylabel("Profil de l'onde")
plt.legend()
plt.savefig('PNG/S02_onde_progressive_spatial.png')
plt.clf()

# Tout d'abord la visualisation spatiale

t = np.linspace(0,10,nb_points)  # Echantillonnage en temps
x = np.linspace(0,0.6,nb_courbes)  # On regarde le profil � diff�rentes positions
c = 0.2 # Vitesse de propagation de l'onde

for xi in x:
    fi = f(xi-c*t) # Echantillonnage du profil pour les diff�rents t
    plt.plot(t,fi,label='$x={}$'.format(round(xi,1))) # Affichage

# La cosm�tique

plt.title('Profil temporel pour differente positions')
plt.xlabel('Temps $t$')
plt.ylabel("Profil de l'onde")
plt.legend()
plt.savefig('PNG/S02_onde_progressive_temporel.png')
plt.clf()    



