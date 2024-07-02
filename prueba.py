class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status}\n{self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"Task '{task.title}' not found")

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

manager = TaskManager()
task1 = Task("Buy groceries", "Milk, Bread, Eggs")
task2 = Task("Pay bills", "Electricity and Water bills")

manager.add_task(task1)
manager.add_task(task2)
manager.list_tasks()

task1.complete()
manager.list_tasks()
