from tkinter import *
from tkinter import ttk
import cx_Oracle


class Info:
    def __init__(self,master,logo):
        self.frame = Frame(master,height=1000, width=1000)
        self.frame.pack(fill=BOTH, expand='true')
        self.frame.config(background='orange')
        self.label = Label(self.frame, image=logo)
        self.label.grid(row=0, column=0, rowspan=20)
        self.l = Label(self.frame)
        self.l.grid(row=0, column=1, columnspan=10)

        self.l1 = Label(self.frame, text="""A Warm Welcome to all the members and visitors of Lion's Club.
                 \nClub's Motto:\nOur Club provides the members and visitors with the number of services \nwhich helps them to rejuvenate from the daily workload.
                 \nServices    \t\tNormal  \t\t\tPremium\n\t\t\t(Cost for 1 month)\t(Cost for 3 months)
                 \n1.Pool\t\t\t\t800\t\t\t2200\n2.Carrom\t\t\t400\t\t\t1000\n3.Bowling\t\t\t500\t\t\t1200\n4.Swimming\t\t\t1000\t\t\t2800\n5.Amphitheatre\t\t\t600\t\t\t1600\n6.Zumba\t\t\t\t500\t\t\t1300
                 \nBased on type of Membership:\n::For normal and premium members all the services are available \nagainst cost per service.
                 \n::Normal members have to pay for period of 1 month whereas the premium members\nwill have to pay for 3 months for which they will get price benefits as shown above.
                 \n::Also for premium members, the club visiting timimgs will be more flexible\ncompared to normal members.
                 \n\nFor more information visit at our place.
                 \nPlease register with your basic information on our official Lion's Club Page.""", bg='orange',
                        font=('Courier', 12, 'bold'), anchor=NW, justify=LEFT)
        self.l1.grid(row=0, column=1)
class Login:
    def __init__(self,master,logo,username):
        self.frame = Frame(master, height=600, width=600)
        self.frame.pack(fill=BOTH, expand='true')
        self.frame.config(background='orange')
        self.label = Label(self.frame, image=logo)
        self.label.grid(row=0, column=0, rowspan=10)
        self.label2 = Label(self.frame, text='Hi '+username+',Welcome to Lion\'s club', font=('Courier', 12, 'bold'), bg='orange')
        self.label2.grid(row=0,column=1,rowspan=2,columnspan=3,sticky=W)
        self.label3 = Label(self.frame, text='Your account\'s information is as follows: ', font=('Courier', 12, 'bold'), bg='orange')
        self.label3.grid(row=1,column=1,columnspan=3,sticky=W)
        connection = cx_Oracle.connect('system/oracle@localhost:1521/xe')
        cursor = connection.cursor()
        query="select * from myproject2 where name='"+username+"'"
        cursor.execute(query)
        # query2 = "commit work"
        # cursor.execute(query2)
        list1=cursor.fetchall()
        #(name varchar(50),email varchar(50),password varchar(50),phone number,service varchar(50),type varchar(50)

        self.label4 = Label(self.frame, text='Name\nEmail ID\nPhone no.\nServices\nUser type ' ,
                            font=('Courier', 12, 'bold'), bg='orange', anchor=NW,justify=LEFT)
        self.label4.grid(row=2, column=1)
        self.label5 = Label(self.frame, text=str(list1[0][0])+"\n"+str(list1[0][1])+"\n"+str(list1[0][3])+"\n"+str(list1[0][4])+"\n"+str(list1[0][5]),
                            font=('Courier', 12, 'bold'), bg='orange',justify=LEFT)
        self.label5.grid(row=2, column=2)
