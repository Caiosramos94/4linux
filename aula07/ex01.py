def soma (a,b):
    print(a+b)
    
def sub (a,b):
    print(a-b)
    
def mult (a,b):
    print(a*b)
    
def div (a,b):
    if b == 0:
        print("nao existe divisão por zero")
    else:
        print(a/b)

dic = {1:soma, 2:sub, 3:mult, 4:div}

try:
    num1 = int(input("Digite o numero 1:"))
    num2 = int(input("Digite o numero 2:"))
except ValueError as err:
    print(err)
else:    
    print ("1-soma/n2 -sub/n3 - mult/n4 -div")

    opcao = int(input("Digite a opcao desejada:"))

    dic [opcao](num1,num2)

exit()
