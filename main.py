def update():
    def update_all():
        print('updated')
    nameval = StringVar()
    salaryval = StringVar()
    areaval = StringVar()
    numberval = StringVar()
    bankval = StringVar()
    ifccodeval = StringVar()
    bnameval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    updateroot = Toplevel(master=dataframe)
    updateroot.title('fill the details of new members')
    updateroot.geometry('470x550+200+80')
    updateroot.grab_set()
    updateroot.resizable(False, False)
    updateroot.iconbitmap('download.ico')
    updateroot.config(bg="black")
    usernlabel = Label(updateroot, text="Name:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                       anchor='w')
    usernlabel.place(x=10, y=10)
    unumber = Label(updateroot, text="Number:", bg='white', font=('times', 20, 'bold'), fg='black', width=9, anchor='w')
    unumber.place(x=10, y=60)
    usalary = Label(updateroot, text="salary:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                    anchor='w')
    usalary.place(x=10, y=110)
    uarea = Label(updateroot, text="area:", bg='white', font=('times', 20, 'bold'), fg='black', width=9, anchor='w')
    uarea.place(x=10, y=160)
    unname = Label(updateroot, text="Bank Name:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                   anchor='w')
    unname.place(x=10, y=210)
    uaccount = Label(updateroot, text="account no:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                     anchor='w')
    uaccount.place(x=10, y=260)
    uifc = Label(updateroot, text="ifc", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                 anchor='w')
    uifc.place(x=10, y=310)
    date = Label(updateroot, text="date", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                 anchor='w')
    date.place(x=10, y=360)
    time = Label(updateroot, text="time", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                 anchor='w')
    time.place(x=10, y=410)
    submit = Button(updateroot, text='submit', bg='red', bd=5, width=20, font=('times', 20, 'bold'),
                    activebackground='white', activeforeground='yellow',command=update_all)
    submit.place(x=50, y=480)
    ###same
    namecc = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=nameval)
    namecc.place(x=180, y=10)
    numbercc = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=numberval)
    numbercc.place(x=180, y=60)
    salarycc = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=salaryval)
    salarycc.place(x=180, y=110)
    areacc = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=areaval)
    areacc.place(x=180, y=160)
    bnamecc = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=bnameval)
    bnamecc.place(x=180, y=210)
    bankcc = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=bankval)
    bankcc.place(x=180, y=260)
    ifcc = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=ifccodeval)
    ifcc.place(x=180, y=310)
    datecc = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=dateval)
    datecc.place(x=180, y=360)
    timeup = Entry(updateroot, font=('roman', 20, 'bold'), bd=5, textvariable=timeval)
    timeup.place(x=180, y=410)
##############################################################################################
def intro():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ' '
        sliderlabel.config(text=text)
    else:
        text = text+ss[count]
        sliderlabel.config(text=text)
    count += 1
    sliderlabel.after(200,intro)
    ########################################################################################
