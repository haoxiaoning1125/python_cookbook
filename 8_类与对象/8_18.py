# coding:utf-8

"""
利用 Mixins 扩展类功能
"""

from collections import defaultdict


class LoggedMappingMixin(object):
    """
    Add logging to get/set/delete operations for debugging.
    """
    __slots__ = ()  # 混入类都没有实例变量，因为直接实例化混入类没有任何意义

    def __getitem__(self, item):
        print ('Getting ' + str(item))
        return super(LoggedMappingMixin, self).__getitem__(item)

    def __setitem__(self, key, value):
        print ('Setting {} = {!r}'.format(key, value))
        return super(LoggedMappingMixin, self).__setitem__(key, value)

    def __delitem__(self, key):
        print ('Deleting ' + str(key))
        return super(LoggedMappingMixin, self).__delitem__(key)


class SetOnceMappingMixin(object):
    '''
    Only allow a key to be set once.
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + 'already set')
        return super(SetOnceMappingMixin, self).__setitem__(key, value)


class StringKeysMappingMixin(object):
    '''
     Restrict keys to strings only
    '''
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('keys must be strings')
        return super(StringKeysMappingMixin, self).__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


if __name__ == '__main__':
    ld = LoggedDict()
    ld['x'] = 23
    print ld['x']
    del ld['x']
    print '-' * 20

    sd = SetOnceDefaultDict()
    sd['y'] = 12
    print sd['y']
