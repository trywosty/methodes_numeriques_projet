import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from matplotlib import pyplot 
from numpy.polynomial.polynomial import polyfit
from numpy.polynomial import Polynomial as poly

def q1():
    x = np.linspace(-1, 1, 100)
    y  = x**2 + 1
    plt.plot(x, y)
    
def q2():
    x = np.arange(10, 1001, 1)
    i = 0
    while i < 991:
        if (x[i]%5 == 0):
            print(x[i])
        i += 1 
        
def q3():
    x = np.zeros((100, 100))
    y = np.arange(1, 101, 1)
    i = 0
    while i < 100:
        x[i, :] = y[:]
        i += 1 
    print(x)
    
def q4():
    x = np.random.rand(100)
    print(np.argmin(x))
    
def q5():
    x = np.random.rand(100, 100)
    i = 0
    while i < 100:
        print(sum(x[: , i]))
        i += 1
        
def q6():
    x = np.random.rand(100, 100)
    print(x[:,np.argwhere(x < 0.01)[0][1]])

def q7():
    x = np.arange(0, 4 ,1 )
    y = ([1, 2, 1 ,2])
    cs = CubicSpline(x, y)
    print(cs(1.5))
    
def q8():
    x = np.arange(0, 4, 1)
    y = ([1, 2, 1, 2])
    q = polyfit(x, y, 3)
    p = poly(q)
    print(p(1.5))
    
def q9():
    x = np.arange(1, 101, 1)
    y = x**2
    print(sum(y))
    
def q10():
    x = np.arange(1, 101, 1)
    y = np.arange(100, 0 , -1)
    print(np.dot(x, y))
    
def q11():
    x = np.arange(1, 1001, 2)
    y = np.sin(x)
    plt.plot(x, y)
    
def q12():
    x = np.random.rand(500, 500)
    print(np.dot(x[3, :], x[:, 455]))
    
def q13():
    x = np.linspace(-10, 10, 100)
    y = x - 1 
    plt.plot(x, y)
    
def q14():
    x = np.random.rand(100, 100)
    print(np.trace(x))
    
def q15():
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    
def q16():
    x = np.random.rand(1000)
    print(np.diff(x))
    
def q17():
    x = np.random.rand(10, 10)
    print(np.argwhere(x < 0.2))
    
def q18():
    x = np.random.uniform(0, 10, 542)
    y = np.arange(1, 543, 1)
    print(x*y)
    
def q19():
    x = np.random.rand(100, 100)
    y = np.random.rand(100, 100)
    xdiag = np.diag(x)
    ydiag = np.diag(y)
    print(np.dot(xdiag , ydiag))
    
def q20():
    x = np.linspace(0, 10, 100)
    y = np.cos(x)
    cs = CubicSpline(x, y)
    print(cs(5.5))
    
def q21():
    x = np.random.rand(100)
    y = np.argwhere(x > 0.5)
    print(len(y))
    
def q22():
    x = np.linspace(-10, 10, 1000)
    y = (100 - x**2)**(1/2)
    plt.plot(x, y)
    plt.plot(x, -y)
    
def q23():
    x = np.zeros(20)
    i = 0
    while i < 19:
        x[i] = x[i]
        i += 1
    y = np.argwhere((1+x)- 1 == 0)
    print(y[0])
    
def q24():
    x = np.arange(0, 31, 1)
    y = 0.5**x
    print(sum(y))
    
def q25():
    x = np.linspace(10**-6, 10**-4, 1000)
    y = (1-np.cos(x))/x**2
    plt.plot(x, y)
    
def q26():
    x = np.arange(1, 6, 1)
    y = x**(1/2)
    cs = CubicSpline(x, y)
    print(cs(2.5))
    
def q27():
    x = np.random.rand(100)
    print(np.argmax(x))
    
def q28():
    x = np.zeros((10, 10))
    i = 0
    j = 0
    while i < 10:
        while j < 10:
            x[i, j] = np.cos(j) * np.exp(i)
            j += 1
        j = 0
        i += 1
    print(x[2, 6])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
