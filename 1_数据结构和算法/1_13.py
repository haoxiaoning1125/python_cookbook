# coding:utf8

"""
根据某个或某几个字典字段来排序字典列表
"""

from operator import itemgetter

if __name__ == '__main__':
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    # 根据任意的字典字段来排序字典
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print ('rows_by_fname:', rows_by_fname)
    print ('rows_by_uid:', rows_by_uid)
    print '-' * 20

    # 支持多个 keys
    rows_by_flname = sorted(rows, key=itemgetter('fname', 'lname'))
    print ('rows_by_flname:', rows_by_flname)
