# ==========================
# SISTEMA ESCOLAR
# ==========================
from time import sleep

# ==========================
# LISTA VAZIA
# ==========================

alunos = []
professores = []
proximo_numero = 1
proximo_professor = 1

# ==========================
# DISCIPLINAS DO CURSO
# ==========================

nomes_disciplinas = [
    "Algoritmo e Programação",
    "Banco de Dados",
    "Engenharia de Software"
]

# ==========================
# CORES TERMINAL
# ==========================

verde = "\033[1;32m"
vermelho = "\033[1;31m"
azul = "\033[1;36m"
reset = "\033[0m"
neutro = "\033[2;37m"
laranja = "\033[1;33m"
negrito = "\033[1m"
sublinhado = "\033[4m"

# ==========================
# TEMPO DE IMPRESSÃO
# ==========================

def imprimir(texto, tempo=1):
    print(texto)
    sleep(tempo)

# ==========================
# VALIDAÇÕES E PREVENÇÃO
# ==========================

def validar_texto(mensagem="\nDigite o nome completo do aluno: "):
    nome = input(mensagem)

    while not nome.replace(" ", "").isalpha():
        print(f"{vermelho}Nome inválido! Digite apenas letras.{reset}")
        nome = input(mensagem)

    return nome

# Solicita o nome completo do aluno e verifica se o valor informado
# contém apenas letras e espaços. Caso o usuário digite números ou
# caracteres especiais, uma mensagem de erro é exibida e a entrada
# é solicitada novamente até que seja válida.

def validar_idade(mensagem="Digite a idade: "):

    while True:
        try:
            idade = int(input(mensagem))

            if idade < 5 or idade > 125:
                print(f"{vermelho}Idade inválida!{reset}")
            else:
                return idade

        except ValueError:
            print(f"{vermelho}Digite apenas números!{reset}")

# Solicita a idade do aluno, garantindo que o valor seja numérico.
# Também verifica se a idade está dentro da faixa permitida (5 a 125 anos).
# Enquanto a entrada for inválida, o usuário deverá informar novamente.

def validar_nota():

    notas = []
    nomes_notas = ["1ª", "2ª", "3ª"]

    for c in range(0, 3):

        while True:
            try:
                nota = float(input(f"{nomes_notas[c]} Nota: ").replace(",", "."))

                if nota < 0 or nota > 10:
                    print(f"{vermelho}Nota inválida! Digite entre 0 e 10.{reset}")
                else:
                    notas.append(nota)
                    break

            except ValueError:
                print(f"{vermelho}Digite apenas números!{reset}")

    media = round(sum(notas) / 3, 2)

    return notas, media

# Coleta três notas do aluno, validando se cada uma está entre 0 e 10.
# Se o usuário informar um valor inválido ou não numérico, uma mensagem
# de erro é exibida. Ao final, calcula e retorna a média das três notas.

def validar_matricula(mensagem="Digite a matrícula do aluno(a): "):

    while True:

        matricula = input(mensagem).strip()

        if matricula.isdigit() and len(matricula) == 5:
            return matricula

        else:
            print(f"{vermelho}Digite uma matrícula válida com 5 dígitos.{reset}")

# Solicita a matrícula do aluno e verifica se ela possui exatamente
# 5 dígitos numéricos. Caso contrário, solicita uma nova entrada até
# que o formato correto seja informado.


def calcular_situacao(nota):

    if nota >= 7:
        return f"{verde}APROVADO{reset}"

    elif nota >= 5:
        return f"{laranja}RECUPERAÇÃO{reset}"

    else:
        return f"{vermelho}REPROVADO{reset}"


#Analisa a média final do aluno e define sua situação acadêmica:
#Média maior ou igual a 7: APROVADO      
#Média entre 5 e 6.99: RECUPERAÇÃO                                
#Média inferior a 5: REPROVADO                                    
#Retorna a situação utilizando cores para facilitar a visualização. 

# ==========================
# EMITIR CERTIFICADO
# ==========================


