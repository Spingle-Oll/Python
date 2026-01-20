serial_num = input("Введите ваш номер: ")

if serial_num[0].isdigit() == False and len(serial_num) == 8:
    print("Вы вошли в систему")
else:
    print("Некорректный номер")
