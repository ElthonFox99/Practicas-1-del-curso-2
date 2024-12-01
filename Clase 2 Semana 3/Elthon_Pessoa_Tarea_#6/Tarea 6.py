
notaT=[]
suma =0
exam=int(input("Digite la cantidad de examenes realizados"))
i = 0
while(i < exam):
    nota=int(input("Digita la nota de sus examenes"))
    if(nota >=70):
        suma=suma+nota
    elif(nota >60 and nota <70):
        suma=suma+nota
    elif(nota<=60):
        suma=suma+nota
        
    i=i+1
notaT.append(suma)

promedio=(notaT[0]/exam)
if(promedio >=70):
    print("Su promedi es:",promedio,"Aprobo")
elif(promedio >60 and promedio <70):
    print("Su promedi es:",promedio,"Ampliacion")
elif(promedio<=60):
    print("Su promedi es:",promedio,"Reprobo")