# Verifica se o aluno foi aprovado em todas as disciplinas.           
# Se todas as médias forem maiores ou iguais a 7, exibe um certificado 
# com o nome do aluno, disciplinas cursadas e resultado final.         
# Caso contrário, informa que o certificado não pode ser emitido.      

def emitir_certificado(aluno):

    aprovado = True

    for disciplina in aluno["disciplinas"]:

        if disciplina["media"] < 7:
            aprovado = False

    if aprovado:
        print()
        print(f"{laranja}" + "=" * 60)
        print("             CERTIFICADO DE APROVAÇÃO")
        print("=" * 60 + f"{reset}")

        print(f"\nCertificamos, para os devidos fins, que {verde}{aluno['nome']}{reset} \nconcluiu com sucesso as seguintes disciplinas:")

        for disciplina in aluno["disciplinas"]:

            print(f"- {disciplina['nome']} | Média: {disciplina['media']}")

        print(f"\nRESULTADO FINAL: {verde}APROVADO{reset}")

        print(f"\n{laranja}" + "=" * 60)
        print("             PARABÉNS PELA CONQUISTA!")
        print("=" * 60 + f"{reset}")

    else:

        print(f"{vermelho}Aluno não possui aprovação em todas as disciplinas.{reset}")
imprimir("-")

# ==========================
# MENU CADASTRO
# ==========================

while True:

    print(f"\n{azul}-=-=-=-=-=- SISTEMA ESCOLAR -=-=-=-=-=-{reset}")
    print("\n1 - Cadastrar Aluno")
    print("2 - Listar Alunos")
    print("3 - Pesquisar Aluno")
    print("4 - Editar Aluno")
    print("5 - Remover Aluno")
    print("6 - Cadastrar Professor")
    print("7 - Listar Professores")
    print("8 - Editar Professor")
    print("9 - Remover Professor")
    print("10 - Emitir Certificado")
    print("11 - Relatório completo")
    print("12 - Sair")

    opcao = input("\nEscolha uma opção: ")
    print()
    imprimir("-" * 40)

# ==========================
# CADASTRAR ALUNO
# ==========================

# Cadastra um novo aluno, coleta seus dados e notas,    
# calcula as médias das disciplinas, gera uma matrícula 
# automática e salva as informações no sistema.         

    if opcao == "1":

        print()
        print("Este módulo é destinado ao cadastro de")
        print("estudantes da área de Tecnologia da")
        imprimir("Informação (TI).")

        nome = validar_texto()
        idade = validar_idade()
        
        while True:
            print("\n===== SELECIONE O CURSO =====")
            print("\n1 - Ciências da Computação")
            print("2 - Análise e Desenvolvimento de Sistemas")

            opcao_curso = input("\nEscolha o curso: ")
            print()

            match opcao_curso:
                case "1":
                    curso = "Ciências da Computação"
                    break

                case "2":
                    curso = "Análise e Desenvolvimento de Sistemas"
                    break

                case _:
                    print(f"{vermelho}Opção inválida! Escolha 1 ou 2.{reset}")

        numero = f"{proximo_numero:05d}"

        print()
        print(f"{laranja}ATENÇÃO!{reset}")
        print("Cada disciplina possui 3 avaliações.")
        imprimir("As notas devem ser informadas de 0 a 10.")
        

        disciplinas = []

        for c in range(0, 3):

            print(f"\n{'-' * 10} {c+1}ª DISCIPLINA {'-' * 10}")
            print()
            imprimir(nomes_disciplinas[c])

            notas, media = validar_nota()

            situacao = calcular_situacao(media)

            disciplinas.append({
                "nome": nomes_disciplinas[c],
                "notas": notas,
                "media": media,
                "situacao": situacao
            })

        aluno = {
            "Numero de Matricula": numero,
            "nome": nome,
            "idade": idade,
            "curso": curso,
            "disciplinas": disciplinas
        }

        alunos.append(aluno)
        proximo_numero += 1

        imprimir(f"\n{verde}Aluno cadastrado com sucesso!{reset}")
        imprimir(f"{verde}Número de matrícula: {numero}{reset}")

# ==========================
# LISTAR ALUNOS
# ==========================

