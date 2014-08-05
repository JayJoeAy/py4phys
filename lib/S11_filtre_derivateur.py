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
Pour un exercice de reconnaissance d'un filtre qui puisse jouer le r�le 
de d�rivateur dans un certain intervalle de fr�quences. On en g�n�re un du 
premier ordre (passe-bas) et un du second ordre (passe-bande).
'''

from scipy import signal        # Pour les fonctions 'lti' et 'bode'
import numpy as np              # Pour np.logspace

# Ceci est un filtre passe-haut donc potentiellement d�rivateur � BF

num = [0.01,0]                  # Polyn�me au num�rateur   (->    0.01*jw   )
den = [0.0099,1]                # Polyn�me au d�nominateur (-> 0.0099*jw + 1)

f = np.logspace(-1,4,num=200)   # L'intervalle de fr�quences consid�r� (�chelle log)
s1 = signal.lti(num,den)        # La fonction de transfert
f,GdB,phase = signal.bode(s1,f) # Fabrication automatique des donn�es

from bode import diag_bode      # Pour g�n�rer le diagramme de Bode

# Appel effectif � la fonction d�di�e.
diag_bode(f,GdB,phase,'PNG/S11_derivateur.png') 

# Ceci est un filtre passe-bande du second ordre (d�rivateur � BF)

num2 = [0.01,0]                 # Num�rateur   (->           0.01*jw         )
den2 = [10**-2,0.01,1]          # D�nominateur (-> 0.01*(jw)**2 + 0.01*jw + 1)

f = np.logspace(-1,4,num=200)   # Intervalle de fr�quences en �chelle log 
s2 = signal.lti(num2,den2)      # Fonction de transfert
f,GdB,phase = signal.bode(s2,f) # Fabrication des donn�es
diag_bode(f,GdB,phase,'PNG/S11_derivateur2.png') # et du diagramme



