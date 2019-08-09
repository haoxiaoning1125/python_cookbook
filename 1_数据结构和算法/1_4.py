# coding:utf-8

"""
heap
"""

import heapq

if __name__ == '__main__':
    nums1 = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print heapq.nlargest(3, nums1)
    print heapq.nsmallest(3, nums1)

    print '-' * 20

    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    print heapq.nsmallest(3, portfolio, key=lambda x: x['price'])
    print heapq.nlargest(3, portfolio, key=lambda x: x['price'])
    print heapq.nsmallest(3, portfolio, key=lambda x: x['name'])

    print '-' * 20

    nums2 = [10, 16, 1, 2, -10, 999, -999]
    heap = []
    for num in nums2:
        heapq.heappush(heap, num)
    print [heapq.heappop(heap) for _ in range(len(nums2))]

    heapq.heapify(nums2)  # 将list类型转化为heap, 在线性时间内, 重新排列列表
    print [heapq.heappop(nums2) for _ in range(len(nums2))]

    print '-' * 20

    num1 = [32, 3, 5, 34, 54, 23, 132]
    num2 = [23, 2, 12, 656, 324, 23, 54]
    num1.sort()
    num2.sort()

    res = heapq.merge(num1, num2)  # 合并多个排序后的序列成一个排序后的序列， 返回排序后的值的迭代器
    ret = []
    for r in res:
        ret.append(r)
    print ret

    print '-' * 20

    nums3 = [1, 2, 3, 4, 5]
    heapq.heapify(nums3)
    heapq.heapreplace(nums3, 23)  # 删除堆中最小元素并加入一个元素
    print [heapq.heappop(nums3) for _ in range(len(nums3))]
