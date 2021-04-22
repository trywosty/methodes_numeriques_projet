from scipy.integrate import solve_ivp as ode45
import numpy as np
from matplotlib import pyplot
from scipy.interpolate import CubicSpline 


def bissection(f, x0, x1, tol):
    if tol < 2*10**(-16):
        print('tolerance impossible')
        return x0,1
    if f(x0)*f(x1) > 0:
        print("Erreur : les f(x0) et f(x1) sont de même signe ! ")
        return x0, 1
    xi  = (x0 + x1) / 2
    while abs((x1-x0)/2) > tol:
        xi = (x1 + x0)/2
        if (f(x0)*f(xi) <= 0):
            x1 = xi
        else:
            x0 = xi
    return (x1+x0)/2, 0

def ternarySearchMax(t,tab, tol = 10**-10):
    fun = CubicSpline(t, tab, bc_type='clamped')
    f = 0
    l = t[-1]
    while abs(l-f) > tol :
        f_third = f + (l-f)/3
        l_third = l - (f_third-f)
        (f := f_third) if fun(f_third) < fun(l_third) else (l := l_third)
    return fun((f+l)/2)

def seirmodel(t, y, gamma, sigma, eta, R_init):
    n = y[0] + y[1] + y[2] + y[3] + y[4]
    dy = np.zeros(5)
    dy[0] = (-y[4]*y[0]*y[2])/n            #s
    dy[1] = (y[4]*y[0]*y[2])/n - (sigma*y[1])          #e
    dy[2] = (sigma*y[1]) - (gamma*y[2])        #x
    dy[3] = gamma*y[2]             #r
    dy[4] = eta*((gamma*R_init)-y[4])                      #beta
    return dy



def R_max_fun(R_star, Xstar,gamma, sigma, eta, y0):
    solution_init = ode45(lambda t, y : seirmodel(t,y,gamma, sigma, eta, R_star), [0, 400], y0, rtol = 1e-12)
    return ternarySearchMax(solution_init.t, solution_init.y[2]) - Xstar

def rechercheReprodSEIR(Xstar, gamma, sigma, eta, y0):
    R_init = 4
    s_0 = y0[0] #R0(t) = β(t)/γ.
    e_0 = y0[1]
    x_0 = y0[2]
    r_0 = y0[3]
    b_0 = y0[4]
    status = 1
    my_fun = lambda R_star : R_max_fun(R_star, Xstar,gamma, sigma, eta, y0,)
    iterant = 0
    while status != 0:
        if iterant > 150:
            print("Trop d'iterations! ")
            return -1
        if Xstar > (y0[0]+y0[1]+y0[2]+y0[3]+y0[4]):
            print("Le nombre de personnes infectés ne peut pas dépasser le nombre d'habitant !")
            return -1
        R_max, status = bissection(my_fun, 0, R_init, 10**(-12))
        R_init += 10
        iterant += 1
    return R_max, status


    


    
    


