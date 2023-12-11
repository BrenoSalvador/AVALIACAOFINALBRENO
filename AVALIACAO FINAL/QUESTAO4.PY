
    # lista q mapeia DDD para cidades
ddds_cidades = {
        61: "Brasília",
        71: "Salvador",
        11: "São Paulo",
        21: "Rio de Janeiro",
        32: "Juiz de Fora",
        19: "Campinas",
        27: "Vitória",
        31: "Belo Horizonte"
    }#assim fica mais facil doq apenas criar uma variavel e comparar usando varios if's e else's
    

while True:
        #o while true e o while normal com a condicao q ele so pararar com a outra funcao chmada break 
        try:
            numero = int(input("Digite um DDD: "))
            #entrada com o ddd numa variavel int
            if numero in ddds_cidades:
                #um if para ver se o numero=ddd esta na lista de cidade e ddd
                cidade = ddds_cidades[numero]
                #ver o ddd ta em alguma cidade cadastrado
                print(f"você digitou o DDD: {numero} - Cidade: {cidade}")
                #pra imprimir o dd e a cidade q ta na lista
                break
            #para o loop se tudo ta certo
            else:
                #se der erro nos passo atras iniciar 
                print("DDD não cadastrado.")
        except ValueError:
            print("Por favor, digite um DDD válido.")


