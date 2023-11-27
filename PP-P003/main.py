import os
import decimal

produtos = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificarCodigo(codigo):
    if not codigo.isdigit():
        return False
    if len(codigo) != 13:
        return False
    return True

def formatarPreco(preco):
    return decimal.Decimal(preco).quantize(decimal.Decimal('0.00'))

def formatarListaProdutos(produtos):
    return '\n'.join(f'{produto["codigo"]} - {produto["nome"]} - R$ {produto["preco"]}' for produto in produtos)

def exibirProdutos():
    produtosOrdenados = sorted(produtos, key=lambda produto: produto["preco"])
    for i in range(0, len(produtosOrdenados), 10):
        clear()
        print(formatarListaProdutos(produtosOrdenados[i:i+10]))
        input('Pressione Enter para continuar...')

def menu():
    clear()
    print("Sistema de Consulta de Preços de Produtos")
    print("1. Inserir novo produto")
    print("2. Excluir produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar preço de um produto")
    print("5. Sair")
    opcao = input("Digite o número da opção desejada: ")
    return opcao

def inserirProduto():
    codigo = input("Digite o código do produto (13 dígitos): ").strip()
    if not verificarCodigo(codigo):
        print("Código inválido!")
        input("Pressione Enter para continuar...")
        return
    nome = input("Digite o nome do produto: ").strip()
    preco = input("Digite o preço do produto: ").strip()
    produtos.append({"codigo": codigo, "nome": nome, "preco": formatarPreco(preco)})
    print("Produto inserido com sucesso!")
    input("Pressione Enter para continuar...")

def excluirProduto():
    codigo = input("Digite o código do produto que deseja excluir: ").strip()
    if not verificarCodigo(codigo):
        print("Código inválido!")
        input("Pressione Enter para continuar...")
        return
    global produtos
    produtos = [produto for produto in produtos if produto["codigo"] != codigo]
    print("Produto excluído com sucesso!")
    input("Pressione Enter para continuar...")

def consultarPreco():
    codigo = input("Digite o código do produto que deseja consultar o preço: ").strip()
    if not verificarCodigo(codigo):
        print("Código inválido!")
        input("Pressione Enter para continuar...")
        return
    produto = next((produto for produto in produtos if produto["codigo"] == codigo), None)
    if produto is None:
        print("Produto não encontrado!")
    else:
        print(f'O preço do produto {produto["nome"]} é R$ {produto["preco"]}')
    input("Pressione Enter para continuar...")

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            inserirProduto()
        elif opcao == "2":
            excluirProduto()
        elif opcao == "3":
            exibirProdutos()
        elif opcao == "4":
            consultarPreco()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

input("Pressione Enter para encerrar...")