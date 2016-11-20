import numpy as np

print '-- Testing shingles computation & jacqard similarity --'
from SimilarItems.shingling import Shingling
from SimilarItems.jacquard import Jacquard

k = 10
shingling = Shingling(k)
doc1 = 'lipsum1.txt'
doc2 = 'lipsum2.txt'

print 'Computing shingles for documents', doc1, 'and', doc2, '.'
print
with open(doc1, 'r') as f:
    print 'Document 1:'
    print f.read()
    print
shg1 = shingling.compute_shingles(doc1)

with open(doc2, 'r') as f:
    print 'Document 2:'
    print f.read()
    print
shg2 = shingling.compute_shingles(doc2)

print 'Jacquard similarity between documents:', Jacquard.similarity(shg1, shg2)
print

print '-- Testing minhash computation --'
from SimilarItems.minhash import MinHash

sh1 = set({'a', 'b', 'f'})
sh2 = set({'b', 'g'})

print 'Sets:', sh1, sh2
mh = MinHash.signatures([sh1, sh2], n=10)
print 'Similarity=', MinHash.compare_signatures(mh)
print

n = 1000
print 'On previous documents, with', n, 'hash functions.'
mh = MinHash.signatures([shg1, shg2], n=n)
print 'Similarity=', MinHash.compare_signatures(mh)


