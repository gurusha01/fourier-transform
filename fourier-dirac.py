import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# step (x,i) calculates the value of fourier transform till ith number and at the given x
# step (x,i)= summation 4/pi*cos((2t+1)pi x)/2t+1

def step(x,i):
    t=0
    f=0
    while(t<i):
        k=np.cos((2*t+1)*np.pi*x)/(2*t+1)
        if (t%2==0):
            f=f+k
        else:
            f=f-k
        
        t=t+1
        
    return 4*f/np.pi
        
#dirac delta

def der_step(x,i):
    t=0
    f=0
    while(t<i):
        k=-1*np.pi*np.sin((2*t+1)*np.pi*x)
        if (t%2==0):
            f=f+k
        else:
            f=f-k
        
        t=t+1
        
    return 4*f/np.pi
        


def makesin(i):
    X=[]
    Y=[]
    x=0
    while(x<1):
        Y.append(der_step(x,2*i+1))
        X.append(x)
        x=x+0.001
    plt.clf()
    plt.plot(X,Y)

        
ani=FuncAnimation(plt.gcf(), makesin, interval=1)
plt.show()
