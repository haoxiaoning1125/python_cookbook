# coding:utf-8

"""
序列中出现次数最多的元素
"""

from collections import Counter

if __name__ == '__main__':
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
        'the', 'eyes', "don't", 'look', 'around', 'the',
        'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
    ]
    # 返回一个字典
    word_counts = Counter(words)
    print word_counts
    print '-' * 20

    # most_common
    top_three = word_counts.most_common(3)
    print ('top_three:', top_three)
    print '-' * 20

    # 增加计数
    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes', 'python']
    # for word in morewords:
    #     word_counts[word] += 1

    word_counts.update(morewords)

    print ('python:', word_counts['python'])
    print '-' * 20

    # Counter 实例可以跟数学运算操作相结合
    a = Counter(words)
    b = Counter(morewords)
    c = a + b
    print c
    d = a & b
    print d
