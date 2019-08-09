# coding:utf-8

"""
从字典中提取子集
"""

if __name__ == '__main__':
    prices = {
        'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
    }

    # 字典生成式
    p1 = {k: v for k, v in prices.items() if v > 200}
    print ('p1:', p1)
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {k: v for k, v in prices.items() if k in tech_names}
    print ('p2:', p2)
    print '-' * 20
