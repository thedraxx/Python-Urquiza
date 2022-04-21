p = input("ingrese una cadena: ")
count = int(0)
vocal = ("a", "e", "i", "o", "u","A", "E", "I", "O", "U")
for i in p:
    if i in vocal:
        count += 1
print("cantidad de vocales:",count)