
from tkinter import *
import math
import tkinter.messagebox
cal=Tk(className="pyhton examples - window color ")
image=PhotoImage(file='C:/Users/CZ3/Pictures/OOP PROJECT/cal.png')
cal.configure(bg="black")
cal.title("GUI SCIENTIFIC CALCULATOR")
display=Entry(cal,width=53,border=10,font="arial",bg="white",fg="black",justify=RIGHT,cursor="arrow")
display.grid(row=0,column=0,columnspan=6,padx=10,pady=20,ipady=18)
cal.resizable(width=False,height=False)
photo=PhotoImage(file="C:/Users/CZ3/Pictures/OOP PROJECT/cal.png")
expression=''
no=''
numb=''
# making calculator class
class calculator:
    def __init__(self):
        pass
    def rad(eslf,no):
        try:
            s=no*(3.14/180)
            return s
        except:
            tkinter.messagebox("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
    def clk(self,no):
        curr=display.get()
        display.delete(0,END)
        display.insert(0,str(curr)+str(no))
    def clear(self):
        display.delete(0,END)
    def equal(self):
        a=display.get()
        display.delete(0,END)
        if expression == "Add":
            try:
                display.insert(0,eval(a))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,a)
        if expression== "Mult":
            try:
                display.insert(0,eval(a))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,a)
        if expression== "Sub":
            try:
                display.insert(0,eval(a))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,eval(a))
        if expression== "Div":
            try:
                display.insert(0,eval(a))
            except ZeroDivisionError:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,a)
        if expression== "Pow":
            try:
                display.insert(0,eval(a))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,a)
        if expression== "Sq":
            try:
                display.insert(0,(eval(str(numb)+ str(math.sqrt(eval(a))))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,no)
        if expression== "fact":
            try:
                display.insert(0,eval(numb)+str(math.factorial(eval(a))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression== "Sin":
            a=eval(a)
            try:
                if a % 90==0:
                    display.insert(0,eval(numb)+str(int(math.sin(math.radians(a)))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression== "Cos":
            a=eval(a)
            try:
                if a%90 ==0:
                    display.insert(0,eval(numb)+str(math.cos(math.radians(a))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression == "Tan":
            a=eval(a)
            try:
                if a%90==0:
                    display.insert0,eval(numb)+str(math.tan(math.radians(a)))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression == "Sininv":
            try:
                display.insert(0,eval(numb) + str(math.degrees(math.asin(eval(a)))))
            except:
                 tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                 display.insert(0,numb)                
        if expression== "Cosinv":
            try:                 
                display.insert(0,eval(numb) +  str(math.degrees(math.acos(eval(a)))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression== "Taninv":
            try:
                display.insert(0,eval(numb) +str(math.degrees(math.acos(eval(a)))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression == "Log":
            try:
                display.insert(0,eval(numb)+str(math.log10(eval(a))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression== "Ln":
            try:
                display.insert(0,eval(numb)+str(math.log(eval(a))))       
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression == "RoundOff":
            try:
                display.insert(0,eval(numb)+str(round(eval(a))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb) 
        if expression== "RAD":
            try:
                display.insert(0,eval(numb)+str(math.radians(eval(a))))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,numb)
        if expression == "MOD":
            try:
                display.insert(0,eval(a))
            except:
                tkinter.messagebox.showerror("ERROR","OOPS ERRROR OCCURED KINDLY RE-ENTER OR CHECK YOUR VALUES AGAIN :)")
                display.insert(0,eval(a))
        if expression == "Remove":
            display.insert(0,math.degrees(math.atan(eval(a))))
    def add(self):
        numb=display.get()
        global no
        no=str(numb) + "+"
        display.delete(0,END)
        global expression
        expression= "Add"
        display.insert(0,no)
    def multiplication(self):
        numb=display.get()
        global no
        no = str(numb) + "*"
        display.delete(0,END)
        global expression
        expression="Mult"
        display.insert(0,no) 
    def substraction(self):
        numb=display.get()
        global no
        no=str(numb)+"-"
        display.delete(0,END)
        global expression
        expression="Sub"
        display.insert(0,no)
    def division(self):
        numb=display.get()
        global no
        no =str(numb) + "/"
        display.delete(0,END)
        global expression
        expression="Div"
        display.insert(0, str(no))
    def power(self):
        numb=display.get()
        global no
        no=str(numb)+"**"
        display.delete(0,END)
        global expression
        expression="Pow"
        display.insert(0,no)
    def square_root(self):
        no=display.get()
        global numb
        numb =str(no) 
        display.delete(0,END)
        global expression
        expression ="Sq"
        display.insert(0,math.sqrt(eval(numb)))
    def factorial(self):
        no=display.get()
        global numb
        numb =str(no) 
        display.delete(0,END)
        global expression
        expression="Fact"
        display.insert(0, math.factorial(eval(numb)))
    def sine(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="Sin"
        display.insert(0,math.sin(math.radians(eval(numb))))
    def cosine(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="Cos"
        display.insert(0,math.cos(math.radians(eval(numb))))
    def tangent(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="Tan"
        display.insert(0,math.tan(math.radians(eval(numb))))
    def sine_inverse(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="Sininv"
        display.insert(0,math.degrees(math.asin(eval(numb))))
    def cosine_inverse(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="Cosinv"
        display.insert(0,math.degrees(math.acos(eval(numb))))
    def tangent_inverse(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="Taninv"
        display.insert(0,math.degrees(math.atan(eval(numb))))
    def loagrithm(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="Log"
        display.insert(0,math.log10(eval(numb)))
    def pi(self):
        numb=display.get()
        display.delete(0,END)
        display.insert(0,eval(str(numb)+str(math.pi)))
    def round_off(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="RoundOff"
        display.insert(0,round(eval(numb)))
    def RADIAN(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="RAD"
    def natural_logarithm(self):
        no=display.get()
        global numb
        numb =str(no)
        display.delete(0,END)
        global expression
        expression="Ln"
        display.insert(0,math.log(eval(numb)))
    def EXPONENT(self):
        numb=display.get()
        display.delete(0,END)
        display.insert(0,eval(str(numb) + str(math.e)))    
    def MODULUS(self):
       numb=display.get()
       global expression
       expression="MOD"
       display.insert(numb,"%")
    def REMOVE(self):
        x=len(display.get())
        y= str(display.get())
        if y == '':
            display.insert(0,'')
        elif y==' ':
            display.insert(0,'')
        elif display=='':
            pass
        else:
            display.delete(0,END)
            display.insert(0,y[0:x-1])
sci=calculator()
btn_1=Button(cal, text="1",padx=43,  pady=20, bg="white", fg="black", font="5",command=lambda: sci.clk(1))
btn_1.grid(row=7, column=0)
btn_2=Button(cal, text="2",padx=43,  pady=20, bg="white", fg="black",font="5" ,command=lambda: sci.clk(2)) 
btn_2.grid(row=7, column=1)            
btn_3=Button(cal, text="3",padx=43,  pady=20, bg="white", fg="black",font="5",command=lambda: sci.clk(3))
btn_3.grid(row=7, column=2)
btn_4=Button(cal, text="4",padx=43,  pady=20, bg="white", fg="black",font="5",command=lambda: sci.clk(4))
btn_4.grid(row=6, column=0)
btn_5=Button(cal, text="5",padx=43,  pady=20, bg="white", fg="black",font="5",command=lambda: sci.clk(5))
btn_5.grid(row=6, column=1)
btn_6=Button(cal, text="6",padx=43,  pady=20, bg="white", fg="black",font="5",command=lambda: sci.clk(6))
btn_6.grid(row=6, column=2)
btn_7=Button(cal, text="7",padx=43,  pady=20, bg="white", fg="black",font="5",command=lambda: sci.clk(7))
btn_7.grid(row=5, column=0)
btn_8=Button(cal, text="8",padx=43,  pady=20, bg="white", fg="black",font="5",command=lambda: sci.clk(8))
btn_8.grid(row=5, column=1)
btn_9=Button(cal, text="9",padx=43,  pady=20, bg="white", fg="black",font="5",command=lambda: sci.clk(9))
btn_9.grid(row=5, column=2)
btn_0=Button(cal, text="0",padx=43,  pady=20, bg="white", fg="black",font="5",command=lambda: sci.clk(0))
btn_0.grid(row=8, column=0)
btn_point=Button(cal, text=".",padx=46,  pady=20, bg="white",font="2", fg="black",command=lambda: sci.clk("."))
btn_point.grid(row=8, column=1)
left_btn=Button(cal, text=")",padx=44,  pady=20, bg="white",font="5", fg="black",command=lambda: sci.clk(")"))
left_btn.grid(row=4, column=1)
right_btn=Button(cal, text="(",padx=45,  pady=20, bg="white",font="5", fg="black",command=lambda: sci.clk("("))
right_btn.grid(row=4, column=0)
EQUAL_btn=Button(cal, text="=",padx=54,  pady=20,font="5", bg="red", fg="white",command=sci.equal)
EQUAL_btn.grid(row=6, column=3)
CLEAR_btn=Button(cal, text="C",padx=58,  pady=20,font="5", bg="black", fg="white",command=sci.clear)
CLEAR_btn.grid(row=2, column=4)
#*********[MATH OPERATIONS]********
ADD_btn=Button(cal, text="+",padx =43,  pady=20, bg="white",font="5", fg="maroon",command=sci.add)
ADD_btn.grid(row=4, column=2)
SUB_btn=Button(cal, text="- ",padx =43,  pady=20, bg="white", fg="maroon",font="5",command=sci.substraction)
SUB_btn.grid(row=1, column=0)
MULT_btn=Button(cal, text="*",padx =45,  pady=20, bg="white", fg="maroon",font="5",command=sci.multiplication)
MULT_btn.grid(row=1, column=1)
DIV_btn=Button(cal, text="/",padx =45,  pady=20, bg="white", fg="maroon",font="5",command=sci.division)
DIV_btn.grid(row=1, column=2)
POW_btn=Button(cal, text="x^y ",padx=36,  pady=20, bg="white", fg="red",font="5",command=sci.power)
POW_btn.grid(row=2, column=0)
SQRT_btn=Button(cal, text=" √x",padx =37,  pady=20, bg="white", fg="red",font="5",command=sci.square_root)
SQRT_btn.grid(row=2, column=1)
FACT_btn=Button(cal, text="X!",padx =40,  pady=20,bg="white", fg="red",font="5",command=sci.factorial)
FACT_btn.grid(row=2, column=2)
SINE_btn=Button(cal, text="Sin", padx=47,  pady=20, bg="white", fg="red",font="5", command=sci.sine)
SINE_btn.grid(row=3, column=3)
COSINE_btn=Button(cal, text="Cos", padx=44,  pady=20, fg="red", bg="white",font="5", command=sci.cosine)
COSINE_btn.grid(row=4, column=3)
TANGENT_btn=Button(cal, text="Tan",padx=45,  pady=20, fg="red", bg="white",font="5", command=sci.tangent)
TANGENT_btn.grid(row=5, column=3)
SINE_INV_btn=Button(cal, text="Sin^-1",padx=42,  pady=20, fg="red", bg="white",font="5", command=sci.sine_inverse)
SINE_INV_btn.grid(row=3, column=4)
COSINE_INV_btn=Button(cal, text="Cos^-1",padx=40,  pady=20, fg="red", bg="white",font="5", command=sci.cosine_inverse)
COSINE_INV_btn.grid(row=4, column=4)
TANGENT_INV_btn=Button(cal, text="Tan^-1",padx=41,  pady=20, fg="red", bg="white",font="5", command=sci.tangent_inverse)
TANGENT_INV_btn.grid(row=5, column=4)
PI_btn=Button(cal, text="π", padx=59, pady=20, bg="white", fg="red",font="5", command=sci.pi)
PI_btn.grid(row=1, column=4)
LOG_btn=Button(cal, text=" Log", padx=43, pady=20, bg="white", fg="red",font="5", command=sci.loagrithm)
LOG_btn.grid(row=2, column=3)
ROUND_btn=Button(cal, text="Round", padx=36, pady=20, bg="white", fg="blue",font="5", command=sci.round_off)
ROUND_btn.grid(row=1, column=3)
RAD_btn=Button(cal, text="Rad", padx=49, pady=20, bg="white", fg="brown",font="5", command=sci.RADIAN)
RAD_btn.grid(row=6, column=4)
LN_btn=Button(cal, text="ln", padx=43, pady=20, bg="white", fg="red",font="5", command=sci.natural_logarithm)
LN_btn.grid(row=3, column=0)
MOD_btn=Button(cal, text="%", padx=41, pady=20, bg="white", fg="red",font="5", command=sci.MODULUS)
MOD_btn.grid(row=3, column=2)
EXPONENT_btn=Button(cal, text="e", padx=42, pady=20, bg="white", fg="red",font="5", command=sci.EXPONENT)
EXPONENT_btn.grid(row=3, column=1)
REM_btn=Button(cal, text="⌫", padx=47, pady=20, bg="yellow", fg="black",font="5", command=sci.REMOVE)
REM_btn.grid(row=7, column=3)
image= photo.subsample(6,9)
IMAGE_btn=Button(cal,state=DISABLED,image=image, height="63", width="136")
IMAGE_btn.grid(row=7, column=4)
text_btn=Button(cal,text="ℂ    𝔸   𝕊   𝕀    𝕆",bg="black",state=DISABLED, padx=144, pady=22)
text_btn.grid(row=8, column=2, columnspan=4)
cal.mainloop()