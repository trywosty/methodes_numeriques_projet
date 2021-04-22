from scipy.integrate import solve_ivp as ode45
import numpy as np
from matplotlib import pyplot



def seirmodel(t, y, gamma, sigma, eta, R_init):
    n = y[0] + y[1] + y[2] + y[3]
    dy = np.zeros(5)
    #beta(t) et e(t) donc 5eqn, page 2 equations
    dy[0] = (-y[4]*y[0]*y[2])/n            #s
    dy[1] = (y[4]*y[0]*y[2])/n - (sigma*y[1])          #e
    dy[2] = (sigma*y[1]) - (gamma*y[2])        #x
    dy[3] = gamma*y[2]             #r
    dy[4] = eta*((gamma*R_init)-y[4])                      #beta
    return dy
#avec une valeur arbitraire fixée 



def main():
    R_init = 4  #logiquement R_random car on ne connait pas la valeur Rstar
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
    pyplot.plot(solution.t, solution.y[0,:], label="Personnes susceptibles")
    pyplot.plot(solution.t, solution.y[1,:], label="Personnes exposées")
    pyplot.plot(solution.t, solution.y[2,:], label="Personnes infectées")
    pyplot.plot(solution.t, solution.y[3,:], label="Personnes guéries")
    pyplot.legend(loc="best")
    pyplot.title("Modèle SEIR")
    pyplot.xlabel("Temps(t)")
    pyplot.ylabel("Nombre de personnes")
    pyplot.savefig("test.png")


    


    


    
    


