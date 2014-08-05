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
Exemple de g�n�ration de filtres du second ordre (ici pour une question de 
cours [QDC pour les intimes]).
'''

import numpy as np                       # Pour np.logspace
from bode import diag_bode, second_ordre # Pour les diagrammes

f100 = np.logspace(1,4,num=1000)         # Echantillonnage en f pour Q=100
f0p1 = np.logspace(0,6,num=200)          # Pareil pour Q=0.1

# Deux passe-bas, puis deux passe-hauts et enfin deux passe-bandes
second_ordre(10**3, 100,'PNG/S11_filtres_QDC_PBs_Q100.png',f=f100)
second_ordre(10**3,1/10,'PNG/S11_filtres_QDC_PBs_Q0_1.png',f=f0p1)
second_ordre(10**3, 100,'PNG/S11_filtres_QDC_PHt_Q100.png',f=f100,type='PHt')
second_ordre(10**3,1/10,'PNG/S11_filtres_QDC_PHt_Q0_1.png',f=f0p1,type='PHt')
second_ordre(10**3, 100,'PNG/S11_filtres_QDC_PBd_Q100.png',f=f100,type='PBd')
second_ordre(10**3,1/10,'PNG/S11_filtres_QDC_PBd_Q0_1.png',f=f0p1,type='PBd')



