def loading_bar(some_number):
    if some_number == 100:
        return "100% Complete!" "\n" "[%%%%%%%%%%]"
    else:
        counter = some_number // 10
        return f"{some_number}% [{counter*'%'}{(10 -counter) * '.'}]" "\n" "Still loading..."






persent = int(input())


print(loading_bar(persent))