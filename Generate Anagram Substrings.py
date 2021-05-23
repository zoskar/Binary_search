class Solution:
    def solve(self, s):
        res = []
        subs = [s[i: j] for i in range(len(s))
        for j in range(i + 1, len(s) + 1)]
        subs_ = []
        for el in subs:
            el = sorted(el)
            subs_.append(''.join(el))
        for i, el in enumerate(subs):
            tmp = subs_[i]
            del(subs_[i])
            if ''.join(sorted(el)) in subs_:
                res.append(el)
            subs_.insert(i, tmp)
        res = sorted(res)
        return res
