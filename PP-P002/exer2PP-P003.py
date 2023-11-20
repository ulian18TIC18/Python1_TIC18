import shelve

def print_menu():
    print("Menu de Opções:")
    print("1 - Listar tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Marcar tarefa como realizada")
    print("4 - Editar tarefa")
    print("5 - Sair")

def listar_tarefas(tarefas):
    print("Listando tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['descricao']} {'[x]' if tarefa['concluida'] else '[ ]'}")

def add_tarefa(tarefas):
    descricao = input("Digite a descrição da nova tarefa: ")
    tarefa = {"descricao": descricao.capitalize(), "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa registrada!!!")

def marcar_realizada(tarefas, id_tarefa):
    id_tarefa = int(id_tarefa)
    if 0 <= id_tarefa < len(tarefas) and not tarefas[id_tarefa]["concluida"]:
        tarefas[id_tarefa]["concluida"] = True
        print("Tarefa marcada como concluída!!!")
    else:
        print("ID de tarefa inválido ou tarefa já concluída.")

def editar_tarefa(tarefas, id_tarefa, nova_descricao):
    id_tarefa = int(id_tarefa)
    if 0 <= id_tarefa < len(tarefas):
        tarefas[id_tarefa]["descricao"] = nova_descricao.capitalize()
        print("Tarefa editada com sucesso!!!")
    else:
        print("ID de tarefa inválido.")

def main():
    # Abra o arquivo de banco de dados shelve
    with shelve.open("ToDoList") as db:
        tarefas = db.get("tarefas", [])

        while True:
            print_menu()
            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                listar_tarefas(tarefas)
            elif opcao == "2":
                add_tarefa(tarefas)
            elif opcao == "3":
                try:
                    id_tarefa = input("Digite o ID da tarefa que deseja marcar como realizada: ")
                    marcar_realizada(tarefas, id_tarefa)
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")
            elif opcao == "4":
                try:
                    id_tarefa = input("Digite o ID da tarefa que deseja editar: ")
                    nova_descricao = input("Digite a nova descrição da tarefa: ")
                    editar_tarefa(tarefas, id_tarefa, nova_descricao)
                except ValueError:
                    print("Valor inválido. Digite um número inteiro.")
            elif opcao == "5":
                print("Saindo do aplicativo ToDoList.")
                break
            else:
                print("Opção inválida. Tente novamente.")

        
        db["tarefas"] = tarefas


main()
