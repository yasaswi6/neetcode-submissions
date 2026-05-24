class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}

        for word in strs:
            alphabets = [0] * 26

            for char in word:
                alphabets[ord(char) - ord('a')] += 1

            key = tuple(alphabets)

            if key not in grouping:
                grouping[key] = []

            grouping[key].append(word)

        return list(grouping.values())