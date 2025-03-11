from tkinter import *
from tkinter import messagebox
import random
from time import sleep
import math



def enter_calculator():
    p1 = random.randint(0,10)
    p2 = random.randint(0,10)
    pt = str(p1) + ' + ' + str(p2) + ' = ' + str(p1+p2)
    messagebox.showinfo('Calculator.io', pt)

def check_ptn():
    global ptn
    if len(ptn) != 1:
        if (('.' in ptn) == False):
            if (ptn[0] == '0'):
                ptn = ptn[1:]
        else:
            if ptn[len(ptn)-1] == '0':
                ptn = ptn[:-1]
                if ptn[len(ptn)-1] == '.':
                    ptn = ptn[:-1]

def cls():
    global ptn
    ptn = 0
    ptn_var.set(ptn)

def clearance():
    global ptn
    global temp
    global mem
    temp = 0
    ptn = 0
    mem = 0
    ptn_var.set(ptn)

def n1():
    global ptn
    ptn =str(ptn)+'1'
    check_ptn()
    ptn_var.set(ptn)

def n2():
    global ptn
    ptn =str(ptn)+'2'
    check_ptn()
    ptn_var.set(ptn)

def n3():
    global ptn
    ptn =str(ptn)+'3'
    check_ptn()
    ptn_var.set(ptn)

def n4():
    global ptn
    ptn =str(ptn)+'4'
    check_ptn()
    ptn_var.set(ptn)

def n5():
    global ptn
    ptn =str(ptn)+'5'
    check_ptn()
    ptn_var.set(ptn)

def n6():
    global ptn
    ptn =str(ptn)+'6'
    check_ptn()
    ptn_var.set(ptn)

def n7():
    global ptn
    ptn =str(ptn)+'7'
    check_ptn()
    ptn_var.set(ptn)

def n8():
    global ptn
    ptn =str(ptn)+'8'
    check_ptn()
    ptn_var.set(ptn)

def n9():
    global ptn
    ptn =str(ptn)+'9'
    check_ptn()
    ptn_var.set(ptn)

def n0():
    global ptn
    ptn =str(ptn)+'0'
    check_ptn()
    ptn_var.set(ptn)

def nd():
    global ptn
    ptn =str(ptn)+'.'
    check_ptn()
    ptn_var.set(ptn)

def negt():
    global ptn
    ptn ='-'+str(ptn)
    check_ptn()
    ptn_var.set(ptn)

def pc():
    global ptn
    ptn = str(float(ptn)/100.0)
    check_ptn()
    ptn_var.set(ptn)

def equ():
    global ptn
    if lc == '+':
        ptn = float(temp) + float(ptn)
    elif lc == '-':
        ptn = float(temp) - float(ptn)
    elif lc == '*':
        ptn = float(temp) * float(ptn)
    elif lc == '/':
        ptn = float(temp) / float(ptn)
    elif lc == '^':
        ptn = pow(float(temp), float(ptn))
    ptn = str(ptn)
    check_ptn()
    ptn_var.set(ptn)

def ad():
    global ptn
    global temp
    global lc
    global rs
    lc = '+'
    temp = ptn
    ptn = 0

def sb():
    global ptn
    global temp
    global lc
    global rs
    lc = '-'
    temp = ptn
    ptn = 0

def mult():
    global ptn
    global temp
    global lc
    global rs
    lc = '*'
    temp = ptn
    ptn = 0


def divd():
    global ptn
    global temp
    global lc
    global rs
    lc = '/'
    temp = ptn
    ptn = 0


def pew():
    global ptn
    global temp
    global lc
    global rs
    lc = '^'
    temp = ptn
    ptn = 0
    check_ptn()
    ptn_var.set(ptn)

def cs():
    global ptn
    ptn = str(round(math.sin(math.radians(float(ptn))),10))
    check_ptn()
    ptn_var.set(ptn)

def cc():
    global ptn
    ptn = str(round(math.cos(math.radians(float(ptn))),10))
    check_ptn()
    ptn_var.set(ptn)

def ct():
    global ptn
    ptn = str(round(math.tan(math.radians(float(ptn))),10))
    check_ptn()
    ptn_var.set(ptn)

def rd():
    global ptn
    ptn = str(round(float(ptn), 3))
    check_ptn()
    ptn_var.set(ptn)

def mcall():
    global mem
    global ptn
    ptn = mem
    check_ptn()
    ptn_var.set(ptn)

def mclear():
    global mem
    mem = 0.0

def mplus():
    global mem
    global ptn
    mem += float(ptn)

def mminus():
    global mem
    global ptn
    mem -= float(ptn)


