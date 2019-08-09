# coding:utf-8

"""
将 Unicode 文本标准化
"""

if __name__ == '__main__':
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print (s1, len(s1), s2, len(s2))
