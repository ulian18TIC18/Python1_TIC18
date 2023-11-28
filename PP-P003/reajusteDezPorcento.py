def adicionarFuncionario(arquivo):
   
    with open(arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip().split(',')
            nome, sobrenome, anoNascimento, RG, anoAdmissao, salario = linha
            funcionarios[f'{nome} {sobrenome}'] = {
                'nome': nome,
                'sobrenome': sobrenome,
                'ano_nascimento': int(anoNascimento),
                'RG': RG,
                'ano_admissao': int(anoAdmissao),
                'salario': float(salario)
            }

def reajustaDezPorcento(funcionarios):
   
    for funcionario, info in funcionarios.items():
        info['salario'] *= 1.1

arquivoFuncionarios = 'funcionarios.txt'
funcionarios = {}
adicionarFuncionario(arquivoFuncionarios)
print("Antes do reajuste:")
print(funcionarios)

reajustaDezPorcento(funcionarios)
print("\nDepois do reajuste:")
print(funcionarios)