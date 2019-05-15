import main
import config
from tkinter import *
from tkinter import scrolledtext
from tkinter import END
from model import tf

root = Tk()
root.geometry('500x300')
root.title('宋词生成器')
frm_UP = Frame(root)

Label(frm_UP,text='请输入词牌名:').pack(side =LEFT)
var = StringVar()
line = Entry(frm_UP,textvariable=var)
line.pack(side = LEFT)
text = scrolledtext.ScrolledText(root,width= 68,height=20)
text.pack(side=BOTTOM)



list = ['水调歌头','满江红','沁园春','贺新郎']

def nanshou():
    print(var.get())
def hello():
    print(1)
    text.delete(1.0, END)  # 使用 delete
    text.edit_reset()
    text.pack()
    m1 = main
    st = line.get()
    if st in list:
        s1 = "D:/Download/Chinese_poem_generator-master/dataset/songci/"+st+".txt"
        s ="D:/Download/Chinese_poem_generator-master/checkpoints/" + st
        m1.main(s1,s)
        p = main.main_Get_str()
        print('-----------------')
        print(p)
        print('-----------------')
        text.insert(END,p)
        tf.reset_default_graph()
    else:
        text.insert(END,'对不起，机器较差，还没有来得及训练'+st+'词牌名'+'\n')
Button(frm_UP,text='生成',command=hello).pack(side= RIGHT)
frm_UP.pack(side = TOP)

root.mainloop()



