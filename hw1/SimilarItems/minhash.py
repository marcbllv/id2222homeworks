import numpy as np
import md5

class MinHash:

    @staticmethod
    def signatures(sets, n=100):
        """
            Apply n hashfunctions to the elements of the set
            to compute a minhash signature.
            The hashfunctions are h(i) = a * i + 1 mod len(union)
        """
        union = set()
        for s in sets:
            union = union | s

        l = len(union)
        signatures = np.inf * np.ones((n, len(sets)))
        hashs = np.zeros((n, len(sets)))

        """
            hash functions are generated using md5 for the first one, then n-1
            random numbers that are XORed with the first hash as the n-1 next
            hash functions.
            Random numbers needs to be the same for all the documents.
        """
        # Random numbers for hash functions, max = 16^4
        rnd = np.random.randint(0, 65536, n)

        for row,elmt in enumerate(union):
            # Computing hash functions
            hashs = np.zeros(n, dtype=int)
            hhh = md5.new(str(elmt)).hexdigest()[:4]
            hashs[0] = int(hhh, 16)
            for i in range(1,n):
                hashs[i] = hashs[0] ^ rnd[i]

            for i,s in enumerate(sets):
                if elmt in s:

                    for j,h in enumerate(hashs):
                        if signatures[j,i] > h:
                            signatures[j,i] = h
                                

        return signatures

    @staticmethod
    def compare_signatures(sign_matrix, col1=0, col2=1):
        """
            Returns the fraction of rows where column 1 and column 2 have the
            same signature
        """
        return np.where(sign_matrix[:,col1] == sign_matrix[:,col2])[0].shape[0] / float(sign_matrix.shape[0])


