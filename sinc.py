import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-10,10,0.25)
a=np.sinc(2*np.pi*t)*(180/np.pi)
plt.plot(t,a)
plt.title('sinc pulse')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
