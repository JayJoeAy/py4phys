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




""" Impl�mentation propos�e par Miriam Heckmann, PCSI3, Lyc�e Kl�ber. """

import numpy as np               # Pour la fonction linspace, zeros et la trigo
import scipy as sp               # Simple alias usuel
import scipy.integrate           # Pour l'int�gration
import matplotlib.pyplot as plt  # Bo�te � outils graphiques

def RLC(R=1e2,L=0.1,C=1e-6,u0=2,du0=0,fichier=None,intervalle=None):
    """ 
    R�ponse de la tension aux bornes du condensateur pour un circuit RLC 
    s�rie. En cas d'absence du nom de fichier, le script fait un affichage 
    interactif du graphique � l'aide de plt.show(). De m�me, si l'intervalle 
    de temps n'est pas sp�cifi� (sous forme d'un doublet), l'affichage se fait 
    de 0 � 3tau.
    """
    omega0=1/np.sqrt(L*C)        # Pulsation propre
    Q=(np.sqrt(L/C))/R           # Facteur de qualit�
    tau=2*Q/omega0               # Temps de relaxation

    if Q  > 0.5: tit='Regime oscillatoire amorti'
    if Q == 0.5: tit='Regime critique'
    if Q  < 0.5: tit='Regime aperiodique'
    
    tit += ' $R={}$ Ohm, $L={}$ H, $C={}$ F'.format(R,L,C)

    def equadiff(y,t):
        u,vu = y                                  # y contient tension et d�riv�e de tension (vu)
        return [vu , - omega0**2 * u - 2*vu/tau]  # On renvoie un doublet pour [du/dt,dvu/dt]

    nb_points=1000                                # Le nombre de points d'un graphe
    if intervalle:
        a,b = intervalle
        t = np.linspace(a,b,nb_points)
    else:
        t=np.linspace(0,3*tau,nb_points)          # La fonction linspace cr�� une liste de valeurs

    plt.clf()   

    sol = sp.integrate.odeint(equadiff,[u0,du0],t)# Int�gration proprement dite
    u = sol[:,0]                 # R�cup�ration de la position
    plt.plot(t,u)                # et affichage

    plt.title(tit)               # annotations
    plt.ylabel('Tension aux bornes du condensateur')
    plt.xlabel('Temps $t$')
    
    if fichier:
        plt.savefig(fichier)     # Sauvegarde dans un fichier
    else:
        plt.show()               # Affichage � l'�cran

RLC(R=10,fichier='PNG/S09_oscillateur_amorti_libre_R00010.png')
RLC(R=100,fichier='PNG/S09_oscillateur_amorti_libre_R00100.png')
RLC(R=1000,fichier='PNG/S09_oscillateur_amorti_libre_R01000.png',intervalle=(0,0.006))



