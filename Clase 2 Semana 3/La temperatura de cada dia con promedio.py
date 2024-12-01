temperatura = 0
sumaTotal = 0
promedio = 0
i = 0
while(i < 7):
 temperatura = float(input(f"Digite la temperatura del día {i + 1} "))
 sumaTotal += temperatura
 i += 1
promedio = sumaTotal / 7
print(f"La temperatura promedio de esta semana fue de: {promedio}")