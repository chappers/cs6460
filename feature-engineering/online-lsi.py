# online lsi out of the box.

import gensim

documents = ["Apple is releasing a new product",
             "Amazon sells many things",
             "Microsoft announces Nokia acquisition"]

stoplist = ['is', 'and']

texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
dictionary = gensim.corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]


lsi = gensim.models.lsimodel.LsiModel(corpus=corpus, id2word=dictionary, num_topics=400)

documents2 = ["Google creates hardware division",
             "Yahoo is nowhere to be seen"]
             
texts2 = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
corpus2 = [dictionary.doc2bow(text) for text in texts2]

lsi.add_documents(corpus2)

lsi.print_topics(10)

# print stuff...

lsi[[(0, 1), (1, 1)]]

lsi[corpus2[1]]
# lsi adjusts weights but doesn't change in size! might not be suitable for our project


# https://github.com/RaRe-Technologies/gensim/issues/74
# https://groups.google.com/forum/#!topic/gensim/HvkeM2wAgMY


"""
Hi, 
- show quoted text -
you're right, the LSI update doesn't take new (or modified) features 
into account. It only updates on new observations (=documents), using 
the same old features. 

Interestingly, feature updates can also be done incrementally, in 
theory. This is not implemented in gensim though, so for modified 
features, your only option right now is to re-train LSI. 

HTH, 
Radim
"""
