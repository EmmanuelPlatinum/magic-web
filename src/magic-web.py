# Importando bibliotecas
import os
import json
# Definindo dicionários para armazenar dados
professores = {}
alunos = {}

# Função para cadastrar professor
def cadastrar_professor(nome, cpf, materia):
    # Verificando se o professor já existe
    if cpf in professores:
        print(f"Professor com CPF {cpf} já cadastrado!")
        return

    # Adicionando o professor ao dicionário
    professores[cpf] = {
        "nome": nome,
        "materia": materia,
        "alunos": []
    }

    print(f"Professor {nome} cadastrado com sucesso!")

# Função para cadastrar aluno
def cadastrar_aluno(nome, cpf, professor_cpf):
    # Verificando se o professor existe
    if professor_cpf not in professores:
        print(f"Professor com CPF {professor_cpf} não encontrado!")
        return

    # Verificando se o aluno já existe
    if cpf in alunos:
        print(f"Aluno com CPF {cpf} já cadastrado!")
        return

    # Adicionando o aluno ao dicionário
    alunos[cpf] = {
        "nome": nome,
        "professor_cpf": professor_cpf
    }

    # Adicionando o aluno à lista de alunos do professor
    professores[professor_cpf]["alunos"].append(cpf)

    print(f"Aluno {nome} cadastrado com sucesso!")


def carregar_dados_json():
    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)

    return dados["professores"], dados["alunos"]



# Função para listar professores
def listar_alunos():
    professores, alunos = carregar_dados_json()

    for cpf, dados in alunos.items():
        print(f"CPF: {cpf}")
        print(f"Nome: {dados['nome']}")
        print(f"Professor: {professores[dados['professor_cpf']]['nome']}")
        print()


def escolher_professor():
    while True:
        cpf = input("Digite o CPF do professor: ")
        if cpf not in professores:
            print(f"Professor com CPF {cpf} não encontrado!")
            continue
        else:
            break
    return cpf

def listar_dados_professor(cpf):
    print(f"**Professor:** {professores[cpf]['nome']}")
    print(f"Matéria: {professores[cpf]['materia']}")
    print(f"Alunos:")
    for aluno_cpf in professores[cpf]['alunos']:
        print(f" - {alunos[aluno_cpf]['nome']}")
    print()





def salvar_dados_json():
    with open("dados.json", "w") as arquivo:
        json.dump({"professores": professores, "alunos": alunos}, arquivo, indent=4)

    print("Dados salvos em dados.json com sucesso!")


def deletar_professor(cpf):
    if cpf not in professores:
        print(f"Professor com CPF {cpf} não encontrado!")
        return

    # Deletar o professor do dicionário
    del professores[cpf]

    # Deletar o professor da lista de alunos de seus alunos
    for aluno_cpf in alunos.values():
        if aluno_cpf['professor_cpf'] == cpf:
            aluno_cpf['professor_cpf'] = None

    salvar_dados_json()

    print(f"Professor com CPF {cpf} deletado com sucesso!")



def deletar_aluno(cpf):
    if cpf not in alunos:
        print(f"Aluno com CPF {cpf} não encontrado!")
        return

    # Deletar o aluno do dicionário
    del alunos[cpf]

    # Remover o aluno da lista de alunos do professor
    professor_cpf = alunos[cpf]['professor_cpf']
    professores[professor_cpf]['alunos'].remove(cpf)

    salvar_dados_json()

    print(f"Aluno com CPF {cpf} deletado com sucesso!")

cpf_aluno = input("Digite o CPF do aluno: ")
deletar_aluno(cpf_aluno)

# Menu principal
while True:
    os.system('clear')
    print("**Sistema de Cadastro de Professores e Alunos**")
    print("1. Cadastrar Professor")
    print("2. Cadastrar Aluno")
    print("3. Listar Professores")
    print("4. Listar Alunos")
    print("5. Deletar Professor")
    print("6. Deletar Aluno ")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do professor: ")
        cpf = input("Digite o CPF do professor: ")
        materia = input("Digite a matéria do professor: ")
        cadastrar_professor(nome, cpf, materia)
        salvar_dados_json()

    elif opcao == "2":
        nome = input("Digite o nome do aluno: ")
        cpf = input("Digite o CPF do aluno: ")
        professor_cpf = input("Digite o CPF do professor do aluno: ")
        cadastrar_aluno(nome, cpf, professor_cpf)
        salvar_dados_json()

    elif opcao == "3":
        cpf_professor = escolher_professor()
        listar_dados_professor(cpf_professor)

    elif opcao == "4":
        listar_alunos()
    elif opcao == '5':
        cpf_professor = escolher_professor()
        deletar_professor(cpf_professor)
    elif opcao == '6':
        cpf_aluno = input("Digite o CPF do aluno: ")
        deletar_aluno(cpf_aluno)

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")

    input("Pressione qualquer tecla para continuar...")

