from gensim.models import Word2Vec
import os

model = Word2Vec.load(os.path.realpath("./src/models/MP2V.model"))
result = model.wv.most_similar("title: Cyberlink PowerDirector 13 Ultimate Suite", topn=20)
print(result)