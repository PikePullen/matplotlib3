import numpy as np
import matplotlib.pyplot as plt

X = np.random.randn(10000)

# draw data in generic weay
# plt.hist(X)

# show more bars
plt.hist(X, bins=50)
#
plt.show()

"""This creates a relatively flat histogram"""
# X = np.random.random(10000)
#
# # draw data in generic weay
# # plt.hist(X)
#
# # show more bars
# plt.hist(X, bins=50)
#
# plt.show()