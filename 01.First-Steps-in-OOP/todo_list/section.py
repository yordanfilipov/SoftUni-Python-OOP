class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        filtered_tasks = [t for t in self.tasks if t.name == task_name]
        if filtered_tasks:
            task = filtered_tasks[0]
            task.completed = True
            return f"Completed task {task.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        all_not_completed_tasks = [t for t in self.tasks if not t.completed]
        n_removed_tasks = len(self.tasks) - len(all_not_completed_tasks)
        self.tasks = all_not_completed_tasks
        return f"Cleared {n_removed_tasks} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n"
        for t in self.tasks:
            res += t.details() + "\n"
        return res
