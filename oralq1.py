import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from numpy.polynomial.polynomial import polyfit
from numpy.polynomial import Polynomial as poly

#1 . Afficher le graphique de la fonction f(x) = x^2 + 1 entre -1 et 1 

def q1():
    fct = lambda x : x**2 +1 
    t = np.linspace(-1, 1, 50)
    plt.plot(t, fct(t), 'g--');
    return
  
#2 Cr´eer un vecteur contenant tous les entiers entre 10 et 1000. Afficher tous
#les elements multiples de 5.

def  q2():
    y = np.arange(10,1001, 1)
    i = 0
    while y[i]<1001:
        if ((y[i]%5) == 0):
            print(y[i])
        i += 1
    return
    

#Creer une matrice 100 × 100 ou chaque ligne contient tous les entiers de 1 à 100

def q3():
    x = np.zeros((100,100))
    i = 0
    tab = np.arange(1,101,1)
    while i <100:
        x[i,:] = tab[:]
        i += 1
    print(x)
    return 
    

#Cr´eer un vecteur de 100 nombres al´eatoires et rechercher l’indice de l’´el´ement
#le plus petit

def q4():
    x = np.random.rand(100)
    y = np.argmin(x)
    print(y)
    return
    
#Creer une matrice 100 × 100 de nombres aleatoires. Calculer la somme de
#chacune de ses colonnes

def q5():
    x = np.random.rand(100, 100)
    i = 0
    print(x)
    while i < 100:
        print(np.sum(x[:,i]))
        i += 1 
    return

"""
#Creer une matrice 100 × 100 de nombres al´eatoires et renvoyer une colonne complete contenant un nombre plus petit que 0.01.
"""

def q6():
    x = np.random.rand(100,100)
    

#Creer une spline reliant les points (0, 1),(1, 2),(2, 1),(3, 2). Evaluer sa valeur en 1.5
def q7():
    x = np.arange(0,4,1)
    y = np.array([1,2,1,2])
    t = np.linspace(0,3,50)
    cs = CubicSpline(x,y,bc_type='clamped')
    plt.plot(t, cs(t), label='Spline')
    print(cs(1.5))
    return
    
    """
 Cr´eer un polynˆome reliant les points (0, 1),(1, 2),(2, 1),(3, 2). Evaluer sa
valeur en 1.5.
"""

def q8():
    x = np.arange(0,4,1)
    y = np.array([1,2,1,2])
    q = polyfit(x, y, 3)
    q1 = poly(q)
    lg = np.linspace(0,3,100)
    plt.plot(lg, q1(lg), label='Spline')
    print(q1(1.5))
    return
    

def q9():
    x = np.arange(1,101,1)
    i = 0
    while i < 100:
        x[i] = x[i]* x[i]
        i+=1
    return np.sum(x)
     
"""
Cr´eer un vecteur a contenant tous les entiers entre 1 et 100 et un vecteur b
contenant tous les entiers entre 100 et 1. Calculer le produit scalaire de a et
b.
"""

def q10():
    x = np.arange(100, 0, -1)
    y = np.arange(1, 101, 1)
    print(np.dot(x,y))
    return 

"""
 Cr´eer un vecteur x contenant des entiers de 1 `a 1000 dont les valeurs des
´el´ements sont incr´ement´ees s´equentiellement de 2. Afficher dans un graphique
la fonction y = sin(x).
"""

def q11():
    x = np.arange(1,1001, 2)
    plt.plot(x, np.sin(x), label = 'sin(x)')
    return
    
"""
Creer une matrice 500 × 500 de nombres al´eatoires. Calculer le produit
scalaire de la 4`eme ligne par la 456`eme colonne.
"""

def q12():
    x = np.random.rand(500,500)
    print(np.dot(x[3,:], x[:,455]))
    
"""
Afficher un graphique de la droite y = x − 1, entre −10 et 10.
"""
def q13():
    fct = lambda x : x-1
    m = np.linspace(-10, 10, 100)
    plt.plot(m, fct(m), label ='fonction')
    return
    
"""
Cr´eer une matrice 100 × 100 de nombres al´eatoires. Calculer la somme de
ses ´el´ements diagonaux.
"""

def q14():
    x = np.random.rand(100,100)
    print(sum(np.diag(x)))
    print(np.trace(x)) #identique
    return

"""
Afficher un graphique de la fonction cosinus entre −2π et 2π
"""

