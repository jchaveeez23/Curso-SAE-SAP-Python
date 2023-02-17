#inicio listas vacias
nombres =[]
ventas=[]
regiones=[]
incentivos=[]
incentivocalculados=[]
remunera = []
sueldofinal = []
#tamaño de lista
tamaño = 2


# inicio de for donde se ingresan datos

for i in range(tamaño):
    print("Ingrese el Nombre de el vendedor: ", i+1)
    nombre =input("nombre: ")
    venta = float(input("Ingrese el monto de ventas realizadas (Q): "))
    print("Ingrese numero de la región de el pais donde labora")
    print("1. Norte ")
    print("2. Sur ")
    print("3. Oriente ")
    print("4. Occidente ")
    region = int(input())
    if region == 1:
        print("REGION NORTE")
        print("Monto de viatico: Q150.00")
        viatico = 150.00
    elif region == 2:
        print("REGION SUR")
        print("Monto de viatico: Q200.00")
        viatico = 200.00

    elif region == 3:
        print("REGION ORIENTE")
        print("Monto de viatico: Q175.00")
        viatico = 175.00

    elif region == 4:
        print("REGION OCCIDENTE")
        print("Monto de viatico: Q225.00")
        viatico = 225.00

  
    else:
        print("ERROR! número de opcion no existe'") 
    

    # inicia incentivo 
    print("Ingrese numero de opcion correspondiente al incentivo que desea se le aplique:'") 
    print("1. Bono 3%") 
    print("2. Comisión 5%")
    incentivo = int(input())

    # inicia if de  incentivo  
    if incentivo == 1:
        print("BONO 3%")
        incentivocalculado = venta * 0.03
        remu = venta + incentivocalculado
        sf = remu + viatico
    elif incentivo == 2:
        print("COMISIÓN 5%")
        incentivocalculado = venta * 0.05
        remu = venta + incentivocalculado
        sf = remu + viatico
    else:
        print("ERROR! número de opcion no existe'")
    # fin de if de  incentivo  
    # termina incentivo




    # agregando datos a las listas
    nombres.append(nombre)
    ventas.append(venta)
    regiones.append(region)
    incentivos.append(incentivo)
    incentivocalculados.append(incentivocalculado)
    remunera.append(remu)
    sueldofinal.append(sf)
    # fin agregando datos a las listas

    # fin de for donde se ingresan datos



# inicio de for donde se muestran datos

for i in range(tamaño):
    print("mostrando los datos de la persona", i + 1)
    print("Nombre vendedor : ", nombres[i])
    print("Monto de ventas : ", ventas[i])
    print("region seleccionada de el pais donde labora: ", regiones[i])
    if regiones[i] == 1:
        print("REGION NORTE")    
    elif regiones[i] == 2:
        print("REGION SUR")
    elif regiones[i]== 3:
        print("REGION ORIENTE")   
    elif regiones[i] == 4:
        print("REGION OCCIDENTE")
    else:
        print("")

    print("Incentivo seleccionado", incentivos[i]) 
    
    if incentivos[i] == 1:
        print("BONO 3%")
        print(f"Incentivo: {incentivocalculado}")
        
    elif incentivos[i] == 2:
        print("COMISIÓN 5%")   
        print(f"Incentivo: {incentivocalculado}")
    else:
        print("")
    print("Su Incentivo es: ", incentivocalculados[i]) 
    print("Su remuneracion es: ", remunera[i])
    print("Su Sueldo final es: ", sueldofinal[i])

   
 # fin de for donde se muestran datos     
