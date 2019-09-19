numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
print("1- soma")
print("2- Subtracao")
print("3- divisao")
print("4- multiplicacao")
print("5- sair")
opcao = int(input("digite a opcao que deseja:"))
if opcao == 1:
    soma = numero1 + numero2
    print("o resultado da operacao e: {0.2f} + {1.2f} = {2.2f}".format(numero1,numero2,soma))
elif opcao == 2:
    subtracao = numero1 - numero2
    print("o resultado da operacao e: {} - {} = {}".format(numero1,numero2,subtracao))
elif opcao == 3:
    divisao = numero1 / numero2
    print("o resultado da operacao e: {} / {} = {}".format(numero1,numero2,divisao))    
elif opcao == 4:
    multiplicacao = numero1 * numero2
    print("o resultado da operacao e: {} * {} = {}".format(numero1,numero2,multiplicacao))    
else:
    print("obrigado")
exit()









# exercicio com range
for numero in range(7):
    print(numero)


    
#exercicio com while - looping calculadora.
while True:
    numero1 = float(input("Digite o primeiro numero:"))
    numero2 = float(input("Digite o segundo numero:"))

    print("1- soma")
    print("2- Subtracao")
    print("3- divisao")
    print("4- multiplicacao")
    print("5- sair")
    opcao = int(input("digite a opcao que deseja:"))

    if opcao == 1:
        soma = numero1 + numero2
        print("o resultado da operacao e: {} + {} = {}".format(numero1,numero2,soma))
    elif opcao == 2:
        subtracao = numero1 - numero2
        print("o resultado da operacao e: {} - {} = {}".format(numero1,numero2,subtracao))
    elif opcao == 3:
        divisao = numero1 / numero2
        print("o resultado da operacao e: {} / {} = {}".format(numero1,numero2,divisao))    
    elif opcao == 4:
        multiplicacao = numero1 * numero2
        print("o resultado da operacao e: {} * {} = {}".format(numero1,numero2,multiplicacao))    
    elif opcao == 5:
        print("obrigado")
        break
    else:
        print("Digite opcao valida")
exit()    


umero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
opcao=1

while opcao <4 and opcao >=1:
    print("1- soma")
    print("2- Subtracao")
    print("3- divisao")
    print("4- multiplicacao")
    print("5- sair")
    opcao = int(input("digite a opcao que deseja:"))

    if opcao == 1:
        soma = numero1 + numero2
        print("o resultado da operacao e: {} + {} = {}".format(numero1,numero2,soma))
    elif opcao == 2:
        subtracao = numero1 - numero2
        print("o resultado da operacao e: {} - {} = {}".format(numero1,numero2,subtracao))
    elif opcao == 3:
        divisao = numero1 / numero2
        print("o resultado da operacao e: {} / {} = {}".format(numero1,numero2,divisao))    
    elif opcao == 4:
        multiplicacao = numero1 * numero2
        print("o resultado da operacao e: {} * {} = {}".format(numero1,numero2,multiplicacao))    
    else:
        print("obrigado")
exit()    






########################333
#Calculadora com formatação na saida. (corrigir)
numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
print("1- soma")
print("2- Subtracao")
print("3- divisao")
print("4- multiplicacao")
print("5- sair")
opcao = int(input("digite a opcao que deseja:"))
if opcao == 1:
    soma = numero1 + numero2
    print("o resultado da operacao e: {}0.2f + {}0.2f = {}0.2f".format(numero1,numero2,soma))
else:
    print("opcao invalida, por favor tente novamente")
exit()


#exercicio calculadora com validador de opção.
numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
print("1- soma")
print("2- Subtracao")
print("3- divisao")
print("4- multiplicacao")
print("5- sair")
opcao = int(input("digite a opcao que deseja:"))
if opcao == 1:
    soma = numero1 + numero2
    print("o resultado da operacao e: {} + {} = {}".format(numero1,numero2,soma))
elif opcao == 2:
    subtracao = numero1 - numero2
    print("o resultado da operacao e: {} - {} = {}".format(numero1,numero2,subtracao))
elif opcao == 3:
    divisao = numero1 / numero2
    print("o resultado da operacao e: {} / {} = {}".format(numero1,numero2,divisao))    
elif opcao == 4:
    multiplicacao = numero1 * numero2
    print("o resultado da operacao e: {} * {} = {}".format(numero1,numero2,multiplicacao))    
elif opcao == 5:
    print("obrigado")
else:
    print("opcao invalida, por favor tente novamente")
        
exit()    


#exercicio calculadora
numero1 = float(input("Digite o primeiro numero:"))
numero2 = float(input("Digite o segundo numero:"))
print("1- soma")
print("2- Subtracao")
print("3- divisao")
print("4- multiplicacao")
print("5- sair")
opcao = int(input("digite a opcao que deseja:"))
if opcao == 1:
    soma = numero1 + numero2
    print("o resultado da operacao e: {0.2f} + {1.2f} = {2.2f}".format(numero1,numero2,soma))
elif opcao == 2:
    subtracao = numero1 - numero2
    print("o resultado da operacao e: {} - {} = {}".format(numero1,numero2,subtracao))
elif opcao == 3:
    divisao = numero1 / numero2
    print("o resultado da operacao e: {} / {} = {}".format(numero1,numero2,divisao))    
elif opcao == 4:
    multiplicacao = numero1 * numero2
    print("o resultado da operacao e: {} * {} = {}".format(numero1,numero2,multiplicacao))    
else:
    print("obrigado")
exit()    
    
        
#ex.02 com format.
geracao = int(input("Qual e o seu ano de nascimento?"))
if geracao <= 1966:
    print("Ano de nascimento {} - Pertence a geracao BB".format(geracao))
elif geracao <= 1980:
    print("Pertence a geracao x")
elif geracao <= 1999:
    print("Pertence a geracao y")
else:
    print("pertence a geração Z")
exit()    


#ex02.py
geracao = int(input("Qual e o seu ano de nascimento?"))
if geracao <= 1966:
    print("Pertence a geracao BB")
elif geracao <= 1980:
    print("Pertence a geracao x")
elif geracao <= 1999:
    print("Pertence a geracao y")
else:
    print("pertence a geração Z")
exit()
             
