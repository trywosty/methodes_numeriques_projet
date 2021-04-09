import numpy as np
from matplotlib import pyplot
from scipy.integrate import solve_ivp as ode45
from scipy.interpolate import CubicSpline

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
def ternarySearchMax(t,tab, tol = 10**-10):
    fun = CubicSpline(t, tab, bc_type='clamped')
    f = 0
    l = t[-1]
    while abs(l-f) > tol :
        f_third = f + (l-f)/3
        l_third = l - (f_third-f)
    #    print("f_third : ", f_third)
     #   print("l_third : ", l_third)
        (f := f_third) if fun(f_third) < fun(l_third) else (l := l_third)
    return (f + l)/2, fun((f+l)/2)




    

def main():
    R_init = 4 #logiquement R_random car on ne connait pas la valeur Rstar
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
    pyplot.plot(solution.t, solution.y[0,:], label="Personnes susceptibles")
    pyplot.plot(solution.t, solution.y[1,:], label="Personnes exposées")
    pyplot.plot(solution.t, solution.y[2,:], label="Personnes infectées")
    pyplot.plot(solution.t, solution.y[3,:], label="Personnes guéries")
    pyplot.plot(solution.t, (n_0) - solution.y[5,:] , label="Décès")
    t_max, y_max = ternarySearchMax(solution.t, (n_0) - solution.y[5])
    pyplot.legend(loc="best")
    pyplot.title("Modèle revisité")
    pyplot.xlabel("Temps(t)")
    pyplot.ylabel("Nombre de personnes")
    pyplot.savefig("modelerevisité.eps", dpi = 1200)
    pyplot.figure()
    pyplot.plot(solution.t, (n_0) - solution.y[5,:] , label="Décès")
    pyplot.legend(loc="best")
    pyplot.title("Modèle revisité")
    pyplot.xlabel("Temps(t)")
    pyplot.ylabel("Nombre de personnes")
    pyplot.savefig("courbedesdécès.png", dpi = 1200)
    print(t_max)
    print(y_max)
