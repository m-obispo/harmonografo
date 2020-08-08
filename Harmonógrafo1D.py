import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import numpy as np

# defining function with default paramters value
def Pendulo(t, A, f, p, d):
    return (A*np.sin(2*np.pi*f*t + p)*np.exp(-1*d*t))

def Amplitude(t, A, d):
	return A*np.exp(-1*d*t)
# creating array for time
t = np.linspace(0, 50*np.pi, 6000)

fig = plt.figure(figsize = (12, 6), dpi = 100)
ax = fig.add_subplot()
ax.set_facecolor('k')
plt.style.use(['dark_background'])
plt.yticks(np.arange(-1., 1., 0.25))
xt = np.zeros(len(t))
yt = np.zeros(len(t))

def update(i):
    xt[i] = Amplitude(t[i], 1, 0.5)
    yt[i] = Pendulo(t[i], 1, 1, 0, 0.5)
    ax.clear()
    ax.plot(t[:i], xt[:i], 'w--', label = 'Amplitude')
    ax.plot(t[:i], -xt[:i], 'w--')
    ax.plot(t[:i], yt[:i], 'g', label = 'Pendulo')
    plt.title('Pendulo Amortecido: $t = $'+str(i), color = 'g')

    #plt.style.use(['dark_background'])
    #plt.axis('off')
    plt.legend(framealpha = 1, loc=1)
    plt.grid(True, color = 'b')
    #ax.set_facecolor('g')
    ax.set_xlabel('$t$')
    ax.set_ylabel('$y$')

ani = animation.FuncAnimation(fig, update, np.arange(600), interval = 10, repeat = False)
#ani.save('Pendulo_Amortecido.gif', writer = PillowWriter(fps = 30))
ani.save('Pendulo_Amortecido.mp4', writer = 'ffmpeg', fps = 60)
#plt.show()