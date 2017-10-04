import numpy as np

d=np.load("unigram.dict.npy").item()
for x in d:
    print(x,d[x])
