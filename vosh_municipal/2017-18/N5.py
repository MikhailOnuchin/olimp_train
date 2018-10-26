

def plusone(ticket):
    for i in range(len(ticket) - 1, -1, -1):
        if ticket[i] < 9:
            ticket[i] += 1
            break
    return ticket


def decrease(ticket, need_sum):
    changes = 0
    for i in range(len(ticket) - 2, -1, -1):
        if sum(ticket) <= need_sum:
            break
        if ticket[i] < 9:
            ticket[i] += 1
            ticket[i+1:] = [0] * (len(ticket) - 1 - i)
            changes += 1
    if changes > 0 and sum(ticket) <= need_sum:
        return ticket
    else:
        return None


def increase_to_sum(ticket, need_sum):
    ticket_sum = sum(ticket)
    diff = need_sum - ticket_sum
    for i in range(len(ticket) - 1, -1, -1):
        if diff <= 0:
            break
        if ticket[i] < 9:
            val = 9 - ticket[i]
            if diff < val:
                val = diff
            ticket[i] += val
            diff -= val
    return ticket


def lucky(ticket):
    my_ticket = []
    for ch in ticket:
        my_ticket.append(int(ch))
    n = len(my_ticket)
    if my_ticket == [9] * n:
        return ('0' * (n // 2 - 1) + '1') * 2
    ticket_left = my_ticket[:n // 2]
    ticket_right = my_ticket[n // 2:]
    left_sum = sum(ticket_left)
    right_sum = sum(ticket_right)
    if left_sum > right_sum:
        ticket_right = increase_to_sum(ticket_right, left_sum)
    if left_sum == right_sum:
        ticket_right = plusone(ticket_right)
        right_sum += 1
    if left_sum < right_sum:
        ticket_right = decrease(ticket_right, left_sum)
        if ticket_right is None:
            ticket_left = plusone(ticket_left)
            ticket_right = [0] * len(ticket_left)
            left_sum += 1
        ticket_right = increase_to_sum(ticket_right, left_sum)
    ticket_left += ticket_right
    ticket = ''
    for val in ticket_left:
        ticket += str(val)
    return ticket


def test():
    assert lucky('0908') == '0909'
    assert lucky('0808') == '0817'
    assert lucky('999999') == '001001'
    assert lucky('032450') == '032500'
    assert lucky('032999') == '033006'
    assert lucky('333433') == '333441'
    assert lucky('0001') == '0101'
    assert lucky('1010') == '1102'


def main():
    print(lucky(input()))


if __name__ == '__main__':
    test()
    #main()