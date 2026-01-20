word = "бунт"

answer = input("Что вы хотите сделать? ")


if word in answer:
    new_word = answer.replace("бунт", "славить капитана")
    print("А, вы хотите " + new_word + "? Это хорошо!")
elif word not in answer:
    print(answer)
