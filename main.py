import random as rand

hemligt_tal = rand.randint(1, 100)
antal_gissningar = 0

while True:
    gissning = int(input("Gissa ett tal mellan 1 och 100 ->"))
    antal_gissningar += 1
    if gissning > hemligt_tal:
        print(f"Talet {gissning} är för stort.")
    elif gissning < hemligt_tal:
        print(f"Talet {gissning} är för litet.")
    else:
        print("RäTT GISSAT!")
        break
print(f"Du klarade spelet på gissning nr. {antal_gissningar}")