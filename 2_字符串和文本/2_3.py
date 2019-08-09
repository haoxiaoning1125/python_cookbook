# coding:utf-8

"""
用 Unix Shell 通配符匹配字符串
"""

from fnmatch import fnmatch, fnmatchcase


if __name__ == '__main__':
    # fnmatch()
    print fnmatch('foo.txt', '*.txt')
    print fnmatch('foo.txt', '?oo.txt')
    print fnmatch('Dat45.csv', 'Dat[0-9]*')
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    print [name for name in names if fnmatch(name, 'Dat*.csv')]
    print '-' * 20

    # fnmatch() 函数使用底层操作系统的大小写敏感规则 (不同的系统是不一样的) 来匹配模式
    print fnmatch('foo.txt', '*.TXT')  # OS X: False, Windows: True
    print fnmatchcase('foo.txt', '*.TXT')
    print '-' * 20

    # 处理非文件名字符串
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    print [addr for addr in addresses if fnmatchcase(addr, '*ST')]
    print [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9]*CLARK*')]
