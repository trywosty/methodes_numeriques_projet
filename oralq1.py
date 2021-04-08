import numpy as np
import matplotlib.pyplot as plt


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
    
#Creer une matrice 100 × 100 de nombres aleatoires. Calculer la somme de
#chacune de ses colonnes 