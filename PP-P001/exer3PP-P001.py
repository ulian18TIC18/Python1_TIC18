#Exercício 3- Manipulação de variáveis de tipo string e explorando o uso de print.

#Tabela ASCII

for i in range(10):
    charInt = chr(ord('0') + i)
    codigo = ord(charInt)
    print(f"'{charInt}' - {codigo}")
print("-------------------------------------------------")

for i in range(10):
    charInt1 = chr(ord('0') + i)
    codigo_decimal = ord(charInt1)
    codigo_octal = oct(codigo_decimal)
    codigo_hexadecimal = hex(codigo_decimal)
    
    print(f"'{charInt1}' - Decimal: {codigo_decimal}, Octal: {codigo_octal}, Hexadecimal: {codigo_hexadecimal}")
print("-------------------------------------------------")

numChar = int(input("Digite um numero inteiro: "))

charInt = chr(numChar)
codigoDecimal = ord(charInt)
codigoOcatal = oct(codigoDecimal)
codigoHExadedimal = hex(codigoDecimal)
print(f"'{numChar}' - Decimal: {codigoDecimal}, Octal: {codigoOcatal}, Hexadecimal: {codigoHExadedimal}")
print("-------------------------------------------------")

primeiroCaractere = input("Digite um caractere: ")

codigoDecimal = ord(primeiroCaractere)
codigoOctal = oct(codigoDecimal)
codigoHexadecimal = hex(codigoDecimal)

print(f"'{primeiroCaractere}' - Decimal: {codigoDecimal}, Octal: {codigoOctal}, Hexadecimal: {codigoHexadecimal}")
          