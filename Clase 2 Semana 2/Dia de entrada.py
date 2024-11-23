dia = int(input("Digite el dia de entrada.. \n\n1 Miercoles \n2 Jueves.\n3 Jueves"))
costo = float(input("Digite el costo de la entrada"))

if(dia == 3):
    costo=costo/2
    print ("El costo de su entrada es: ",costo)