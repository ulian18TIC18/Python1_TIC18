'''
Considerações de Python e C++: Diferentemente do cpp, o py tem maior facilidade de atribuição de variáveis.
#A sua sintaxe simples e direta permite a criação de variáveis sem a demanda de declação.
Devido a competência do Python em identificar o caráter das variáveis, pode-se realizar alterações desde 
que não exista grandes perdas de informação.
'''

#Operadores simples

a = 10
b = 4

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
#expoente
print(a^b)
#raiz 
print(a ** (0.5))
print(b ** (0.5))
#tipo
print(type(a), " ", type(b))
#imaginário
print(a.real, ' + ', a.imag, ' i ') #Método de retorno da separação de um inteiro em real e imaginário
print(b.real, ' + ', b.imag, ' i ')
#trucamento
print((a + b) == 5)
#unário negativo
print(-a,' ', -b)

#Operadores compostos

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
#binário
a = 10
b = 4
a &= b
print(a)
#combinação de bits
a |= b
print(a)
#exponenciação
a ^= b
print(a)
#deslocamento binário à esquerda
a <<= b
print(a)
#deslocamento binário à direita
a >>= b
print(a)

#Caculando o fatorial de 30
fatorial = 30
for n in range (1, fatorial, 1):
    fatorial *= n
print(fatorial)
'''
O maior valor inteiro diretamente obtido pela linguagem C++ eh: 2147483647.
Já em Python, os limite são maiores e dependem da quantidade de memória disponível
para a execução do comando.
'''

a = 10
b = a  
a += 5 

print("a =", a)  # O valor de 'a' foi modificado para 15
print("b =", b)  # Porém, o 'b' mantém seu valor original, que é 10

x = 2
y = x
print("X = ", x)
print("Y = ", y)

x += 5

print("X = ", x)
print("Y = ", y)

'''
Alguns do principais métodos disponíveis para variáveis do tipo inteiro:
'''

minByts = x.bit_length() #Retorna o número mínimo de bits para um inteiro.
print(minByts)

#Métodos de conversão

y = 5

numInt = int(y)
print(numInt)

numBin = bin(x)
print(numBin)

numOct = oct(x)
print(numOct)

numHex = hex(y)
print(numHex)

#Métodos Matemáticos

numAbsoluto = abs(y)
print(numAbsoluto)

intRestoDivisao = divmod(x , y)
print(intRestoDivisao)

potencia = pow(x, y)
print(potencia)

#Comparação entre valores
 
print(x == y)

print(x != y)

print(x > y)

print(x <= y)

#Conversão de inteiro em string

class MeuInteiro: 
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"MeuInteiro: {self.valor}"

meu_numero = MeuInteiro(42)

print(meu_numero) 

#Métodos disponíveis para variáveis inteiras.
intMetodo = 4
help(intMetodo)
