class Shingling:
    def __init__(self, k=10):
        self.k = k

    def shingles(self, doc):
        """
            doc is a file retreived using open('filepath')
        """
        shingls = {}
        curr_shingl = doc.read(self.k)
        shingls[curr_shingl] = 1

        while True:
            c = doc.read(1)
            if not c:
                break
            curr_shingl = curr_shingl[1:] + c
            shingls[curr_shingl] = 1
        

if __name__ == '__main__':
    k = 10
    shingling = Shingling(k)
    with open('topics/accuracy_garmin_nuvi_255W_gps.txt.data', 'r') as f:
        shingling.shingles(f)
