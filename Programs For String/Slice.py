a = input("Введите что-то ")

if len(a) > 15:
    b = a[0:15]
    print(b + "...")
else:
    print(a)
