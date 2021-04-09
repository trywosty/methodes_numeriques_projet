import numpy as np
from scipy.integrate import solve_ivp as ode45
import timeit

def bissection(f, x0, x1, tol):
    if not tol:
        print('tolerance nulle ! Impossible')
        return [x0,1]
    if f(x0)*f(x1) > 0:
        print("Erreur : les f(x0) et f(x1) sont de même signe ! ")
        return [x0, 1]
    xi  = (x0 + x1) / 2
    f_x0 = f(x0) 
    while abs((x1-x0)/2) > tol:
       # print("je ne passe pas ici !")
        xi = (x1 + x0)/2
        f_xi  = f(xi)
        if (f_x0*f_xi <= 0):
            x1 = xi
        else:
            x0 = xi
            f_x0 = f_xi
    #print("Tout s'est passé comme il faut")
    return [(x1+x0)/2, 0]
  #est-ce que le changement de valeur est bonne, ou l'inverse ? 

def sirmodel(t, y, beta , gamma):
    n = y[0] + y[1] + y[2]
    dy = np.zeros(3)
    dy[0] = (-beta * y[0] * y[1]) / n
    dy[1] = (beta*y[0]*y[1]) / n - gamma*y[1]
    dy[2] = gamma*y[1]
    return dy
# Fonction a valeur continue au lieu d'un tableau à valeurs discrètes
# plus de precision
def ternarySearchMax(t,tab, tol = 10**-10):
    fun = CubicSpline(t, tab, bc_type='clamped')
    f = 0
    l = t[-1]
    while abs(l-f) > tol :
        f_third = f + (l-f)/3
        l_third = l - (f_third-f)
        print("f_third : ", f_third)
        print("l_third : ", l_third)
        (f := f_third) if fun(f_third) < fun(l_third) else (l := l_third)
    return fun((f+l)/2)
  
def b_max_fun(beta, Xstar,gamma,  y0):
    solution_init = ode45(lambda t, y : sirmodel(t,y, beta, gamma), [0, 400], y0)
    return ternarySearchMax(solution_init.t, solution_init.y[1]) - Xstar

def recherchebetaSIR(Xstar, gamma, y0):
    beta_it = 0.06 * 4
    my_fun = lambda beta_test : b_max_fun(beta_test, Xstar, gamma, y0)
    status = 1
    it = 0
    while status != 0:
        if it >= 150:
            print("Trop d'iterations! ")
            return [0, 1]
        if Xstar > (y0[0]+y0[1]+y0[2]):
            print("Le nombre de personnes infectés ne peut pas dépasser le nombre d'habitant !")
            return [0, -1]
        beta_max, status = bissection(my_fun, 0, beta_it, 10**(-14))
        beta_it += 1
        it += 1
    return [beta_max, 0]

def secante(f, x0, x1, tol, it_max = 150):
    try:
        iterant = 0
        if not tol:
            raise ValueError("Tolérence nulle ! Impossible")
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        while abs(f_x1) > tol:
            diff  = f_x1 - f_x0
           
            if not diff:
                raise ZeroDivisionError
     
            if iterant >it_max:
                raise StopIteration('On a dépasse le nombre max d\'itérations ! ')
            x2 = x1 - ((f_x1*(x1-x0)) / (diff))
            x0 = x1
            x1 = x2
            f_x0 = f_x1
            f_x1 = f(x1)
            iterant += 1
    except ZeroDivisionError :
            print("Division par zero ! ")
            return [x1, 1]
    except StopIteration as e:
            print("Boucle stoppée !  : ", e)
            return [x1, -1]
    except Exception as e:
            print("Erreur survenue !  : ", e)
            return [x1, -1]
    except ValueError as e:
            print("Erreur de valeur ! : ", e)
            return [x1, 1]
        
    return [x1, 0]


#prend en compte toutes les possibilités ? -non convergence


#x, y = secante(lambda x : 1/x  , 0.5, 2, 10**(-5))
def testbetasir():
    x_0 = 100
    s_0 = 10**(7) - x_0
    r_0 = 0
    y0 = [s_0, x_0, r_0]
    gamma = 0.06
    start = timeit.default_timer()
    my_beta = recherchebetaSIR(101, 0.06, y0)
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    solution_test = ode45(lambda t,y : sirmodel(t, y, my_beta[0], gamma), [0,400], y0)
    
    print("beta", my_beta[0])
    print("MAX VAL : ", solution_test.y[1].max())
