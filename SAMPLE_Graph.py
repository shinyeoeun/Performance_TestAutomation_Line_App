"""
x축 값을 커스텀하는 방법
xticks: x축을 구성하는 단위를 정의
xticklabels: x축에 해당하는 라벨을 정의
"""

import matplotlib.pyplot as plt
from numpy.random import randn

r = randn(1000).cumsum()
print(r)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xticks([0, 250, 500, 750, 1000])
ax.set_xticklabels(["item_1", "item_2", "item_3", "item_4", "item_5"], rotation=45, fontsize='small')
ax.set_title('wow')
ax.set_xlabel('hehe')
ax.plot(r)

plt.show()



