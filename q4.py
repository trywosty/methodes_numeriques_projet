from scipy.integrate import solve_ivp as ode45
import numpy as np
from matplotlib import pyplot



def bissection(f, x0, x1, tol):
    if tol < 2*10**(-16):
        print('tolerance impossible')
        return x0,1
    if f(x0)*f(x1) > 0:
        print("Erreur : les f(x0) et f(x1) sont de même signe ! ")
        return x0, 1
    xi  = (x0 + x1) / 2
    print("je passe ici !")
    while abs((x1-x0)/2) > tol:
       # print("je ne passe pas ici !")
        xi = (x1 + x0)/2
        print("milieu", xi)
        if (f(x0)*f(xi) <= 0):
            x1 = xi
        else:
            x0 = xi
    #print("Tout s'est passé comme il faut")
    return (x1+x0)/2, 0
  #est-ce que le changement de valeur est bonne, ou l'inverse ? 

def seirmodel(t, y, gamma, sigma, eta, R_init):
    n = 10**7
    dy = np.zeros(5)
    #beta(t) et e(t) donc 5eqn, page 2 equations
    dy[0] = (-y[4]*y[0]*y[2])/n            #s
    dy[1] = (y[4]*y[0]*y[2])/n - (sigma*y[1])          #e
    dy[2] = (sigma*y[1]) - (gamma*y[2])        #x
    dy[3] = gamma*y[2]             #r
    dy[4] = eta*((gamma*R_init)-y[4])                      #beta
    return dy
#avec une valeur arbitraire fixée 


def R_max_fun(R_star, Xstar,gamma, sigma, eta, y0):
    solution_init = ode45(lambda t, y : seirmodel(t,y,gamma, sigma, eta, R_star), [0, 400], y0)
    return solution_init.y[2].max() - Xstar



def rechercheReprodSEIR(Xstar, gamma, sigma, eta, y0):
    R_init = 4
    s_0 = y0[0] #R0(t) = β(t)/γ.
    e_0 = y0[1]
    x_0 = y0[2]
    r_0 = y0[3]
    b_0 = y0[4]
    status = 1
    my_fun = lambda R_star : R_max_fun(R_star, Xstar,gamma, sigma, eta, y0)
    iterant = 0
    while status != 0:
        if iterant > 150:
            print("Trop d'iterations! ")
            return -1
        if Xstar > (y0[0]+y0[1]+y0[2]+y0[3]+y0[4]):
            print("Le nombre de personnes infectés ne peut pas dépasser le nombre d'habitant !")
            return -1
        R_max, status = bissection(my_fun, 0, R_init, 10**(-10))
        R_init += 10
        iterant += 1
    return R_max, status


def main():
    R_init = 4  #logiquement R_random car on ne connait pas la valeur Rstar
    Xstar = 10**5
    gamma = 0.06
    eta = 0.1
    sigma = 0.2
    n = 10**7
    x_0 = 100
    s_0 = n - x_0
    r_0 = 0
    b_0 = R_init*gamma
    e_0 = 0
    solution = ode45(lambda t, y : seirmodel(t,y, gamma, sigma, eta, R_init), [0, 400], [s_0, e_0, x_0, r_0, b_0])
    pyplot.figure()
    pyplot.plot(solution.t, solution.y[0,:], label="S")
    pyplot.plot(solution.t, solution.y[1,:], label="E")
    pyplot.plot(solution.t, solution.y[2,:], label="X")
    pyplot.plot(solution.t, solution.y[3,:], label="R")
    pyplot.legend(loc="best")
    pyplot.title("Modèle SEIR")
    pyplot.xlabel("Temps(t)")
    pyplot.ylabel("Nombre de personnes")
    pyplot.savefig("test.png")

def R_seir():
    Xstar = 10**5
    gamma = 0.06
    eta = 0.1
    sigma = 0.2
    n = 10**7
    x_0 = 100
    s_0 = n - x_0
    r_0 = 0
    b_0 = 4*gamma
    e_0 = 0
    my_R, status = rechercheReprodSEIR(Xstar, gamma, sigma, eta, [s_0, e_0, x_0, r_0, b_0])
    print(my_R, status)
    solution_test = ode45(lambda t,y : seirmodel(t, y, gamma, sigma, eta, my_R), [0,400], [s_0, e_0, x_0, r_0, b_0])
    print("MAX VAL : ", solution_test.y[2].max())

    


    


    
    