class BeALion:
    def __init__(self,master,logo):
        self.frame = Frame(master,height=600, width=600)
        self.frame.pack(fill=BOTH, expand='true')
        self.frame.config(background='orange')
        self.label = Label(self.frame,image=logo)
        self.label.grid(row=0, column=0, rowspan=10)
        self.label2 = Label(self.frame, text='Registration ', font=('Courier', 18, 'bold'), bg='orange')
        self.label2.grid(row=0, column=1, columnspan=20)
        self.label3 = Label(self.frame, text='Name', font=('Courier', 12, 'bold'), bg='orange',justify=LEFT)
        self.entry = Entry(self.frame)
        self.entry.grid(row=1, column=2,sticky=W,ipadx=10)
        self.label3.grid(row=1, column=1,sticky=W,ipadx=10)
        self.label3 = Label(self.frame, text='Email id', font=('Courier', 12, 'bold'), bg='orange')
        self.label3.grid(row=2, column=1,sticky=W,ipadx=10)
        self.entry2 = Entry(self.frame)
        self.entry2.grid(row=2, column=2,sticky=W,ipadx=10)
        self.l3 = Label(self.frame, text="Password ", font=('Courier', 12, 'bold'), bg="orange")
        self.l3.grid(row=3, column=1,sticky=W,ipadx=10)
        self.entry3 = Entry(self.frame,show='*')
        self.entry3.grid(row=3, column=2,sticky=W,ipadx=10)
        self.l3 = Label(self.frame, text="Phone no. ", font=('Courier', 12, 'bold'), bg="orange")
        self.l3.grid(row=4, column=1,sticky=W,ipadx=10)
        self.entry4 = Entry(self.frame)
        self.entry4.grid(row=4, column=2,sticky=W,ipadx=10)
        self.l3 = Label(self.frame, text="Select the event you wish to have ", font=('Courier', 12, 'bold'), bg="orange")
        self.l3.grid(row=5, column=1,columnspan=2)
        self.var1=IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7=StringVar()

        self.c1 = Checkbutton(self.frame, text="Pool", bg="orange",variable=self.var1)
        self.c1.grid(row=6, column=1,sticky=W)
        self.c2 = Checkbutton(self.frame, text="Carrom", bg="orange",variable=self.var2)
        self.c2.grid(row=6, column=2,sticky=W)
        self.c3 = Checkbutton(self.frame, text="Bowling", bg="orange",variable=self.var3)
        self.c3.grid(row=6, column=3,sticky=W)
        self.c5 = Checkbutton(self.frame, text="Swimming", bg="orange",variable=self.var4)
        self.c5.grid(row=7, column=1,sticky=W)
        self.c6 = Checkbutton(self.frame, text="Amphitheatre", bg="orange",variable=self.var5)
        self.c6.grid(row=7, column=2,sticky=W)
        self.c7 = Checkbutton(self.frame, text="Zumba", bg="orange",variable=self.var6)
        self.c7.grid(row=7, column=3,sticky=W)
        self.l3 = Label(self.frame, text="Select user type", font=('Courier', 12, 'bold'),bg="orange")
        self.l3.grid(row=8, column=1, columnspan=2,sticky=W)
        self.r1 = Radiobutton(self.frame, text="Normal", value="Normal", bg="orange",variable=self.var7)
        self.r1.grid(row=9, column=1,sticky=W)
        self.r2 = Radiobutton(self.frame, text="Premium", value="Premium", bg="orange",variable=self.var7)
        self.r2.grid(row=9, column=2,sticky=W)
        self.button2 = ttk.Button(self.frame, text='Submit')
        self.button2.grid(row=10, column=2,sticky=W)
        self.button2.bind("<Button-1>",self.database)


    def database(self,event):
        connection = cx_Oracle.connect('system/oracle@localhost:1521/xe')
        cursor = connection.cursor()
        str1=""
        if(self.var1.get()==1):
            str1=str1+" "+self.c1.cget("text")
        if (self.var2.get() == 1):
            str1 = str1 +" "+ self.c2.cget("text")
        if (self.var3.get() == 1):
            str1 = str1 +" "+ self.c3.cget("text")
        if (self.var4.get() == 1):
            str1 = str1 +" "+ self.c5.cget("text")
        if (self.var5.get() == 1):
            str1 = str1 +" "+ self.c6.cget("text")
        if (self.var6.get() == 1):
            str1 = str1 +" "+ self.c7.cget("text")
        str2=self.var7.get()
        #(name varchar(50),email varchar(50),password varchar(50),phone number,service varchar(50),type varchar(50)
        #query0 = "insert into myproject values('Omkar','omkardalvi','omkar1234',12345,'cool cool','premium')"

        query0 = "insert into myproject2 values('"+self.entry.get()+"','"+self.entry2.get()+"','"+self.entry3.get()+"',"+self.entry4.get()+",'"+str1+"','"+str2+"')"
        cursor.execute(query0)
        query = "select * from myproject2"
        cursor.execute(query)
        print(cursor.fetchall())
        query2 = "commit work"
        cursor.execute(query2)
        self.l1 = Label(self.frame, text=self.entry.get()+" added", font=('Courier', 12, 'bold'), bg="orange")
        self.l1.grid(row=11, column=1,sticky=W)
class MyProject:
    def __init__(self,master):
        self.frame=Frame(master,height=600,width=700)
        self.frame.pack(fill=BOTH,expand='true')
        self.frame.config(background='orange')
        self.logo=PhotoImage(file='reallion.png')
        self.small_logo=self.logo.subsample(1,1)
        self.label=Label(self.frame,image=self.small_logo)
        self.label.grid(row=0,column=0,rowspan=10)

        self.label2 = Label(self.frame,text='Welcome to Lion\'s Club ', font=('Courier', 18, 'bold'),bg='orange')
        self.label2.grid(row=0,column=1,columnspan=10)
        self.label3=Label(self.frame,text='Username',font=('Courier', 12, 'bold'),bg='orange')
        self.entry=Entry(self.frame)
        self.entry.grid(row=1,column=2)
        self.label3.grid(row=1,column=1)
        self.label3=Label(self.frame,text='Password',font=('Courier', 12, 'bold'),bg='orange')
        self.label3.grid(row=2,column=1)
        self.entry2=Entry(self.frame,show='*')
        self.entry2.grid(row=2,column=2)


        self.button=ttk.Button(self.frame,text='Be a Lion!!',command=self.beALion)
        self.button.grid(row=4,column=1)
        self.button3=ttk.Button(self.frame,text='Login',command=self.login)
        self.button3.grid(row=3,column=1)
        self.button2 = ttk.Button(self.frame, text='Know more!!',command=self.info)
        self.button2.grid(row=4,column=2)

    def beALion(self):
        root1=Toplevel()
        root1.wm_geometry("950x550")
        b=BeALion(root1,self.logo)
    def login(self):
        connection = cx_Oracle.connect('system/oracle@localhost:1521/xe')
        cursor = connection.cursor()
        query="select * from myproject2 where name='"+self.entry.get()+"' and password='"+self.entry2.get()+"'"
        cursor.execute(query)
        # query2 = "commit work"
        # cursor.execute(query2)
        if(cursor.fetchall()==[]):
            self.label4 = Label(self.frame, text='Invalid credentials!\nClick on Be a Lion!! for registration.', font=('Courier', 12, 'bold'), bg='orange',anchor=W,justify=LEFT)
            self.label4.grid(row=5,column=1,columnspan=3)

        else:

            root2=Toplevel()
            root2.wm_geometry("1000x550")
            b=Login(root2,self.logo,self.entry.get())
    def info(self):
        root3=Toplevel()
        root3.wm_geometry("1350x550")
        i=Info(root3,self.logo)
root=Tk()
root.title("LION'S CLUB")
#root.minsize(width="800",height="800")
myProject=MyProject(root)
root.mainloop()
