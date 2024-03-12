# Importar bibliotecas
import os
import json

# Definindo dicionários para armazenar dados
professores = {}
alunos = {}

# Função para cadastrar professor
def cadastrar_professor(nome, cpf, materia):
    """
    # cadastrar_professor():
    Cadastra um novo professor no sistema.
    Parâmetros:
    - nome (str): Nome do professor a ser cadastrado.
    - cpf (str): CPF do professor a ser cadastrado.
    - materia (str): Matéria que o professor leciona.
    """
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
    """
    cadastrar_aluno():
    Cadastra um novo aluno no sistema.
    Parâmetros:
    - nome (str): Nome do aluno a ser cadastrado.
    - cpf (str): CPF do aluno a ser cadastrado.
    - professor_cpf (str): CPF do professor do aluno.
    """
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
    """
    carrgar_dados_json():
    Carrega os dados de professores e alunos a partir de um arquivo JSON.
    Retorna:
    - tuple: Uma tupla contendo os dados dos professores e alunos carregados.
    """
    with open("dados.json", "r") as arquivo:
        dados = json.load(arquivo)

    return dados["professores"], dados["alunos"]

# Função para listar alunos
def listar_alunos():
    """
    Lista todos os alunos cadastrados no sistema.
    """
    professores, alunos = carregar_dados_json()
    
    for cpf, dados in alunos.items():
        print(f"CPF: {cpf}")
        print(f"Nome: {dados['nome']}")
        print(f"Professor: {professores[dados['professor_cpf']]['nome']}")
        print()

def escolher_professor():
    """
    Solicita ao usuário que digite o CPF de um professor.
    Retorna:
    - str: CPF do professor escolhido.
    """
    while True:
        cpf = input("Digite o CPF do professor: ")
        if cpf not in professores:
            print(f"Professor com CPF {cpf} não encontrado!")
            #return None
        else:
            return cpf

def listar_dados_professor(cpf):
    """
    Lista os dados de um professor específico.
    Parâmetros:
    - cpf (str): CPF do professor.

    Retorna:
    - bool: True se o professor foi encontrado e False caso contrário.
    """
    if cpf not in professores:
        print(f"Professor com CPF {cpf} não encontrado!")
        return False

    print(f"**Professor:** {professores[cpf]['nome']}")
    print(f"Matéria: {professores[cpf]['materia']}")
    print(f"Alunos:")
    for aluno_cpf in professores[cpf]['alunos']:
        print(f" - {alunos[aluno_cpf]['nome']}")
    print()
    return True

def listar_professores():
    """
    Lista todos os professores cadastrados no sistema.
    """
    if not professores:
        print("Nenhum professor cadastrado.")
        return

    print("Professores:")
    for cpf, dados in professores.items():
        print(f"CPF: {cpf}")
        print(f"Nome: {dados['nome']}")
        print(f"Materia: {dados['materia']}")
        print()

def listar_todos_alunos():
    """
    Lista todos os alunos, incluindo o nome do professor que eles pertencem.
    """
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("Alunos:")
    for cpf, dados in alunos.items():
        print(f"CPF: {cpf}")
        print(f"Nome: {dados['nome']}")
        print(f"Professor: {professores[dados['professor_cpf']]['nome']}")
        print()

def deletar_professor():
    """
    deletar_professor():
    Chama a funcao listar_professores().\n
    Chama a funcao escolher_professor().\n
    Recebe o CPF.\n
    Busca professor por CPF.\n
    Deletar professor.
    """
    listar_professores()
    cpf_professor = escolher_professor()
    if cpf_professor:
        del professores[cpf_professor]
        for aluno_cpf in alunos.values():
            if aluno_cpf['professor_cpf'] == cpf_professor:
                aluno_cpf['professor_cpf'] = None
        salvar_dados_json()
        print(f"Professor com CPF {cpf_professor} deletado com sucesso!")

def deletar_aluno():
    """
    Deleta um aluno do sistema.
    Este processo envolve selecionar um aluno da lista e removê-lo, 
    juntamente com a atualização do professor associado a ele.
    """
    listar_todos_alunos()
    cpf_aluno = input("Digite o CPF do aluno: ")
    if cpf_aluno in alunos:
        professor_cpf = alunos[cpf_aluno]['professor_cpf']
        alunos.pop(cpf_aluno)
        professores[professor_cpf]['alunos'].remove(cpf_aluno)
        salvar_dados_json()
        print(f"Aluno com CPF {cpf_aluno} deletado com sucesso!")
    else:
        print(f"Aluno com CPF {cpf_aluno} não encontrado!")

def salvar_dados_json():
    with open("dados.json", "w") as arquivo:
        json.dump({"professores": professores, "alunos": alunos}, arquivo, indent=4)

    print("Dados salvos em dados.json com sucesso!")

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
        listar_professores()

    elif opcao == "4":
        listar_alunos()

    elif opcao == '5':
        deletar_professor()

    elif opcao == '6':
        deletar_aluno()

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")

    input("Pressione qualquer tecla para continuar...")
