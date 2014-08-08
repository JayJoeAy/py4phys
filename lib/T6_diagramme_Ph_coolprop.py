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
Fabrication d'un diagramme (P,h) avec les iso-choses ad�quates.
"""

import numpy as np               # Les outils math�matiques
import CoolProp.CoolProp as CP   # Les outils thermodynamiques
import CoolProp.Plots as CPP     # Les outils thermographiques
import matplotlib.pyplot as plt  # Les outils graphiques


print(CP.FluidsList())           # Pour regarder les fluides disponibles
fluide= 'Water'                  # Le choix du fluide
Plogscale = True                 # Axe en pression logarithmique ?
iso_T = True                     # Veut-on des isothermes ?
iso_x = True                     # et les isotitres ?
iso_s = True                     # et les isentropiques ?
iso_v = True                     # et les isochores ?

# Donn�es pour les isothermes
dT = 20                                 # Incr�ment de temp�ratures
Ttriple = CP.PropsSI(fluide,'Ttriple')  # Valeur de la temp�rature au point triple
Tcrit = CP.PropsSI(fluide,'Tcrit')      # et au point critique
Tmin = int(Ttriple/10)*10 + 10          # Par d�faut, on par pr�s du point triple
val_T = np.arange(Tmin,1.5*Tcrit,dT)    # et on d�passe un peu le point critique
T_to_show = list(range(2,len(val_T),2)) # S�lection des T � afficher (mettre None pour toutes)

# Donn�es pour les isotitres
val_x = np.linspace(0.1,0.9,9)          # Les valeurs des isotitres

# Donn�es pour les isentropiques
ds = 0.5e3
striple_x0 = CP.PropsSI('S','Q',0,'T',Ttriple,fluide) # Entropie triple � gauche
striple_x1 = CP.PropsSI('S','Q',1,'T',Ttriple,fluide) # Entropie triple � droite
val_s = np.arange(striple_x0,striple_x1*1.2,ds)       # Valeurs � tracer
s_to_show = list(range(2,len(val_s),2))               # et � afficher

# Donn�es pour les isochores (r�parties de mani�re logarithmique par d�faut)
vcrit = 1/CP.PropsSI(fluide,'rhocrit')                 # Volume massique critique
exp_min = int(np.floor(np.log10(vcrit)))+1             # Puissance de 10 proche
vtriple_x1 = 1/CP.PropsSI('D','Q',1,'T',Ttriple,fluide)# Point triple � droite
exp_max = int(np.ceil(np.log10(vtriple_x1)))-1         # Puissance de 10 proche
# Les valeurs � prendre
val_v = [a * 10**b for a in [1,2,5] for b in range(exp_min,exp_max+1)]
v_to_show = None                                       # On les affiche toutes.

# Quelques constantes
UNITS = {'T': 'K', 'Q': '', 'S': 'kJ/K/kg', 'V': 'm$^3$/kg'}
LABEL = {'T': 'T', 'Q': 'x','S': 's', 'V': 'v'}
COLOR_MAP = {'T': 'Darkred',
             'P': 'DarkCyan',
             'H': 'DarkGreen',
             'V': 'DarkBlue',
             'S': 'DarkOrange',   
             'Q': 'black'}

# On pr�pare un format pour impression sur A3 ou presque (dimensions en pouces)
plt.figure(figsize=(30,21))

def place_label(x,y,label,indice=None,cotan=False,color='k'):
    """ Routine qui se d�brouille pour mettre un label semi-transparent au 
    niveau de la courbe donn�es par ses coordonn�es x et y. Si on sait que le 
    label sera presque vertical avec possibilit� de d�passer 90�, on peut 
    utiliser cotan=True pour corriger (consid�ration purement esth�tique). 
    'indice' correspond � la position dans les tableaux x et y o� devra 
    s'afficher le label demand�. """
    print(x[0],y[0],label) # un peu de feedback pour savoir ce qu'on calcule
    N = len(x)//2          # Emplacement par d�faut
    if indice: N=indice    # sauf si l'utilisateur impose la valeur
    xi,xf = plt.xlim()     # Les limites en x du graphe
    yi,yf = plt.ylim()     # Pareil en y
    Xsize = xf - xi        # La largeur
    # Pour la hauteur et la pente, cela d�pend si les ordonn�es sont en rep�re 
    # logarithmique ou non.
    if Plogscale:
        Ysize = np.log10(yf) - np.log10(yi)
        a = (np.log10(y[N+1])-np.log10(y[N-1]))/(x[N+1]-x[N-1]) * Xsize/Ysize
    else:
        Ysize = yf - yi
        a = (y[N+1]-y[N-1])/(x[N+1]-x[N-1]) * Xsize/Ysize
    bbox = plt.gca().get_window_extent() # R�cup�ration de la taille de la figure
    a *= bbox.height / bbox.width        # Correction de la pente avec la taille 
    rot = np.degrees(np.arctan(a))       # Calcul de l'angle de rotation
    if cotan: rot = 90 - rot             # Si on d�passe la verticale
    t = plt.text(x[N],y[N],label,        # On met le texte au bon endroit
    ha='center',va='center',color=color,rotation = rot) # Avec la bonne rotation
    # On se d�brouille pour que la "bo�te" d'�criture soit semi-transparente
    t.set_bbox(dict(facecolor='w',edgecolor='None',alpha=0.8))