# Exibe a lista de alunos cadastrados no sistema.     
# Mostra matrícula, nome, idade, curso, notas, médias 
# e a situação de cada disciplina. Caso não existam   
# alunos cadastrados, informa ao usuário.             

    elif opcao == "2":

        if len(alunos) == 0:

            print(f"{vermelho}\nNenhum aluno cadastrado.{reset}")

        else:

            imprimir("\n ---=== ALUNOS CADASTRADOS ===---")
            print()
            imprimir("-" * 40)

            for aluno in alunos:

                print(f"\nMatrícula: {negrito}{aluno['Numero de Matricula']}{reset}")
                print(f"Nome: {negrito}{aluno['nome']}{reset}")
                print(f"Idade: {negrito}{aluno['idade']}{reset}")
                print(f"Curso: {negrito}{aluno['curso']}{reset}")

                for disciplina in aluno["disciplinas"]:

                    notas_formatadas = " | ".join(f"{n:.1f}" for n in disciplina["notas"])
                    print()
                    print(f"  Disciplina: {sublinhado}{disciplina['nome']}{reset}")
                    print(f"  Notas: {negrito}{sublinhado}{notas_formatadas}{reset}")
                    print(f"  Média: {negrito}{disciplina['media']:.2f}{reset}")
                    print(f"  Situação: {disciplina['situacao']}")

                print()

        imprimir("-" * 40)

# ==========================
# PESQUISAR ALUNO
# ==========================

# Permite consultar um aluno pelo número de matrícula.             
# Caso encontrado, exibe seus dados pessoais, disciplinas,         
# notas, médias e situação em cada matéria. Se a matrícula         
# não existir no sistema, informa que o aluno não foi encontrado.  

    elif opcao == "3":

        print()
        matricula_busca = validar_matricula()

        encontrado = False

        for aluno in alunos:

            if matricula_busca == aluno["Numero de Matricula"]:

                print(f"\n{verde}  ---=== ALUNO ENCONTRADO ===---{reset}")
                print(f"\nMatrícula: {aluno['Numero de Matricula']}")
                print(f"Nome: {negrito}{aluno['nome']}{reset}")
                print(f"Idade: {negrito}{aluno['idade']}{reset}")
                print(f"Curso: {negrito}{aluno['curso']}{reset}")

                for disciplina in aluno["disciplinas"]:

                    notas_formatadas = " | ".join(f"{n:.1f}" for n in disciplina["notas"])
                    print()
                    print(f"Disciplina: {disciplina['nome']}")
                    print(f"Notas: {notas_formatadas}")
                    print(f"Média: {disciplina['media']:.2f}")
                    print(f"Situação: {disciplina['situacao']}")

                encontrado = True
                break

        if not encontrado:
            print(f"{vermelho}Aluno não encontrado!{reset}")
        imprimir("-" * 40)

# ==========================
# EDITAR ALUNO
# ==========================

