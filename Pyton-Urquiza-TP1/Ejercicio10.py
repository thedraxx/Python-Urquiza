p = input('ingrese una cadena')
count = int(0)
for i in p:
    if i == " ":
        count +=1
        
print("cantidad de espacios en blanco:",count)