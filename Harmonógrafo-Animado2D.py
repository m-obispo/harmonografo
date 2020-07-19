import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#Definindo a função pendulo com valor de parâmetros padrão
def Pendulo(t, A = 1, f = 5, p = 0, d = 0.05):
    return (A*np.sin(2*np.pi*f*t + p)*np.exp(-1*d*t))

#Criando um array para t
t = np.linspace(0, 50*np.pi, 30000)

#Plotando os resultados
fig = plt.figure(figsize = (12, 6), dpi = 100)

ax = fig.add_subplot()
ax.set_facecolor('k')
plt.style.use(['dark_background'])

xt = np.zeros(len(t))
yt = np.zeros(len(t))

#Plotando a animação
def update(i):
    xt[i] = Pendulo(t[i], 2, 4, -1, 0.05) + Pendulo(t[i], 1, 2, np.pi, 0.01)
    yt[i] = Pendulo(t[i], 4, 2, np.pi/4, 0.02) + Pendulo(t[i], 1, 2, np.pi/2, 0.25) 
    ax.clear()
    ax.plot(xt[:i], yt[:i], 'g')
    #plt.axis('off')
    plt.grid(True)
    plt.title('$Harmonógrafo$: t = '+str(i), color = 'g')
    #plt.title('t = '+str(i))
    ax.set_xlabel('$x(t)$', color = 'g')
    ax.set_ylabel('$y(t)$', color = 'g')

#Plotagem para chamar a função update() periodicamente
ani = animation.FuncAnimation(fig, update, np.arange(600), interval = 10, repeat = False)
ani.save('Harmonógrafo2D.gif', writer = PillowWriter(fps = 100))
#plt.show()