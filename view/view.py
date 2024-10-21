import tkinter as tk


class view:
    def __init__(self) -> None:
        root = tk.Tk()
        root.title("connect-4")
        root.geometry("400x300")
        label = tk.Label(root, text="choose a mode from below", font=("Arial", 20))
        label.pack(pady=20)
        option_1 = tk.Button(root, text="human vs.computer(Human Starts)", command=lambda: print("human vs.computer(Human Starts)"))
        option_1.pack(pady=10)
        option_2 = tk.Button(root, text="computer vs. human (Computer Starts)", command=lambda: print("computer vs. human (Computer Starts)"))
        option_2.pack(pady=10)
        option_3 = tk.Button(root, text = "computer vs computer", command=lambda: print("computer vs computer!"))
        option_3.pack(pady=10)
        root.mainloop()







