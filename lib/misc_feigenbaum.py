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
Encore une illustration tir�e du livre "Dieu joue-t-il aux d�s ?" de Ian 
Stewart pour illustrer les doublements de p�riodes successifs dans les cycles 
limites de suites r�cursives � partir de l'application logistique 
x -> k*x*(1-x).
L'id�e est d'it�rer la suite sur un certain nombre (iterations_avant_cycle) de 
termes et repr�senter les valeurs d'un certain nombre (it�rations_dans_cycle) 
de termes suivants en esp�rant avoir atteint la limite. Il suffit alors de 
repr�senter ces termes en fonction de k pour obtenir le diagramme de 
bifurcation.
"""

import numpy as np                # Bo�te � outils num�riques
import matplotlib.pyplot as plt   # Bo�te � outils graphiques
import film                       # Bo�te � outils visuels

kmin,kmax = 2.9,4                 # Limites horizontales
ylim = None                       # Limites verticales
# � essayer aussi:
# kmin = 3.9055
# kmax = 3.9068
# ylim = (0.48,0.52)

nb_points = 1000                  # Nb de points d'�chantillonnage en k
iterations_avant_cycle = 1000     # Nb de points avant d'arriver � la limite
iterations_dans_cycle  = 100      # Nb de points � repr�senter
u0 = 0.1                          # Valeur initiale



def f(x,k):                       # D�finition de la fonction logistique
    return k*x*(1-x)

def get_cycle(k,u0):              # R�cup�ration du cycle
    """Renvoie un doublet des valeurs avant l'arriv�e sur le cycle puis des 
    valeurs sur le cycle"""
    tot = np.zeros(iterations_avant_cycle + iterations_dans_cycle)
    tot[0] = u0                   # Initialisation
    for i in range(1,len(tot)):   # It�rations
        tot[i] = f(tot[i-1],k)
    return tot[:iterations_avant_cycle],tot[iterations_avant_cycle:]

base_name = 'PNG/misc_feigenbaum_araignee'
def graphique_araignee(avant,k,i,suffix='avant'):
    print(i,k)
    araignee = plt.figure(i)
    double = [a for a in avant for b in range(2)]
    x = np.linspace(0,1,100)
    plt.plot(x,f(x,k),'k',linewidth=2)
    plt.plot(x,x,'k',linewidth=2)
    plt.plot(double[1:-1],double[2:])
    plt.title('$k={:.4f}$'.format(k))
    araignee.savefig(base_name + '_{}_{:04d}'.format(suffix,i))
    plt.close(araignee)

fig = plt.figure()                # Initialisation de la figure principale
feigenbaum = fig.gca()            # R�cup�ration de "l'axe"

k_list = np.linspace(kmin,kmax,nb_points)

for i,k in enumerate(k_list):     # Pour toutes les valeurs de la liste des k
    avant,dans = get_cycle(k,u0)  # on r�cup�re le cycle et on l'affiche
    feigenbaum.plot([k]*len(dans),dans,'.k',markersize=1)
    graphique_araignee(avant,k,i) # Fabrication du graphique "en araign�e"
    graphique_araignee(dans,k,i,'apres') 

if ylim: feigenbaum.set_ylim(ylim)# Rajout des limites verticales 
feigenbaum.set_xlim(kmin,kmax)    # et horizontales de la figure principale
plt.title('Figuier de Feigenbaum')
plt.xlabel('$k$')
plt.ylabel('$x$ limite')
fig.savefig('PNG/misc_feigenbaum.png') # Sauvegarde


# Reste � faire les petits films correspondants aux graphes en araign�es
film.make_film(base_name + '_avant')
film.make_film(base_name + '_apres',PNM='PPM')



