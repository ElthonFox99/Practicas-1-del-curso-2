#Aun programa que solicite el expediente médico de un paciente, debe solicitar nombre, primer apellido,
#segundo apellido, número de cédula, estatura, peso, preguntar si padece de alguna enfermedad, luego deberá
#mostrar en pantalla los datos digitados con un saludo inicial.
Nombre_Persona = ""
Apellido_Persona = ""
SecApellido_Persona = ""
Nombre_Completo = Nombre_Persona + Apellido_Persona + SecApellido_Persona
Numero_Cedula = 0-0000-0000
Numero_Estatura = 0.00
Numero_Peso = 00
Pregunta_Persona = ""

Nombre_Persona = input("Digite su nombre")
Apellido_Persona = input("Digite su primer apellido")
SecApellido_Persona = input("Digite su segundo apelido")
Numero_Cedula = int(input("Digite su numero de cedula"))
Numero_Estatura =float(input("Digite su estatura"))
Numero_Peso = int(input("Digite su peso"))
Pregunta_Persona = str (input("Padece de alguna enfermedad"))
print("Hola",Nombre_Persona,Apellido_Persona,SecApellido_Persona,"estos son su datos del diagnostico" )
print("Cedula: ",Numero_Cedula)
print("Estatura: ",Numero_Estatura)
print("Peso: ",Numero_Peso)
print("Padece de: ",Pregunta_Persona)
