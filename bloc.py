import tkinter as tk

root = tk.Tk()
root.title("Bloc de Notas")
root.geometry("600x400")

text_area = tk.Text(root, wrap='word')
text_area.pack(expand=1, fill='both')

root.mainloop()


