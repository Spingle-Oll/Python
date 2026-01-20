a = input("Введите что-нибудь ")
b = a.find("#")

if b == -1:
   print(a)
else:
    c = a[0:b]
    print(c)