#Permite localizar um aluno pela matrícula e editar seus dados.       
#O usuário pode alterar nome, idade, curso, notas das disciplinas     
#ou todas as informações de uma vez. Após a edição das notas,         
#a média e a situação da disciplina são recalculadas automaticamente. 
#Caso a matrícula não seja encontrada, uma mensagem de erro é exibida.

    elif opcao == "4":

        print()
        matricula_busca = validar_matricula()

        encontrado = False

        for aluno in alunos:

            if matricula_busca == aluno["Numero de Matricula"]:

                encontrado = True

                print(f"\nAluno encontrado: {aluno['nome']}")

                while True:

                    print("\n----===== EDITAR ALUNO =====----")
                    print("\n1 - Alterar nome")
                    print("2 - Alterar idade")
                    print("3 - Alterar curso")
                    print("4 - Alterar as notas das disciplinas")
                    print("5 - Alterar todas as Informações")
                    print("6 - Voltar ao menu principal")

                    edicao = input("\nEscolher uma opção: ")
                    imprimir("-" * 40)

                    if edicao == "1":

                        aluno["nome"] = validar_texto("\nNovo nome: ")
                        print(f"{verde}Nome atualizado com sucesso!{reset}")
                        imprimir("-" * 40)

                    elif edicao == "2":

                        aluno["idade"] = validar_idade("\nNova idade: ")
                        print(f"{verde}Idade atualizada com sucesso!{reset}")
                        imprimir("-" * 40)

                    elif edicao == "3":
                        while True:
                            print("\n---=== SELECIONE O NOVO CURSO ===---")
                            print("1 - Ciências da Computação")
                            print("2 - Análise e Desenvolvimento de Sistemas")

                            opcao_curso = input("\nEscolha o novo curso: ")
                            imprimir("-" * 40)

                            match opcao_curso:
                                case "1":
                                    aluno["curso"] = "Ciências da Computação"
                                    print(f"{verde}Curso atualizado com sucesso!{reset}")
                                    imprimir("-" * 40)
                                    break

                                case "2":
                                    aluno["curso"] = "Análise e Desenvolvimento de Sistemas"
                                    print(f"{verde}Curso atualizado com sucesso!{reset}")
                                    imprimir("-" * 40)
                                    break
                                case _:
                                    print(f"{vermelho}Opção inválida! Escolha 1 ou 2.{reset}")

                    elif edicao == "4":

                        print("\n---=== ALTERAR NOTAS ===--- ")

                        for c in range(len(aluno["disciplinas"])):
                            print()
                            print(f"{c+1} - {aluno['disciplinas'][c]['nome']}")

                        print(f"{len(aluno['disciplinas'])+1} - Voltar")

                        escolha = input("\nEscolha a disciplina: ")

                        if escolha.isdigit():

                            escolha = int(escolha)

                            if 1 <= escolha <= len(aluno["disciplinas"]):

                                disciplina = aluno["disciplinas"][escolha - 1]

                                print(f"\nDisciplina: {negrito}{disciplina['nome']}{reset}")
                                imprimir("informe as novas notas:")
                                print()

                                notas, media = validar_nota()

                                disciplina["notas"] = notas
                                disciplina["media"] = media
                                disciplina["situacao"] = calcular_situacao(media)

                                print(f"\n{verde}Notas atualizadas!{reset}")

                            elif escolha == len(aluno["disciplinas"]) + 1:

                                print("\nVolta ao menu.")

                            else:
                                print(f"{vermelho}Disciplina inválida!{reset}")

                        else:

                            print(f"{vermelho}Digite uma opção válida{reset}")

                    elif edicao == "5":

                        aluno["nome"] = validar_texto("Novo nome: ")
                        aluno["idade"]= validar_idade("Nova idade: ")
                        while True:
                            print("\n---=== SELECIONE O NOVO CURSO ===---")
                            print("1 - Ciências da Computação")
                            print("2 - Análise e Desenvolvimento de Sistemas")

                            opcao_curso = input("\nEscolha o novo curso: ")
                            imprimir("-" * 40)

                            match opcao_curso:
                                case "1":
                                    aluno["curso"] = "\nCiências da Computação"
                                    print(f"{verde}Curso atualizado com sucesso!{reset}")
                                    imprimir("-" * 40)
                                    break

                                case "2":
                                    aluno["curso"] = "Análise e Desenvolvimento de Sistemas"
                                    print(f"{verde}Curso atualizado com sucesso!{reset}")
                                    imprimir("-" * 40)
                                    break
                                case _:
                                    print(f"{vermelho}Opção inválida! Escolha 1 ou 2.{reset}")


                        for disciplina in aluno["disciplinas"]:

                            print(f"\nDisciplina: {disciplina['nome']}")

                            notas, media = validar_nota()

                            disciplina["notas"]= notas
                            disciplina["media"]= media
                            disciplina["situacao"]= calcular_situacao(media)

                        print(f"{verde}Informações atualizadas{reset}")

                    elif edicao =="6":

                        imprimir("\nVoltando ao menu principal...")
                        break

                    else:
                        print(f"{vermelho}Opção inválida!{reset}")

                break
        if not encontrado:

            print(f"\n{vermelho}Aluno não encontrado!{reset}")

            imprimir("-"*40)
                