def q15():
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    plt.plot(x, np.cos(x))
    return 

"""
Cr´eer un vecteur de 1000 nombres al´eatoires et calculer la diff´erence entre
chaque ´el´ement successif.
"""

def q16():
    x = np.random.rand(1000)
    y = np.roll(x, -1)
    x -= y
    x = x[:-1]
    print(x)
    
"""
Cr´eer une matrice 10 × 10 de nombres al´eatoires et donner la position des
´el´ements strictement plus petit que 0.2
"""
def q17():
    x = np.random.rand(10,10)
    pos = np.argwhere(x < 0.2)
    print(pos)
    return

"""
Cr´eer deux vecteurs a et b de 542 ´el´ements o`u a contient des nombres
al´eatoires compris entre 0 et 10 et b contient tous les entiers entre 1 et 542.
Effectuez le produit de a par b ´el´ement par ´el´ement et affichez le r´esultat
"""

def q18():
    a = np.random.uniform(0,10,542)
    b = np.arange(1,543,1)
    y = np.dot(a,b)
    print(y)
    return 
    
"""
Cr´eer deux matrices A et B de taille 100×100 remplies de nombres al´eatoires.
Calculer le produit scalaire des deux diagonales des matrices A et B.
"""

def q19():
    a = np.random.rand(100,100)
    b = np.random.rand(100,100)
    print(np.dot(np.diag(a), np.diag(b)))
    return 

"""
Cr´eer un vecteur x allant de 0 `a 10 et un vecteur y = cos(x). Utilisez la
fonction spline avec x et y pour calculer la valeur en x = 5.5.
"""

def q20():
    x = np.linspace(0,10,100)
    y = np.cos(x)
    cs = CubicSpline(x, y)
    print(cs(5.5))
    return
    
"""
Cr´eer un vecteur al´eatoire de dimension 100. D´eterminer le nombre de termes
sup´erieurs `a 0.5.
"""
#attention
def q21():
    x = np.random.rand(100)
    a_number = 0.5
    nombre_element = len([element for element in x if element > a_number])
    print(nombre_element)
    
"""
Faire un plot d’un cercle de rayon 10.
"""
def q22():
    c = lambda x : (100-x**2)**(1/2) 
    y = np.linspace(-10,10,100)
    plt.figure()
    plt.plot(y, c(y))
    plt.plot(y, -c(y))
    return 

"""
Construire un vecteur de dimension 20 dont les composantes sont x(i) = 10−i
.
Trouver la plus petite valeur de i telle que l’op´eration (1 + x(i)) − 1 donne 0.
"""
#vérifier
def q23():
    x = np.zeros(20)
    i = 0
    while i < 20:
        x[i] = 10**-i
        i+= 1
    y = np.where((1+x-1)==0)
    print(y[0][0])

    
"""
Calculer la suite g´eom´etrique P30
i=0 x
i pour x = 0.5 sans utiliser d’instruction
de boucle.
"""

def q24():
    y = np.arange(0,31, 1)
    print(sum(0.5**y))
    
"""
Faire un plot de la fonction (1 − cos(x))/x2
, pour x variant de 10−6 `a 10−4
.
"""

def q25():
    fct = lambda x : (1-np.cos(x))/x**2
    y = np.linspace(10**-6, 10**-4, 20)
    plt.plot(y, fct(y))
    
"""
D´efinir un vecteur x comprenant les entiers de 1 `a 5 et un vecteur y =
√
x.
Utiliser une interpolation par spline cubique pour calculer la valeur de y pour
x = 2.5.
"""
def q26():
    x = np.arange(1,6,1)
    y = lambda v : v**(1/2)
    cs = CubicSpline(x, y(x))
    print(cs(2.5))
    
"""
Cr´eer un vecteur al´eatoire de dimension 100. Trouver l’indice du plus grand
´el´ement de ce vecteur.

"""
def q27():
    x = np.random.rand(100)
    y = np.argmax(x)
    print(y)

"""
D´efinir une matrice A de 10 lignes et 10 colonnes telle que A(i, j) = cos(j) exp(i).

"""

def q28():
    x = np.random.rand(10,10)
    i = 0
    j = 0
    while i < 10:
        while j < 10:
            x[i, j] = np.cos(j)*np.exp(i)
            j +=1
        j = 0
        i += 1
    print(x[3,3])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
