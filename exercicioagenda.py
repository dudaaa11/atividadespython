import os

agenda_file = "agenda.txt"

agenda = {
    "Pessoais": [],
    "Profissionais": [],
    "Românticos": [],
}

def abrir_agenda():
    global agenda
    if os.path.exists(agenda_file):
        with open(agenda_file, "r") as file:
            agenda = eval(file.read())

def listar_contatos():
    for categoria, contatos in agenda.items():
        print(f"Contatos {categoria}:")
        for contato in contatos:
            print(contato)

def criar_contato():
    global agenda
    nome = input("Digite o nome do contato que deseja: ")
    telefone = input("Digite o telefone do contato: ")
    endereco = input("Digite o endereço do contato: ")
    categoria = input("Digite a categoria (Pessoais/Profissionais/Românticos): ").capitalize()

    if categoria in agenda:
        novo_contato = {"Nome": nome, "Endereço": endereco, "Telefone": telefone}
        agenda[categoria].append(novo_contato)
        print("Contato adicionado com sucesso!")
    else:
        print("Categoria inválida. Tente novamente...")

def editar_contato():
    global agenda
    nome = input("Digite o nome do contato que deseja editar: ")
    for categoria, contatos in agenda.items():
        for contato in contatos:
            if contato["Nome"] == nome:
                print(f"Editando contato {categoria}: {contato}")
                novo_nome = input("Novo nome (deixe em branco para manter o mesmo): ")
                novo_telefone = input("Novo telefone (deixe em branco para manter o mesmo): ")
                novo_endereco = input("Novo endereço (deixe em branco para manter o mesmo): ")

                if novo_nome:
                    contato["Nome"] = novo_nome
                if novo_telefone:
                    contato["Telefone"] = novo_telefone
                if novo_endereco:
                    contato["Endereço"] = novo_endereco

                print("Contato editado com sucesso.")
                return
    print(f"Contato '{nome}' não encontrado.")

def excluir_contato():
    global agenda
    nome = input("Digite o nome do contato que deseja excluir: ")
    for categoria, contatos in agenda.items():
        for contato in contatos:
            if contato["Nome"] == nome:
                contatos.remove(contato)
                print(f"Contato {categoria} removido com sucesso.")
                return
    print(f"Contato '{nome}' não encontrado. Tente novamente...")

def salvar_agenda():
    global agenda
    with open(agenda_file, "w") as file:
        file.write(str(agenda))
    print("Agenda salva com sucesso!")

def fechar_agenda():
    resposta = input("Deseja salvar a agenda antes de fechar? (S/N): ").strip().lower()
    if resposta == "s":
        salvar_agenda()
    elif resposta == "n":
        pass
    else:
        print("Resposta inválida. A agenda não será salva.")

def main():
    abrir_agenda()
    while True:
        print("\n=== Agenda de Contatos ===")
        print("1. Listar Contatos")
        print("2. Criar Contato")
        print("3. Editar Contato")
        print("4. Excluir Contato")
        print("5. Fechar Agenda")
        escolha = input("Escolha uma opção (1/2/3/4/5): ").strip()

        if escolha == "1":
            listar_contatos()
        elif escolha == "2":
            criar_contato()
        elif escolha == "3":
            editar_contato()
        elif escolha == "4":
            excluir_contato()
        elif escolha == "5":
            fechar_agenda()
            break
        else:
            print("Opção inválida. Tente novamente...")

if __name__ == "__main__":
    main()