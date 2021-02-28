import numpy as np
from scipy.integrate import solve_ivp as ode45

def bissection(f, x0, x1, tol):
    if tol < 2*10**(-16):
        print('tolerance impossible')
        return x0,1
    if f(x0)*f(x1) > 0:
        print("Erreur : les f(x0) et f(x1) sont de même signe ! ")
        return x0, 1
    xi  = (x0 + x1) / 2
    print("je passe ici !")
    f_x0 = f(x0) 
    while abs((x1-x0)/2) > tol:
       # print("je ne passe pas ici !")
        xi = (x1 + x0)/2
        f_xi  = f(xi)
        print("milieu", xi)
        if (f_x0*f_xi <= 0):
            x1 = xi
        else:
            x0 = xi
            f_x0 = f_xi
    #print("Tout s'est passé comme il faut")
    return (x1+x0)/2, 0
  #est-ce que le changement de valeur est bonne, ou l'inverse ? 

def secante(f, x0, x1, tol, it_max = 50):
    try:
        mantisse  = 2*10**(-16)
        iterant = 0
        if tol < mantisse:
            raise ValueError("Tolérence plus grand que la mantisse !")
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        while abs(f_x1) > tol:
            print("x : ", x1, " f_x1 : " , f_x1, " f_x1 - f_x0 : " , f_x1-f_x0)
            diff  = f_x1 - f_x0
           
            if not diff:
                raise ZeroDivisionError
            if abs(f_x1) < mantisse:
                print('Mantisse ! ')
                return x1, -1 
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
            return x1, -1
    except StopIteration as e:
            print("Boucle stoppée !  : ", e)
            return x1, -1
    except Exception as e:
            print("Erreur survenue !  : ", e)
            return x1, -1
        
    return x1, 0
def sirmodel(t, y, beta , gamma):
    n = y[0] + y[1] + y[2]
    dy = np.zeros(3)
    dy[0] = (-beta * y[0] * y[1]) / n
    dy[1] = (beta*y[0]*y[1]) / n - gamma*y[1]
    dy[2] = gamma*y[1]
    return dy

#prend en compte toutes les possibilités ? -non convergence

#vérifier les codes erreurs
# f(x) = X- x*
def b_max_fun(beta, Xstar,gamma,  y0):
    solution_init = ode45(lambda t, y : sirmodel(t,y, beta, gamma), [0, 400], y0)
    return solution_init.y[1].max() - Xstar

def recherchebetaSIR(Xstar, gamma, y0, incr = 1, it_max=150):
    beta_it = 0.06 * 4
    my_fun = lambda beta_test : b_max_fun(beta_test, Xstar, gamma, y0)
    status = 1
    it = 0
    while status != 0:
        if it >= it_max:
            print("Trop d'iterations! ")
            return -1
        if Xstar > (y0[0]+y0[1]+y0[2]):
            print("Le nombre de personnes infectés ne peut pas dépasser le nombre d'habitant !")
            return -1
        beta_max, status = bissection(my_fun, 0, beta_it, 10**(-14))
#        if status == -1:
#            print("Le méthode ne converge pas !")
#            return -1
        beta_it += incr
        it += 1
    return beta_max

def seirmodel(t, y, gamma, sigma, eta, Rstar):
    n = 10**7
    dy = np.zeros(5)
    #beta(t) et e(t) donc 5eqn, page 2 equations
    dy[0] = (-y[4]*y[0]*y[2])/n            #s
    dy[1] = (y[4]*y[0]*y[2])/n - (sigma*y[1])          #e
    dy[2] = (sigma*y[1]) - (gamma*y[2])        #x
    dy[3] = gamma*y[2]             #r
    dy[4] = eta*((gamma*Rstar)-y[4])                      #beta
    return dy
#avec une valeur arbitraire fixée 

def r_max_fun(r, gamma, sigma, eta, y0, Xstar):
    solution = ode45(lambda t, y : seirmodel(t,y,gamma,sigma,eta,r), [0,400], y0)
    return solution.y[2].max() -Xstar


def rechercheReprodSEIR(Xstar, gamma, sigma, eta, y0):
    my_fun = lambda r_test : r_max_fun(r_test, gamma, sigma, eta,y0, Xstar)
    r_it = 4
    status = 1
    while status != 0:
        r_max, status = bissection(my_fun, 0, r_it, 10**(-12))
        r_it += 1000
    return r_max

#x, y = secante(lambda x : 1/x  , 0.5, 2, 10**(-5))
def testbetasir():
    x_0 = 100
    s_0 = 10**(7) - x_0
    r_0 = 0
    y0 = [s_0, x_0, r_0]
    gamma = 0.06
    my_beta = recherchebetaSIR(9.99*10**(6), 0.06, y0)
    solution_test = ode45(lambda t,y : sirmodel(t, y, my_beta, gamma), [0,400], y0)
    
    print("beta", my_beta)
    print("MAX VAL : ", solution_test.y[1].max())

def testReprodSEIR():
    Rstar = 4  #logiquement R_random car on ne connait pas la valeur Rstar
    Xstar = 5*10**(6)
    gamma = 0.06
    eta = 0.1
    sigma = 0.2
    n = 10**7
    x_0 = 100
    s_0 = n - x_0
    r_0 = 0
    b_0 = Rstar*gamma
    e_0 = 0
    r_max = rechercheReprodSEIR(Xstar, gamma, sigma, eta, [s_0, e_0, x_0, r_0, b_0])
    solution_test = ode45(lambda t, y : seirmodel(t,y, gamma, sigma, eta, r_max), [0, 400], [s_0, e_0, x_0, r_0, b_0])
    print("MAX VAL: ", solution_test.y[2].max())
    print("Rstar : ", r_max)
#print(x, y)
#testReprodSEIR()
#testbetasir()
x, status = bissection(lambda x: np.cos(x)+np.sin(x)-1/2, 1, 3, 10**(-15))
print(" x : ", x , " f(x) " , np.cos(x)+np.sin(x)-1/2)



