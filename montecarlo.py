import numpy as np
import matplotlib.pyplot as plt


N_MUESTRAS = 10000

LADO_CUADRADO = 1

x = np.zeros((N_MUESTRAS))
y = np.zeros((N_MUESTRAS))

x_inlis = []
y_inlis = []

x_outlis = []
y_outlis = []

x_in = np.zeros

pilist = []

for i in range(N_MUESTRAS):
    x[i], y[i] = np.random.rand(2, 1)
    if (x[i] - LADO_CUADRADO/2)**2 + (y[i] - LADO_CUADRADO/2)**2 <= (LADO_CUADRADO/2)**2:
        x_inlis.append(x[i])
        y_inlis.append(y[i])
        x_in, y_in = np.array(x_inlis), np.array(y_inlis)
  
    else:
        x_outlis.append(x[i])
        y_outlis.append(y[i])
        x_out, y_out = np.array(x_outlis), np.array(y_outlis)
    
    numerical_pi = 4*(len(x_inlis)/(i+1))
    pilist.append(numerical_pi)
    plt.gca().set_aspect('equal')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title(r'Nª de muestras: %s / %s, $\pi \approx$ %.6f' %(i+1, N_MUESTRAS, numerical_pi))
    plt.plot(x_inlis[:i], y_inlis[:i], '.r')
    plt.plot(x_outlis[:i], y_outlis[:i], '.b')
    plt.pause(1e-5)
    plt.clf()
        


piarr = np.array(pilist)

def best_estimation(pi_array):
    realpiarray = np.zeros((len(pi_array)))
    diff = []
    for i in range(3000,len(pi_array)):
        absdiff = abs(pi_array[i] - np.pi)
        diff.append(absdiff)
    
    bestindex = 0
    for j in range(len(diff)):
        if diff[j-1] == min(diff):
            bestindex = j + 3000
        else:
            continue
            
    
    return bestindex
            
    


    

'''
x = np.linspace(1, N_MUESTRAS, N_MUESTRAS)



plt.title(r'$\pi$ estimation via Monte Carlo algorithm')
plt.plot(x, piarr, 'k')
plt.axhline(np.pi, ls='--', c='g', label=r'Real $\pi$ value')
plt.plot(best_estimation(piarr), piarr[best_estimation(piarr) - 1], 'r*', label = '$\pi$ $\\approx$ %.8f' %(piarr[best_estimation(piarr)]))
plt.xlabel('Nº of counts')
plt.ylabel(r'Estimation of $\pi$')
plt.legend()
plt.tight_layout()
plt.grid()
plt.savefig('piestimation.pdf')
'''
plt.show()




