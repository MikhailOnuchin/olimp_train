

def elevator(building, el_cap):
    time = 0
    el_pos = 0
    el_free = el_cap
    for floor in range(1, len(building) + 1):
        people = building[floor-1]
        if  people > 0:
            if el_pos < floor:
                el_pos = floor
            if people < el_free:
                el_free -= people
                continue
            time += 2*el_pos
            people -= el_free
            el_free = el_cap
            time += 2*el_pos*(people//el_cap)
            el_free -= people % el_cap
    if el_free != el_cap:
        time += 2*el_pos
    return time


def test1():
    assert elevator([3,0,1], 2) == 8


def test2():
    assert elevator([3,0,2], 2) == 14


def test_large():
    building = []
    for i in range(100000):
        building.append(1000000000)
    elevator(building, 1000000000)


def main():
    k = int(input())
    building = []
    for i in range(int(input())):
        building.append(int(input()))
    print(elevator(building, k))


if __name__ == '__main__':
    #main()
    test1()
    test2()
