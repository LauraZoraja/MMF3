import numpy as np
import math as math
import matplotlib.pyplot as plt

def hermit(x = 10, n = 10):
    H0 = 1
    H1 = 2*x
    H_l = [H0, H1]
    for i in range (2,n+1):
        H = 2*x*H_l[i-1] - 2*(i-1)*H_l[i-2]
        H_l.append(H)
    return H

hermit()

def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

print('Derivacija unaprijed za h=10^-1 je {}'.format(forward_diff(hermit, 10, 10**(-1))))
print('Derivacija centralno za h=10^-1 je {}'.format(central_diff(hermit, 10, 10**(-1))))
print('Derivacija unaprijed za h=10^-3 je {}'.format(forward_diff(hermit, 10, 10**(-3))))
print('Derivacija centralno za h=10^-3 je {}'.format(central_diff(hermit, 10, 10**(-3))))