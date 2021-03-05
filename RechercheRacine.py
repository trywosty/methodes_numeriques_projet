import numpy as np

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



