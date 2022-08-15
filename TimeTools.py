import time
import calendar

# 处理UTC时间到指定的字符串
str_time = '2022-08-15T01:25:29.126869+00:00'
refactor_time = time.strptime(str(str_time.replace('T', ' ')[:-6]), "%Y-%m-%d %H:%M:%S.%f") # just remain seconds
second = calendar.timegm(refactor_time)
mill_seconds = str_time[-12:-6]
time_with_ms = float(str(second) + "." + mill_seconds)
print(time_with_ms)
