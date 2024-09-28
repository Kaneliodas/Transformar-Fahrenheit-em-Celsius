#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
#Calculo: C = 5 * ((F-32) / 9).
Fahrenheit = int(input("Quantos graus está em Fahrenheit? "))
C = 5 * ((Fahrenheit-32) / 9)
print("Sua temperatura Fahrenheit em graus celsius fica: " +  str(C))  
