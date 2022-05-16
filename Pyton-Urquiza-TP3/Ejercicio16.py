def titulo(palabra):
    palabra = string.lower()
    palabra = string.capitalize()
    return palabra
    
    
string = input("Ingrese una cadena: ")
print(titulo(string))