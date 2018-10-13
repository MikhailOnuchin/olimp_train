def slice(rect, slices):
    if rect in slices:
        return
    slices.add(rect)
    x1, y1, x2, y2 = rect
    # slice horisontally
    for x in range(x1 + 1, x2):
        slice((x1, y1, x, y2), slices)
        slice((x, y1, x2, y2), slices)
    # slice vertically
    for y in range(y1 + 1, y2):
        slice((x1, y1, x2, y), slices)
        slice((x1, y, x2, y2), slices)


slices = set()
slice((0, 0, 3, 1), slices)
print "total:", len(slices)
for s in slices:
    print s
