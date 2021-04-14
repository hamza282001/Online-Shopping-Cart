##  CEP TERM PROJECT
##
##  1) Hamza Munir CS-19140
##  2) M.Uzair Farooqui CS-19143


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from abc import ABC, abstractmethod

#------------------------------------------------------------------- Building an Abstract Class -----------------------------------------------------------------------------

class frames_container(ABC):

    ## These methods contains all the frames that are created in an interface.

    @abstractmethod
    def history_method(self):
        self.title('History Menu')
        self.frame2 = Frame(self,padx=50,pady=35)
        self.frame2.place(x=350,y=230)
        self.frame3 = Frame(self)
        self.frame3.place(x=0,y=0)

    def cart_method(self):
        self.title('Cart Menu')
        self.frame2 = Frame(self,padx=50,pady=35)
        self.frame2.place(x=165,y=130)
        self.frame3 = Frame(self,padx=220,pady=20)
        self.frame3.place(x=165,y=500)

    def product_method(self):
        self.title('Products Menu')
        self.frame2 = Frame(self,padx=50,pady=35)
        self.frame2.place(x=275,y=120)
        self.frame3 = Frame(self,padx=128,pady=10)
        self.frame3.place(x=275,y=530)

    def mid_method(self):
        self.title('Main Menu') 
        self.frame1 = Frame(self,pady=15,padx=233,relief=RAISED)
        self.frame1.place(x= -20,y=55)

    def signup_method(self):
        self.title('Signup Menu')
        self.frame1 = Frame(self, pady=39,padx=90,relief=RAISED)
        self.frame1.place(x=470,y=180)

    def login_method(self):
        self.title('Login Menu')
        self.frame1 = Frame(self,pady=70,padx=94,relief=RAISED)
        self.frame1.place(x=470,y=180)

    def account_method(self):       
        self.frame1 = Frame(self, pady=99,padx=50,relief=RAISED)
        self.frame1.place(x=470,y=180)
           

#------------------------------------------------------------- A Class To Read Products From The File ----------------------------------------------------------------------

class File_Reader:

    def displayproducts(self,frame):
        
        self.count = 0
        f = open('products.txt','r')
        f1 = open('prices.txt','r')
        for i in range(10):
            x = f.readline()
            y = f1.readline()
            self.count+=1
            Label(frame,text = str(self.count)).grid(row = self.count,column = 0)
            Label(frame, text = '\t',font = ('times new roman',16)).grid(row=self.count,column =1)
            Label(frame,text = str(x[0:-1])).grid(row = self.count,column =2)
            Label(frame, text = '\t',font = ('times new roman',16)).grid(row=self.count,column =3)
            Label(frame,text = str(y)).grid(row=self.count,column=4)
            
        f.close()
        f1.close()

#-------------------------------------------------------------- A Class To Write Products To The File ----------------------------------------------------------------------

class File_Saver:

    def savetofile(self,x,y,z,listing,amount):

        self.f1 = open(x,'w')
        self.f4 = open(y,'w')
        self.f5 = open(z,'w')
        
        for i in listing:
            self.f1.write(i[0]+'\n')
            self.f4.write(i[1]+'\n')
            self.f5.write(i[2]+'\n')
        self.f5.write(str(amount))
        self.f1.close()
        self.f4.close()
        self.f5.close()
    
#---------------------------------------------------------- The Main Class Where All The Methods Are Stored ----------------------------------------------------------------------

