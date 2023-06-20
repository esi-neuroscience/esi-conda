#
# Check most basic interactive plotting functionality
#
# Copyright © 2023 Ernst Strüngmann Institute (ESI) for Neuroscience
# in Cooperation with Max Planck Society
#
# SPDX-License-Identifier: CC-BY-NC-SA-1.0
#

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
plt.ion()
plt.figure()
plt.plot(x, np.sin(x))
