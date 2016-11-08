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

