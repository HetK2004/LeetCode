class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0

        cur_sum = arr[0]
        cur_sum_del = 0
        max_sum = arr[0]

        for i in range(1,len(arr)):
            cur_sum_del = max(cur_sum ,cur_sum_del + arr[i])
            cur_sum = max(arr[i] , cur_sum + arr[i])
            max_sum = max(max_sum,cur_sum,cur_sum_del)
        return max_sum