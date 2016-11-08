from collections import Counter
import hashlib

class Shingling:
    def __init__(self, k=10):
        self.k = k
        self.shingles = Counter()
        self.hshr = hashlib.md5()

    def compute_shingles(self, filename):

        with open(filename, 'r') as f:
            curr_shingl = f.read(self.k)
            self.shingles = Counter({self._hashr(curr_shingl): 1})

            while True:
                c = f.read(1)
                if not c:
                    break
                curr_shingl = curr_shingl[1:] + c
                self.shingles = self.shingles + Counter({self._hashr(curr_shingl): 1})
        return self.shingles

    def _hashr(self, string, size=4):
        self.hshr.update(string)
        return int(self.hshr.hexdigest()[-size:], 16)

