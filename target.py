def fibonacci_check(num):
    a, b = 0, 1
    while a <= num:
        if a == num:
            return f"O número {num} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {num} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(fibonacci_check(numero))

def count_a(string):
    count = string.lower().count('a')
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

texto = input("Informe uma string: ")
print(count_a(texto))

indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k
print(soma) #resultado 77.

#a) 1, 3, 5, 7, resultado 9   passo de 2
#b) 2, 4, 8, 16, 32, 64, resultado 128 multiplicacao por 2
#c) 0, 1, 4, 9, 16, 25, 36, resultado 49 posicao elevada a 2
#d) 4, 16, 36, 64, resultado 100 
#e) 1, 1, 2, 3, 5, 8, resultado 13 somas dos dois numeros anteriores 
#f) 2,10, 12, 16, 17, 18, 19, resultado 20 


#Ligue o primeiro interruptor e deixe ligado por alguns minutos.
#Desligue o primeiro interruptor e ligue o segundo interruptor.
#Vá até a sala das lâmpadas:
#A lâmpada acesa está conectada ao segundo interruptor.
#A lâmpada que está apagada, mas quente, está conectada ao primeiro interruptor.
#A lâmpada apagada e fria está conectada ao terceiro interruptor.