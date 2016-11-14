import numpy as np

print '-- Testing shingles computation & jacqard similarity --'
from shingling import Shingling
from jacquard import Jacquard

k = 10
shingling = Shingling(k)
doc1 = 'topics/accuracy_garmin_nuvi_255W_gps.txt.data'
doc2 = 'topics/battery-life_ipod_nano_8gb.txt.data'

print 'Computing shingles for document', doc1
shg1 = shingling.compute_shingles(doc1)
print 'Computing shingles for document', doc2
shg2 = shingling.compute_shingles(doc2)

print 'Jacquard similarity between documents:', Jacquard.similarity(shg1, shg2)
print

print '-- Testing minhash computation --'
from minhash import MinHash

sh1 = set({'a', 'b', 'c', 'd', 'e', 'f'})
sh2 = set({'b', 'e', 'g'})

print 'Sets:', sh1, sh2
mh = MinHash.min_hash([sh1, sh2], k=100)
print mh
print 'Similarity=', np.where(mh[:,0] - mh[:,1] == 0)[0].shape[0] / float(mh.shape[0])

#print
#print 'On previous documnts:'
#mh = MinHash.min_hash([shg1, shg2], k=100)
#print mh
#print 'Similarity=', 1 - np.sum(mh[:,0] - mh[:,1]) / float(mh.shape[0])