def fait_isolignes(type,valeurs,position=None,nb_points=1000,to_show=None,round_nb = 0 ):
    """ S'occupe du calcul et du trac� des isolignes. """
    if not(to_show):                        # Valeurs par d�fauts:
        to_show = list(range(len(valeurs))) # toutes !
    Pmin,Pmax = plt.ylim()                  # On regarde les 
    Hmin,Hmax = plt.xlim()                  # limites du graphique
    # Il y a un bug au niveau des unit�s du graphe et des points de 
    # repr�sentation, d'o� les 1e3 qui trainent un peu partout
    # Par d�faut, l'�chantillonnage en P est lin�aire
    val_P = np.linspace(Pmin*1e3,Pmax*1e3,nb_points) 
    # Sinon, on se met en �chelle log. (1e3 -> 3)
    if Plogscale: val_P = 3+np.logspace(np.log10(Pmin),np.log10(Pmax),nb_points)
    # Cas o� les lignes ne vont pas sur tout l'�ventail des pression, on 
    # �chantillonne en temp�ratures (car on ne peut pas directement 
    # �chantillonner en enthalpie h)
    Tmin = Ttriple
    Tmax = CP.PropsSI('T','P',Pmax,'H',Hmax,fluide)
    val_T = np.linspace(Tmin,Tmax,nb_points)
    # Pour chacune des valeurs demand�es, 
    for val,i in zip(valeurs,range(len(valeurs))):
        if type == 'V':  # Cas particulier des volumes massiques: �chantillonnage
            val_P = CP.PropsSI('P','T',val_T,'D',1/val,fluide)  # en temp�rature
            val_H = CP.PropsSI('H','T',val_T,'D',1/val,fluide)  # et non en P
        else:            # Sinon, on utilise l'�ventail des pression
            val_H = CP.PropsSI('H','P',val_P,type,val,fluide)
        if type == 'S': val /= 1e3 # Pour mettre en kJ/K/kg
        if round_nb >0 : val = str(round(val,round_nb)) # Pour faire joli
        else: val = str(int(round(val)))                # l� aussi...
        label = '${}={}$ {}'.format(LABEL[type],val,UNITS[type])
        plt.plot(val_H,val_P,color=COLOR_MAP[type])     # Affichage courbe
        if i in to_show: # Ainsi que du label s'il fait partie de la liste
            place_label(val_H,val_P,label,int(position*nb_points))

# Le programme proprement dit commence ici.

ph_plot = CPP.PropsPlot(fluide,'Ph')   # On demande gentiment le plot de base
if Plogscale: plt.yscale('log')        # Passage en log(P)

if iso_x: # Les lignes isotitres sont un peu sp�ciales, donc ont leur code propre
    ph_plot.draw_isolines('Q',val_x)   # Trac� des lignes isotitres
    # R�cup�ration de la liste des isotitres.
    isoQ = CPP.Plots.IsoLines(fluide,'Ph','Q').get_isolines(val_x)
    for line in isoQ:                  # Rajout des label
        label = line['label'] + line['unit']
        x,y = line['x'],line['y']
        place_label(x,y,label,indice=len(x)//20)

# Ici, on fait toutes les autres isolignes (le boulot a �t� fait plus haut)
if iso_T: fait_isolignes('T',val_T,position=0.8,to_show=T_to_show)
if iso_s: fait_isolignes('S',val_s,position=0.3,to_show=s_to_show,round_nb=3)
if iso_v: fait_isolignes('V',val_v,position=0.25,to_show=v_to_show,round_nb=3)

plt.grid(which='both') # Rajout de la grille
ph_plot._draw_graph()  # On oblige le dessin avant la sauvegarde
plt.savefig('PNG/T6_diagramme_Ph_coolprop_{}.png'.format(fluide))



