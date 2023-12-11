salario=float(input("digite seu salario atual: "))
#PECO O SALARIO COM INPUT DE FLOUT PARA NUMEROS QUEBRADOS 
if 0 <= salario <= 400.00: 
#DECISAO 
    REAJ15 = (salario * 15 ) / 100 
#SE SIM APLICAR A FORMULA DE PORCENTAGEM
    print(f"novo salario: {REAJ15 + salario:.2f}" ) 
#FAZER O PRINT USANDO A FORMULA ":.2"PARA CORTAR AS CASA DECIMAIS Q SOBRAM
    print(f"reajuste ganho: {REAJ15:.2f}")
#IMPRIMIR O REAJUSTE GANHO           
    print("15%")
#AGORA SO REPETIR TUDO MUDANDO OS NUMEROS E SO repetir
if 400.01 <= salario <= 800.00:
    REAJ12 = (salario * 12 ) / 100
    print(f"novo salario: {REAJ12 + salario:.2f}" )
    print(f"reajuste ganho: {REAJ12:.2f}")
    print("12%")
if 800.01 <= salario <= 1200.00:
    REAJ10 = (salario * 10 ) / 100
    print(f"novo salario: {REAJ10 + salario:.2f}" )
    print(f"reajuste ganho: {REAJ10:.2f}")
    print("10%")
if 1200.01 <= salario <= 2000.00:
    REAJ7= (salario * 7 ) / 100
    print(f"novo salario: {REAJ7 + salario:.2f}" )
    print(f"reajuste ganho: {REAJ7:.2f}")
    print("7%")
if salario > 2000.01:
    REAJ4= (salario * 4 ) / 100
    print(f"novo salario: {REAJ4 + salario:.2f}" )
    print(f"reajuste ganho: {REAJ4:.2f}")
    print("4%")