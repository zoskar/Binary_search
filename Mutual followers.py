class Solution:
    def solve(self, relations):
        secik = set()
        ppl = set()
        for relation in relations:
            tup = tuple(sorted(relation))
            if tup in secik:
                ppl.add(tup[0])
                ppl.add(tup[1])
            else:
                secik.add(tup)
        return sorted(list(ppl))