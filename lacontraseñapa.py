import random
caracteres= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length=int(input("que tan larga es tu contraseña rey"))

contraseña=""

for i in range(length):
    contraseña+=random.choice(caracteres)

print("esta es tu contraseña rey",contraseña) 
