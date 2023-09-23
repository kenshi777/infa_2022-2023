l = int(input())
animal = input()

if animal == "monkey":
    d = l // 90
elif animal == "parrot":
    d = l // 10
elif animal == "elephant":
    d = l // 300

if d == 0:
    print(1)
else:
    print(d)