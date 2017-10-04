from tokenise import tokenise
import numpy as np
corpus=raw_input("Enter the name of corpus file: ")
V=int(raw_input("Enter size of vocabulary: "))
t=tokenise(corpus)
t.unigram_create()
t.bigram_create()
t.trigram_create()
np.save("unigram.dict",t.unigram)
np.save("bigram.dict",t.bigram)
#np.save("n1w1.dict",t.n1w1)
#np.save("n1w2.dict",t.n1w2)
np.save("trigram.dict",t.trigram)
#np.save("n1w1w2.dict",t.n1w1w2)
#np.save("n1w2w3.dict",t.n1w2w3)

#info={'corpus':corpus,'V':V, "chEp":t.chEp, "n1Ep":t.n1Ep, "n1w2s":t.n1w2s}
info={'corpus':corpus,'V':V}
np.save("info.dict",info)
