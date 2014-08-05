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
Un filtre "bizarre" dont il faut trouver la fonction de transfert sachant 
qu'il est du premier ordre.
'''

from scipy import signal # Pour lti et bode
import numpy as np       # Pour l'�chantillonnage

num = [0.001,10.1]       # Num�rateur   (-> 0.001*jw + 10.1)
den = [0.0101,1]         # D�nominateur (-> 0.0101*jw + 1  )


# Extraction des donn�es
f = np.logspace(0,6,num=200)
s1 = signal.lti(num,den)
f, GdB, phase = signal.bode(s1,f)

# Et pr�paration du diagramme
from bode import diag_bode
diag_bode(f,GdB,phase,'PNG/S11_filtre_bizarre.png')


