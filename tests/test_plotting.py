# -*- coding: utf-8 -*-
#
# Check most basic interactive plotting functionality
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
plt.ion()
plt.figure()
plt.plot(x, np.sin(x))
