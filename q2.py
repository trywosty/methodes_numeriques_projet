from scipy.integrate import solve_ivp as ode45
import numpy as np
from matplotlib import pyplot
from scipy.interpolate import CubicSpline
def sirmodel(t, y, beta , gamma):
    n = y[0] + y[1] + y[2]
    dy = np.zeros(3)
    dy[0] = (-beta * y[0] * y[1]) / n
    dy[1] = (beta*y[0]*y[1]) / n - gamma*y[1]
    dy[2] = gamma*y[1]
    return dy

def OLD_eulerexplicite_OLD(f, t_span, y0, h):
    t_f = t_span[1]
    t = np.array([t_span[0]])
    y  = np.array([y0])
    index = 0
    while t[index] <= t_f:
            y_t = y[index] + h*f(t[index], y[index])
            y = np.append(y, [y_t], axis = 0)
            t = np.append(t, t[index] + h)
            index += 1
    y = np.transpose(y)
    return  t, y
def eulerexplicite(f, t_span, y0, h):
    nbr_element = ((t_span[1] - t_span[0])//h) + 1 
    y = np.zeros((len(y0), nbr_element    ))
    t = np.linspace(t_span[0], t_span[1], num = nbr_element)
    y[:,0] = y0
    index = 0
    while index < len(t)-1:
        y_t = y[:,index] + h*f(t[index], y[:,index])
        index += 1
        y[:,index] = y_t
    return t, y
def main():
    n = 10**(7)
    x_0 = 100
    s_0 = n - x_0
    r_0 = 0
    gamma = 0.06
    # beta = R0 * gamma
    beta = gamma * 4
    solution = ode45(lambda t, y : sirmodel(t,y, beta, gamma), [0, 400], [s_0, x_0, r_0])
    pyplot.figure()
    pyplot.plot(solution.t, solution.y[0,:], label="S")
    pyplot.plot(solution.t, solution.y[1,:], label="X")
    pyplot.plot(solution.t, solution.y[2,:], label="R")
    pyplot.legend(loc="best")
    pyplot.title("Modèle Sir")
    pyplot.xlabel("Temps(t)")
    pyplot.ylabel("Nombre de personnes")
    pyplot.savefig("test.png")
    print(solution.y[1].max())
    function1 = CubicSpline(solution.t, solution.y[1], bc_type="clamped")
    t1 ,y1 = eulerexplicite(lambda t, y : sirmodel(t,y,beta,gamma),[0, 400], [s_0, x_0, r_0], 1    )
    print(function1)
    print(t1)
    print(y1)
    type(function1)
    pyplot.figure()
    pyplot.plot(t1, y1[0,:], label="S")
    pyplot.plot(t1, y1[1,:], label="X")
    pyplot.plot(t1, y1[2,:], label="R")
    pyplot.savefig("secondtest.png")
    print(solution.y[1].max())
    function2 = CubicSpline(t1, y1[1], bc_type="clamped")
    print(function2)

main()
