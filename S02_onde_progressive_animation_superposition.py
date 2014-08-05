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
Animation montrant la propagation de trois ondes de profil identique mais de 
vitesse diff�rente ainsi que leur superposition. Peut servir � illustrer 
qualitativement la notion d'�talement du paquet d'onde.
'''

import numpy as np               # Pour np.linspace, np.exp et np.cos
import matplotlib.pyplot as plt  # Pour les dessins


def f(u,k=10):
    '''Le profil de l'onde � propager: une gaussienne multipli�e par un cosinus.'''
    return np.exp(-3*u**2) * np.cos(k*u-5)

nb_points  = 1000   # Le nombre de points d'�chantillonnage du graphe
nb_courbes = 3      # Le nombre de courbes � repr�senter
nb_images  = 151    # Le nombre d'images � cr�er.
c = np.linspace(0.1,0.3,nb_courbes) # Les diff�rentes vitesses de propagation

# On fait une visualisation spatiale

x = np.linspace(- 4, 4,nb_points)   # Echantillonnage en position
t = np.linspace(-15,15,nb_images)   # On regarde le profil � diff�rents temps

base_name = 'PNG/S02_onde_progressive_superposition_'

for i,ti in enumerate(t):
    plt.subplot(211)              # La premi�re sous-figure
    plt.ylim(-3,3)                # et ses limitations
    plt.ylabel("Profil de l'onde")# ainsi que le label des ordonn�es
    plt.title('Profil spatial pour $t={}$'.format(round(ti,2)))
    ftot = np.zeros(len(x))       # Initialisation du signal superpos�
    for cj in c:                  # On regarde chaque vitesse
        fi = f(x-cj*ti) # Echantillonnage du profil pour les diff�rents x
        plt.plot(x,fi)  # Affichage
        ftot += fi      # On ajoute � l'onde totale
    plt.subplot(212)              # La seconde sous-figure
    plt.ylim(-3,3)                # et ses limitations
    plt.ylabel("Profil de l'onde")# ainsi que le label des ordonn�es
    plt.plot(x,ftot)              # Affichage du signal superpos�
    plt.xlabel('Position $x$')    # et label des abscisses
    fichier = base_name + '{:03d}'.format(i)
    plt.savefig(fichier)          # On sauvegarde un fichier par temps
    plt.clf()                     # et on nettoie pour le suivant
    
# Ne reste plus qu'� rassembler en un fichier gif � l'aide de convert

import subprocess

cmd = "convert -delay 1 -dispose Background +page {}".format(base_name + '*.png')
cmd+= " -loop 0 {}".format(base_name + 'film.gif') 

print("Execution de la commande de conversion")
print(cmd)
p = subprocess.Popen(cmd, shell=True)
print("Fin de la commande de conversion")