class account:

    def __init__(self):

        self.cart_list = []
        self.total_amount = 0

    ## A method for SigningUp to create an account.

    def signup(self):

        if self.username.get() == ''or self.password.get() == '' or self.gmail.get() == '':
            messagebox.showerror('Error','All fields are required to login.')

        else:
            try:
                f = open(self.username.get(),'r')
                messagebox.showerror('Error','Username not available.')

            except:
                self.f = open(self.username.get(),'w+')
                self.f.write(self.username.get())
                self.f.write('\n'+str(self.password.get()))
                self.f.write('\n'+str(self.gmail.get()))
                self.f.close()
                result = messagebox.showinfo('Successful','Account successfully created.\nLogin to continue.')
                if result == True:
                    main_menu.func2(self)

        self.username.delete(0,END)
        self.password.delete(0,END)
        self.gmail.delete(0,END)

    ## A method to login to the application.

    def login(self):

        try:
            self.f = open(self.username.get(),'r')
            self.x1 = self.f.readline()
            self.x2 = self.f.readline()

            if self.username.get() == self.x1[0:-1] and self.password.get() == self.x2[0:-1]:
                result = messagebox.askyesno('Welcome','Succesfully Logged in.\nAre you sure this is you?')
                if result == True:
                    self.user = self.x1[0:-1]
                    main_menu.mid_menu(self)
                else:
                    main_menu.func2(self)

            else:
                messagebox.showerror('Error','Enter valid value.')
                         
        except FileNotFoundError:
            messagebox.showerror('Error','No Account found with this username.')


    ## A method that displays all the products.

    def getproducts(self):

        Label(self.frame2, text = 'S.no',font = ('times new roman',16)).grid(row=0,column =0)
        Label(self.frame2, text = '\t',font = ('times new roman',16)).grid(row=0,column =1)
        Label(self.frame2, text = 'Product',font = ('times new roman',16)).grid(row=0,column =2)
        Label(self.frame2, text = '\t',font = ('times new roman',16)).grid(row=0,column =3)
        Label(self.frame2, text = 'Price',font = ('times new roman',16)).grid(row=0,column =4)
        account.displayproducts(self,self.frame2)


    ## This method adds your selected items to the cart which is temporaryily saved in a list.

    def addtocart(self):

        temporary_items = []
        temporary_prices = []

        with open('products.txt','r') as filehandle:
            for line in filehandle:
                temporary_items.append(line[:-1])
        
        with open('prices.txt','r') as filehandle:
            for line in filehandle:
                temporary_prices.append(line[:-1])

        if self.productno.get() == '' or self.productquan.get() == '' :
            messagebox.showerror('Error','Enter all values.')

        else:
            if self.productno.get() == '1':
                self.cart_list.append([temporary_items[0],self.productquan.get(),temporary_prices[0]])
            elif self.productno.get() == '2':
                self.cart_list.append([temporary_items[1],self.productquan.get(),temporary_prices[1]])
            elif self.productno.get() == '3':
                self.cart_list.append([temporary_items[2],self.productquan.get(),temporary_prices[2]])
            elif self.productno.get() == '4':
                self.cart_list.append([temporary_items[3],self.productquan.get(),temporary_prices[3]])
            elif self.productno.get() == '5':
                self.cart_list.append([temporary_items[4],self.productquan.get(),temporary_prices[4]])
            elif self.productno.get() == '6':
                self.cart_list.append([temporary_items[5],self.productquan.get(),temporary_prices[5]])
            elif self.productno.get() == '7':
                self.cart_list.append([temporary_items[6],self.productquan.get(),temporary_prices[6]])
            elif self.productno.get() == '8':
                self.cart_list.append([temporary_items[7],self.productquan.get(),temporary_prices[7]])
            elif self.productno.get() == '9':
                self.cart_list.append([temporary_items[8],self.productquan.get(),temporary_prices[8]])
            elif self.productno.get() == '10':
                self.cart_list.append([temporary_items[9],self.productquan.get(),temporary_prices[9]])  
            else:
                messagebox.showerror('Error','Enter valid data.')
        self.productno.delete(0, END)
        self.productquan.delete(0, END)
        self.addtocart


    ## This method displays the cart and shows amount of the selected items.
    
    def viewcart(self):

        if self.cart_list == []:
            messagebox.showerror('Error','The cart is Empty.')

        else:
            Label(self.frame2, text = 'S.no',font = ('times new roman',16)).grid(row=0,column =0)
            Label(self.frame2, text = '\t',font = ('times new roman',16)).grid(row=0,column =1)
            Label(self.frame2, text = 'Product',font = ('times new roman',16)).grid(row=0,column =2)
            Label(self.frame2, text = '\t',font = ('times new roman',16)).grid(row=0,column =3)
            Label(self.frame2, text = 'Quantity',font = ('times new roman',16)).grid(row=0,column =4)
            Label(self.frame2, text = '\t',font = ('times new roman',16)).grid(row=0,column =5)
            Label(self.frame2, text = 'Price',font = ('times new roman',16)).grid(row=0,column =6)
            self.count = 0
            self.total_amount = 0
            for (key,value1,value2) in self.cart_list:
                if value1 == '':
                    value1 = 0
                    self.count += 1
                    t = int(value1)*int(value2)
                    Label(self.frame2,text = str(self.count)).grid(row = self.count,column = 0)
                    Label(self.frame2,text = str(key)).grid(row = self.count,column =2)
                    Label(self.frame2,text = str(value1)).grid(row = self.count,column =4)
                    Label(self.frame2,text = str(t)).grid(row=self.count,column=6)
        
                else:
                    self.count += 1
                    t = int(value1)*int(value2)
                    Label(self.frame2,text = str(self.count)).grid(row = self.count,column = 0)
                    Label(self.frame2, text = '\t',font = ('times new roman',16)).grid(row=self.count,column =1)
                    Label(self.frame2,text = str(key)).grid(row = self.count,column =2)
                    Label(self.frame2, text = '\t',font = ('times new roman',16)).grid(row=self.count,column =3)
                    Label(self.frame2,text = str(value1)).grid(row = self.count,column =4)
                    Label(self.frame2, text = '\t',font = ('times new roman',16)).grid(row=self.count,column =5)
                    Label(self.frame2,text = str(t)).grid(row=self.count,column=6)
                    self.total_amount += t
            Label(self.frame2, text= '').grid(row=self.count+2,column=2)
            Label(self.frame2, text= '').grid(row=self.count+3,column=2)
            Label(self.frame2, text= '').grid(row=self.count+2,column= 6)
            Label(self.frame2, text= '').grid(row=self.count+3,column=6)
            Label(self.frame2,text = 'Total Amount: ',font = ('times new roman',14)).grid(row=self.count+4,column=2)
            Label(self.frame2,text = str(self.total_amount),font = ('times new roman',14)).grid(row=self.count+4,column = 6)
            Label(self.frame2, text= '').grid(row=self.count+5,column=6)
            Button(self.frame2,text='  ORDER  ',command = self.order ).grid(row=self.count+6,column=6)

    ## This method open up a new window for ordering the products.

    def order(self):

        self.root = Tk()
        self.root.minsize(600,400)
        self.root.maxsize(600,400)
        self.root.title('Order')
        self.ford = Frame(self.root)
        self.ford.place(x=230,y=40)
        Label(self.ford,text='Order Details',font=('times new roman',18)).pack()
        Label(self.ford,text='').pack()
        Label(self.ford, text= 'Enter Credit Card Number:').pack()
        self.card_number = Entry(self.ford)
        self.card_number.pack()
        Label(self.ford, text= '').pack()
        Label(self.ford, text= 'Select Delivery Speed:').pack()
        Radiobutton(self.ford,text = 'FEDex Express',value=1).pack()
        Radiobutton(self.ford,text = 'FEDex',value=2).pack()
        Label(self.ford, text= '').pack()
        Button(self.ford,text = '   Proceed  ',command = self.setting).pack()
        self.root.mainloop()

    ## This method just makes sure if all the payement details are entered and then orders and saves the cart.

    def setting(self):

        if self.card_number.get() == '':
            messagebox.showerror('Error','Card Number not added.')
            self.order()

        else:
            messagebox.showinfo('Success','Order successfully placed!\nThank you for shopping with us.')
            self.savetocart()
            self.cart_list.clear()
            main_menu.mid_menu(self)
            self.root.destroy()


    ## This method permanently saves your cart in a file once you checkout of the application.
                
    def savetocart(self):

        self.hname = str(self.user) +'_'+ str('history')

        try:
            f2 = open(self.hname,'r')
            f2.close()
        except:
            f2 = open(self.hname,'w+')
            f2.close()
           
        self.f = open(self.hname,'r')
        self.x = self.f.readline()
        if self.x == '' or self.x == 0 or self.x == '0':
            self.count = 0
        else:
            self.count = int(self.x)      
        self.count += 1
        self.f3 = open(self.hname,'w')
        self.f3.write(str(self.count))
        self.f3.close()
        self.f.close()
        

        self.name = str(self.user) +'_'+ str('cart')+ str(self.count)
        self.nameq = str(self.user) +'_'+ str('cart')+ str(self.count)+'_'+str('Quantity')
        self.namep = str(self.user) +'_'+ str('cart')+ str(self.count)+'_'+str('price')
        
        try:
            self.f1 = open(self.name,'r')
            self.f1.close()
        except:
            self.f1 = open(self.name,'w+')
            self.f1.close()

        try:
            self.f4 = open(self.nameq,'r')
            self.f4.close()
        except:
            self.f4 = open(self.nameq,'w+')
            self.f4.close()

        try:
            self.f5 = open(self.namep,'r')
            self.f5.close()
        except:
            self.f5 = open(self.namep,'w+')
            self.f5.close()

        self.total_amount = 0
        for (key,value1,value2) in self.cart_list:
            if value1 == '':
                value1 = 0
                t = int(value1)*int(value2)
                self.total_amount += t
            else:
                t = int(value1)*int(value2)
                self.total_amount += t

        account.savetofile(self,self.name,self.nameq,self.namep,self.cart_list,self.total_amount)
        messagebox.showinfo('Success','Cart Succesfully saved.')

    ## A method for removal of itmes.

    def remove(self):
            
        if self.removal.get() == '':
            messagebox.showerror('Error','Enter valid value.')

        else:
            self.x = int(self.removal.get()) - 1
            self.cart_list.pop(self.x)


    ## This method displays the total no.of checkouts ever made by the user.
        
    def checkhistory(self):

        name = str(self.user) +'_'+ str('history')

        try:
            f = open(name,'r')
            f.close()
        except:
            f =open(name,'w+')
            f.close()

        f = open(name,'r')
        self.ch = f.read()
        if self.ch == 0 or self.ch == '' or self.ch == '0':
            Label(self.frame2, text = 'Total Number Of Chechkouts: 0').pack()
        else:
            Label(self.frame2, text = 'Total Number Of Chechkouts: '+str(self.ch)).pack()
            for i in range(1,int(self.ch)+1):
                Label(self.frame2,text = 'Cart History'+str(i)).pack()



    ## This method shows the history that you selected.

    def selecthistory(self):

        if self.ch == '' or self.ch == '0' or self.ch == 0 :
            messagebox.showerror('Error','No History for new accounts.')
           
        else:
            name = str(self.user) +'_'+ str('cart') + str(self.historyno.get())
            nameq = str(self.user) +'_'+ str('cart')+ str(self.historyno.get())+'_'+str('Quantity')
            namep = str(self.user) +'_'+ str('cart')+ str(self.historyno.get())+'_'+str('price')

            try:
                f = open(name,'r')
                f = f.readline()
                if f == '' or f == None:
                    messagebox.showerror('Error','Empty History File.')
                    
                else:
                    try:
                        # Created a new frame window for displaying th eselected cart history.
                        root = Tk()
                        self.count = 0
                        root.minsize(600,400)
                        root.maxsize(600,400)
                        root.title('Cart History'+str(self.historyno.get()))
                        f5 = Frame(root)
                        f5.place(x =230,y=40)
                        f = open(name,'r')
                        f1 = open(nameq,'r')
                        f2 = open(namep,'r')
                        x = f.readlines()
                        
                        for i in x:
                            self.count += 1
                            q = f1.readline()
                            p = f2.readline()
                            Label(f5,text= str(self.count)+')'+str(i)+'  Price: '+str(p)+'  Quantity: '+str(q),compound = LEFT).pack()

                        Label(f5,text= 'Total Amount: '+str(f2.readline())).pack()
                        Label(root,text='Cart History'+str(self.historyno.get()),font=('times new roman',18),bg='grey').place(x=0,y=0,relwidth=1)                      

                    except:
                        messagebox.showerror('Error','No history found!')
            except:
                messagebox.showerror('Error','Enter valid value.')

        self.historyno.delete(0,END)

    ## This method will self check if the cart is empty or not before signing out.

    def ending(self):
        if self.cart_list == []:
            pass
        else:
            ans = messagebox.askquestion('Check Point','Do you wish to order the cart before exiting?')
            if ans == 'yes':
                self.order()
                self.savetocart()
            else:
                pass

    ## These two methods are associated to the above two classes 'File_Saver' & 'File_Reader'.

    def displayproducts(self,frame):

        fs = File_Reader()
        fs.displayproducts(frame)

    def savetofile(self,x,y,z,listing,amount):

        fs = File_Saver()
        fs.savetofile(x,y,z,listing,amount)                            



