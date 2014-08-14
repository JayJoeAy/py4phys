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
Portrait de phase d'un oscillateur de Landau (bille libre de se d�placer sur 
une barre horizontale retenue par un ressort accroch� � une distance d � la 
verticale de l'origine) tilt� d'un angle alpha par rapport � la verticale 
(alpha=90� correspondrait au cas sym�trique "habituel")
"""

import numpy as np                # Les bo�tes
import scipy as sp                # � outils
import scipy.integrate            # num�riques
import matplotlib.pyplot as plt   # La bo�te � outils graphiques
# Pour les portraits de phase
from portrait_de_phase import portrait_de_phase,diagramme_energetique

tmax = 40                         # Temps d'int�gration
nb_points = 2000                  # Nb de point pour l'�chantillonnage en temps
x0 = np.arange(-8,8.1,0.79999999) # Positions initiales
v0 = np.array([0]*len(x0))        # Vitesses initiales (nulles)
k,m,d,ell0,g = 1,1,3,5,1          # Quelques constantes
alpha = np.radians(90-20)         # L'angle de 'tilt'

colors = ["blue","red","green","magenta","cyan","yellow",
          "darkblue","darkred","darkgreen","darkmagenta","darkcyan"]*10

def landau(y,t):                  # �quation d'�volution
    x,v = y
    return [v,-m*g*np.cos(alpha) -
              k*(x-d*np.cos(alpha))/m*
              (np.sqrt(d**2+x**2-2*x*d*np.cos(alpha))-ell0)/
              (np.sqrt(d**2+x**2-2*x*d*np.cos(alpha)))]

def Em(x,v):                      # �nergie m�canique
    return 0.5*k*(np.sqrt(x**2+d**2-2*x*d*np.cos(alpha)) - ell0)**2 +            m*g*x*np.cos(alpha) + 0.5*m*v**2

t = np.linspace(0,tmax,nb_points) # �chantillonnage en temps
x,v = [],[]                       # Initialisation
for xi,vi in zip(x0,v0):          # It�ration sur les conditions initiales
    print(xi,vi)                  # Un peu de feedback
    sol = sp.integrate.odeint(landau,[xi,vi],t) # On int�gre
    x.append(sol[:,0])            # et on stocke � la fois les positions
    v.append(sol[:,1])            # et les vitesses

fig = plt.figure(figsize=(10,10)) # Cr�ation de la figure

vlim = (np.min(v),np.max(v))      # Limites verticales (horizontales impos�es par les CI)
base_name='PNG/M4_oscillateur_de_landau_tilte_portrait_de_phase'

for i,ti in enumerate(t):         # On regarde � chaque instant d'int�gration
    print(ti)                     # Un peu de feedback
    xi = [xp[:i+1] for xp in x]   # On stocke l'avancement
    vi = [vp[:i+1] for vp in v]   # jusqu'� l'instant pr�sent
    plt.suptitle('Oscillateur de Landau tilte, $t={}$'.format(round(ti,2)))
    plt.subplot(2,1,1)            # Premi�re sous-figure
    portrait_de_phase(xi,vi,fantome=50,clearfig=False,color=colors,ylim=vlim)
    plt.xlabel('')
    plt.subplot(2,1,2)            # Seconde sous-figure
    diagramme_energetique(xi,vi,Em,color=colors,clearfig=False,fantome=50)
    plt.savefig('{}_{:04d}.png'.format(base_name,i))
    plt.clf()

from film import make_film        # Bo�te � outil visuelle

make_film(base_name)              # et fabrication du film correspondant



