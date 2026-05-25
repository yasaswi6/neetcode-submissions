class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1

        sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_freq[i][0])

        return result