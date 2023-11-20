#Manipulando listas
print("--------------------------------------")
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[::-1]) #ordem inversa
print(L[-1::]) #primeiro elemento impresso
print(L[:-1:]) #ordem correta
print(L[::-2]) #remove os pares
print(L[-2::]) #imprime os dois ultimos elementos
print(L[:-2:]) #remove os dois ultimos elementos
print("--------------------------------------")

anoDeNascimento = 1988

anoZodiacoChines = (anoDeNascimento % 12)

tabelaZodiaco = {
    0: "Macaco",
    1: "Galo",
    2: "Cao",
    3: "Porco",
    4: "Rato",
    5: "Boi",
    6: "Tigre",
    7: "Coelho",
    8: "Dragao",
    9: "Serpente",
    10: "Cavalo",
    11: "Cabra"
}

animalZodiaco = tabelaZodiaco[anoZodiacoChines]
print(f"Seu animal eh: {animalZodiaco}")


