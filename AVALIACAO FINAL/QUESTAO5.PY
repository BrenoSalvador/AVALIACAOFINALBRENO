NUMS = []
#variavel para criar uma lista 
for i in range(5):
#range para percorrer o input o tanto de vezes dentro dos parenteses

    NUM = int(input(f"digite o {i + 1} °numero: "))
    #variavel criando com numero int com uma f de chaves para poder receber o i + 1 
    #assim toda vez q rodado o input ele aumentara o i para mais 1

    NUMS.append(NUM)
    #seria para guarda os numneros do input dentro da lista numeros



numeros_pares = [num for num in NUMS if num % 2 == 0]
# os numeros na variavel numeros dividindo os por 2 e vendo se o resto representado por %
# é igual a 0 se for vai ser guardado na variavel numeros_pares 


quantidade_numeros_pares = len(numeros_pares)
#criando uma variavel de quanti usamos a funçao len para nos numeros pares assim tendo a quaintidade

print(f"A quantidade de números pares é: {quantidade_numeros_pares}")
#print com o f e funcao de {} para ter uma variavel dentro do texto