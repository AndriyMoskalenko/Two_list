def Lists():
    import random

    list1 = [random.randint(1, 10) for i in range(9)]
    list2 = [random.randint(1, 10) for i in range(9)]
    print('Список №1:', list1)
    print('Список №2:', list2)
    if list1 < list2:
        print('Список №2 больше:')
        list3 = list1 + list2
        print('Список №3:', list3)
    elif list1 > list2:
        print('Список №1 больше')
        list4 = [max(list1)] + [min(list2)]
        print('Список №3:', list4)
Lists()