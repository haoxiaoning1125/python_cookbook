# coding:utf-8

"""
匿名函数捕获变量值
"""

if __name__ == '__main__':
    # 运行时绑定而非定义时绑定
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y
    print (a(10), b(10))

    # 定义时绑定
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print (a(10), b(10))
    print '-' * 20

    #
    funcs = [lambda x: x + n for n in range(5)]
    print [f(0) for f in funcs]
    #
    funcs = [lambda x, n=n: x + n for n in range(5)]
    print [f(0) for f in funcs]

