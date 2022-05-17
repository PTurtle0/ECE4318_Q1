import numpy as np
import scipy.integrate as integrate

def cdf(x):
    cdf_constant = 1.0 / np.sqrt(2*np.pi)
    cdf_integral = np.e ** ((-x**2) / 2.0)
    return (cdf_constant * cdf_integral)

z = np.arange(0, 4.99, 0.01, dtype=float)
phi = []

for i in z:
    x = z
    output = integrate.trapezoid(cdf, np.NINF, x)
    phi[i] = output

print(phi)
    

