from time import strptime

ts_str1 = '2000-03-10T15:43:10+05:30'
ts_str2 = '2000-03-10T15:45:10+05:30'
ts1 = strptime(ts_str1, '%Y-%m-%dT%H:%M:%S+05:30')
ts2 = strptime(ts_str2, '%Y-%m-%dT%H:%M:%S+05:30')
print(ts2-ts1)