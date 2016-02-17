import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

mpl.rc('text', usetex = True)

def theta(x):
    return 0.5 * (np.sign(x) + 1)
    
def phi_1(x):
    return np.pi*0.5 * (np.sign(x) + 1)
    
def phi_2(x):
    return -np.pi*0.5 * (np.sign(x) + 1) - np.pi/4.
    
x = np.arange(-150.,150,0.1)

plt.figure(1)
plt.subplot(211)
plt.axis([-150,150,-0.1,1.1])
plt.ylabel('Intensity')
plt.plot(x, theta(x), 'k')
plt.grid(True)

plt.subplot(212)
plt.axis([-150,150,-2*np.pi,2*np.pi])
plt.xlabel(r'Position [$\mu$m]')
plt.ylabel(r'Phase $\phi$')
plt.plot(x, phi_1(x), 'k', x, phi_2(x), 'b')
plt.yticks(np.arange(-2*np.pi, 2*np.pi + 1, 0.5*np.pi), [r'$-2\pi$', r'$-3/2 \pi$', r'$-\pi$', r'$-1/2 \pi$', '$0$', r'$1/2 \pi$', r'$\pi$', r'$3/2 \pi$', r'$2 \pi$'])
plt.grid(True)

plt.show()