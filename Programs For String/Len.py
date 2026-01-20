password = input("Введите пароль ")
length = len(password)

if length > 6:
    print("Ваш пароль подходит")
elif length <= 6:
    print("Ваш пароль слишком короткий")
