from matplotlib.pyplot import subplots
import numpy as np
fig,ax = subplots(figsize=(8,8))
x = np.linspace(-np.pi,np.pi,50)
y=x
f= np.multiply .outer(np.cos(y),1/(1+x**2))
ax.contour(x,y,f);
