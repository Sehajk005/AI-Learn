import tkinter as tk

first_num=sec_num=operator=None
def clear():
    result_label.config(text='')

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def operation(op):
    global first_num, operator
    first_num = int(result_label['text'])
    operator = op
    result_label.config(text=str(first_num)+str(operator))

def get_result():
    global first_num, sec_num, operator
    expression = result_label['text']
    if operator == '+':
        first_num, sec_num = expression.split('+')
        result = int(first_num) + int(sec_num)
    elif operator == '-':
        first_num, sec_num = expression.split('-')
        result = int(first_num) - int(sec_num)
    elif operator == '*':
        first_num, sec_num = expression.split('*')
        result = int(first_num) * int(sec_num)
    elif operator == '/':
        first_num, sec_num = expression.split('/')
        if int(sec_num) == 0:
            result = 'Error'
        else:
            result = round(int(first_num) / int(sec_num), 2)

    result_label.config(text=str(result))
root = tk.Tk()
root.title("Calculator")

root.geometry("280x380")
root.resizable(0,0)

root.configure(background="black")

result_label = tk.Label(root, text='', fg="white", bg="black")
result_label.grid(row=0, column=0, columnspan=6, pady=(50,25), sticky="w")
result_label.configure(font=('verdana',30,'bold'))

btn_7 = tk.Button(root, text="7", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(7))
btn_7.grid(row=1, column=0)
btn_7.configure(font=('verdana',14))

btn_4 = tk.Button(root, text="4", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(4))
btn_4.grid(row=2, column=0)
btn_4.configure(font=('verdana',14))

btn_1 = tk.Button(root, text="1", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(1))
btn_1.grid(row=3, column=0)
btn_1.configure(font=('verdana',14))

btn_clear = tk.Button(root, text="C", bg="#00a65a", fg="black", width=5, height=2, command=lambda: clear())
btn_clear.grid(row=4, column=0)
btn_clear.configure(font=('verdana',14))

btn_8 = tk.Button(root, text="8", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(8))
btn_8.grid(row=1, column=1)
btn_8.configure(font=('verdana',14))

btn_5 = tk.Button(root, text="5", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(5))
btn_5.grid(row=2, column=1)
btn_5.configure(font=('verdana',14))

btn_2 = tk.Button(root, text="2", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(2))
btn_2.grid(row=3, column=1)
btn_2.configure(font=('verdana',14))

btn_0 = tk.Button(root, text="0", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(0))
btn_0.grid(row=4, column=1)
btn_0.configure(font=('verdana',14))

btn_9 = tk.Button(root, text="9", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(9))
btn_9.grid(row=1, column=2)
btn_9.configure(font=('verdana',14))

btn_6 = tk.Button(root, text="6", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(6))
btn_6.grid(row=2, column=2)
btn_6.configure(font=('verdana',14))

btn_3 = tk.Button(root, text="3", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_digit(3))
btn_3.grid(row=3, column=2)
btn_3.configure(font=('verdana',14))

btn_equal = tk.Button(root, text="=", bg="#00a65a", fg="black", width=5, height=2, command=lambda: get_result())
btn_equal.grid(row=4, column=2)
btn_equal.configure(font=('verdana',14))

btn_add = tk.Button(root, text="+", bg="#00a65a", fg="black", width=5, height=2, command=lambda: operation('+'))
btn_add.grid(row=1, column=3)
btn_add.configure(font=('verdana',14))

btn_sub = tk.Button(root, text="-", bg="#00a65a", fg="black", width=5, height=2, command=lambda: operation('-'))
btn_sub.grid(row=2, column=3)
btn_sub.configure(font=('verdana',14))

btn_mul = tk.Button(root, text="*", bg="#00a65a", fg="black", width=5, height=2, command=lambda: operation('*'))
btn_mul.grid(row=3, column=3)
btn_mul.configure(font=('verdana',14))

btn_div = tk.Button(root, text="/", bg="#00a65a", fg="black", width=5, height=2, command=lambda: operation('/'))
btn_div.grid(row=4, column=3)
btn_div.configure(font=('verdana',14))

root.mainloop()