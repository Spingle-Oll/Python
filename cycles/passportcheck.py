password = "pillow"
attempts = 3

for i in range(attempts):
    user_input = input("Введите пароль: ")
    
    if user_input == password:
        print("Доступ разрешен")
        break
else:
    print("В доступе отказано")
