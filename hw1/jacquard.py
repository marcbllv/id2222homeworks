class Jacquard:

    @staticmethod
    def similarity(set1, set2):
        return float(len(set1 & set2)) / float(len(set1 | set2))
