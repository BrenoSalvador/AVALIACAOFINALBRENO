# #começa com variaveis zeradas 3 TENTATIVA

imposto8 = 0
imposto18 = 0
imposto28 = 0

# INICIAR COM INPUT
# COMEÇA COM UM INPUT PARA SABER O SALARIO
renda = float(input("Digite sua renda: "))
# FAZER UMA FUNÇÃO
renda8 = (renda * 0.08 )
renda18 =( renda * 0.18 )
renda28 =( renda * 0.28 )

# VOU FAZER UNS IF ELSE ELIF PARA CLASSIFICAR A RENDA ENTRE ISENTO, 0.08, 0.18, 0.28
if renda <= 2000.00:
    print("ISENTO") #ISEÇÃO USANDO O MAIOR E IGUAL
elif 2000.01 <= renda <= 3000.00: #USANDO AGORA ELA NO MEIO PRA ASSIM COMPARAR A RENDA COM 2 TERMOS DIFERENTE
     imposto8 = renda * 0.08 # USANDO O PRINCIPIDE DE MULTIPLICAR E DIVIDIR POR CEM MAS NAO PRECISA JA QUE O 0,08 JA ESTAR DIVIDIDO PELO O MESMO
     print(f"Valor do Imposto de 8%: {imposto8:.2f}") #USANDO A FUNCAO ".2F" PARA CORTAS AS PROXIMAS CASAS DECIMAIS E FICAR SO 2
elif 3000.01 <= renda <= 4500.00:
     imposto18 = renda * 0.18 
     print(f"Valor do Imposto de 18%: {imposto18:.2f}")  #PRINT BASICO COM A FUNÇÃO DAS CASAS DECIMAIS
if renda > 4500.00:
     imposto28 = renda * 0.28
     print(f"Valor do Imposto de 18%: {imposto28:.2f}") # AGR FOI APENAS REPETIR O PROCESSO