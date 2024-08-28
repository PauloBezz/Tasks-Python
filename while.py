
"""
    O comando while serve para a necessidade de repetir um certo trecho no código, categoria de loop.

while {condição}:
    {conjunto de comandos}    

# Exemplo
Cont = 1
while Cont <= 10:
    print(Cont)
    Cont = Cont + 1
"""
# Cont = 1
# while Cont <= 10:
#     print(Cont)
#     Cont = Cont + 1


A = int(input("Digite um número para A: "))
B = int(input("Digite um número para B: "))
C = int(input("Digite um número para C: "))
delta = (B ** 2) - (4 * A * C)
raiz = delta ** (1/2)
x1 = ((-1 * B) + raiz) / (2 * A)     
x2 = ((-1 * B) + (-1 * raiz)) / (2 * A)
print(f"Primeira raiz = {x1}")
print(f"Segunda raiz = {x2}")