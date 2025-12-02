import tkinter as tk

class Menu:
    def __init__(self):
        self.mode = "single"
        self.difficulty = "medium"
        

        self.root = tk.Tk()
        self.root.title("Pong Menu")
        self.root.geometry("300x260")
        self.root.resizable(False, False)


        tk.Label(self.root, text="PONG GAME", font=("Arial", 20, "bold")).pack(pady=10)

        # drop down
        tk.Label(self.root, text="Select Mode:", font=("Arial", 12)).pack(pady=5)
        self.mode_var = tk.StringVar(value="Single_Player")
        tk.OptionMenu(self.root, self.mode_var, "Single_Player", "Double_Player").pack()

        tk.Label(self.root, text="Select Difficulty:", font=("Arial", 12)).pack(pady=5)
        self.diff_var = tk.StringVar(value="medium")
        tk.OptionMenu(self.root, self.diff_var, "easy", "medium", "hard").pack()



        tk.Button(self.root, text="Start Game", width=15, height=2,
                  command=self._start_game).pack(pady=15)

        self.root.mainloop()

    def _start_game(self):
        self.mode = self.mode_var.get()
        self.difficulty = self.diff_var.get()
        self.root.destroy()

    def user_input(self):
        return self.mode, self.difficulty