window = Tk()
window.geometry('1250x800')
window.title('Calculator.io')
window.iconbitmap(bitmap='geo.ico')
window.maxsize(1250, 800)
window.minsize(1000,500)
window.configure(bg='PaleTurquoise')
ptn=0
cx = 560
cy = 275
lc = ''
temp = 0
mem = 0
txts = 'Arial 15'

Clear = Button(window, text='C', width=10, height=5, command=cls, font=txts)
Clear.place(x=cx, y=cy, anchor='center')

AC = Button(window, text='AC', width=10, height=5, command=clearance, font=txts)
AC.place(x=cx-150, y=cy, anchor='center')

pw = Button(window, text='^', width=10, height=5, command=pew, font=txts)
pw.place(x=cx-150, y=cy+100, anchor='center')

Sin = Button(window, text='sin', width=10, height=5, command=cs, font=txts)
Sin.place(x=cx-150, y=cy+200, anchor='center')

Cos = Button(window, text='cos', width=10, height=5, command=cc, font=txts)
Cos.place(x=cx-150, y=cy+300, anchor='center')

Tan = Button(window, text='tan', width=10, height=5, command=ct, font=txts)
Tan.place(x=cx-150, y=cy+400, anchor='center')

roundd = Button(window, text='round', width=10, height=5, command=rd, font=txts)
roundd.place(x=cx-300, y=cy, anchor='center')

m = Button(window, text='M', width=10, height=5, command=mcall, font=txts)
m.place(x=cx-300, y=cy+100, anchor='center')

mc = Button(window, text='MC', width=10, height=5, command=mclear, font=txts)
mc.place(x=cx-300, y=cy+200, anchor='center')

mp = Button(window, text='M+', width=10, height=5, command=mplus, font=txts)
mp.place(x=cx-300, y=cy+300, anchor='center')

mm = Button(window, text='M-', width=10, height=5, command=mminus, font=txts)
mm.place(x=cx-300, y=cy+400, anchor='center')

one = Button(window, text='1', width=10, height=5, command=n1, font=txts)
one.place(x=cx, y=cy+300, anchor='center')

two = Button(window, text='2', width=10, height=5, command=n2, font=txts)
two.place(x=cx+150, y=cy+300, anchor='center')

three = Button(window, text='3', width=10, height=5, command=n3, font=txts)
three.place(x=cx+300, y=cy+300, anchor='center')

four = Button(window, text='4', width=10, height=5, command=n4, font=txts)
four.place(x=cx, y=cy+200, anchor='center')

five = Button(window, text='5', width=10, height=5, command=n5, font=txts)
five.place(x=cx+150, y=cy+200, anchor='center')

six = Button(window, text='6', width=10, height=5, command=n6, font=txts)
six.place(x=cx+300, y=cy+200, anchor='center')

seven = Button(window, text='7', width=10, height=5, command=n7, font=txts)
seven.place(x=cx, y=cy+100, anchor='center')

eight = Button(window, text='8', width=10, height=5, command=n8, font=txts)
eight.place(x=cx+150, y=cy+100, anchor='center')

nine = Button(window, text='9', width=10, height=5, command=n9, font=txts)
nine.place(x=cx+300, y=cy+100, anchor='center')

zero = Button(window, text='0', width=26, height=5, command=n0, font=txts)
zero.place(x=cx+75, y=cy+400, anchor='center')

dot = Button(window, text='.', width=10, height=5, command=nd, font=txts)
dot.place(x=cx+300, y=cy+400, anchor='center')

divide = Button(window, text='÷', width=10, height=5, command=divd, font=txts)
divide.place(x=cx+450, y=cy, anchor='center')

multiply = Button(window, text='x', width=10, height=5, command=mult, font=txts)
multiply.place(x=cx+450, y=cy+100, anchor='center')

sub = Button(window, text='-', width=10, height=5, command=sb, font=txts)
sub.place(x=cx+450, y=cy+200, anchor='center')

add = Button(window, text='+', width=10, height=5, command=ad, font=txts)
add.place(x=cx+450, y=cy+300, anchor='center')

equal = Button(window, text='=', width=10, height=5, command=equ, font=txts)
equal.place(x=cx+450, y=cy+400, anchor='center')

percent = Button(window, text='%', width=10, height=5, command=pc, font=txts)
percent.place(x=cx+300, y=cy, anchor='center')

neg = Button(window, text='+/-', width=10, height=5, command=negt, font=txts)
neg.place(x=cx+150, y=cy, anchor='center')

ptn_var = StringVar()
ptn_var.set(ptn) 
output = Label(window, textvariable=ptn_var, bg='Turquoise', font=('Comfortaa', 40), width=100, height=4)
output.pack()

window.mainloop()


