class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {} # sorted(str) : i
        final_list = list()
        for i in strs:
            id = tuple(sorted(i))
            if id in dic.keys():
                final_list[dic[id]].append(i)
            else:
                dic[id]=len(final_list)
                final_list.append([i])
        return final_list
