py4phys
-------

Projet pour rassembler l'ensemble des programmes Python qui peuvent �tre 
utiles pour illustrer le cours de physique de CPGE.

## Organisation

* Le fichier py4phys.pdf rassemble les codes et les graphiques qui en sont issus. 
* Le r�pertoire lib/ rassemble les fichiers .py pr�ts � �tre utilis�s.
* Vous trouverez aussi quelques animations sur la page 
http://pcsi.kleber.free.fr/IPT/py4phys.html

## Roadmap

Pour le moment, j'essaie de rassembler toutes les id�es concernant le cours de 
physique de PCSI, plus quelques illustrations annexes que j'ai toujours voulu 
mettre en oeuvre (comme l'exploration des zones chaotiques de la rotation 
d'Hyp�rion autour de Saturne).

## Description succincte des fichiers

### Bloc Induction
* I1_lignes_champ_magnetique.py: Code �crit par Sylvain Condamin (adapt� d'un 
code de Thierry Pr�) pour simuler les lignes de champ magn�tique autour de 
divers objets (fil infini, dip�le magn�tique ou spire)
* I2_champ_tournant_diphase.py (non encore �crit): Fabrique une petite 
animation pour illustrer la notion de champ tournant � partir de deux bobines 
en quadrature de phase.
* I2_champ_tournant_triphase.py (non encore �crit): Comme le pr�c�dent, mais 
en triphas�.
* I4_couplage_de_deux_circuits.py: r�solution num�rique d'un couplage de 
circuits oscillants pour illustrer notamment la notion de battements en cas de 
couplage faible.

### Bloc M�canique
* M2_trainee.py (non encore fait): illustration de l'influence de la tra�n�e 
sur un tir d'obus.
* M2_trainee_portrait_de_phase.py (non encore fait): pareil via un portrait de 
phase.
* M4_oscillateur_de_landau_effets_non_lineaires.py (non encore fait): Non 
isochronisme des oscillations dans le cas d'un oscillateur de Landau.
* M4_oscillateur_de_landau_portrait_de_phase.py (non encore fait): Portrait de 
phase pour un oscillateur de Landau
* M4_pendule_simple_non_isochronisme.py (non encore fait): Non isochronisme 
des oscillations pour un pendule simple.
* M4_pendule_simple_oscillations_amorties.py (non encore fait): Oscillations 
amorties dans le cadre du pendule simple.
* M4_pendule_simple_portrait_de_phase.py (non encore fait): fabrication du 
portrait de phase d'un pendule simple. 
* M5_mouvement_dans_champ_E_et_B.py (non encore fait): calcul de la 
trajectoire d'une particule charg�e soumise � la fois � un champ E et un champ 
B.
* M5_mouvement_helicoidal.py (non encore fait): Trajectoire d'une particule 
charg�e soumise uniquement � un champ magn�tique.
* M_hyperion.py: �tude d'une section de Poincar� pour la rotation propre 
d'Hyp�rion (satellite de Saturne) qui mette en avant le caract�re chaotique 
d'une telle rotation (cf Ian Stewart, "Dieu joue-t-il aux d�s" pour une 
introduction � cette probl�matique).
* M_papillon_de_lorentz.py (non encore fait): Illustration du concept 
d'attracteur �trange � l'aide du papillon de Lorentz
* M_pendule_double.py (non encore fait): Illustration de la d�pendance aux 
conditions initiales pour les mouvements chaotiques sur l'exemple du pendule 
double rigide.
* portrait_de_phase.py (non encore fait): Module g�n�rique pour produire un 
portrait de phase

