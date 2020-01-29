import numpy as np
import prop as prop
from pandas import *
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import font_manager
from numpy.random import randn

r = randn(1000).cumsum()
print(r)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xticks([0, 250, 500, 750, 1000])
ax.set_xticklabels(["61609", "62141", "61958", "62638", "60847", "60763", "60143", "60844", "61771", "61800"], rotation=45, fontsize='small')
ax.set_title('wow')
ax.set_xlabel('hehe')
ax.plot(r)

plt.show()