# ==========================
# REMOVER ALUNO
# ==========================

# Permite excluir um aluno cadastrado a partir da matrícula.    
# Solicita confirmação antes da remoção e, caso confirmada,     
# remove o aluno da lista. Se a operação for cancelada ou a     
# matrícula não for encontrada, exibe uma mensagem informativa. 

    elif opcao == "5":

        if len(alunos) == 0:

            print(f"{vermelho}Nenhum aluno cadastrado.{reset}")

        else:

            matricula_busca = validar_matricula()

            removido = False

            for aluno in alunos:

                if matricula_busca == aluno["Numero de Matricula"]:

                    confirmar = input(f"Confirma remover {aluno['nome']}? (S/N): ").upper()

                    if confirmar == "S":

                        alunos.remove(aluno)

                        print(f"{verde}\nAluno removido com sucesso!{reset}")
                        print()
                        imprimir("-" * 40)

                    else:
                        print(f"{vermelho}Operação cancelada.{reset}")
                        print()
                        imprimir("-" * 40)

                    removido = True
                    break

            if not removido:
                print("\nAluno não encontrado.")
                print()
                imprimir("-" * 40)

    # ==========================
    # CADASTRAR PROFESSOR
    # ==========================

    elif opcao == "6":

        print(f"{negrito}\n Bem-vindo ao módulo de cadastro de professores!{reset}\nPreencha os dados solicitados para realizar o cadastro.\nAo finalizar, será gerado automaticamente um número de matrícula.")

        professor = validar_texto("\nDigite o nome completo do professor: ")

        idade = validar_idade("Digite a idade: ")

        while True:
            print("\n------ SELECIONE O CURSO ------")
            print("\n1 - Ciências da Computação")
            print("2 - Análise e Desenvolvimento de Sistemas")

            opcao_curso = input("\nEscolha o curso: ")

            match opcao_curso:
                case "1":
                    curso = "Ciências da Computação"
                    break

                case "2":
                    curso = "Análise e Desenvolvimento de Sistemas"
                    break

                case _:
                    print(f"{vermelho}Opção inválida! Escolha 1 ou 2.{reset}")

        numero_professor = f"{proximo_professor:05d}"

        professor = {
            "Numero de Matricula": numero_professor,
            "nome": professor,
            "idade": idade,
            "curso": curso
        }

        professores.append(professor)

        proximo_professor += 1

        print(f"{verde}\nProfessor cadastrado com sucesso!{reset}")
        print(f"{verde}Matrícula: {numero_professor}{reset}")

        imprimir("-" * 40)

    # ==========================
    # LISTAR PROFESSORES
    # ==========================

    elif opcao == "7":

        if len(professores) == 0:
            print(f"{vermelho}\nNenhum professor cadastrado.{reset}")

        else:
            print("\n=== PROFESSORES CADASTRADOS ===")

            for professor in professores:

                print(f"\nMatrícula: {negrito}{professor['Numero de Matricula']}{reset}")
                print(f"Nome: {verde}{professor['nome']}{reset}")
                print(f"Idade: {verde}{professor['idade']} anos{reset}")
                print(f"Curso: {verde}{professor['curso']}{reset}")
                print("-" * 30)   

    # ==========================
    # EDITAR PROFESSOR
    # ==========================
 
    elif opcao == "8":

        matricula_busca = validar_matricula("Digite a matrícula do professor: ")

        encontrado = False

        for professor in professores:

            if matricula_busca == professor["Numero de Matricula"]:

                encontrado = True

                print(f"\nProfessor encontrado: {professor['nome']}")

                professor["nome"] = validar_texto("Novo nome: ")
                professor["idade"] = validar_idade("Nova idade: ")

                while True:

                    print("\n===== SELECIONE O NOVO CURSO =====")
                    print("\n1 - Ciências da Computação")
                    print("2 - Análise e Desenvolvimento de Sistemas")

                    opcao_curso = input("\nEscolha o novo curso: ")

                    match opcao_curso:

                        case "1":
                            professor["curso"] = "Ciências da Computação"
                            break

                        case "2":
                            professor["curso"] = "Análise e Desenvolvimento de Sistemas"
                            break

                        case _:
                            print(f"{vermelho}Opção inválida!{reset}")

                print(f"{verde}\nProfessor atualizado com sucesso!{reset}")
                break

        if not encontrado:
            print(f"{vermelho}Professor não encontrado!{reset}")
            imprimir("-" * 40)

    # ==========================
    # REMOVER PROFESSOR
    # ==========================

    elif opcao == "9":

        if len(professores) == 0:

            print(f"{vermelho}Nenhum professor cadastrado.{reset}")

        else:

            matricula_busca = validar_matricula("Digite a matrícula do professor para remover: ")

            removido = False

            for professor in professores:

                if matricula_busca == professor["Numero de Matricula"]:

                    confirmar = input(
                        f"Confirma remover {professor['nome']}? (S/N): "
                    ).upper()

                    if confirmar == "S":

                        professores.remove(professor)

                        print(f"{verde}Professor removido com sucesso!{reset}")

                    else:

                        print(f"{laranja}Operação cancelada.{reset}")

                    removido = True
                    break

            if not removido:
                print(f"{vermelho}Professor não encontrado!{reset}")

            imprimir("-" * 40)
