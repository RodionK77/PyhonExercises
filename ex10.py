def edit(lst):
    for i in range(len(lst)):
        lst[i][4] = None

    for i in range(len(lst)):
        lst[i] = list(filter(None, lst[i]))

    lst = list(filter(None, lst))

    for i in range(len(lst)):
        lst[i][1] = lst[i][1].replace('-', '.')

    l1 = []
    for i in lst:
        l1.append([])

    for i in range(len(lst)):
        if lst[i][0][0:2] == 'да':
            l1[i].append('Выполнено')
            l1[i].append(lst[i][0][10:19])
            l1[i].append(lst[i][1])
        elif lst[i][0][0:3] == 'нет':
            l1[i].append('Не выполнено')
            l1[i].append(lst[i][0][11:20])
            l1[i].append(lst[i][1])
    return l1


def main(lst):
    return edit(lst)


l = [['да|+7(114)127-12-84', None, '18-11-00', None, '18-11-00'],
     ['да|+7(675)948-14-80', None, '05-08-04', None, '05-08-04'],
     ['да|+7(551)630-61-58', None, '20-12-03', None, '20-12-03'],
     [None, None, None, None, None],
     ['да|+7(425)403-49-80', None, '21-12-03', None, '21-12-03']]
print(main(l))
