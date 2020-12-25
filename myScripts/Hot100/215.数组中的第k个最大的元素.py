from typing import List
import heapq

# 使用堆排序实现
# 遍历数组建立一个结点数为k的最大堆，堆顶元素即为第k个最大的元素
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = []
#         n = len(nums)
#         for i in range(n):
#             # 如果堆中元素个数小于k，则将元素压入堆中
#             if len(heap) < k:
#                 heapq.heappush(heap, nums[i])
#             # 否则，如果当前元素比堆顶元素大，则将堆顶元素弹出，并将当前元素压入堆中
#             else:
#                 if nums[i] > heap[0]:
#                     heapq.heapreplace(heap, nums[i])
#
#         return heap[0]

import random


# 快速排序中的partition思想
class Solution:
    def _partition(self, nums, left, right):
        pivotIndex = random.randint(left, right)
        pivot = nums[pivotIndex]
        # pivotIndex = 4
        nums[pivotIndex], nums[left] = nums[left], nums[pivotIndex]
        i = left
        for j in range(left + 1, right + 1):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[left], nums[i] = nums[i], nums[left]
        return i

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        left, right = 0, n - 1
        while True:
            idx = self._partition(nums, left, right)
            if idx == target:
                return nums[idx]
            elif idx < target:
                left = idx + 1
            else:
                right = idx - 1


# Nums = [3, 2, 1, 5, 6, 4]
# K = 2
Nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
K = 4
print(Solution().findKthLargest(Nums, K))

# Nums = [2, 8, 21, 4, 2, 5, 3, 5, 7]
# Solution().partition(Nums, 0, len(Nums) - 1)
