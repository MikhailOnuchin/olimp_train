

a = input()
b = input()
c = input()
timea = int(a[:2])*3600 + int(a[3:5])*60 + int(a[6:])
timeb = int(b[:2])*3600 + int(b[3:5])*60 + int(b[6:])
timec = int(c[:2])*3600 + int(c[3:5])*60 + int(c[6:])
if timea > timec:
    timec += 86400
delta = (timec-timea)/2
timeb += delta
timeb %= 86400
hours = str(int(timeb//3600 + 0.5))
timeb %= 3600
mins = str(int(timeb//60 + 0.5))
secs = str(int(timeb%60 +0.5))
if len(hours) == 1:
    hours = '0' + hours
if len(mins) == 1:
    mins = '0' + mins
if len(secs) == 1:
    secs = '0' + secs
print(hours, ':', mins, ':', secs, sep=''
                                       '')