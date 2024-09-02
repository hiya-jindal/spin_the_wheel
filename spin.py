import tkinter as tk

class SpinTheWheelGame:
    def __init__(root):
        root.window = tk.Tk()
        root.window.title("Spin the Wheel Game")
        root.window.geometry("400x400")

        root.wheel = tk.Canvas(root.window, width=300, height=300)
        root.wheel.pack()

        root.result_label = tk.Label(root.window, text="", font=("Arial", 24))
        root.result_label.pack()

        root.spin_button = tk.Button(root.window, text="Spin the Wheel", command=root.spin_the_wheel)
        root.spin_button.pack()

        root.quit_button = tk.Button(root.window, text="Quit", command=root.window.destroy)
        root.quit_button.pack()

        root.draw_wheel()

    def draw_wheel(root):
        root.wheel.delete("all")
        root.wheel.create_oval(50, 50, 250, 250)
        root.wheel.create_line(150, 50, 150, 250)
        root.wheel.create_text(150, 100, text="Yes", font=("Arial", 24))
        root.wheel.create_text(150, 200, text="No", font=("Arial", 24))

    def spin_the_wheel(root):
        root.result_label.config(text="Yes")

game = SpinTheWheelGame()
game.window.mainloop()