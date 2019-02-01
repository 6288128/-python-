import tkinter as tk
from equation_func import get_solution


def get_x(Return=None):
    x=input_.get()
    if x:
        solution = get_solution(x)
        solution_text.set(solution)
    else:
        solution_text.set('请输入一个方程')

window = tk.Tk()
window.title('解方程')
window.geometry('400x200')

solution_text = tk.StringVar()
solution_text.set('请输入一个方程')

input_ = tk.Entry(window, show=None)
input_.bind("<Return>", get_x)
input_.pack()

button1 = tk.Button(window, text ="解方程",command=get_x)
button1.pack()

senten = tk.Label(window, textvariable=solution_text)
senten.pack()

window.mainloop()