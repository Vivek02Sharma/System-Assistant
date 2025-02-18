class TaskManager:
    def __init__(self):
        self.todo_file = "todo.txt"

    def add_todo(self, task):
        with open(self.todo_file, "a") as file:
            file.write(f"{task}\n")
        return f"Added '{task}' to your todo list"

    def read_todo(self):
        try:
            with open(self.todo_file, "r") as file:
                tasks = [line.strip() for line in file.readlines() if line.strip()]
        except FileNotFoundError:
            return "Your todo list is empty"
        
        if not tasks:
            return "Your todo list is empty"
        return "Your tasks:\n" + "\n".join(f"{i+1}. {task}" for i, task in enumerate(tasks))

    def clear_todo(self):
        open(self.todo_file, "w").close()
        return "Todo list cleared"
    

