

def sntp(a, b, c):
    timea = int(a[:2]) * 3600 + int(a[3:5]) * 60 + int(a[6:])
    timeb = int(b[:2]) * 3600 + int(b[3:5]) * 60 + int(b[6:])
    timec = int(c[:2]) * 3600 + int(c[3:5]) * 60 + int(c[6:])
    if timea > timec:
        timec += 86400
    delta = (timec-timea) / 2
    timeb = int(timeb + delta + 0.5) % 86400
    hours = timeb // 3600
    mins = (timeb % 3600) // 60
    secs = timeb % 60
    return '%02d:%02d:%02d' % (hours, mins, secs)


def test1():
    assert sntp('15:01:00', '18:09:45', '15:01:40') == '18:10:05'


def test2():
    assert sntp('16:00:40', '00:00:00', '16:01:30') == '00:00:25'


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(sntp(a, b, c))


if __name__ == '__main__':
    test1()
    test2()
    #main()