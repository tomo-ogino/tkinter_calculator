import tkinter as tk
import tkinter.font as font
import tkinter.ttk as ttk
import lib.calc as cal

class Frame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.create_display(0,0)
        self.createbutton_num(1,0)
        self.createbutton_ope(1,3)
    
    def create_display(self, argr, argc):
        d_font = font.Font(family="System",size=12,weight="bold")
        r = argr
        c = argc
        labelframe = tk.LabelFrame(bd=2,relief="ridge",text="計算結果")
        labelframe.grid(row=r, column=c, columnspan=4)
        label = tk.Label(labelframe,text=0,font = d_font, width=60,height=3)
        label.grid(row=r, column=c, columnspan=4)
        
    #数字ボタン作成
    def createbutton_num(self, argr, argc):
        n_font = font.Font(family="System",size=10,weight="bold")
        num = ((7,8,9),(4,5,6),(1,2,3))
        r = 0
        gridr = argr
        while r < len(num):
            nu = num[r]
            c = 0
            gridc = argc
            while c < len(nu):
                button = tk.Button(text=str(num[r][c]),font=n_font,width=10,height=3)
                button.grid(row=(gridr) ,column=(gridc) ,padx=20,pady=20)
                c += 1   
                gridc += 1
            r += 1
            gridr += 1
        button = tk.Button(text=0,font=n_font,width=26,height=3)
        button.grid(row=gridr,column=argc,columnspan=2,padx=20,pady=20)
        button = tk.Button(text="c",font=n_font,width=12,height=3)
        button.grid(row=gridr,column=argc + 2,columnspan=1,padx=20,pady=20)

    #演算子ボタン作成
    def createbutton_ope(self, argr, argc):
        o_font = font.Font(family="System",size=10,weight="bold")
        ope = ("÷","×","-","+")
        r = 0
        gridr = argr
        c = 0
        gridc = argc
        while r < len(ope):
            button = tk.Button(text=ope[r],font=o_font,width=10,height=3)
            button.grid(row=gridr,column=gridc, padx=20,pady=20)
            r += 1
            gridr += 1           

if __name__ == '__main__':
  root = tk.Tk()
  root.title("calculator")
  root.geometry("600x600")
  app = Frame(root)
  root.mainloop()