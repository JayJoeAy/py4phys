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
Module de g�n�ration automatique de portrait de phase et d'animations 
correspondantes..
"""

def portrait_de_phase(x,vx,titre='Portrait de phase',
    xlabel='$x$',ylabel='$v_x$',file=None,position=True,xlim=None,ylim=None):
    """
    Repr�sentation de vx en fonction de x pour les diff�rentes trajectoires 
    donn�es en entr�e (x et vx sont des tableaux de tableaux).
    Si 'file' est pr�cis�, on enregistre dans le fichier correspond, sinon on 
    affiche � l'�cran.
    Si 'position' est True, on affiche sous forme de rond le dernier point de 
    la trajectoire.
    Si 'xlim' ou 'ylim' sont sp�cifi�s, ils d�finissent les bords du graphe. 
    Sinon, c'est matplotlib qui choisit tout seul.
    """



