a = input("Введите что-нибудь ")

if len(a) % 2 == 0:
    print("длина строки должна быть нечетной")
else:
    b = len(a)
    b = b // 2
    b = a[b]
    print(b)
