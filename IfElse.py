# Exercício 1
X = int(input("Digite um número: "))
if X < 0:
    print("O número",X, "é menor que zero." )
elif X == 0:
    print("O número é zero")
else:
    print("O número",X, "é maior que zero.")

# Exercício 2
A = int(input("Digite um número para A: "))
B = int(input("Digite um número para B: "))
if A < B:
    print("O menor é",A)
elif A == B:
    print("Ambos são iguais")
else:
    print("O menor é",B)

# Exercicio 3
A = int(input("Digite um número: "))
B = int(input("Digite um número: "))
if A > B:
    print("Maior:",A," Menor:",B)
elif A == B:
    print("Ambos são iguais")
else:
    print("Maior:",B," Menor:",A)

# Exercicio 4
n = int(input("Digite um número: "))
if n % 2 == 0:
    print("O número",n,"é par.")
else:
    print("O número",n,"é ímpar.")

# Exercício 5
n = int(input("Digite um número: "))

if n > 0:
    print("O número",n,"é positivo.")
elif n < 0:
    print("O número",n,"é negativo.")
else:
    print("O número é zero.")

#Exercicio 6
lutador = input("Digite o nome do lutador: ")
peso = float(input("Digite o peso do mesmo: "))

if peso < 65:
    print("O lutador", lutador,"pesa",peso,"kg e se enquadra na categoria Pena.")
elif peso < 72:
    print("O lutador", lutador,"pesa",peso,"kg e se enquadra na categoria Leve.")
elif peso < 79:
    print("O lutador", lutador,"pesa",peso,"kg e se enquadra na categoria Ligeiro.")
elif peso < 86:
    print("O lutador", lutador,"pesa",peso,"kg e se enquadra na categoria Meio médio.")
elif peso < 93:
    print("O lutador", lutador,"pesa",peso,"kg e se enquadra na categoria Médio.")
elif peso < 100:
    print("O lutador", lutador,"pesa",peso,"kg e se enquadra na categoria Meio pesado.")
else:
    print("O lutador", lutador,"pesa",peso,"kg e se enquadra na categoria Pesado.")

# Exercício 7

A = int(input("Digite um número para A: "))
B = int(input("Digite um número para B: "))
C = int(input("Digite um número para C: "))
delta = (B ** 2) - (4 * A * C)
raiz = delta ** (1/2)
x1 = ((-1 * B) + raiz) / (2 * A)     
x2 = ((-1 * B) + (-1 * raiz)) / (2 * A)

if delta > 0:
    print("Apresenta duas raízes") 
    print("Primeira raiz = {:n}".format(x1))
    print("Segunda raiz = {:n}".format(x2))
elif delta == 0:
    print("Apresenta uma raíz")
    print("Única raiz = {:n}".format(x1))
else: 
    print("Não apresenta raízes reais")

# Exercicio 8
l1 = int(input("Defina o valor do lado 1: "))
l2 = int(input("Defina o valor do lado 2: "))
l3 = int(input("Defina o valor do lado 3: "))

if l1 <= 1 or l2 <= 1 or l3 <= 1:
    print("Digite valores reais e maiores que zero")
elif l1 < (l2 + l3) and l1 >= l2 >= l3 or l1 >= l3 >= l2:
    if l1 != l2 == l3 or l1 == l2 != l3 or l1 == l3:
        print("Triângulo Isósceles")
    elif l1 == l2 == l3:
        print("Triângulo Equilátero")
    else: 
        print("Triângulo Escaleno")
elif l2 < (l1 + l3) and l2 >= l1 >= l3 or l2 >= l3 >= l1:
    if l2 != l1 == l3 or l2 == l1 != l3 or l2 == l3:
        print("Triângulo Isósceles")
    elif l2 == l1 == l3:
        print("Triângulo Equilátero")
    else: 
        print("Triângulo Escaleno")
elif l3 < (l2 + l1) and l3 >= l2 >= l1 or l3 >= l1 >= l2:
    if l3 != l2 == l1 or l3 == l2 != l1 or l3 == l1:
        print("Triângulo Isósceles")
    elif l3 == l2 == l1:
        print("Triângulo Equilátero")
    else: 
        print("Triângulo Escaleno")
else:
    print('Não será possível criar um triângulo')