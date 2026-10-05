import numpy as np
import matplotlib.pyplot as plt

N_MUESTRAS = 10000

POS_INICIAL_x = 0
POS_INICIAL_y = 10000

COTA_BORDES = 9000

R_0 = np.zeros((N_MUESTRAS, 2))
R_0[:, 0] = POS_INICIAL_x
R_0[:, 1] = POS_INICIAL_y

def coinflip():
    result = 0
    randnum = np.random.rand(1)[0]
    if randnum >= 0.5:
        result = 1
    else:
        result = -1
    
    return result 



def galtonboard(R0):
    R = R0
    for i in range(N_MUESTRAS):
        while R[i, 1] >= COTA_BORDES + 1:
            R[i, 0] += coinflip()
            R[i, 1] = R[i, 1] - 1 
        
        if i == 0:
            R[i, 1] = 0
        elif max(R[:i, 1]*(R[:i, 0] == R[i, 0])) == COTA_BORDES:
            R[i, 1] == 0
        elif max(R[:i, 1]*(R[:i, 0] == R[i, 0])) >= 0:
            R[i, 1] = max(R[:i, 1]*(R[:i, 0] == R[i, 0])) + 1
    return R
            
R = galtonboard(R_0)

x = R[:, 0]
y = R[:, 1]


def gaussian_distribution(x, mu, sigma):
    term = (x - mu)/sigma
    exponent = -(1/2)*term**2
    module = 1/(sigma*np.sqrt(2*np.pi))
    return 250 * np.exp(exponent)

xx = np.linspace(min(R[:,0]), max(R[:,0]), 1000)
mu = 0
sigma = 35



print(xx)
plt.plot(x, y, 'sr', label='Data')
#plt.plot(xx, gaussian_distribution(xx, mu, sigma), 'g', label='Interfered Gaussian')
plt.title(r'Galton Board result for N = %i' %N_MUESTRAS)
plt.grid()
plt.tight_layout()
plt.legend()
plt.savefig('GaltonBoard.pdf')
plt.show()



