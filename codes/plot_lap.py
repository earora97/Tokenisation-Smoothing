#!/usr/bin/python

import numpy as np
import re
import matplotlib.pyplot as plt
import math
 
plt.show()

x5 = []
y5 =[]

i = 0 
dictr = np.load("trigram_wb_kn.dict.npy").item()
for a in dictr:
	print i, dictr[a]
	x5.append(i)
	y5.append(dictr[a])
	i += 1

y5.sort()
plt.plot(x5, y5)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Kenser Ney incorporating WB counts (Trigram)')
plt.show()