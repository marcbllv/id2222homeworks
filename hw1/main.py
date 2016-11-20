import numpy as np
import os
from SimilarItems.shingling import Shingling
from SimilarItems.minhash import MinHash

k = 10
shingling = Shingling(k)

path = 'topics'
documents = [os.path.join(path, f) for f in os.listdir(path)]

shingls = []

n_docs = 40
print 'Computing similarity matrix for the following', n_docs, 'documents.'
for d in documents[:n_docs]:
    print '-', d
    shingls.append(shingling.compute_shingles(d))

mh = MinHash.signatures(shingls, n=100)

compared = np.zeros((mh.shape[1], mh.shape[1]))
for i in range(mh.shape[1]):
    for j in range(i):
        compared[i,j] = MinHash.compare_signatures(mh, col1=i, col2=j)

print compared

