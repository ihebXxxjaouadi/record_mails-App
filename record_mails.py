import tkinter
from tkinter import *
from tkinter import messagebox
import os

form=Tk()
form.config(bg='#ffffff')
form.title ('program of record @mails')
class management:
    def __init__(self):
        self.ctreate_labels()
        self.ctreate_Entry()
        self.ctreate_buttons()

    def ctreate_labels(self):
        self.lbl=Label(form,text= 'name    :',font='consoalas 12 bold',bg='#ffffff').grid(row=0,column=0,sticky='NWNESWSE')
        self.lbl=Label(form,text= 'social_media:',font='consoalas 12 bold',bg='#ffffff').grid(row=1,column=0,sticky='NWNESWSE')        
        self.lbl=Label(form,text= '@mail   :',font='consoalas 12 bold',bg='#ffffff').grid(row=2,column=0,sticky='NWNESWSE')
        self.lbl=Label(form,text='PassWord:',font='consoalas 12 bold',bg='#ffffff').grid(row=3,column=0,sticky='NWNESWSE')
        self.txt=Label(form,text='MADE it By IHEB>>>original<<<',font='consoalas 6 bold',bg='#ffffff').grid(row=4,column=1,sticky='NWNESWSE')

    def ctreate_Entry(self):
        global l1
        global l2
        global n
        global lm
        l1=StringVar()
        l2=StringVar()
        n=StringVar()
        lm=StringVar()
        self.ent0=Entry(form,borderwidth=1,font='consoalas 10 bold',textvariable=n)
        self.ent0.grid(row=0,column=1)
        self.entm=Entry(form,borderwidth=1,font='consoalas 10 bold',textvariable=lm)
        self.entm.grid(row=1,column=1)        
        self.ent1=Entry(form,borderwidth=1,font='consoalas 10 bold',textvariable=l1)
        self.ent1.grid(row=2,column=1)
        self.ent2=Entry(form,show='*',borderwidth=1,font='consoalas 10 bold',textvariable=l2)
        self.ent2.grid(row=3,column=1)
    def ctreate_buttons(self):
        self.b=Button(form,text='OK',font='arial 10 bold',command=self.save).grid(row=3,column=2)
    def save(self):
        if n.get().strip()=='':messagebox.showerror('error','the name is invalid');self.ent0.focus()
        elif lm.get().strip()=='': messagebox.showerror('error','the social_media is invalid');self.entm.focus()        
        elif l1.get().strip()=='': messagebox.showerror('error','the adress is invalid');self.ent1.focus()
        elif l2.get()=='': messagebox.showerror('error','the password is invalid');self.ent2.focus()
        else:
            try: 
                os.makedirs("records")
            except: 
                pass
            name=n.get()+'.txt'
            self.f=open('records/'+name,'w')
            name=n.get()
            social_media=lm.get()
            adresse=l1.get()
            password=l2.get()
            self.f.write('\nthe name IS: ' + name)            
            self.f.write('\nthe social_media IS: ' + social_media)            
            self.f.write('\nthe adresse of your mail IS:'+adresse)
            self.f.write('\nthe password IS: ' + password)
            self.f.close()
            messagebox.showinfo('valid',n.get()+' your @mail is record succefuly (;')
            
            self.ent0.delete(0, last=END)
            self.entm.delete(0, last=END)
            self.ent1.delete(0, last=END)
            self.ent2.delete(0, last=END)
            self.ent0.focus()
            
            
        
mg=management()
form.mainloop()