def search():
    def subsearch():
        print('search')
    nameval = StringVar()
    salaryval = StringVar()
    areaval = StringVar()
    numberval = StringVar()
    bankval = StringVar()
    ifccodeval = StringVar()
    bnameval = StringVar()
    dateval = StringVar()
    serachroot = Toplevel(master=dataframe)
    serachroot.title('fill the details of new members')
    serachroot.geometry('470x500+200+80')
    serachroot.grab_set()
    serachroot.resizable(False, False)
    serachroot.iconbitmap('download.ico')
    serachroot.config(bg="black")
    usernlabel = Label(serachroot, text="Name:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                       anchor='w')
    usernlabel.place(x=10, y=10)
    unumber = Label(serachroot, text="Number:", bg='white', font=('times', 20, 'bold'), fg='black', width=9, anchor='w')
    unumber.place(x=10, y=60)
    usalary = Label(serachroot, text="salary:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                    anchor='w')
    usalary.place(x=10, y=110)
    uarea = Label(serachroot, text="area:", bg='white', font=('times', 20, 'bold'), fg='black', width=9, anchor='w')
    uarea.place(x=10, y=160)
    unname = Label(serachroot, text="Bank Name:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                   anchor='w')
    unname.place(x=10, y=210)
    uaccount = Label(serachroot, text="account no:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                     anchor='w')
    uaccount.place(x=10, y=260)
    uifc = Label(serachroot, text="ifc", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                 anchor='w')
    uifc.place(x=10, y=310)
    date = Label(serachroot, text="date", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                 anchor='w')
    date.place(x=10, y=360)
    submit = Button(serachroot, text='submit', bg='red', bd=5, width=20, font=('times', 20, 'bold'),
                    activebackground='white', activeforeground='yellow',command=subsearch)
    submit.place(x=50, y=430)
    ###same
    namecc = Entry(serachroot, font=('roman', 20, 'bold'), bd=5, textvariable=nameval)
    namecc.place(x=180, y=10)
    numbercc = Entry(serachroot, font=('roman', 20, 'bold'), bd=5, textvariable=numberval)
    numbercc.place(x=180, y=60)
    salarycc = Entry(serachroot, font=('roman', 20, 'bold'), bd=5, textvariable=salaryval)
    salarycc.place(x=180, y=110)
    areacc = Entry(serachroot, font=('roman', 20, 'bold'), bd=5, textvariable=areaval)
    areacc.place(x=180, y=160)
    bnamecc = Entry(serachroot, font=('roman', 20, 'bold'), bd=5, textvariable=bnameval)
    bnamecc.place(x=180, y=210)
    bankcc = Entry(serachroot, font=('roman', 20, 'bold'), bd=5, textvariable=bankval)
    bankcc.place(x=180, y=260)
    ifcc = Entry(serachroot, font=('roman', 20, 'bold'), bd=5, textvariable=ifccodeval)
    ifcc.place(x=180, y=310)
    datecc = Entry(serachroot, font=('roman', 20, 'bold'), bd=5, textvariable=dateval)
    datecc.place(x=180, y=360)
###############################################################
def newone():


    def submm():
        accountno = bankval.get()
        name = nameval.get()
        number = numberval.get()
        salary = salaryval.get()
        area = areaval.get()
        bank_name = bnameval.get()
        ifc = ifccodeval.get()
        addeddate = time.strftime('%d/%m/%Y')
        addedtime = time.strftime('%H:%M:%S')
        print(accountno, name, number, salary,area, bank_name,ifc, addeddate, addedtime)

        try:
            strr = 'insert into studentdata1 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (accountno, name, number, salary, area, bank_name, ifc, addeddate, addedtime))
            com.commit()
            resclear = messagebox.askyesnocancel('notifications','Bank {} Name {} added sucessfully...and want to clean form'.format(accountno,name), parent=noroot)
            if(resclear == True):
                nameval.set('')
                salaryval.set('')
                areaval.set('')
                numberval.set('')
                bankval.set('')
                ifccodeval.set('')
                bnameval.set('')
        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=noroot)

    noroot = Toplevel(master=dataframe)
    noroot.title('fill the details of new members')
    noroot.geometry('470x470+200+80')
    noroot.grab_set()
    noroot.resizable(False, False)

    noroot.config(bg="black")
    usernlabel = Label(noroot, text="account number:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                       anchor='w')
    usernlabel.place(x=10, y=10)
    unumber = Label(noroot, text="Name:", bg='white', font=('times', 20, 'bold'), fg='black', width=9, anchor='w')
    unumber.place(x=10, y=60)
    usalary = Label(noroot, text="Number:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                    anchor='w')
    usalary.place(x=10, y=110)
    uarea = Label(noroot, text="Salary:", bg='white', font=('times', 20, 'bold'), fg='black', width=9, anchor='w')
    uarea.place(x=10, y=160)
    unname = Label(noroot, text="Area:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                   anchor='w')
    unname.place(x=10, y=210)
    uaccount = Label(noroot, text="bank name:", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                     anchor='w')
    uaccount.place(x=10, y=260)
    uifc = Label(noroot, text="ifc", bg='white', font=('times', 20, 'bold'), fg='black', width=9,
                 anchor='w')
    uifc.place(x=10, y=310)
    submit = Button(noroot, text='submit', bg='red', bd=5, width=20, font=('times', 20, 'bold'),
                    activebackground='white', activeforeground='yellow',command=submm)
    submit.place(x=50, y=380)
    ###same
    nameval = StringVar()
    salaryval = StringVar()
    areaval = StringVar()
    numberval = StringVar()
    bankval = StringVar()
    ifccodeval = StringVar()
    bnameval = StringVar()
    nameccc = Entry(noroot, font=('roman', 20, 'bold'), bd=5, textvariable=bankval)
    nameccc.place(x=180, y=10)
    numberccc = Entry(noroot, font=('roman', 20, 'bold'), bd=5, textvariable=nameval)
    numberccc.place(x=180, y=60)
    salaryccc = Entry(noroot, font=('roman', 20, 'bold'), bd=5, textvariable=numberval)
    salaryccc.place(x=180, y=110)
    areaccc = Entry(noroot, font=('roman', 20, 'bold'), bd=5, textvariable=salaryval)
    areaccc.place(x=180, y=160)
    bnameccc = Entry(noroot, font=('roman', 20, 'bold'), bd=5, textvariable=areaval)
    bnameccc.place(x=180, y=210)
    bankccc = Entry(noroot, font=('roman', 20, 'bold'), bd=5, textvariable=bnameval)
    bankccc.place(x=180, y=260)
    ifccc = Entry(noroot, font=('roman', 20, 'bold'), bd=5, textvariable=ifccodeval)
    ifccc.place(x=180, y=310)

    noroot.mainloop()

    #############################u########################################
def exitapp():
    res = messagebox.askyesno('notification','do you really want to exit')
    if(res == True):
        root.destroy()
###########################################################################################

def connectdb():
    def submitdb():
        global com, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            com = pymysql.connect(host=host,user=user,password=password)
            mycursor = com.cursor()
        except:
            messagebox.showerror("notification","incorrect data")
            return
        try:
            strr = 'create database studentmanagmentsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagmentsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata1(accountno int, name varchar(20), number int, salary int,area varchar(100), bank_name varchar(20), ifc varchar(20), date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column accountno int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column accountno int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('congo','now db created and you are connect to database',parent=dbroot)

        except:
            strr = 'use studentmanagmentsystem'
            mycursor.execute(strr)
            messagebox.showinfo('congo', 'now you are connect to database', parent=dbroot)


    dbroot = Toplevel()
    dbroot.title('database connrctivety')
    dbroot.geometry('600x300+200+100')
    dbroot.grab_set()
    dbroot.resizable(False,False)
    dbroot.iconbitmap('download.ico')
    dbroot.config(bg="black")
    dblabel = Label(dbroot,text="enter host:",bg='white',font=('times',20,'bold'),fg='black',width=13,anchor='w')
    dblabel.place(x=10,y=10)
    dbuser = Label(dbroot, text="enter user:", bg='white', font=('times', 20, 'bold'),fg='black',width=13,anchor='w')
    dbuser.place(x=10, y=60)
    dbps = Label(dbroot, text="enter password:", bg='white', font=('times', 20, 'bold'),fg='black',width=13,anchor='w')
    dbps.place(x=10, y=110)
    dbhelp = Label(dbroot,text='for help contact on 8080206053',bg='black',font=('times',20,'bold'),fg='blue',anchor='w')
    dbhelp.place(x=10,y=260)
    ########################################################
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    ehroot = Entry(dbroot,font=('roman',20,'bold'),bd=5,textvariable=hostval)
    ehroot.place(x= 250,y=10)
    euroot = Entry(dbroot, font=('roman', 20, 'bold'),bd=5,textvariable=userval)
    euroot.place(x=250, y=60)
    eproot = Entry(dbroot, font=('roman', 20, 'bold'),bd=5,textvariable=passwordval)
    eproot.place(x=250, y=110)
    submit = Button(dbroot,text='submit',bg='red',bd=5,width=20,font=('times',20,'bold'),activebackground='white',activeforeground='yellow',command=submitdb)
    submit.place(x=130,y=180)

    dbroot.mainloop()

def colourslider():
    fg = random.choice(colours)
    sliderlabel.config(fg=fg)
    sliderlabel.after(20,colourslider)

def timer():
    time_c =time.strftime('%H:%M:%S')
    date_c = time.strftime('%d/%M/%Y')
    clocklabel.config(text="time :"+time_c+ "\n"+"date :" +date_c)
    clocklabel.after(100,timer)

from tkinter import *
import random
import pymysql
import time
from tkinter.ttk import Treeview
from tkinter import ttk
from tkinter import Toplevel,messagebox
root =Tk()
root.title("student management system")
root.config(bg="gold2")
root.geometry('1170x650+40+10')
root.iconbitmap('download.ico')
root.resizable(False,False)
ss = 'welcome to portal'
count = 0
text = ''
colours = ['red','yellow','gold2','black']
#####frames
dataframe = Frame(root,bg='gold',relief="sunken",borderwidth=5)
dataframe.place(x=10,y=100,width=450,height=500)
headline = Label(dataframe,text='-----------opretion------------',bg='gold2',font=('arial',20,'italic bold'),width=25)
headline.pack(side=TOP,expand=True)
add = Button(dataframe,text='1.addtion',bg='white',font=('arial',20,'bold'),bd=5,fg='black',width=15,activebackground='black',activeforeground='white',command=newone)
add.pack(side=TOP,expand=True)
search = Button(dataframe,text='2.search',bg='white',font=('arial',20,'bold'),bd=5,fg='black',width=15,activebackground='black',activeforeground='white',command=search)
search.pack(side=TOP,expand=True)
delete = Button(dataframe,text='3.delete',bg='white',font=('arial',20,'bold'),bd=5,fg='black',width=15,activebackground='black',activeforeground='white')
delete.pack(side=TOP,expand=True)
update = Button(dataframe,text='4.update',bg='white',font=('arial',20,'bold'),bd=5,fg='black',width=15,activebackground='black',activeforeground='white',command=update)
update.pack(side=TOP,expand=True)
show = Button(dataframe,text='5.show',bg='white',font=('arial',20,'bold'),bd=5,fg='black',width=15,activebackground='black',activeforeground='white')
show.pack(side=TOP,expand=True)
export = Button(dataframe,text='6.export',bg='white',font=('arial',20,'bold'),bd=5,fg='black',width=15,activebackground='black',activeforeground='white')
export.pack(side=TOP,expand=True)
exit = Button(dataframe,text='7.exit',bg='white',font=('arial',20,'bold'),bd=5,fg='black',width=15,activebackground='black',activeforeground='white',command=exitapp)
exit.pack(side=TOP,expand=True)
###############################################################
showdata  = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
showdata.place(x=500,y=100,width=460,height=500)
style = ttk.Style()
style.configure('Treeview.Heading',font=('roman',10,'bold'),fg='orange')
axisx = Scrollbar(showdata,orient=HORIZONTAL)
axisy = Scrollbar(showdata,orient=VERTICAL)
showdetail = Treeview(showdata,columns=('name','number','bank name','accountno','ifc','date','time','area','salary'),yscrollcommand=axisy.set,xscrollcommand=axisx.set)
axisx.pack(side=BOTTOM,fill=X)
axisy.pack(side=RIGHT,fill=Y)
axisx.config(command=showdetail.xview)
axisy.config(command=showdetail.yview)
showdetail.heading('name',text='name')
showdetail.heading('number',text='mobile no:')
showdetail.heading('bank name',text='bank name')
showdetail.heading('accountno',text='account no:')
showdetail.heading('ifc',text='ifc code')
showdetail.heading('date',text='date')
showdetail.heading('time',text='time')
showdetail.heading('area',text='area')
showdetail.heading('salary',text='salary')
showdetail['show'] = 'headings'
showdetail.column('name',width=100)
showdetail.pack(fill=BOTH,expand=1)
##########################################################,##########
sliderlabel = Label(root,bg='blue',text=ss,font=('chiller',30,'italic bold'),width=35,borderwidth=5)
sliderlabel.place(x=280,y=0)
clocklabel = Label(root,bg='green',font=('times',10,'bold'),width=15,borderwidth=5)
clocklabel.place(x=0,y=0)
db = Button(root,bg="green",text='connect to db',width=12,relief=RIDGE,font=('chiller',20,'italic bold'),activebackground='white',activeforeground='yellow',command=connectdb)
db.place(x=1000,y=0)
intro()
timer()
colourslider()
root.mainloop()
