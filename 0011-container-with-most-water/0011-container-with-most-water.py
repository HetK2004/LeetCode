class Solution:
    def maxArea(self, h: List[int]) -> int:
        low = 0
        hei = len(h) - 1
        max_area = 0

        while low < hei:
            area = min(h[low],h[hei]) * (hei-low)

            max_area = max(max_area,area)

            if h[low] < h[hei]:
                low = low + 1
            else:
                hei = hei - 1
        return max_area