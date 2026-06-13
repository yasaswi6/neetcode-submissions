class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # Ensure A is the smaller array
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        left, right = 0, m

        while True:
            i = (left + right) // 2
            j = half - i

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')

            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total length
                if total % 2:
                    return min(Aright, Bright)

                # Even total length
                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            # Too many elements taken from A
            elif Aleft > Bright:
                right = i - 1

            # Too few elements taken from A
            else:
                left = i + 1