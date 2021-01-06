import numpy as np

x = np.arange(1,10)
y = 32 * 45
z = y / 0.25


if z < 0.001:
    print('an error has occured')

print(x, y, z)


# Wriju added this line
# This will create a conflict with
# The Pull request from Sergio
