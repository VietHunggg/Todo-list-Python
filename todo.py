import tkinter as tk
import random 
class Todo(tk.Tk):
    def __init__(self, tasks = None):
        super().__init__()

        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
        
        #define the title and original size of app
        self.title("First app by VietHung")
        self.geometry("400x600")
        
        #make a label in the app to contact with user
        todo1 = tk.Label(self, text="What will u do ?", bg="#546A76", fg="orange", pady= 10)
        
        #add label todo1 into the frames of the app
        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)
        self.task_creat = tk.Text(self, height=3, bg="#FAD4D8", fg="#546A76")

        self.task_creat.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_creat.focus_set()

        self.bind("<Return>", self.add_task)
        #t cần nhồi cái hàm colors(self) dưới kia vào cái để cái giá trị của "bg" vs "fg" này là kiểu pick random
        self.colour_schemes = [{"bg": "#88A0A8", "fg": "black"},{"bg": "#B4CEB3","fg": "white"},{"bg": "#DBD3C9", "fg": "#F06C9B"}]

    #def pick random colors
    
    def add_task(self, event = None):
        task_text = self.task_creat.get(1.0, tk.END).strip()

        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady= 10)
            _, task_style_choice = divmod(len(self.tasks), 3)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])

            new_task.pack(side=tk.TOP, fill=tk.X)

            self.tasks.append(new_task)

        self.task_creat.delete(1.0, tk.END)

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()