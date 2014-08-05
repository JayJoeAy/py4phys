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
Programme pour construire une section de Poincar� pour Hyp�rion. L'id�e d'une 
section de Poincar� est de repr�senter le couple (theta,Omega) � chaque fois 
que l'on passe dans le plan phi=0. Il suffit donc de demander � scipy les 
valeurs pour les multiples de 2pi et de tracer les trajectoires pour de 
multiples conditions initiales. On reconna�tra les trajectoires 
quasi-p�riodiques par le fait que les points successifs tombent proches les 
uns des autres et dessinent une courbe bien d�finie alors que pour les 
trajectoires chaotiques, les points semblent se d�poser "au hasard" sur toute 
une surface de la section de Poincar�.
"""

import numpy as np
import scipy as sp
import scipy.integrate
import matplotlib.pyplot as plt

# Les constantes de notre probl�me
e = 0.1                # Excentricit� de l'orbite d'Hyp�rion
BmAsC = 0.265          # Valeur de B Moins A Sur C (B-A)/C pour Hyp�rion

def hyperion(y,phi):
    """ Fonction d�finissant le syst�me diff�rentiel (en phi) r�gissant 
    l'�volution de theta et Omega pour Hyp�rion. """
    theta,Omega = y
    a_sur_r = (1 + e*np.cos(phi))/(1-e**2)
    dtheta_sur_dphi = 1/a_sur_r**2 * Omega
    dOmega_sur_dphi = - BmAsC * 3 / (2*(1-e**2)) * a_sur_r * np.sin(2*(theta-phi))
    return [dtheta_sur_dphi,dOmega_sur_dphi]

def trajectoire(Omega0,n=200,dphi=2*np.pi):
    """ R�cup�ration d'une trajectoire dans la section de Poincar�. Renvoie un 
    triplet contenant les theta mesur�s, les Omega et les phicorrespondants. 
    """
    y0  = [0,Omega0]                      # Condition initiale (theta=0)
    phi = np.arange(0,n*dphi,dphi) # n points r�partis tous les 2pi
    sol = sp.integrate.odeint(hyperion,y0,phi)  # Int�gration effective
    theta = (sol[:,0]+np.pi)%(2*np.pi)-np.pi
    Omega = sol[:,1]
    return theta,Omega,phi

# Les conditions initiales regard�es (qui bien s�r doivent d�pendre de e et
# BmAsC pour bien d�limiter les zones chaotiques [ici 0.2] des zones 
# quasi-p�riodiques [toutes les autres])
L_Omega0 = [0,0.2,0.3,0.7,2.37,2.7,2.85]
for Omega0 in L_Omega0:
    if Omega0 == 0.2: n = 5000   # Il faut plus de point pour la zone chaotique
    else: n = 500
    theta,Omega,phi = trajectoire(Omega0,n=n)
    plt.plot(theta,Omega,'.',label='$\Omega_0={}$'.format(Omega0))

plt.xlim((-np.pi,6))
plt.ylim((0,3))
plt.title('Hyperion: Section de Poincare dans le plan $\phi=0[2\pi]$')
plt.xlabel('$\\theta$')
plt.ylabel('$\\Omega=\\dot\\theta$')
plt.legend()
plt.savefig('PNG/M_hyperion.png')
plt.clf()

# Regardons aussi ce que donne une trajectoire quasi-periodique et une 
# trajectoire chaotique en observant la vitesse angulaire Omega en fonction de 
# la position phi sur l'orbite
def plot_trajectoire_donnee(Omega0,phi_max,n,titre='',fichier=None):
    theta,Omega,phi = trajectoire(Omega0,n=n,dphi=phi_max/n)
    plt.plot(phi,Omega)
    plt.title(titre)
    plt.xlabel("Position $\\phi$ sur l'orbite")
    plt.ylabel("Vitesse $\\Omega$ de rotation")
    if fichier: plt.savefig(fichier)
    else: plt.show()
    plt.clf()

plot_trajectoire_donnee(0,100,1000,'Trajectoire quasi-periodique $\\Omega_0=0$',
     'PNG/M_hyperion_0.png')
plot_trajectoire_donnee(0.2,400,1000,'Trajectoire chaotique $\\Omega_0=0.2$',
     'PNG/M_hyperion_0_2.png')






# �volution des zones chaotiques quand on modifie progressivement 
# l'excentricit� de l'orbite.

def fait_diagramme(e,L_Omega0=np.arange(0,3.1,0.2),
                   label=False,n=200,fichier=None):
    """ Fait automatiquement la section de Poincar� pour l'excentricit� e 
    fournie et en utilisant les valeurs initiales contenue dans L_Omega0 pour 
    les vitesses angulaires. N'affiche les label que si 'label' est � True.
    On peut aussi changer le nombre 'n' de points d'�chantillonnage.
    Si le nom du fichier est donn�, on y sauvegarde le r�sultat. Sinon, on 
    l'affiche � l'�cran.
    """
    for Omega0 in L_Omega0:
        theta,Omega,phi = trajectoire(Omega0,n=n)
        plt.plot(theta,Omega,'.',label='$\\Omega_0={}$'.format(Omega0))
    if label: plt.xlim(-np.pi,6) ; plt.legend()
    else:     plt.xlim(-np.pi,np.pi)
    plt.ylim(0,5)
    plt.xlabel('$\\theta$')
    plt.ylabel('$\\Omega$')
    plt.title("Section de Poincare d'Hyperion, $e={:.4f}$".format(e))
    if fichier: plt.savefig(fichier)
    else: plt.show()
    plt.clf()

base_name = 'PNG/M_hyperion_e'

for e in np.arange(0,0.2,0.0002):
    print('e={}'.format(e))
    fichier = base_name + '{:.4f}'.format(e).replace('.','_')
    fait_diagramme(e,fichier=fichier)
    
# Ne reste plus qu'� rassembler en un fichier mpeg � l'aide de convert puis de
# ppmtoy4m et mpeg2enc (paquet mjpegtools � installer sur la machine)

import os

cmd = '(for f in ' + base_name + '*png ; '
cmd+= 'do convert -density 100x100 $f -depth 8 -resize 600x600 PNM:- ; done)'
cmd+= ' | ppmtoy4m -S 420mpeg2'
cmd+= ' |  mpeg2enc -f1 -b 12000 -q7 -G 30 -o {}film.mpeg'.format(base_name)

print("Execution de la commande de conversion")
print(cmd)
os.system(cmd)
print("Fin de la commande de conversion")



