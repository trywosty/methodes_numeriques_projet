import numpy as np
from matplotlib import pyplot
from scipy.integrate import solve_ivp as ode45
from scipy.interpolate import CubicSpline

def seirmodel(t, y, gamma, sigma, eta, Rstar):
    n = 10**7
    dy = np.zeros(5)
    #beta(t) et e(t) donc 5eqn, page 2 equations
    dy[0] = (-y[4]*y[0]*y[2])/n                        #s
    dy[1] = (y[4]*y[0]*y[2])/n - (sigma*y[1])          #e
    dy[2] = (sigma*y[1]) - (gamma*y[2])                #x
    dy[3] = gamma*y[2]                                 #r
    dy[4] = eta*((gamma*Rstar(t))-y[4])                #beta
    return dy

"""
on utilise les interpolations cubiques car si n > 10, les intervalles
[0, 1] et [ n-1, n] seraient problématiques dû à la création d'un  polynôme de degré n-1
"""
def q5(t, R, gamma = 0.06, eta = 0.1, sigma = 0.2, n = 10**7, y0 = [10**7-100, 0, 100, 0, 4*0.06], t_span = [0,400]):
    try:
        if( len(t) != len(R)):
            raise ValueError('Les données ne sont pas valides !')
        if not t or not R:
            raise ValueError('Aucune donnée !')
        R_func = CubicSpline(t,R, bc_type = 'clamped')
        solution = ode45(lambda t_ode, y : seirmodel(t_ode, y, gamma, sigma, eta, R_func), t_span, y0)
        #Dessiner graphique
        pyplot.figure()
        pyplot.plot(solution.t, solution.y[0,:], label="S")
        pyplot.plot(solution.t, solution.y[1,:], label="E")
        pyplot.plot(solution.t, solution.y[2,:], label="X")
        pyplot.plot(solution.t, solution.y[3,:], label="R")
        pyplot.plot(t, R, 'ro', label="Données")
        pyplot.legend(loc="best")
        pyplot.title("Modèle Sir")
        pyplot.xlabel("Temps(t)")
        pyplot.ylabel("Nombre de personnes")
        pyplot.savefig("pic_q5.png")
        return
    except ValueError as e:
        print('Erreur dans les données : ', e)
        return
    except Exception as e:
        print('Quelque chose s\'est mal passé : ', e)
        return
    
def test_q5():
    t = [ 0, 100, 200, 300]
    R = [ 0.5, 2, 3, 4]
    q5(t, R)
    
test_q5()


            
    
