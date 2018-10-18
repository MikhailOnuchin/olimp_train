

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
hours = int(timeb//3600 + 0.5)
timeb %= 3600
mins = int(timeb//60 + 0.5)
secs = int(timeb%60 +0.5)
print('%02d:%02d:%02d' % (hours, mins, secs))