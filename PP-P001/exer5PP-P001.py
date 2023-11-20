# Manipulação de variáveis de ponto flutuante, explorando as características e os limites.
#Operadores simples

a = 3.56
b = 2.6

#soma
print(a + b)
#subtração
print(a - b)
#multiplicação
print(a * b)
#divisão
print(a / b)
#divisão trucada
print(b // a)
#exponenciação
print(a ** b)
#resto da divisão
print(a % 2)
print(b % 3)

#raiz 
print(a ** (0.5))
print(b ** (0.5))
#tipo
print(type(a), " ", type(b))

#imaginário
print(a.real, ' + ', a.imag, ' i ') 
print(b.real, ' + ', b.imag, ' i ')
#trucamento
print((a + b) == 5)
#unário negativo
print(-a,' ', -b)
#soma
a += b
print(a)
#subtração
a -= b
print(a)
#multiplicação
a *= b
print(a)
#divisão
a /= b
print(a)
#divisão truncada
a //= b
print(a)
#resto da divisão
a %= b
print(a)
#exponenciação
a **= b
print(a)
print("--------------------------------------------------")

import sys

menorPotenciaExpoente = sys.float_info.min_exp
maiorPotenciaExpoente = sys.float_info.max_exp

menorPow = 2 ** menorPotenciaExpoente
maiorPow = 2 ** maiorPotenciaExpoente

print(f"A menor potencia de 2 eh:{menorPotenciaExpoente}")
print(f"A maior potencia de 2 eh:{maiorPotenciaExpoente}")

print(f"Valor da potencia de 2: {menorPow}")
print(f"Valor da potencia de 2: {maiorPow}")
print("--------------------------------------------------")

#Tentativa de modificar diretamente uma variável float
numFloat = 3.25
print("Valor original:", numFloat)
numFloat = 42.1
print("Novo valor:", numFloat)
print("--------------------------------------------------")
print("----------------------METODOS---------------------")

#Métodos disponíveis para floats
import math

resultado = round(math.pi, ndigits=2) == round(22 / 7, ndigits=2)
print(resultado)

x = 3.14159
x.as_integer_ratio()
(3537115888337719, 1125899906842624)
print(x == 3537115888337719 / 1125899906842624)

x.hex()
'0x1.921f9f01b866ep+1'
print(x == float.fromhex('0x1.921f9f01b866ep+1'))

from decimal import Decimal
from fractions import Fraction

print(Fraction.from_float(0.1))

print((0.1).as_integer_ratio())

print(format(Decimal.from_float(0.1), '.17'))

#Métodos disponíveis para variáveis do tipo float.
floatMetodo = 4.5
help(floatMetodo)