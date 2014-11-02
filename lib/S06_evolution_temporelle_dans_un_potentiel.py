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

Le programme suivant est quasiment enti�rement repris depuis le MOOC 
Statistical Mechanics: Algorithms and Computations de Werner Krauth (ENS) avec 
la participation de Micha�l Kopf, Vivien Lecomte et Alberto Rosso.

Le programme a �t� adapt� d'un programme fourni dans le tutorial 5 concernant 
l'�volution temporelle (en partant du concept de "temps imaginaire") en 
m�canique quantique.

L'id�e est de partir de la fonction d'onde et de lui appliquer le formalisme 
d'�volution � partir d'op�rateur exponentiels faisant intervenir � la fois le 
potentiel V(x) dans lequel on place la particule (cas des multiplications 
simples) et le hamiltonien de la particule libre (H_free = p^2/2m).

Tout ceci est extr�mement bien expliqu� dans le tutorial 5 du MOOC � suivre 
sur la page https://www.coursera.org/course/smac

Bien s�r tout ceci est normalis� de sorte que hbar=1 et m=1

"""

import numpy as np               # Bo�te � outils num�riques
import scipy as sp               # Simple alias
import scipy.integrate           # Pour l'int�gration (cumtrapz)
import matplotlib.pyplot as plt  # Bo�te � outils graphiques
from matplotlib import animation # Pour l'animation progressive

def funct_potential(x):
    """ 
    Le potentiel dans lequel est plong� la particule. On fournit plusieurs 
    types de potentiel, il suffit de commenter/d�commenter les zones 
    int�ressantes pour changer selon les besoins.
    """
    # Potentiel de la bo�te ferm�e:
    #if abs(x) > 3: return 1e150 # Presque l'infini...
    #else:  return 0.0
    #
    # Potentiel pour voir l'effet tunnel
    if x < -3: return 1e150
    elif 3 <= x <= 4: return 1.0
    else: return 0.0
    #
    # Potentiel pour un oscillateur harmonique
    #return x**2/9

steps = 500     # Echantillonnage en x et p
x_min,x_max = -5.0,30.0
affiche_xmin,affiche_xmax =-5,10 # On r�duit l'affichage pour �viter les effets de bords
grid_x, dx = np.linspace(x_min, x_max, steps, retstep = True) # Grille des valeurs en x
p_max = 1/dx
p_min = -p_max
grid_p, dp = np.linspace(p_min, p_max, steps, retstep = True) # ainsi qu'en p
delta_t = 0.01  # Pas de temps
t = 0
nb_images = 10000


# �chantillonage du potentiel utilis�
potential = np.array([funct_potential(x) for x in grid_x])

# D�finition de la fonction d'onde que l'on va faire �voluer temporellement 
# par la suite. Ici, on donne l'exemple d'une combinaison de deux �tats 
# propres du puit infini. (� changer si vous changer de potentiel...)

psi = np.sin(np.pi*(grid_x+3)/6) + np.sin(2*np.pi*(grid_x+3)/6)
psi[abs(grid_x)>3] = 0.0  # La fonction d'onde est nulle en dehors du puit infini
norm = ((np.abs(psi)**2).sum() * dx)
psi /= norm**0.5  # Normalisation (ne pas oublier la racine...)

def fourier_x_to_p(phi_x, dx):
    """ 
    Transform�e de Fourier de la fonction d'onde psi(x) 
    Ne pas oublier de d�finir grid_x et grid_p "accordingly" et en variables globales.
    """
    phi_p = [(phi_x * np.exp(-1j * p * grid_x)).sum() * dx for p in grid_p]
    return np.array(phi_p)

def fourier_p_to_x(phi_p, dp):
    """ 
    Transform�e de Fourier inverse de la fonction d'onde hat{psi}(p) dans le 
    domaine impulsionnel.    
    Ne pas oublier de d�finir grid_x et grid_p "accordingly" et en variables globales.
    """
    phi_x = [(phi_p * np.exp(1j * x * grid_p)).sum() for x in grid_x]
    return np.array(phi_x) /  (2.0 * np.pi)

def time_step_evolution(psi0, potential, grid_x, grid_p, dx, dp, delta_t):
    """ 
    �volution temporelle proprement dite. On utilise l'approximation

    psi(t+dt) = exp(-i*dt*V(x)/2) * exp(-i*dt*H_free) * exp(-i*dt*V(x)/2) * psi(t)

    Voir tutorial 5 du MOOC https://www.coursera.org/course/smac pour le 
    d�tail des explications.
    """
    psi0 = np.exp(-1j * potential * delta_t / 2.0) * psi0  # Multiplication r�elle
    psi0 = fourier_x_to_p(psi0, dx)                        # Passage dans le domaine impulsionnel
    psi0 = np.exp(-1j * grid_p**2 * delta_t / 2.0) * psi0  # O� H est simple ! (p^2/2m)
    psi0 = fourier_p_to_x(psi0, dp)                        # Repassage en coordonn�es r�elles
    psi0 = np.exp(-1j * potential * delta_t / 2.0) * psi0  # donc simple multiplication 
    norm = ((np.abs(psi0)**2).sum() * dx) # On renormalise (pour �viter les d�rives?)
    psi0/= norm**0.5
    return psi0  # Renvoi de la fonction d'onde


# D�finition de la figure (on fait deux "axes" de sorte � mettre deux �chelles 
# gradu�es, une pour la fonction d'onde et l'autre pour le potentiel)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()         # Making an evil twin :o)
#ax2 = ax1
# On dessine la fonction d'onde sur l'axe de gauche (ax1)
psi_line, = ax1.plot(grid_x, np.abs(psi)**2, 'g', linewidth = 2.0, label = '$|\psi(x)|^2$')
#ax1.set_xlim(-6, 6)
ax1.set_ylim(0, max(np.abs(psi)**2)*1.5)
plt.xlim((affiche_xmin,affiche_xmax))
ax1.set_xlabel('$x$', fontsize = 20)
ax1.set_ylabel('Densite de probabilite $|\psi|^2$')
ax1.legend(loc=2)
# En revanche, on fait le potentiel sur l'axe de droite (ax2)
ax2.plot(grid_x, potential, 'k', linewidth = 2.0, label = '$V(x)$')
ax2.set_ylabel('Potentiel')
ax2.set_ylim(0, max(np.abs(psi)**2)*1.5)
ax2.set_ylim(0,2)
plt.title('time = {}'.format(t))
plt.legend(loc=1)

def init():
    pass

def animate(i):
    global psi
    t = i*delta_t
    psi = time_step_evolution(psi, potential, grid_x, grid_p, dx, dp, delta_t)
    # Je n'arrive pas � comprendre pourquoi une fois sur deux on se r�cup�re 
    # une facteur correctif de 3600... Ca ne semble pas d�pendre du nombre de 
    # points d'�chantillonnage, ni de l'extension de l'intervalle initial en 
    # x. Le probl�me est d�j� pr�sent sur les fichiers propos�s par le MOOC de 
    # l'ENS, mais ils ont gentiment mis cela sous le tapis en ne prenant 
    # qu'une image sur 4...
    #if i%2 == 0: 
    #    psi_line.set_ydata(np.abs(psi)**2)
    #else:
    #    correction = 3*1e3*1.2
    #    correction = 1
    #    psi_line.set_ydata(np.abs(psi)**2*correction)
    # Trouv� !!! C'est la normalisation � qui il manquait une racine 
    # (forc�ment, on normalisait avec la somme des psi**2, il fallait bien 
    # prendre la racine...). Donc plus besoin de correction :o)
    psi_line.set_ydata(np.abs(psi)**2)
    plt.title('time = {}'.format(t))
    

# L'animation proprement dite
anim = animation.FuncAnimation(fig,animate,frames=nb_images,interval=33)

plt.show()