### Bloc Signal
* S01_oscillateur_harmonique_energie.py: Illustration de la conservation de 
l'�nergie pour un oscillateur harmonique.
* S01_oscillateur_harmonique_periode.py: Illustration de l'isochronisme des 
oscillations pour un oscillateur harmonique.
* S02_onde_progressive.py: Illustration de la notion d'onde progressive
* S02_onde_progressive_animation_superposition.py: Petite animation sur 
l'exemple pr�c�dent en superposant plusieurs ondes se d�pla�ant � diverses 
vitesses.
* S03_battements.py: Illustration de la notion de battements lors de la 
superposition de deux ondes de fr�quences voisines.
* S03_diffraction.py: Diffraction (2D) d'une onde plane apr�s passage d'une 
ouverture plane. On peut jouer sur l'angle d'incidence sur l'ouverture.
* S03_fresnel.py: Fabrication d'�nonc�s et de corrig�s pour entra�ner les 
�l�ves sur les constructions de Fresnel.
* S03_interferences.py: Animation montrant la mise en place d'interf�rences 
lors de la superposition des signaux en provenance de deux points sources.
* S03_ondes_stationnaires.py (non encore fait): Illustration de la notion 
d'onde stationnaire lors de la superposition d'ondes progressives de sens 
oppos�s
* S04_arc_en_ciel_turtle.py: Programme 'turtle' �crit par Tom Morel pour 
expliquer la r�fraction � l'int�rieur d'une goutte d'eau.
* S04_lois_de_descartes.py (non encore fait): Illustration de la loi de 
Descartes via une animation de r�fraction pour de multiples incidences.
* S05_distortion_chromatique.py: Programme 'turtle' �crit par Tom Morel pour 
mettre en avant la d�pendance de la distance focale avec la couleur des rayons 
incidents
* S05_gauss_4P.py: Programme 'turtle' �crit par Tom Morel pour illustrer la 
r�gle des "4P" (Plus Plat, Plus Pr�s)
* S05_lentilles_construction_graphique.py (non encore fait): Illustration des 
construction graphique pour les lentilles
* S06_paquet_d_ondes_MQ.py: Programme �crit par Miriam Heckmann pour simuler 
un paquet d'ondes en m�canique quantique
* S07_elec_resolution_pivot_de_gauss.py (non encore fait): R�solution d'un 
syst�me �lectrique lin�aire sans d�riv�es temporelles � l'aide d'un pivot de 
Gauss
* S08_circuit_premier_ordre_complexe.py (non encore fait): R�solution d'un 
syst�me �lectrique complexe en se contentant d'�crire les lois des mailles, 
des noeuds et relations �lectriques de chaque dip�le.
* S08_circuit_premier_ordre_simple.py (non encore fait): R�solution d'un    
syst�me �lectrique simple en se contentant d'�crire les lois des mailles,   
des noeuds et relations �lectriques de chaque dip�le.
* S09_oscillateur_amorti_libre.py (non encore fait): 
* S10_oscillateur_amorti_force.py (non encore fait):
* S11_filtre_bizarre.py: Dessine le diagramme de Bode d'un filtre du type 
(A+jw/w1)/(1+jw/w2)
* S11_filtre_derivateur.py: Diagramme de Bode pour deux filtres o� il faut 
d�terminer la zone qui se comporte comme un d�rivateur
* S11_filtre_diagrammes_en_amplitudes.py: Diagrammes de Bode en amplitude pour 
d�termination graphique de w0 et Q.
* S11_filtre_integrateur.py: Diagramme de Bode pour deux filtres o� il faut 
d�terminer la zone qui se comporte comme un int�grateur
* S11_filtres_second_ordre.py: Exemples de g�n�ration de diagramme de Bode 
pour des filtre du second ordre en utilisant le module 'bode.py'
* bode.py: Module de g�n�ration de diagrammes de Bode.

### Bloc Thermodynamique
* T1_balles_rebondissantes_en_boite.py
* T1_particules_en_boite_libre.py
* T1_particules_en_boite_mouvement_brownien.py
* T2_diagramme_PT_coolprop.py
* T2_diagramme_Pv_coolprop.py
* T2_reseau_d_isothermes_coolprop.py
* T5_isentropique_GP_vs_gaz_reel_coolprop.py
* T6_cycle_de_carnot_reel_et_GP.py
* T6_diagramme_Ph_coolprop.py
* T6_resolution_cycle_diesel.py
