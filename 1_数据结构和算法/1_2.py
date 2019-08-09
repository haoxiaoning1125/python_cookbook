def drop_first_last(grades):
    # _, *middles, _ = grades   # python versions < 3.0
    return grades[1:len(grades) - 1]


if __name__ == '__main__':
    list_ = [1, 2, 3, 4]
    print drop_first_last(list_)
