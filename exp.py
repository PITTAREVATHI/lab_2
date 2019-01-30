import numpy as np
import matplotlib.pyplot as plt
f=float(input('enter the frequency'))
t=np.arange(0,10,0.25)
a=np.exp(2*np.pi*f*t)
plt.plot(t,a)
plt.title('exponential')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
