from ctypes import sizeof
from datetime import datetime,timedelta
from time import time


a = [
    # '11:49',
    # '4:05',
    # '15:42',
    # '7:48',
    # '3:02',
    # '54:43',
    # '6:45',
    # '31:14',
    # '1:17:56',
    # '31:47',
    # '38:37',
    # '1:16:53',
    # '26:27',
    # '43:26',
    # '32:39',
    # '23:49',
    # '15:07',
    # '43:28',
    # '27:44',
    # '13:27',
    # '9:29',
    # '1:09:27',
    # '12:37',
    # '57:33',
    # '40:44',
    # '31:55',
    # '12:04',
    # '7:49',
    # '33:01',
    # '12:57',
    # '10:00',
    # '25:40',
    # '7:57',
    # '10:52',
    # '25:09',
]

timestamp = []
for t in a:
    if(len(t)<=5):
        d = datetime.strptime(t, '%M:%S').time()
    else:
        d = datetime.strptime(t, '%H:%M:%S').time()
    s = ()
    a = (d.hour,)
    s = s + a
    a = (d.minute,)
    s = s + a
    a = (d.second,)
    s = s + a
    timestamp.append(s)

ho,mi,se = 0,0,0
for aaa in timestamp:
    ho += aaa[0]
    mi += aaa[1]
    se += aaa[2]

mi = mi * 60
ho = ho * 60 * 60
se = se + mi +ho

def convert(n):
    return str(timedelta(seconds = n))
     
print(convert(se))