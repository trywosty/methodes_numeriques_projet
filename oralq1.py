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
    plt.plot(x, q1(x), label='Spline')
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
    print(x)
    y = np.linspace(0,2*np.pi, 200)
    plt.plot(y, np.sin(y), label = 'sin(x)')
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
