from xy import generate_xy as xygen
from matplotlib import pyplot as plt

xy_list = xygen.generate_xy(int(input('Enter a\n')), int(input('Enter b\n')))

plt.plot(xy_list[0], xy_list[1], label='x and y')
plt.title('x and y plot')
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()
plt.show()
