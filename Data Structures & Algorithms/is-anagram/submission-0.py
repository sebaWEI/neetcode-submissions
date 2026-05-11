class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset = set(s)
        tset = set(t)
        sdict = dict()
        tdict = dict()
        for i in sset:
            sdict[i] = self.count(s, i)
        for i in tset:
            tdict[i] = self.count(t, i)
        if sdict == tdict:
            return True
        return False
        
    def count(self, target: str, character: str) -> int:
        count = 0
        target = "".join(i for i in target)
        for i in target:
            if i == character:
                count += 1
        return count
