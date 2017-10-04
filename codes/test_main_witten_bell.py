from tokenise_wb import tokenise
from witten_bell import witten_bell
import numpy as np
corpus=raw_input("Enter the name of corpus file: ")
V=int(raw_input("Enter size of vocabulary: "))
t=tokenise(corpus)
t.unigram_create()
info=np.load("info.dict.npy").item()
info["chEp"]=t.chEp
info["n1Ep"]=t.n1Ep
np.save("info_wb.dict",info)
t.bigram_create()
np.save("n1w1.dict",t.n1w1)
t.trigram_create()
np.save("n1w1w2.dict",t.n1w1w2)

w=witten_bell()
w.unigram_smooth()
np.save("unigram_wb.dict",w.unigram_wb)
w.bigram_smooth()
np.save("bigram_wb.dict",w.bigram_wb)
w.trigram_smooth()
np.save("trigram_wb.dict",w.trigram_wb)
