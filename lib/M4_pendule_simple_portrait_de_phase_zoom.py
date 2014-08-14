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




import numpy as np               # Bo�tes
import scipy as sp               # � outils
import scipy.integrate           # num�riques
import matplotlib.pyplot as plt  # Bo�te � outil graphique
# Pour le trac� des portraits de phase et les diagrammes �nerg�tiques
from portrait_de_phase import portrait_de_phase,diagramme_energetique

tmax = 10                        # Temps d'int�gration
nb_points = 500                  # Nombre d'instant �chantillonn�s
th0  = np.arange(-0.15,0.151,0.01)# Positions angulaires initiales
thp0 = np.array([0]*len(th0))    # Vitesses angulaires initiales
g,m,ell = 9.81,1,1               # Quelques constantes

# Pour avoir des couleurs qui changent et se correspondent
colors = ["blue","red","green","magenta","cyan","yellow",
          "darkblue","darkred","darkgreen","darkmagenta","darkcyan"]*10

def Em(th,thp):                  # Energie m�canique du pendule simple
    return m*g*ell*(1-np.cos(th)) +  0.5*m*(ell*thp)**2

def pendule(y,t):                # Equations d'�volution du pendule simple
    th,thp = y
    return [thp,-g/ell * np.sin(th)]

t = np.linspace(0,tmax,nb_points)# Echantillonnage en temps
th,thp = [],[]                   # Initialisation
for thi,thpi in zip(th0,thp0):   # On it�re sur les conditions initiales
    sol = sp.integrate.odeint(pendule,[thi,thpi],t) # Int�gration
    th.append(sol[:,0])          # Ajout des positions
    thp.append(sol[:,1])         # et vitesses correspondantes

fig = plt.figure(figsize=(10,10))# Cr�ation de la figure

th_lim = (np.min(th),np.max(th)) # Limites en theta
thp_lim=(np.min(thp),np.max(thp))# Limites en theta point
base_name='PNG/M4_pendule_simple_portrait_de_phase_zoom'

for i,ti in enumerate(t):        # Affichage progressif
    print(ti)                    # Un peu de feed back
    thi = [th_p[:i+1] for th_p in th]    # On ne prend que jusqu'�
    thpi= [thp_p[:i+1] for thp_p in thp] # l'instant pr�sent
    plt.suptitle('Pendule simple, $t={}$'.format(round(ti,2)))
    plt.subplot(2,1,1)           # Sous-figure du haut
    portrait_de_phase(thi,thpi,fantome=20,clearfig=False,
                      color=colors,xlim=th_lim,ylim=thp_lim)
    plt.xlabel('')
    plt.subplot(2,1,2)           # Sous-figure du bas
    diagramme_energetique(thi,thpi,Em,color=colors,clearfig=False,fantome=20,xlim=th_lim)
    plt.savefig('{}_{:04d}.png'.format(base_name,i))
    plt.clf()                    # Nettoyage

from film import make_film       # Bo�te � outil pour faire un film

make_film(base_name)             # et appel effectif



