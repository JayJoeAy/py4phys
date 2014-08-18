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
Travail propos� par Simon LAURETTE (PSI, Lyc�e Robespierre, Arras) pour 
illustrer l'amplification des oscillations pour un oscillateur � pont de Wien.
"""


from math import *              # Outils math�matiques
import numpy as np              # Outils num�riques
import matplotlib.pyplot as plt # Outils graphiques

R=1e3                           # Resistance du Pont de Wien
C=100e-9                        # Capacite du Pont de Wien
K=3.2                           # Gain de l'etage d'amplification
tfin=15e-3                      # instant final de la simulation
dt=0.01e-3                      # pas
vsat=15                         # tension de saturation de l'AO

# Conditions Initiales
t=[0.0]
e=[0.01]   # entree de l'etage d'amplitication ; 0.01 simule le bruit
s=[0.0]    # sortie de l'etage d'amplification / entree du Pont de Wien
ds=[0.0]   # derivee de s
de=[0.01]  # derivee de e ; 0.01 simule le bruit en entree

# Resolution de l'equa-diff + Prise en compte de la saturation de l'AO
while t[-1]<tfin:
    de.append((1/(R*C)*ds[-1]-3/(R*C)*de[-1]-e[-1]/(R*R*C*C))*dt+de[-1])
    e.append(de[-1]*dt+e[-1])
    if e[-1]<-vsat/K:
        s.append(-vsat)
    elif e[-1]>vsat/K:
        s.append(vsat)
    else:
        s.append(K*e[-1])
    ds.append((s[-1]-s[-2])/dt)
    t.append(t[-1]+dt)

# Traces des courbes
plt.subplot(2,1,1)   # Sous-figure 1: �volution temporelle
plt.plot(t,e)
plt.xlabel("t (s)")
plt.ylabel("e (V)")
plt.title("Demarrage des oscillations")
plt.subplot(2,1,2)   # Sous-figure 2: Portrait de phase
plt.plot(e,de)
plt.xlabel("e (V)")
plt.ylabel("de/dt (V/s)")
plt.title("Plan de phase")
plt.tight_layout()   # Pour ajuster les espaces autour des sous-figures
plt.savefig('PNG/PSI_pont_de_wien.png')