##-------------------------------------------------------------- This Is The Main User Interface Class -------------------------------------------------------------

class main_menu(Tk,account,frames_container):

    ## This __init__ method holds the main interface of the application.

    def __init__(self):

        super().__init__()
        account.__init__(self)

        self.minsize(1000,700)
        self.maxsize(1000,700)
        self.title('Virtual Shopping Cart')
        canvas = Canvas(self,width=1024,height=683)
        image =ImageTk.PhotoImage(Image.open("CS-19140_4.png"))
        canvas.create_image(0,0,anchor=NW,image=image)
        canvas.pack()
        self.account_menu()
        self.iconbitmap('CS-19140_2.ico')
        self.mainloop()

    ## These methods are frame displayers and they als destroy previous frames and show new ones.

    def account_menu(self):
        self.account_interface()

    def login_menu(self):

        try:
            self.frame1.destroy()
            self.title('Login Menu')
            self.login_interface()

        except:
            self.login_interface()

  
    def signup_menu(self):

        try:
            self.frame1.destroy()
            self.signup_interface()
            
        except:
            self.signup_interface() 

    def mid_menu(self):

        try:
            self.frame1.destroy()
            self.frame2.destroy()
            self.frame3.destroy()
            self.mid_interface()

        except:
            self.mid_interface()

    def viewprod(self):

        try:
            self.frame2.destroy()
            self.frame3.destroy()
            self.product_interface()

        except:
            self.product_interface()
          

    def seecart(self):
      
        try:
            self.frame2.destroy()
            self.frame3.destroy()
            self.cart_interface()

        except:
            self.cart_interface()


    def viewhistory(self):

        try:
            self.frame2.destroy()
            self.frame3.destroy()
            self.history_interface()

        except:
            self.history_interface()

    # Now these are the two function methods I created to execute multiple methods.
    # I could have done this with a lambda function but i wanted these two instantiation to be executed one after another.
    # Whereas lambda function runs both at the same time.

    def func(self):

        account.remove(self)
        main_menu.seecart(self)

    def func2(self):

        self.destroy()
        main_menu.__init__(self)
        

    # These are the methods that contains the proper interfaces.

    def history_interface(self):

        self.history_method()
        account.checkhistory(self)
            
        Label(self.frame2, text ='').pack()
        Label(self.frame2, text ='Enter the history number:').pack()
        self.historyno = Entry(self.frame2)
        self.historyno.pack()
        Button(self.frame2, text = '  Check  ',command = super().selecthistory).pack()

    def cart_interface(self):

        self.cart_method()

        if self.cart_list == []:
            messagebox.showerror('Error','The cart is Empty.')
            self.mid_menu()

        else:
            account.viewcart(self)
                    
            Label(self.frame3,text='Enter Product Number to remove from cart:').pack()
            self.removal = Entry(self.frame3)
            self.removal.pack()
            Label(self.frame3,text='').pack()
            Button(self.frame3, text = 'Remove',command = self.func).pack()

    def product_interface(self):

        self.product_method()      
        account.getproducts(self)

        Label(self.frame3,text='').pack()
        Label(self.frame3,text='Enter Product Number to add to cart:').pack()
        self.productno = Entry(self.frame3)
        self.productno.pack()
        Label(self.frame3,text='Enter Product Quantity:').pack()
        self.productquan = Entry(self.frame3)
        self.productquan.pack()
        Button(self.frame3, text = 'Add +',command = super().addtocart ).pack()

    def mid_interface(self):

        self.mid_method()

        self.frame2 = Frame(self,padx=5,pady=5)
        self.frame2.place(x=160,y=200)
        self.author = ImageTk.PhotoImage(file = 'CS-19140_1.png')
        author = Label(self.frame2,image = self.author)
        author.pack()
        Button(self.frame1,text='  Products  ',command =  self.viewprod ).grid(row=0,column=1)
        Label(self.frame1,text='             ').grid(row=0,column=2)
        Button(self.frame1,text= '     Cart     ',command = self.seecart).grid(row=0,column=3)
        Label(self.frame1,text='             ').grid(row=0,column=4)
        Button(self.frame1,text= '    History  ',command = self.viewhistory ).grid(row=0,column=5)
        Label(self.frame1,text='             ').grid(row=0,column=6)
        Button(self.frame1,text= '     Logout    ',command = self.logout ).grid(row=0,column=7)
        Label(self.frame1,text='             ').grid(row=0,column=8)
        Button(self.frame1,text= '     Main Menu    ',command = self.mid_menu).grid(row=0,column=9)
        Label(self.frame1,text='             ').grid(row=0,column=10)
        Label(self,text='HAMZA\'S VIRTUAL SHOPPING CART',font=('times new roman',30),bg = 'grey').place(x=0,y=0,relwidth=1)

    def signup_interface(self):

        self.signup_method()
        
        Label(self.frame1,text='Signup',font = ('times new roman',16)).pack()
        Label(self.frame1,text='').pack()
        Label(self.frame1,text='Register your Username.').pack()
        self.username = Entry(self.frame1)
        self.username.pack()
        Label(self.frame1,text='').pack()
        Label(self.frame1,text='Register your Password.').pack()
        self.password = Entry(self.frame1)
        self.password.pack()
        Label(self.frame1,text='').pack()
        Label(self.frame1,text='Register your email.').pack()
        self.gmail= Entry(self.frame1)
        self.gmail.pack()
        Label(self.frame1,text='').pack()
        Button(self.frame1,text= '        Register       ',command = super().signup ).pack()
        Button(self.frame1,text= 'Back to Main Menu',command = self.func2).pack()
        Label(self,text='HAMZA\'S VIRTUAL SHOPPING CART',font=('times new roman',30),bg = 'grey').place(x=0,y=0,relwidth=1)

    def login_interface(self):

        self.login_method()
        
        Label(self.frame1,text='Login',font = ('times new roman',16)).pack()
        Label(self.frame1,text='').pack()
        Label(self.frame1,text='Enter your Username.').pack()
        self.username = Entry(self.frame1)
        self.username.pack()
        Label(self.frame1,text='').pack()
        Label(self.frame1,text='Enter your Password.').pack()
        self.password = Entry(self.frame1)
        self.password.pack()
        Label(self.frame1,text='').pack()
        Button(self.frame1,text= '          Next         ',command = super().login).pack()
        Button(self.frame1,text= 'Back to Main Menu',command = self.func2 ).pack()
        Label(self,text='HAMZA\'S VIRTUAL SHOPPING CART',font=('times new roman',30),bg = 'grey').place(x=0,y=0,relwidth=1)

    def account_interface(self):

        self.account_method()
        self.frame2 = Frame(self,padx=4,pady=5)
        self.frame2.place(x=190,y=180)
        self.author = ImageTk.PhotoImage(file = 'CS-19140_3.png')
        author = Label(self.frame2,image = self.author)
        author.pack()

        Label(self.frame1,text='Welcome to Virtual Cart',font = ('times new roman',16)).pack()
        Label(self.frame1,text='').pack()
        Label(self.frame1,text='Choose from the options below.').pack()
        Label(self.frame1,text='').pack()
        Button(self.frame1,text=' Login ',command = self.login_menu).pack()
        Label(self.frame1,text='').pack()
        Button(self.frame1,text=' Signup ',command = self.signup_menu).pack()
        Label(self,text='HAMZA\'S VIRTUAL SHOPPING CART',font=('times new roman',30),bg = 'grey').place(x=0,y=0,relwidth=1)

    # inheritance methods from abstract class frames_container.

    def history_method(self):
        super().history_method()

    def cart_method(self):
        super().cart_method()

    def products_method():
        super().product_method()

    def mid_method(self):
        super().mid_method()

    def signup_method(self):
        super().signup_method()

    def login_method(self):
        super().login_method()

    def account_method(self):
        super().account_method()

    # Everytime a user logs out of his account these methods are executed.
     
    def logout(self):
        account.ending(self)
        self.destroy()
        main_menu.__init__(self)


#----------------------------------------------------------------------|  THE END  |-----------------------------------------------------------------------
# And this is the instantiation.
# Thank You!

main_menu()


        
