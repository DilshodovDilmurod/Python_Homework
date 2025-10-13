### 1. ToDo List Application
# Create a Task class with attributes such as task title, description, due date, and status.
class Task:
    def __init__(self, title, description,due_date, status=bool):
        self.title = title
        self.description = description
        self.due_data = due_date
        self.status = status
task1 = Task('yurish', 'kunda 10 mint sayr', 2025-12-12, 1)
print(task1.status)

## Create a ToDoList class that manages a list of tasks.
## Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
class ToDoList:
    def __init__(self):
        self.all_tasks = []
    
    def add_task(self, title, description, due_date, status):
        task ={
            'title':title,
            'description': description,
            'due_date':due_date,
            'status':status
        }
        self.all_tasks.append(task)
        print(f'{task['title']} buyrigi royxatga qoshildi')

    def mark_task(self, name, statuses):
        for task in self.all_tasks:
            if name == task['title']:
                task['status'] = statuses
                print(f'{task['title']} ning statusi {statuses} ga ozgartirildi')
          
    def show_tasks(self):
        for f in self.all_tasks:
            print(f'Title: {f['title'].title()}, description: {f['description']}, tugatish sanasi: {f['due_date']}, hozirgi holati:{f['status']}')

    def incomplete(self):
        for task in self.all_tasks:
            if not task['status'] == 'tugallangan':
                print(f'Title:{task['title']}')


add_task
tasks = ToDoList()
tasks.add_task('yurish', 'kunda 10 mint sayr', '2025-12-12', 'tugallanmagan')
tasks.add_task('uy vazifasi', 'homeworklarni yechish', '2025-12-10', 'tugallanmagan')

mark_task
tasks.mark_task('yurish', 'tugallangan')
show_task
tasks.show_tasks()
incomplete
tasks.incomplete()

### Develop a simple CLI to interact with the ToDoList.
Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
class ToDoList:
    def __init__(self):
        self.all_tasks = []
    
    def add_task(self, title, description, due_date, status):
        task ={
            'title':title,
            'description': description,
            'due_date':due_date,
            'status':status
        }
        self.all_tasks.append(task)
        print(f'{task['title']} buyrigi royxatga qoshildi')

    def mark_task(self, name, statuses):
        for task in self.all_tasks:
            if name == task['title']:
                task['status'] = statuses
                print(f'{task['title']} ning statusi {statuses} ga ozgartirildi')
          
    def show_tasks(self):
        for f in self.all_tasks:
            print(f'Title: {f['title'].title()}, description: {f['description']}, tugatish sanasi: {f['due_date']}, hozirgi holati:{f['status']}')

    def incomplete(self):
        for task in self.all_tasks:
            if not task['status'] == 'tugallangan':
                print(f'Title:{task['title']}')


def run_cli():
    todo = ToDoList()

    while True:
        print("=== ToDo List CLI===")
        print("1. Yangi vazifa qoshish")
        print("2. Vazifalarni korish")
        print("3. Holatini ozgartirish")
        print("4. Dasturdan chiqish")

        tanlov = input("Tanlang (1-4): ")

        if tanlov == '1':
            title = input('Vazifa nomini kiriting:')
            description = input('Tavsif kiriting:')
            due_date = input('Tugatish sanasini kiriting:')
            status = input('Hozirgi holtini kiriting(tugallangan/tugallanmagan):')
            todo.add_task(title, description, due_date, status)
        elif tanlov == '2':
            todo.show_tasks()
        elif tanlov == '3':
            name = input('Ozgartirmoqchi bolgan vazifa nomini kiriting:')
            status = input('Hozirgi holtini kiriting(tugallangan/tugallanmagan):')
            todo.mark_task(name, status)
        elif tanlov == '4':
            print('Dasturdan chiqildi.')
            break
        else:
            print('Notogri tanlov, 1-4 oraliqda tanlang!')
