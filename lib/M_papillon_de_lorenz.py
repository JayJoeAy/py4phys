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
Animation montrant l'apparition de l'attracteur �trange dit du "papillon 
de Lorenz" (NB: ce n'est pas le Lorentz des transformations relativistes: il 
n'a pas de 't'), qui correspond � la solution du syst�me diff�rentiel
	dx/dt = a*(y-x)
	dy/dt = b*x - y - x*z
	dz/dt =-c*z + x*y
Les valeurs "simple" de (a,b,c) qui m�nent au chaos sont (10,28,8/3).
On va essayer d'illustrer deux ph�nom�nes diff�rents: la sensibilit� aux 
conditions initiales et le fait qu'un certain ordre se cache tout de m�me dans 
le chaos (voir Ian Stewart, Dieu joue-t-il aux d�s, p196 et suivantes pour 
plus de d�tails)
"""

import numpy as np              # Bo�te � outils num�rique
import scipy as sp
import scipy.integrate          # Pour l'int�gration num�rique
import matplotlib.pyplot as plt # Bo�te � outil graphique

# N�cessaire pour la 3D, m�me si cela n'appara�t pas explicitement
from mpl_toolkits.mplot3d import Axes3D 

tmax = 30                       # Tfinal d'int�gration
nb_points = 3000                # Nombre de points pour l'�chantillonnage en t
yvect0 = np.array([1.0,1.0,1.0])# Position initiale (x,y,z)
ecart_relatif = 0.01            # �cart relatif des deux positions initiales

def systeme_de_Lorenz(yvect,t): # Syst�me diff�rentiel � int�grer
    a,b,c = 10,28,8/3.0         # Les constantes du syst�me
    x,y,z = yvect               # Les variables
    return [a*(y-x),b*x-y-x*z,-c*z+x*y]

# �chantillonnage en temps et int�gration num�rique
t = np.linspace(0,tmax,nb_points)
sol1 = sp.integrate.odeint(systeme_de_Lorenz,yvect0,t)
sol2 = sp.integrate.odeint(systeme_de_Lorenz,yvect0*(1+ecart_relatif),t)

# R�cup�ration des positions pour les deux solutions recherch�es
X1,Y1,Z1 = sol1[:,0],sol1[:,1],sol1[:,2]
X2,Y2,Z2 = sol2[:,0],sol2[:,1],sol2[:,2]

# D�tection des maximum dans l'id�e de repr�senter la position d'un maximum en 
# fonction de la position du maximum pr�c�dent pour Z -> l'ordre dans le chaos!
def trouve_positions_maximums(X):
    """ Renvoie la liste des indices correspondant aux maximums de la liste X 
    fournie en param�tre. """
    positions = []
    for i in range(1,len(X)-1):
        if X[i] > X[i-1] and X[i] > X[i+1]:
            positions.append(i)
    return positions



def both_plot(ax,X1,Y1,X2,Y2):
    ax.plot(X1,Y1,'b',X2,Y2,'r')               # Les deux trac�s continus
    ax.plot(X1[-1],Y1[-1],'o',color='cyan')    # Dernier point premier trac�
    ax.plot(X2[-1],Y2[-1],'o',color='magenta') # Dernier point second trac�
    

def fait_plot(X,Y,Z,Xp,Yp,Zp,t,i): # Routine pour faire le plot effectif
    ax1 = fig.add_subplot(2,4,1)   # Sous-figure 1 (en haut � gauche)
    both_plot(ax1,X,Z,Xp,Zp)       # Trac�
    plt.xlabel('X')                # Labels
    plt.ylabel('Z')
    plt.xlim(-20,20)               # et limites 
    plt.ylim(0,50)
    ax2 = fig.add_subplot(2,4,2)   # Sous-figure 2 (en haut au milieu)
    both_plot(ax2,Y,Z,Yp,Zp)       # Trac�
    plt.xlabel('Y')                # Labels
    plt.ylabel('Z') 
    plt.xlim(-30,30)               # et limites
    plt.ylim(0,50)
    ax3 = fig.add_subplot(2,4,6)   # Sous-figure 6 (en bas au milieu)
    both_plot(ax3,Y,X,Yp,Xp)       # Trac�
    plt.xlabel('Y')                # Labels
    plt.ylabel('X')
    plt.ylim(-20,20)               # et limites
    plt.xlim(-30,30)
    ax4 = fig.add_subplot(2,4,5)   # Sous-figure 5 (en bas � gauche)
    # On cherche les maxima de Z et, si on en a trouv�, on trace le maximum 
    # courant en fonction du pr�c�dent
    pos = trouve_positions_maximums(Z)
    if len(pos) > 1: ax4.plot(Z[pos[:-1]], Z[pos[1:]], 'b.')
    if len(pos) > 0: ax4.plot(Z[pos[-1]] , Z[-1], 'o', color='cyan')
    # Pareil pour la 2e condition initiale
    pos = trouve_positions_maximums(Zp)
    if len(pos) > 1: ax4.plot(Zp[pos[:-1]],Zp[pos[1:]],'r.')
    if len(pos) > 0: ax4.plot(Zp[pos[-1]] ,Zp[-1], 'o', color='magenta')
    plt.xlabel('Z$_k$')            # Labels
    plt.ylabel('Z$_{k+1}$')
    plt.ylim(25,50)                # et limites
    # La derni�re sous-figure occupe les 4 carr�s de droite
    ax5 = plt.subplot2grid((2,4),(0,2),colspan=2,rowspan=2,projection='3d')
    ax5.set_xlabel('X')            # Labels
    ax5.set_ylabel('Y')
    ax5.set_zlabel('Z')
    ax5.set_xlim(-20,20)           # Limites
    ax5.set_ylim(-30,30)
    ax5.set_zlim(0,50)
    ax5.plot(X,Y,Z,'b')            # et trac�s
    ax5.plot(Xp,Yp,Zp,'r')
    ax5.plot([X[-1]],[Y[-1]],[Z[-1]],'o', color='cyan')
    ax5.plot([Xp[-1]],[Yp[-1]],[Zp[-1]],'o', color='magenta')
    # On modifie l'angle de vue au fur et � mesure
    ax5.view_init(elev=10,azim=i%360)
    # Titre global de la figure
    plt.suptitle('Papillon de Lorenz, $t={}$'.format(t))
    # Sauvegarde et nettoyage
    plt.savefig('{}{:05d}.png'.format(base_name,i))
    plt.clf()

# Le programme proprement dit

base_name = 'PNG/M_papillon_de_lorenz_' # Nom des figures

fig = plt.figure(figsize=(16,8))        # D�finition de la figure

# For debugging purposes
#i = 1000
#fait_plot(X1[:i],Y1[:i],Z1[:i],X2[:i],Y2[:i],Z2[:i],round(t[i],3),i)


for i in range(5,len(t)):  # La ronde des images
    print(i)
    fait_plot(X1[:i],Y1[:i],Z1[:i],X2[:i],Y2[:i],Z2[:i],round(t[i],2),i)

# Ne reste plus qu'� rassembler en un fichier mpeg � l'aide de convert puis de
# ppmtoy4m et mpeg2enc (paquet mjpegtools � installer sur la machine)
    
import os

cmd = '(for f in ' + base_name + '*png ; '
cmd+= 'do convert -density 100x100 $f -depth 8 -resize 1200x600 PNM:- ; done)'
cmd+= ' | ppmtoy4m -S 420mpeg2'
cmd+= ' |  mpeg2enc -f1 -b 12000 -q7 -G 30 -o {}film.mpeg'.format(base_name)

print("Execution de la commande de conversion")
print(cmd)
os.system(cmd)
print("Fin de la commande de conversion")



