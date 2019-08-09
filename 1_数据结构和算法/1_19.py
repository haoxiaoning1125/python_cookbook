# coding:utf-8

"""
转换并同时计算数据
你需要在数据序列上执行聚集函数 (比如 sum() , min() , max() )，但是首先你需要先转换或者过滤数据
向聚集函数传递生成器表达式而不是临时列表
"""

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]

    print sum(x * x for x in nums)
    print '-' * 20

    portfolio = [
        {'name': 'GOOG', 'shares': 50}, {'name': 'YHOO', 'shares': 75},
        {'name': 'AOL', 'shares': 20}, {'name': 'SCOX', 'shares': 65}
    ]
    min_shares = min(s['shares'] for s in portfolio)
    print min_shares
    print '-' * 20

    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))

    # s = sum((x * x for x in nums))  # 显示的传递一个生成器表达式对象
    # s = sum(x * x for x in nums) # 更加优雅的实现方式，省略了括号
