from collections import Counter
import md5

class Shingling:
    def __init__(self, k=10):
        self.k = k
        self.shingles = None
        self.hshr = md5

    def compute_shingles(self, filename):

        with open(filename, 'r') as f:
            curr_shingl = f.read(self.k)
            self.shingles = set([self._hasher(curr_shingl)])

            while True:
                c = f.read(1)
                if not c:
                    break
                curr_shingl = curr_shingl[1:] + c
                self.shingles.add(self._hasher(curr_shingl))
        return self.shingles

    def _hasher(self, string, size=4):
        hashed = self.hshr.new(string).hexdigest()
        return int(hashed[-size:], 16)

