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
� nouveau pour une question de cours: des diagrammes en amplitudes et �chelle 
lin�aire en pulsation. Le but pour les �l�ves est de savoir retrouver Q et w0 
� partir de ces donn�es (comme en TP).
'''

import numpy as np                    # Pour l'�chantillonage
import matplotlib.pyplot as plt       # Pour les dessins
import math                           # Fonctions math�matiques
import cmath                          # et calculs en complexes

A = 3                                 # Amplitude globale des mesures
wmin = 0.1                            # Pulsation minimale �chantillonn�e
wmax = 300                            # Pulsation maximale
nb_points = 20                        # nombre de points de "mesure"
w = np.linspace(wmin,wmax,nb_points)  # �chantillonage effectif

def H(w,w0,Q):
    '''Fonction de transfert pour un passe bas du second ordre'''
    return A/(1-(w/w0)**2 + 1j*w/(Q*w0))


def Z0(w,w0,Q):
    '''Amplitude de la fonction de transfert.'''
    return abs(H(w,w0,Q))

def phi(w,w0,Q):
    '''Phase de la fonction de transfert (en degr�s).'''
    return cmath.phase(H(w,w0,Q))*180/math.pi

def amplitude_et_phase(w0,Q,base_fichier):
    '''Le dessin proprement dit'''
    plt.plot(w,[phi(wi,w0,Q) for wi in w],'o')     # �chantillonage de la phase
    plt.xlabel(r'$\omega$ en rad.s$^{-1}$')        # L�gende en abscisse
    plt.ylabel(r'$\varphi$ en degres')             # L�gende en ordonn�e
    plt.title('Dependance en phase')               # Titre
    plt.grid(which='both')                         # La grille
    plt.savefig(base_fichier + '_phase.png')       # Sauvegarde
    plt.clf()                                      # Nettoyage
    plt.plot(w,[Z0(wi,w0,Q) for wi in w],'o')      # On repart sur l'amplitude
    plt.xlabel(r'$\omega$ en rad.s$^{-1}$')        # L�gende en abscisse
    plt.ylabel(r'Amplitude des oscillations en cm')# L�gende en ordonn�e
    plt.title('Dependance en amplitude')           # Titre
    plt.grid(which='both')                         # La grille
    plt.savefig(base_fichier + '_amplitude.png')   # Sauvegarde
    plt.clf()                                      # Nettoyage

# Appel effectif
amplitude_et_phase(130,1.5,'PNG/S11_trouver_w0_et_Q_01')
amplitude_et_phase(130,1.0,'PNG/S11_trouver_w0_et_Q_03')

def H(w,w0,Q):
    '''Nouvelle fonction de transfert -> passe haut cette fois'''
    return -A*(w/w0)**2/(1-(w/w0)**2 + 1j*w/(Q*w0))

# Comme H a �t� red�finie, c'est automatiquement celle appel�e par Z0 et phase
amplitude_et_phase(170,1.5,'PNG/S11_trouver_w0_et_Q_04')
amplitude_et_phase(170,1.0,'PNG/S11_trouver_w0_et_Q_02')




