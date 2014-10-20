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




""" Programme qui fait �voluer des points repr�sentatifs des cr�tes d'un front 
d'onde au passage d'une interface en modifiant la vitesse de propagation mais 
pas la direction => le front d'onde change naturellement de direction."""

import numpy as np               # Bo�te � outils num�riques
import matplotlib.pyplot as plt  # Bo�te � outils graphiques
from matplotlib import animation # Pour l'animation progressive

angle_incident = np.pi/6         # Angle incident par rapport � la normale (x=0)
extension = 10                   # Taille de l'image
c1 = 2                           # Vitesse dans le milieu du bas
c2 = 5                           # Vitesse dans le milieu du haut
dt = 0.01                        # Pas de temps entre deux images

fig = plt.figure(figsize=(10,10))# Cr�ation de la figure

plt.ylim((-extension,extension)) # On met � la bonne taille en y
plt.xlim((-extension,extension)) # et en x

# Trac� de la ligne de s�paration
plt.plot([-extension,extension],[0,0],'b',linewidth=4)

# La pente initiale des suites de particules
a = np.sin(angle_incident) / np.cos(angle_incident)
y0= 0           # La distribution des points commence en y0
dX= 0.2         # avec un certain �cart horizontal (m�me ligne de cr�te)
dY= 2           # et un �cart vertical (entre deux lignes de cr�te)
X = []          # Ensemble des coordonn�es x
Y = []          # et y des points trouv�s
while y0 > -extension:  # R�partition de tout ces points
    y = y0
    x = -extension
    while y >= -extension:
        X.append(x)
        Y.append(y)
        y -= a*dX
        x += dX
    y0 -= dY

X = np.array(X) # Transformation en array
Y = np.array(Y) # pour faciliter les calculs suivants

positions, = plt.plot(X,Y,'ro',markersize=5) # Affichage initial des positions

def init():     # Pas de travail particulier pour l'initialisation
    pass


def animate(i):
    # � chaque pas de temps, on avance d'une petite distance en x et en y qui 
    # va d�pendre de savoir si on est du c�t� du milieu 1 (y<0) ou du c�t� du 
    # milieu 2 (y>0).
    X[Y >=0] += c2*np.sin(angle_incident)*dt
    X[Y < 0] += c1*np.sin(angle_incident)*dt
    Y[Y >=0] += c2*np.cos(angle_incident)*dt
    Y[Y < 0] += c1*np.cos(angle_incident)*dt
    positions.set_xdata(X)
    positions.set_ydata(Y)

# Objet d'animation
anim = animation.FuncAnimation(fig,animate,frames=1000,interval=20)

# Affichage de l'animation proprement dite.
plt.show()



