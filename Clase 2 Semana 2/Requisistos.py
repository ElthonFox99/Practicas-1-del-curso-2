idioma=int(input("Digite el idioma que habla: \n1.Ingles \n2.Portugues \n3.Ambos\n4.Otro \n5.Ninguno"))

if(idioma==1 or idioma ==2 or idioma==3):
    edad=int(input("Digite su edad"))
    if(edad >= 18):
        expe =int(input("Digite sus años de expriencia"))
        if(expe >= 1):
            print("Califico")
        else:
            print("No califico por la experiencia")
    else:
        print("Su edad no califia")
else:
    print("No posee ningun idioma requerido")

