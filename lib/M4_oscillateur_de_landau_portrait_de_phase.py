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




import numpy as np
import scipy as sp
import scipy.integrate
from portrait_de_phase import portrait_de_phase

def landau(y,t):
    x,vx = y
    k,m,d,ell0 = 1,1,3,5
    return [vx,-k*x/m*(np.sqrt(d**2+x**2) - ell0)/(np.sqrt(d**2+x**2))]





