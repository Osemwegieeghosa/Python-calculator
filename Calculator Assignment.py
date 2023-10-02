from tkinter import *
import re


# First i defined my functions


def answer():
    try:
        solve = res.get()
        if re.search('[(]', solve):
            solve = re.sub(r'[(]', '*(', solve)
        if re.search(r'^[0]\d', solve):
            solve = re.sub(r'^[0]', '', solve)
        ans = eval(solve)
        res.set(f'{ans}')
    except ZeroDivisionError:
        res.set('Math Error')
    except:
        res.set('Syntax error')


def clear():
    res.set('')


def clean():
    user_input = res.get()
    res.set(user_input[:-1])


base = Tk()
base.geometry('400x500')
base.configure(bg='black')
base.title("Eghosa's Calculator")
# Creating the frames
first = Frame(base, bg='black')
first.pack(fill='x', side='top', ipadx=20, ipady=5)
second_frame = Frame(base, bg='black')
second_frame.pack(fill='x', ipadx=20, ipady=10)
third_frame = Frame(base, bg='black')
third_frame.pack(fill='x', ipadx=20, ipady=10)
fourth_frame = Frame(base, bg='black')
fourth_frame.pack(fill='x', ipadx=20, ipady=10)
fifth_frame = Frame(base, bg='black')
fifth_frame.pack(fill='x', ipadx=20, ipady=10)
sixth_frame = Frame(base, bg='black')
sixth_frame.pack(fill='x', ipadx=20, ipady=10)

# Items for the first frame

res = StringVar()
result = Entry(first, bg='black', fg='white', textvariable=res, font=('Ariel', 20), justify='right')
result.pack(padx='5', pady='10', fill='x', ipadx=20, ipady=50)

# Second frame

clear_var = BooleanVar
clear = Button(second_frame, text='AC', command=clear, fg='orange', bg='black', font=('calibre', 10, 'bold'))
clear.pack(side='left', padx=10, ipadx=50, ipady=7)
clean = Button(second_frame, text='C', fg='orange', bg='black', font=('calibre', 10, 'bold'),
               command=clean)
clean.pack(padx=10, ipadx=35, ipady=7, side='left')
opened = Button(second_frame, text='(', fg='orange', bg='black', font=('calibre', 10, 'bold'),
                command=lambda: result.insert(END, '('))
opened.pack(side='left', padx=10, ipadx=20, ipady=7)
close = Button(second_frame, text=')', fg='orange', bg='black', font=('calibre', 10, 'bold'),
               command=lambda: result.insert(END, ')'))
close.pack(padx=10, ipadx=20, ipady=7, side='left')


# Frame 3

one = Button(third_frame, text='1', fg='orange', bg='black', font=('calibre', 10, 'bold'),
             command=lambda: result.insert(END, '1'))
one.pack(side='left', padx=10, ipadx=30, ipady=7)
two = Button(third_frame, text='2', fg='orange', bg='black', font=('calibre', 10, 'bold'),
             command=lambda: result.insert(END, '2'))
two.pack(side='left', padx=10, ipadx=30, ipady=7)
three = Button(third_frame, text='3', fg='orange', bg='black', font=('calibre', 10, 'bold'),
               command=lambda: result.insert(END, '3'))
three.pack(side='left', padx=10, ipadx=30, ipady=7)
multiple = Button(third_frame, text='x', fg='orange', bg='black', font=('calibre', 10, 'bold'),
                  command=lambda: result.insert(END, '*'))
multiple.pack(side='left', padx=10, ipadx=30, ipady=7)

# frame 4

four = Button(fourth_frame, text='4', fg='orange', bg='black', font=('calibre', 10, 'bold'),
              command=lambda: result.insert(END, '4'))
four.pack(side='left', padx=10, ipadx=30, ipady=7)
five = Button(fourth_frame, text='5', fg='orange', bg='black', font=('calibre', 10, 'bold'),
              command=lambda: result.insert(END, '5'))
five.pack(side='left', padx=10, ipadx=30, ipady=7)
six = Button(fourth_frame, text='6', fg='orange', bg='black', font=('calibre', 10, 'bold'),
             command=lambda: result.insert(END, '6'))
six.pack(side='left', padx=10, ipadx=30, ipady=7)
divide = Button(fourth_frame, text='/', fg='orange', bg='black', font=('calibre', 10, 'bold'),
                command=lambda: result.insert(END, '/'))
divide.pack(side='left', padx=10, ipadx=30, ipady=7)

# fifth frame

seven = Button(fifth_frame, text='7', fg='orange', bg='black', font=('calibre', 10, 'bold'),
               command=lambda: result.insert(END, '7'))
seven.pack(side='left', padx=10, ipadx=30, ipady=7)
eight = Button(fifth_frame, text='8', fg='orange', bg='black', font=('calibre', 10, 'bold'),
               command=lambda: result.insert(END, '8'))
eight.pack(side='left', padx=10, ipadx=30, ipady=7)
nine = Button(fifth_frame, text='9', fg='orange', bg='black', font=('calibre', 10, 'bold'),
              command=lambda: result.insert(END, '9'))
nine.pack(side='left', padx=10, ipadx=30, ipady=7)
plus = Button(fifth_frame, text='+', fg='orange', bg='black', font=('calibre', 10, 'bold'),
              command=lambda: result.insert(END, '+'))
plus.pack(side='left', padx=10, ipadx=30, ipady=7)

# sixth

dot = Button(sixth_frame, text='.', fg='orange', bg='black', font=('calibre', 10, 'bold'),
             command=lambda: result.insert(END, '.'))
dot.pack(side='left', padx=10, ipadx=30, ipady=7)
zero = Button(sixth_frame, text='0', fg='orange', bg='black', font=('calibre', 10, 'bold'),
              command=lambda: result.insert(END, '0'))
zero.pack(side='left', padx=10, ipadx=30, ipady=7)
minus = Button(sixth_frame, text='-', fg='orange', bg='black', font=('calibre', 10, 'bold'),
               command=lambda: result.insert(END, '-'))
minus.pack(padx=10, ipadx=30, ipady=7, side='left')
equal = Button(sixth_frame, text='=', fg='orange', bg='black', command=answer, font=('calibre', 12, 'bold'))
equal.pack(side='left', padx=10, ipadx=45, ipady=7)

base.mainloop()
