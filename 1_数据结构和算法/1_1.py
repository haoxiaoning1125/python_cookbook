if __name__ == '__main__':
    x, y = (1, 2)
    print x, y

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print name, shares, price, date

    try:
        data = ['ACME', 50, 91.1, (2012, 12, 21)]
        name, shares, price = data
    except Exception as e:
        print e

    s = 'hello'
    a, b, c, d, e = s
    print a, b, c, d, e

    _, b, c, d, _ = s
    print b, c, d
