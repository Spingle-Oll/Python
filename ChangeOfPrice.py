First_price = float(input("Введите перую цену: "))
Second_price = float(input("Введите вторую цену: "))
if(First_price < Second_price):
    Change_of_price =  Second_price - First_price
    Change_of_price = round(Change_of_price, 2)
    Change_of_price_percent = round((First_price * Change_of_price) / 100, 2)
    print("Товар стал дороже на", Change_of_price, "Цена изменилась на", Change_of_price_percent, "%")
elif(Second_price < First_price):
    Change_of_price = First_price - Second_price
    Change_of_price = round(Change_of_price, 2)
    Change_of_price_percent = round((First_price * Change_of_price) / 100, 2)
    print("Товар подешевел на", Change_of_price, "Цена упала на", Change_of_price_percent, "%")
