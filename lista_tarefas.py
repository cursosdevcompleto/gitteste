tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)

def listar_tarefas():
    for i, t in enumerate(tarefas, start=1):
        print(f"{i}. {t}")

if __name__ == "__main__":
    adicionar_tarefa("Estudar Git")
    adicionar_tarefa("Fazer exercício")
    listar_tarefas()