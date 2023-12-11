numeros = []
#uma variavel com uma lista aberta
SOMA = 0
#variavel da soma dos positivos zeradas
QUANT = 0
#variavel dos positivos zeradas
for x in range(5): 
#loop para fazer o input rodar 5x
    numero = float(input(f"Digite o {x+1}º numero:"))
#receber os numeros 
    numeros.append(numero)
    #amarzenar os numeros recebido do input na variavel numeros de lista
    if numero > 0:
#ver se os numero sao maiore que 0
        SOMA += numero
        QUANT += 1
if QUANT > 0:
#definir os positivos 
    media_positivos = SOMA / QUANT
# fazer o calculo de media das somas do positivos
    print(F"quantidade de numeros positivos é: {QUANT}")
    print(f"A média dos números positivos é: {media_positivos}") 
#print com fucao de variavel dentro de string
else:
    print("Não foram inseridos números positivos.")
    # se a caso nao for inseridos os numeros positivos