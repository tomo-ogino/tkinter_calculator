
import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
from lib.calc import *


class Tk_Frame(ttk.Frame):
    def __init__(self, master=None, num="0", **kwargs):
        super().__init__(master, **kwargs)
        self.display = tk.StringVar()
        self.display.set(num)
        self.create_display(num,0,0)
        self.createbutton_num(1,0)
        self.createbutton_ope(1,3)

    #ディスプレイ作成
    def create_display(self, num, r, c):
        d_font = font.Font(family="System",size=12,weight="bold")
        #labelframe = tk.LabelFrame(bd=2,relief="ridge",text="calculate result")
        #labelframe.grid(row=r, column=c, columnspan=4)
        
        
        self.label = tk.Label(root,textvariable=self.display, font = d_font, width=60,height=3)
        self.label.grid(row=r, column=c, columnspan=4)
        
    #数字ボタン作成
    def createbutton_num(self, argr, argc):
        n_font = font.Font(family="System",size=10,weight="bold")
        num = ((7,8,9),(4,5,6),(1,2,3))
        for r in range(0,3):
            for c in range(0,3):
                n = str(num[r][c])
                button = tk.Button(root,text=n,font=n_font,width=10,height=3,command=Push(n,"num"))
                button.grid(row=(r + argr) ,column=(c + argc) ,padx=20,pady=20)
        
        #0
        button = tk.Button(root, text=0,font=n_font,width=26,height=3, command=Push("0","num"))
        button.grid(row=argr+3,column=argc,columnspan=2,padx=20,pady=20)

        #C（クリア）
        button = tk.Button(root, text="c",font=n_font,width=12,height=3, command=Push("C","ope"))
        button.grid(row=argr+3,column=argc + 2, columnspan=1,padx=20,pady=20)
    
    #演算子ボタン作成
    def createbutton_ope(self, argr, argc):
        o_font = font.Font(family="System",size=10,weight="bold")
        ope = ("÷","×","-","+")
        for r in range(0, len(ope)):
            button = tk.Button(root, text=ope[r],font=o_font,width=10,height=3,command=Push(ope[r],"ope"))
            button.grid(row=r + argr,column=argc, padx=20,pady=20)

#Labelクラス
class Label:
    def __init__(self, name):
        self.name = name
    def __call__(self, event=None):
        pass

#Pushクラス(Frameクラス継承)
class Push(Tk_Frame):
    #ボタン名とアクションをセット
    def __init__(self, str, action):
        self.name = str
        self.action = action
    #コンストラクタでセットしたアクションを実行
    def __call__(self,event=None):
        if self.action == "ope":
            print("クリア")
        else:
            self.append_num()
    
    def append_num(self):
        #super().create_display(super().var().get()+self.name,0,0)
        self.display.set("aaa")

if __name__ == '__main__':
  root = tk.Tk()
  root.title("calculator")
  root.geometry("600x600")
  app = Tk_Frame(root)
  root.mainloop()