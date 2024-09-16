class TodoList:
    def __init__(self,name):
        self.name = name
        self.tasks = []
    
    def getList(self):
        return self.tasks
    def setTask(self,desc):
        task = {"description" : desc, "complete" : False}
        self.tasks.append(task)
        print("Tarefa adicionada com sucesso!")
    def removeTask(self,i):
        res = input(f'Deseja excluir "{self.tasks[i-1]}" da lista? (y,n)')
        if res == "y":
            self.tasks.pop(i-1)
            print("Tarefa removida com sucesso!")
        
    def completeTask(self,i):
        self.tasks[i-1].complete = True
        print('Tarefa marcada como concluida')
List = TodoList("Lista")
runing = True
while runing:
    print("Tarefas:")
    print("")
    for task in List.tasks:
        print(f'{[task]} - {task.description} => {"completo" if task.complete else "incompleta"}')
    
    

