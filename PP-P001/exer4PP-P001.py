#Manipulação de variáveis de tipo string e explorando os métodos da classe.

nome = input("Digite seu nome e sobrenome: ")


partesNome = nome.split()

if len(partesNome) >= 2:
    nome = partesNome[0]
    sobrenome = ' '.join(partesNome[1:])  
    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
else:
    print("Entrada invalida...")
print("----------------------------------------------------")

nome = input("Digite seu nome e sobrenome: ")

partesNome = nome.split()

if len(partesNome) >= 2:
    nome = partesNome[0]
    sobrenome = ' '.join(partesNome[1:])  

    menor= min(nome, sobrenome)

    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
    print("Na ordem alfabetica, '{}' e '{}'.".format(menor, nome if menor== sobrenome else sobrenome))

else:
    print("Entrada invalida...")
print("----------------------------------------------------")

nome = input("Digite seu nome e sobrenome: ")

partesNome = nome.split()

if len(partesNome) >= 2:
    nome = partesNome[0]
    sobrenome = ' '.join(partesNome[1:])  

    print("Nome:", nome)
    print("Quantidade de caracteres no nome:", len(nome))
    print("Sobrenome:", sobrenome)
    print("Quantidade de caracteres no sobrenome:", len(sobrenome))

else:
    print("Entrada invalida...")
print("----------------------------------------------------")

nome = input("Digite seu nome e sobrenome: ")

partesNome = nome.split()

if len(partesNome) >= 2:
    nome = partesNome[0]
    sobrenome = ' '.join(partesNome[1:])  

    nomePalindromo = nome.lower() == nome.lower()[::-1]

    print("Nome:", nome)
    print("Sobrenome:", sobrenome)
    
    if nomePalindromo:
        print("Seu nome e um palindromo!")
    else:
        print("Seu nome nao e um palindromo.")
else:
    print("Entrada invalida...")

print("----------------------------------------------------")