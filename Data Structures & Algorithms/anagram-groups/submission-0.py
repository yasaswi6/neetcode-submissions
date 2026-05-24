class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}
        for i in range (0,len(strs)):
            alphabets = [0] * 26
            for j in strs[i]:
                alphabets[ord(j) - ord('a')] += 1
            grouping[tuple(alphabets)] = []
        
        for i in range (0,len(strs)):
            alphabets = [0] * 26
            for j in strs[i]:
                alphabets[ord(j) - ord('a')] += 1
            if tuple(alphabets) not in grouping:
                grouping[tuple(alphabets)] = [""]
            else:
                grouping[tuple(alphabets)].append(strs[i])
        print(grouping)
        return list(grouping.values())




        
        