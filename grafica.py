import os
import numpy as np
import matplotlib.pyplot as plt


os.system("Marcha.cpp > datos.dat")

data = np.loadtxt("datos.dat")

plt.figure()
plt.plot(data[:,0], data[:,1])
plt.savefig("caminata.png")
