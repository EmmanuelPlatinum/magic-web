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

# Função para listar professores
def listar_professores():
    for cpf, dados in professores.items():
        print(f"**Professor:** {dados['nome']}")
        print(f"Matéria: {dados['materia']}")
        print(f"Alunos:")
        for aluno_cpf in dados['alunos']:
            print(f" - {alunos[aluno_cpf]['nome']}")
        print()

def salvar_dados_json():
    with open("dados.json", "w") as arquivo:
        json.dump({"professores": professores, "alunos": alunos}, arquivo, indent=4)

    print("Dados salvos em dados.json com sucesso!")

# Função para listar alunos
def listar_alunos():
    for cpf, dados in alunos.items():
        print(f"CPF: {cpf}")
        print(f"Nome: {dados['nome']}")
        print(f"Professor: {professores[dados['professor_cpf']]['nome']}")
        print()


# Menu principal
while True:
    os.system('clear')
    print("**Sistema de Cadastro de Professores e Alunos**")
    print("1. Cadastrar Professor")
    print("2. Cadastrar Aluno")
    print("3. Listar Professores")
    print("4. Listar Alunos")
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
        listar_professores()

    elif opcao == "4":
        listar_alunos()

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")

    input("Pressione qualquer tecla para continuar...")

