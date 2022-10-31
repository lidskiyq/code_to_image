list1 = list(map(int,input().split(' ')))
set1 = set(list1)
list2 = list(map(int,input().split(' ')))
set2 = set(list2)
set3 = set1&set2
if set1.isdisjoint(set2) == True:
    print("BAD DAY")
else:
    print(*sorted(set1.intersection(set2), reverse=True, key=int))