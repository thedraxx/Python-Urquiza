# Aca se llama a las funciones
import modulo_funciones_basicas as mod_bac

def main():
    
    tiempo_prueba_lista = []
    cont_dias = int(0)
    while cont_dias < 10:
        tiempo_prueba_lista.append(mod_bac.leer_tiempo_prueba(cont_dias))
        cont_dias += 1
    es_apto = mod_bac.validar_aptitud_atleta(tiempo_prueba_lista)
    mod_bac.informar_aptitud(es_apto)
    opcion = int(input('Seleccione una opcion:\n 1 - se mostrara el promedio de todas las pruebas \n 2- se mostrara la prueba con el mayor tiempo \n 3- se mostrara la prueba con el menor tiempo: '))   
    
    if (opcion == 1):
        # Aca se calcula el promedio de las listas
        print ('el promedio de todas las pruebas es; ',mod_bac.totalP(tiempo_prueba_lista) , 'minutos')

    elif(opcion == 2):
        # Aca se visualiza la prueba que mas se tardo
        print ("El mayor tiempo que hizo el atleta fue de: ",mod_bac.maxT(tiempo_prueba_lista), 'minutos')

    elif(opcion == 3):
        # Aca se visualiza la prueba con menos tiempo
        print ("El menor tiempo que hizo el atleta fue de: ",mod_bac.minT(tiempo_prueba_lista), 'minutos')

    else:
        opcion = int(input('No es una opcion valida. Seleccione una opcion: 1 - se mostrara el promedio de todas las pruebas / 2- se mostrara la prueba con el mayor tiempo / 3- se mostrara la prueba con el menor tiempo: ')) 

main()
