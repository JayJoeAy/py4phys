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
Petit module pour rassembler la proc�dure de trac� de diagramme de Bode pour 
pouvoir se concentrer uniquement sur ce qu'il y a autour.
'''

import matplotlib.pyplot as plt  # Pour les dessins

def diag_bode(f,GdB,phase,out_file,titre=None):
    '''Dessine un diagramme de bode quand on donne la fr�quence, le gain et la 
    phase correspondants. Le r�sultat est �crit dans le fichier 'out_file'.'''
    plt.figure()                 # Ouverture de la figure
    plt.subplot(211)             # La premi�re sous-figure
    if titre: plt.title(titre)   # Rajout du titre si demand�
    plt.semilogx(f, GdB)         # Graphique semi-log en x pour le gain
    plt.grid(which='both')       # On rajoute la grille
    plt.ylabel(r'Gain (dB)')     # Label vertical
    plt.subplot(212)             # La seconde sous-figure
    plt.semilogx(f, phase)       # Graphique semi-log en x pour la phase
    plt.ylabel(r'Phase (deg)')   # Label en y
    plt.xlabel(r'Frequence (Hz)')# et label en x commun
    plt.grid(which='both')       # On rajoute la grille
    plt.savefig(out_file)        # Sauvegarde du fichier
    plt.close()                  # et fermeture de la figure

# Le module signal poss�de une fonction "bode" d�di�e que l'on va utiliser
from scipy import signal

def second_ordre(f0,Q,filename='defaut.png',type='PBs',f=None):
    '''Petite fonction pour faciliter l'utilisation de la fonction "bode" du 
    module "signal" quand on s'int�resse � des filtres du 2e ordre. Il suffit 
    de donner la fr�quence propre f0 et le facteur de qualit� Q pour obtenir 
    ce que l'on veut. Autres param�tres:
    * filename: le nom du fichier ('defaut.png' par d�faut)
    * type: le type du filtre, � choisir parmi 'PBs' (passe-bas), 
    'PBd' (passe-bande) et 'PHt' (passe-haut). On peut aussi d�finir soi-m�me 
    le num�rateur sous forme d'une liste de plusieurs �l�ments, le degr� le 
    plus haut donn� en premier. NB: le '1.01' des d�finitions est juste l� 
    pour am�liorer sans effort le rendu graphique.
    * f: les fr�quences � �chantillonner (si None, la fonction choisit 
    d'elle-m�me un intervalle ad�quat).
    '''
    den = [1./f0**2,1./(Q*f0),1]              # Le d�nominateur de la fonction de transfert
    if   type == 'PBs': num = [1.01]          # Le num�rateur pour un passe-bas
    elif type == 'PBd': num = [1.01/(Q*f0),0] # pour un passe-bande
    elif type == 'PHt': num = [1.01/f0**2,0,0]# pour un passe-haut
    else: num = type                          # sinon, c'est l'utilisateur qui le d�finit.
    s1 = signal.lti(num,den)                  # D�finition de la fonction de transfert
    f, GdB, phase = signal.bode(s1,f)         # Obtention des valeurs ad�quates
    diag_bode(f,GdB,phase,filename)           # Dessin du diagramme proprement dit



