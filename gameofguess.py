import random
from PIL import Image
import requests
import climage
from io import BytesIO

amountOfTries = 0
HintWord = "hint"
AmountOfHint = 0
RulesList = ["1. Вам нужно отгадать задуманное число", "2. У вас 3 попытки", "3. Вы имеете право на 1 подсказку, которая не отбирает попытки", "4. Чтобы вызвать подсказку напишите hint", "5. Вы дисквалифицируетесь, если введете не число и не слово-подсказку", "6. Вы должны выбрать диапозон числа от 1 до 10 или от 10 до 100"]
print("Правила игры:", RulesList)
a = input("")
ChoiceOfRange = input("Выберете диапозон числа. Если вы введете 1, то диапозон будет от 1 до 10. Если вы введете 2, то диапозон будет от 10 до 100. Введите 1 или 2: ")

if ChoiceOfRange == "1":
  number = random.randint(1, 10)
elif ChoiceOfRange == "2":
  number = random.randint(10, 100)


if ChoiceOfRange == "1":
  while amountOfTries < 3 and AmountOfHint <= 1:
      answer = input("Введите вашу догадку: ")
      if answer.lower().strip() == HintWord:
          amountOfTries = amountOfTries - 1
          AmountOfHint = AmountOfHint + 1
          if number > 5:
              print("Псс. Число больше 5")
          else:
              print("Псс. Число не больше 5")
      elif answer != HintWord and answer.isdigit():
          answer = int(answer)
      else:
          print("Вы ввели не число и не слово-подсказку. Вы нарушили павило:", RulesList[4])
          break
      amountOfTries = amountOfTries + 1

      if answer == number:
          print("Вы угадали! Задуманное число ", number, "!")
          response = requests.get("https://masterpiecer-images.s3.yandex.net/5fb0b52da7f3537:upscaled")
          img_data = response.content
          image = BytesIO(img_data)
          output = climage.convert(image)
          print(output)
          break

      elif amountOfTries < 3 and answer != number:
          if 3 - amountOfTries > 1:
              print("Вы не угадали. У вас осталось", 3 - amountOfTries, "поптыки")
          else:
              print("Вы не угадали. У вас осталось", 3 - amountOfTries, "поптыка")
      elif amountOfTries == 3:
          print("Потыки кончились.", "Задуманное число было", number, "Ничего, попробуйте снова.")

elif ChoiceOfRange == "2":
    while amountOfTries < 3 and AmountOfHint <= 1:
        answer = input("Введите вашу догадку: ")
        if answer.lower().strip() == HintWord:
            amountOfTries = amountOfTries - 1
            AmountOfHint = AmountOfHint + 1
            NumberForHint = str(number)
            HintLastNumber = NumberForHint[-1:]
            print("Псс. Последняя цифра числа", HintLastNumber)
        elif answer != HintWord and answer.isdigit():
            answer = int(answer)
        else:
            print("Вы ввели не число и не слово-подсказку. Вы нарушили павило:", RulesList[4])
            break
        amountOfTries = amountOfTries + 1

        if answer == number:
            print("Вы угадали! Задуманное число ", number, "!")
            response = requests.get("https://masterpiecer-images.s3.yandex.net/5fb0b52da7f3537:upscaled")
            img_data = response.content
            image = BytesIO(img_data)
            output = climage.convert(image)
            print(output)
            break

        elif amountOfTries < 3 and answer != number:
            if 3 - amountOfTries > 1:
                print("Вы не угадали. У вас осталось", 3 - amountOfTries, "поптыки")
            else:
                print("Вы не угадали. У вас осталось", 3 - amountOfTries, "поптыка")
        elif amountOfTries == 3:
            print("Потыки кончились.", "Задуманное число было", number, "Ничего, попробуйте снова.")
else:
    print("Вы не выбрали диапозон. Вы нарушили правило:", RulesList[5])
