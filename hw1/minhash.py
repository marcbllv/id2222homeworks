import numpy as np

class MinHash:

    @staticmethod
    def min_hash(sets, k=100):
        """
            Apply k hashfunctions to the elements of the set
            to compute a minhash signature.
            The hashfunctions are h(i) = a * i + 1 mod k
        """
        union = set()
        for s in sets:
            union = union | s

        print len(union)

        l = len(union)
        signatures = np.inf * np.ones((k, len(sets)))

        for row,elmt in enumerate(union):
            for a in range(0, k):
                current_hash = ((a + 1) * row + 1) % k
            
                for i,s in enumerate(sets):
                    if elmt in s:
                        if signatures[a,i] > current_hash:
                            signatures[a,i] = current_hash

        return signatures


