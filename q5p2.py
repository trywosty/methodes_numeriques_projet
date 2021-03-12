import numpy as np
from matplotlib import pyplot
from scipy.integrate import solve_ivp as ode45


def seirnmodel(t, y, gamma, sigma, eta, R_init, periode):
    dy = np.zeros(6)
    #beta(t) et e(t) donc 5eqn, page 2 equations
    dy[0] = (-y[4]*y[0]*y[2])/y[5]            #s
    dy[1] = (y[4]*y[0]*y[2])/y[5] - (sigma*y[1])          #e
    dy[2] = (sigma*y[1]) - (gamma*y[2])        #x
    dy[3] = gamma*y[2]             #r
    dy[4] = eta*((gamma*R_init)-y[4])  #beta
    dy[5] = (-1+(gamma*periode))*dy[2]
    return dy



    

def main():
    R_init = 4  #logiquement R_random car on ne connait pas la valeur Rstar
    gamma = 0.06
    n_0 = 10**7
    eta = 0.1
    sigma = 0.2
    x_0 = 100
    s_0 = n_0 - x_0
    r_0 = 0
    b_0 = R_init*gamma
    e_0 = 0
    periode = 16
    solution = ode45(lambda t, y : seirnmodel(t,y, gamma, sigma, eta, R_init, periode), [0, 400], [s_0, e_0, x_0, r_0, b_0, n_0])
    pyplot.figure()
    pyplot.plot(solution.t, solution.y[0,:], label="S")
    pyplot.plot(solution.t, solution.y[1,:], label="E")
    pyplot.plot(solution.t, solution.y[2,:], label="X")
    pyplot.plot(solution.t, solution.y[3,:], label="R")
    pyplot.plot(solution.t, (n_0) - solution.y[5,:] , label="Décès")
    pyplot.legend(loc="best")
    pyplot.title("Modèle revisité")
    pyplot.xlabel("Temps(t)")
    pyplot.ylabel("Nombre de personnes")
    pyplot.savefig("test.png")
    pyplot.figure()
    pyplot.plot(solution.t, (n_0) - solution.y[5,:] , label="Décès")
    pyplot.legend(loc="best")
    pyplot.title("Modèle revisité")
    pyplot.xlabel("Temps(t)")
    pyplot.ylabel("Nombre de personnes")
