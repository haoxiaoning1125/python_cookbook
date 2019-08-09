# coding:utf-8

"""
结合时区的日期操作
"""

from datetime import datetime, timedelta
from pytz import timezone, utc


if __name__ == '__main__':
    d = datetime(2012, 12, 21, 9, 30, 0)
    print 'd: {}'.format(d)

    # Localize the date for Chicago
    central = timezone('US/Central')
    loc_d = central.localize(d)
    print 'loc_d: {}'.format(loc_d)

    # Convert to Bangalore time
    bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
    print 'bang_d: {}'.format(bang_d)

    # 处理本地化日期的通常的策略先将所有日期转换为 UTC 时间
    print ('loc_d: ', loc_d)
    utc_d = loc_d.astimezone(utc)
    print ('utc_d: ', utc_d)
    later_utc = utc_d + timedelta(minutes=30)
    print ('later_utc: ', later_utc.astimezone(central))
