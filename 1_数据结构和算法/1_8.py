# coding:utf-8

"""
字典运算
"""

if __name__ == '__main__':
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    print ('prices_keys:', prices.keys())
    print ('prices_values:', prices.values())
    print '-' * 20

    # ????
    prices_and_names = zip(prices.values(), prices.keys())
    print(min(prices_and_names))  # OK
    print(max(prices_and_names))  # ValueError: max() arg is an empty sequence
    print '-' * 20

    min_prize = min(zip(prices.keys(), prices.values()), key=lambda x: x[1])
    print ("min_prize:", min_prize)
    max_prize = max(zip(prices.keys(), prices.values()), key=lambda x: x[1])
    print ('max_prize:', max_prize)
    prices_sorted = sorted(zip(prices.keys(), prices.values()), key=lambda x: x[1], reverse=True)
    print ('prices_sorted:', prices_sorted)
    print '-' * 20

    # 当多个实体拥有相同的值的时候，键会决定返回结果
    prices = {'AAA': 45.23, 'ZZZ': 45.23}
    print min(zip(prices.values(), prices.keys()))
    print max(zip(prices.values(), prices.keys()))
