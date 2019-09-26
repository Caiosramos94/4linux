







#lista de compras.
dic = {1:8.5, 2:3.25, 3:4.60}

lista = []

lista.append(1)
lista.append(2)
lista.append








def soma (*args):
    total = 0
    for e in args:
        total += e
    return total

def media (*args):
    return total/len(*args)

num1 = int(input("Digite o numero 1:"))
num2 = int(input("Digite o numero 2:"))
num3 = int(input("Digite o numero 3:"))
num4 = int(input("Digite o numero 4:"))
num5 = int(input("Digite o numero 5:"))
num6 = int(input("Digite o numero 6:"))

print(media)


exit()








# Calculadora com dicionário - Olhar condição na divisão.
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

num1 = int(input("Digite o numero 1:"))
num2 = int(input("Digite o numero 2:"))

print ("1-soma/n2 -sub/n3 - mult/n4 -div")

opcao = int(input("Digite a opcao desejada:"))

dic [opcao](num1,num2)

exit()









#exercicio média com função
def soma (*args):
    total = 0
    for e in args:
        total += e
    return total

def media (*args):
    return soma(*args)/len(*args)

num1 = int(input("Digite o numero 1:"))
num2 = int(input("Digite o numero 2:"))
num3 = int(input("Digite o numero 3:"))
num4 = int(input("Digite o numero 4:"))
num5 = int(input("Digite o numero 5:"))
num6 = int(input("Digite o numero 6:"))

exit()

        
        
    










#calculadore com função
def soma (a,b):
    print(a+b)
    
def sub (a,b):
    print(a-b)
    
def mult (a,b):
    print(a*b)
    
def div (a,b):
    print(a/b)
                
num1 = int(input("Digite o numero 1:"))
num2 = int(input("Digite o numero 2:"))

print ("1-soma/n2 -sub/n3 - mult/n4 -div")

opcao = int(input("Digite a opcao desejada:"))

if opcao == 1:
    soma (num1,num2)
elif opcao ==2:
    sub (num1,num2)
elif opcao ==3:
    mult (num1,num2)
elif opcao ==4:
    div (num1,num2)
else:
    print("obrigado")
                   
exit()    

#função soma
def soma (a,b):
    print(a+b)
num1 = 7
num2 = 4
num3 = 5
num4 = 9

soma (num1, num2)
soma (num3, num4)
exit()

#dicionário
dicionario = {"nome":"jose", "idade":24, "sexo":"masculino"}
print(dicionario["nome"])
exit()

#contador de vogais com for e if
palavra = "4linux open source specialists"
vogais = "aeiouAEIOU !;"
conta_vogal = 0

for caractere in palavra:
    if caractere in vogais:
        conta_vogal +=1
print (conta_vogal) 
exit()    


# exercicio com listas - while e for
frutas = ["banana", "maca", "pera"]
for elemento in frutas:
    print(elemento)
exit()
    
   
        
    
