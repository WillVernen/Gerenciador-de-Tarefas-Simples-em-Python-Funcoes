# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade (alta, média, baixa): ").lower()
    categoria = input("Categoria (trabalho, estudo, lazer, etc.): ").lower()

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i + 1}. Nome: {tarefa['nome']}")
            print(f"   Descrição: {tarefa['descricao']}")
            print(f"   Prioridade: {tarefa['prioridade']}")
            print(f"   Categoria: {tarefa['categoria']}")
            print(f"   Status: {status}")
            print("-" * 30)

# Função para marcar uma tarefa como concluída
def marcar_concluida():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

# Função para exibir tarefas por prioridade
def exibir_por_prioridade():
    prioridade = input("Digite a prioridade (alta, média, baixa): ").lower()
    tarefas_filtradas = [t for t in tarefas if t["prioridade"] == prioridade]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Categoria: {tarefa['categoria']}")
            print(f"Status: {'Concluída' if tarefa['concluida'] else 'Pendente'}")
            print("-" * 30)
    else:
        print(f"Nenhuma tarefa com prioridade '{prioridade}' encontrada.")

# Função para exibir tarefas por categoria
def exibir_por_categoria():
    categoria = input("Digite a categoria: ").lower()
    tarefas_filtradas = [t for t in tarefas if t["categoria"] == categoria]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Status: {'Concluída' if tarefa['concluida'] else 'Pendente'}")
            print("-" * 30)
    else:
        print(f"Nenhuma tarefa na categoria '{categoria}' encontrada.")


# Função principal do programa
def main():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            exibir_por_prioridade()
        elif opcao == "5":
            exibir_por_categoria()
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
        print()

# Executar o programa
if __name__ == "__main__":
    main()
    