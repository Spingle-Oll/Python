from turtle import *

i = 0
amountofiteration = 5
Range = range(60, 220, 10)

while i < amountofiteration:
    forward(50)
    left(90)
    i = i + 1
    if i == 2:
        for j in Range:
            forward(j)
            left(90)
            i = i + 1
    if i >= amountofiteration:
        done()
