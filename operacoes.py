# Exercicio 1
x = 0.0
y = 18
z = x + y
print('z:',z,'\ntipo:',type(z))

# Exercicio 2
# É identificado o erro e é sugerido a variável criada como ideia para o comando 'print', desta forma:
# NameError: name 'A' is not defined. Did you mean: 'a'?

# Exercicio 3
# <class 'str'>, o tipo String serve para texto em Python.

# Exercicio 4
A = 14
B = 5
soma = A + B
print(soma)

sub = A - B
print(sub)

mult = A * B
print(mult)

div = A/B
print(div)

divInt = A // B
print(divInt)

Mod = A % B
print(Mod)

Pot = A ** B
print(Pot)

# Exercicio 5
base = 9
alt = 6
area = (base * alt) / 2
print('Área do triângulo: {:n}'.format(area))

# Exercicio 6
hora = 163
salarioHora = hora * 14.25
extra = 20
salarioExtra = extra * 28.5
Bruto = salarioHora + salarioExtra
print('Dia de pagamento \nHoras:',hora,'\nExtra:',extra,'\nBruto:',Bruto)

# Exercicio 7
A = 4
B = 5
C = 1

Res = (A+B)/2
print(Res)

R = ((3*A)+(2*B)) / (A+B)
print(R)

import math
raiz = math.sqrt((B ** 2) - (4 * A * C))
x = ((-1 * B) + raiz) / (2*A)          
print(x)                   

Z = (7.6 * A) - (B ** 1.7)                
print(Z)             

# Exercicio 8
# O comando input permite que o usuário do programa digite o valor para o processamento de dados, por exemplo, o login de um site com dois inputs sendo um para email e o outro para senha.
# Aqui está o um exemplo visual:

print('Programa de conversão: Celsius para Fahrenheit ')
cels = float(input('Digite a temperatura em graus Celsius: '))
fahr = (cels * 1.8) + 32
print('A temperatura em Fahrenheit é {:.2F} graus.' .format(fahr))