# ==========================
# EMITIR CERTIFICADO
# ==========================

# Permite emitir o certificado de aprovação de um aluno.                        
# Busca o aluno pela matrícula e verifica se ele existe no sistema.             
# Se encontrado, gera o certificado com base em seu desempenho.                 
# Caso a matrícula não seja localizada, informa que o aluno não foi encontrado. 

    elif opcao == "10":

        if len(alunos) == 0:

            print(f"{vermelho}Nenhum aluno cadastrado.{reset}")

        else:

            matricula_busca = validar_matricula("Digite a matrícula do aluno(a) para a emissão do certificado: ")

            encontrado = False

            for aluno in alunos:

                if matricula_busca == aluno["Numero de Matricula"]:

                    emitir_certificado(aluno)
                    encontrado = True
                    break

            if not encontrado:
                print(f"{vermelho}Aluno não encontrado.{reset}")
                

    elif opcao=="11":
        print()
        imprimir(f"{azul}-=-=-=-=-=- RELATÓRIO FINAL -=-=-=-=-=-{reset}")
        print()
        imprimir(f"{laranja}\n  ALUNOS CADASTRADOS {reset}")

        for aluno in alunos:

            print(f"\n  Matrícula: {negrito}{aluno['Numero de Matricula']}{reset}")
            print(f"  Nome: {negrito}{aluno['nome']}{reset}")
            print(f"  Idade: {negrito}{aluno['idade']}{reset}")
            print(f"  Curso: {negrito}{aluno['curso']}{reset}")

            for disciplina in aluno["disciplinas"]:

                notas_formatadas = " | ".join(f"{n:.1f}" for n in disciplina["notas"])
                print()
                print(f"  Disciplina: {sublinhado}{disciplina['nome']}{reset}")
                print(f"  Notas: {negrito}{sublinhado}{notas_formatadas}{reset}")
                print(f"  Média: {negrito}{disciplina['media']:.2f}{reset}")
                print(f"  Situação: {disciplina['situacao']}")

            print()
            imprimir("-" * 40)

        print(f"{laranja}\n  PROFESSORES CADASTRADOS {reset}")

        for professor in professores:

            print(f"\n  Matrícula: {negrito}{professor['Numero de Matricula']}{reset}")
            print(f"  Nome: {verde}{professor['nome']}{reset}")
            print(f"  Idade: {verde}{professor['idade']} anos{reset}")
            print(f"  Curso: {verde}{professor['curso']}{reset}")
            print("-" * 40)


    # ==========================
    # SAIR
    # ==========================

    elif opcao == "12":

        print(f"{verde}\nSistema encerrado. 0brigado!{reset}")
        break

    # ==========================
    # OPÇÃO INVÁLIDA
    # ==========================

    else:
    
        print("\nOpção inválida.")
        print()
        imprimir("-" * 40)

