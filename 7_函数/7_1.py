# coding:utf-8

"""
可接受任意数量参数的函数
"""


def avg(first, *rest):
    return float(first + sum(rest)) / float(1 + len(rest))


def make_element(name, value, **attrs):
    keyvals = ['%s == "%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name} {attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=value
    )
    return element


def anyargs(*args, **kwargs):
    print args
    print kwargs


if __name__ == '__main__':
    print avg(1, 2)
    print avg(1, 2, 3, 4)
    print '-' * 20

    print make_element('item', 'Albatross', size='large', quantity=6)
    print make_element('p', '<spam>')
    print '-' * 20

    print anyargs(1, 2, 3, k=1, w=2, e=3)
    print '-' * 20
