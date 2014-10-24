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
Travail inspir� � la fois par un script de Vincent Grenard (PCSI, Lyc�e 
Poincar�, Nancy) et un autre de Jean-Pierre Simond (MPSI, Lyc�e Kl�ber, 
Strasbourg).

L'id�e est de pr�senter une animation de ce qui se passe quand on envoie des 
photons un par un dans un syst�me de deux fentes fines.

"""




import numpy as np               # Bo�te � outils num�riques
import random as rd              # Tirages al�atoire par loi uniforme
import scipy as sp               # Simple alias
import scipy.interpolate         # Pour l'interpolation (interp1d)
import scipy.integrate           # Pour l'int�gration (cumtrapz et quad)
import matplotlib.pyplot as plt  # Bo�te � outils graphiques
from matplotlib import animation # Pour l'animation progressive

####################################################
Xmin=-3 ; Xmax=3
Ymin=-1 ; Ymax=1
extent = Xmin,Xmax,Ymin,Ymax
Xpixel=50 #Nombre de pixels selon X
Ypixel=50 #Nombre de pixels selon Y
Nbre_Photons=10000

####################################################
# Densite de probabilite en x, elle est uniforme sur y (donc directement 
# donn�e par rd.random()).

# Profil voulu (non normalis�)

def pb(x):
    return (1 + np.cos(2*np.pi*x)) * (np.sin(x)/(x+1e-4))**2

# Normalisation (calcul�e � part pour �conomiser des calculs)
pb_norm = sp.integrate.quad(pb,Xmin,Xmax)[0]

# Probabilit� normalis�e
def p(x): return pb(x) / pb_norm

X = np.linspace(Xmin,Xmax,10000)
pX= p(X)
PX= sp.integrate.cumtrapz(pX,X,initial=0)  # Densite de probabilite cumulee en x
# La fonction r�ciproque (cf le TP09 sur pcsi.kleber.free.fr/IPT/)
HX= lambda x: float(sp.interpolate.interp1d(PX,X)(x))

plt.plot(X,PX)
plt.plot(X,pX)
plt.show()

####################################################
#initialisation des listes des positions des photons
ListeX=[]
ListeY=[]
#Tirage des valeurs de x et y pour tous les photons
for i in range(Nbre_Photons):
    # Tirage des valeurs de x et y que l'on range dans deux listes:
    # * x par la m�thode de l'ant�c�dent � partir d'une distribution uniforme 
    # pr�sent�e dans le TP09 sur pcsi.kleber.free.fr/IPT/
    alea=rd.random()
    ListeX.append(HX(alea))
    # * y par une simple distribution uniforme
    ListeY.append(Ymin+(Ymax-Ymin)*rd.random())
# Conversion en np.array pour les facilit�s de slicing
ListeX = np.array(ListeX)
ListeY = np.array(ListeY)

# La figure globale
fig = plt.figure(figsize=(8,7.76))
# L'image des interf�rences
ax1= plt.subplot2grid((3,3),(0,0),colspan=2,rowspan=2)
Image = np.zeros((Xpixel,Ypixel))
im = ax1.imshow(Image,cmap='gray',extent=extent,aspect='auto')
plt.ylabel('$y$')
# La figure du bas
ax2= plt.subplot2grid((3,3),(2,0),colspan=2,sharex=ax1)
plt.xlabel('$x$')
histX = plt.hist([1,0,1],bins=Xpixel,range=(Xmin,Xmax))

# La figure de droite
ax3= plt.subplot2grid((3,3),(0,2),rowspan=2,sharey=ax1)
histY = plt.hist([1,0,1],bins=Ypixel,orientation='horizontal',range=(Ymin,Ymax))

histY[0][10] = 4
histY[-1][10].set_width(histY[0][10])
ax3.set_xlim(min(histY[0]),max(histY[0]))
print(histY)


def init():
    im.set_data(Image)
    im.set_vmin(0)

dN = 1
N  = 1
    
def animate(i):
    global N,dN
    if i == 100: dN = 10
    if i == 200: dN = 100
    N += dN
    if N < Nbre_Photons:
        ax1.set_title('{} photons'.format(N))
        for j in range(dN):
            # Calcul de la Position X et Y du photon re�u (en pixel)
            # C'est un facteur d'�chelle pour passer de [Xmin,Xmax] � [0,Xpixel]
            PositionX=int(Xpixel*(ListeX[N-j]-Xmin)/(Xmax-Xmin))
            # Pareil en Y
            PositionY=int(Ypixel*(ListeY[N-j]-Ymin)/(Ymax-Ymin))
            # Incr�mentation de la valeur du pixel o� arrive le photon.
            Image[PositionY][PositionX]+=1
        im.set_data(Image)
        im.autoscale()
        # On refait les histogrammes
        ax2.clear()
        ax2.hist(ListeX[:N+1],bins=Xpixel,range=(Xmin,Xmax))
        ax3.clear()
        ax3.hist(ListeY[:N+1],bins=Ypixel,orientation='horizontal',range=(Ymin,Ymax))

anim = animation.FuncAnimation(fig,animate,frames=Nbre_Photons,interval=1)

plt.show()



