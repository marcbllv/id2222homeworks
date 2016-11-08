from collections import Counter

class Shingling:
    def __init__(self, k=10):
        self.k = k

    def shingles(self, filename):
        curr_shingl = doc.read(self.k)
        shingls = Counter({curr_shingl: 1})

        while True:
            c = doc.read(1)
            if not c:
                break
            curr_shingl = curr_shingl[1:] + c
            shingls = shingls + Counter({curr_shingl: 1})

if __name__ == '__main__':
    k = 10
    shingling = Shingling(k)
    with open('topics/accuracy_garmin_nuvi_255W_gps.txt.data', 'r') as f:
        shingling.shingles(f)
