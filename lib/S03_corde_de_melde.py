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
Simulation d'un corde de Melde. Le but est de visualiser comment une onde de 
faible amplitude au d�part peut s'amplifier � mes que se r�flexions 
successives se superposent. On introduit une att�nuation arbitraire de l'onde 
pour forcer la convergence.
"""

import numpy as np              # Bo�te � outils num�riques
import matplotlib.pyplot as plt # Bo�te � outils graphiques
import film                     # Bo�te � outils vid�os

def corde_de_melde(base_name,w=1,k=1,L=1,A=0.1,tmax=10,N=1000,ylim=None):
    """ 
    Produit un film (base_name + '_film.mpeg') d'une corde de Melde de 
    longueur L, fix�e � droite et excit�e � gauche par un moteur de pulsation 
    w imposant la propagation d'une onde d'amplitude de nombre d'onde k en 
    observant les r�flexions r�guli�re de l'onde jusqu'au temps tmax sur un 
    total de N images. Si ylim est pr�cis�, il contiendra les limites 
    verticales, sinon c'est matplotlib qui d�cidera, ce qui d�clenchera une 
    adaptation progressive de l'amplitude.
    """
    t = np.linspace(0,tmax,N)
    for i,ti in enumerate(t):
        print(ti)
        fichier = base_name + '{:04d}'.format(i)
        fait_corde(ti,file=fichier,w=w,k=k,L=L,A=A,ylim=ylim)
    film.make_film(base_name)

def fait_corde(t,file=None,w=1,k=1,L=1,A=0.1,ylim=None,nb_points=400):
    """ 
    Dessine effectivement la corde de Melde � l'instant t.
    Si 'file' n'est pas renseign�, on l'affiche � l'�cran.
    """
    x = np.linspace(0,L,nb_points)
    plt.plot(x,corde(x,t,w,k,L,A),'k',linewidth=2.0)
    if ylim: plt.ylim(ylim)
    plt.title('Corde de Melde, $t={}$'.format(t))
    plt.xlabel('x')
    if file:
        plt.savefig(file)
        plt.clf()
    else: 
        plt.show()

def corde(x,t,w,k,L,A):
    """ 
    Calcul it�ratif de l'�tat de la corde
    """
    c = w/k
    u = w*t - k*x
    u0= w*t
    #print(u)
    gauche = A*f(w*t,u0)
    droite = 0.0
    gauche = 0.0
    resultat = A*f(u,u0)*be_positive(u)
    plt.plot(x,resultat)
    for i in range(1,int(c*t/L)+1):
        u -= k*L
        if i%2 == 0: 
            addition = (gauche + A*f(u,u0))*be_positive(u)
        else:        
            addition = list(reversed((droite - A*f(u,u0))*be_positive(u)))
        plt.plot(x,addition)
        resultat += addition
    return resultat

def be_positive(u):
    res = np.ones(u.shape)
    res[u<0] = 0.0
    return res    

def f(u,u0): 
#    if u0 == 0: return 0.0
#    return np.sin(u)*u/u0
    return np.sin(u)/(1 + u0-u)**0.3
#    res = np.sin(u)
#    res[u<0] = 0.0
#    return res    

#fait_corde(0)
#fait_corde(1)
#fait_corde(1.2)
#fait_corde(1.5)
#fait_corde(2)
#fait_corde(2.5)
#fait_corde(3)

L=10

lambda1 = 2*L/(3)
lambda2 = 2*L/(3+0.5)

corde_de_melde('PNG/S03_corde_de_melde_amplif',
               L=L,k=2*np.pi/lambda1,N=1500,ylim=(-1,1),tmax=150)
corde_de_melde('PNG/S03_corde_de_melde_non_amplif',
               L=L,k=2*np.pi/lambda2,N=1500,ylim=(-1,1),tmax=150)



