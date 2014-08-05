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




""" Impl�mentation propos�e par Miriam Heckmann, PCSI3, Lyc�e Kl�ber """

import numpy as np               # Pour la fonction linspace, zeros et la trigo
import matplotlib.pyplot as plt  # Bo�te � outils graphiques

def paquet_d_onde(N):
    """Construction d'un paquet d'onde � N ondes"""
    nb_points=1000                   # Le nombre de points d'�chantillonage
    x=np.linspace(-100,100,nb_points)# �chantillonnage en position
    y=np.zeros(nb_points)            # Cr�ation d'une liste de z�ros 

    for i in range(N):
        y += (1-i/N)*np.sin(np.pi*x/(2+i/100))+(1-i/N)*np.sin(np.pi*x/(2-i/100))
    plt.plot(x,y)
    plt.title("Paquet d'onde pour $N={}$".format(N))
    plt.savefig('PNG/S06_paquet_d_ondes_MQ_N{:03d}.png'.format(N))
    plt.clf()

paquet_d_onde(10)
paquet_d_onde(50)



