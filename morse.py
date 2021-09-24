import tkinter
import webbrowser
import winsound
import sqlite3
from tkinter import *
root=tkinter.Tk()
root.title("weee")
root.geometry('10000x10000')
########################################################################################################
def learn():                                                          #learn morsecode fuction to call
    
   
    url = "https://www.artofmanliness.com/articles/morse-code/"
    webbrowser.open(url)

################################################################################################################################################################################################

def about():                                                         #about us function
    
   
    url = "https://www.morsecodeninja.com/index.html"
    webbrowser.open(url)
    

######################################################################################################################################################################
def project():                                                        #Translate

    
    mList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
         '0','1','2','3','4','5','6','7','8','9','.',',','@','/',')','(',':',';','"','-','=','?','!','&','+','_','$','*','^','#','`','~',' '] #decrypted text


    
    win=tkinter.Toplevel()                                          
    win.configure(bg="SlateBlue4")
    win.geometry('10000x10000')
    head=tkinter.Label(win,text="Converse Morse To Text And Text To Morse",background="SlateBlue4",fg="white")

    head.configure(font=('bold'  ,30))
    head.place(relx=0.27,rely=0.05,anchor="center")

    t=tkinter.Label(win,text="ENTER MESSAGE =",background="SlateBlue4",fg="white")
    t.configure(font=('Algerian 25'))
    t.place(relx=0.45,rely=0.2,anchor="center")
    text= tkinter.StringVar()                                           
    text_message=tkinter.Entry(win,textvariable=text,width=70)
    text_message.place(relx=0.74,rely=0.2,anchor="center")
    text_message.configure(font=("bold",11))



    j = Label(win, image=imgg)
    j.place(relx=0.18,rely=0.25,anchor="center")



    l=Label(win, image=ma,height=300)
    l.place(relx=0.165,rely=0.65,anchor="center")



    
    bt = tkinter.Button(win,text="QUIT",command=win.destroy,background="SlateBlue4",fg="white")
    bt.place(relx=0.82,rely=0.82,anchor="center")
    bt.configure(font=("bold"))
    bt.configure(background="dark slate gray",width=25,height=1)

    



    mCode = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-----------.-','.-..','--','-.','---','.--.','--.-','.-.',
         '...','-','..........-','...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....','-....','--...'
         ,'---..','----.','-............','.---.','-.-','...-.','.-.-.-','...---','.--..','----...','..--..-','..-.--','.-.-.-.-','..-.-.','-.-.-----',
             '.-.--.-.--','--.--.-','.-...-...-','-...-....-...-.','-..--....','........------','.--...--.-','.-.-.-----....','..------.-.-',' '] #encrypted text
    
    morse_code_dict={}                                                 
    msg = tkinter.Text(win,height=2,width=23)                          

    for i in range(0,len(mList)):                                       
        morse_code_dict[mList[i]]=mCode[i]
   
    
    def morse_this():
        text_message=text.get().upper()
        morse_code_list = []
        for each_char in text_message:
            for morse_key,morse_value in morse_code_dict.items():
                 if each_char == morse_key:
                        morse_code_list.append(morse_value)
        morse_code_string=' '.join(morse_code_list)
        frequency = 2500
        duration = 100
        for i in morse_code_list:
            winsound.Beep(frequency,duration)
            
        msg.insert(tkinter.END,morse_code_string)
        msg.place(relx=0.47,rely=0.5,anchor="center")
        msg.configure(font=(None,15))
    m = tkinter.Text(win,height=2,width=23)
    def decrypt_this():
        st=''
        text_message=text.get().upper()
        for i in text_message.split():
            for key,value in morse_code_dict.items():
                if value==i:
                    st+=key
        frequency = 2500
        duration = 100




        for i in text_message:
            winsound.Beep(frequency,duration)
        m.insert(tkinter.END,st)
        m.place(relx=0.75
                ,rely=0.5,anchor="center")
        m.configure(font=(None,15))
        
        
    btn = tkinter.Button(win,image=d,command=morse_this)
    btn.place(relx=0.47,rely=0.35,anchor="center")
    btn.configure(font=("bold"))
    btn.configure(background="dark slate gray",width=250,height=102)

    btn1 = tkinter.Button(win,image=dec,command=decrypt_this)
    btn1.place(relx=0.75,rely=0.35,anchor="center")
    btn1.configure(font=("bold"))
    btn1.configure(background="DarkOrchid4",width=250,height=102)


    
    
def sugges():
    a = tkinter.Toplevel(root)
    a.geometry('10000x10000')
    a.title("Suggestion Box ")
    a.configure(bg='SlateBlue4')

    k = Label(a, image=picc)
    k.place(relx=0.28,rely=0.35,anchor="center")
    
    Fullname=StringVar()
    Email=StringVar()
    var=IntVar()
    c=StringVar()
    var1=StringVar()
    s=StringVar()

    def database():
        name1=Fullname.get()
        email=Email.get()
        gender=var.get()
        country=c.get()
        suggestion=s.get()
        conn=sqlite3.connect('Form.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS STUDENT(Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Suggestion)')
        cursor.execute('INSERT INTO Student (Fullname,Email,Gender,country,Suggestion)VALUES(?,?,?,?,?)',(name1,email,gender,country,suggestion))
        conn.commit()
    label_0 = Label(a, text="Suggestion Box",width=20,font=("bold", 40))
    label_0.place(x=790,y=49)


    label_1 = Label(a, text="FullName",width=20,font=("bold", 10))
    label_1.place(x=900,y=180)

    entry_1 = Entry(a,textvar=Fullname)
    entry_1.place(x=1140,y=180)

    label_2 = Label(a, text="Email",width=20,font=("bold", 10))
    label_2.place(x=900,y=230)

    entry_2 = Entry(a,textvar=Email)
    entry_2.place(x=1140,y=230)

    label_3 = Label(a, text="Gender",width=20,font=("bold", 10))
    label_3.place(x=900,y=280)

    Radiobutton(a, text="Male",padx = 5, variable=var, value=1).place(x=1130,y=280)
    Radiobutton(a, text="Female",padx = 20, variable=var, value=2).place(x=1190,y=280)

    label_4 = Label(a, text="country",width=20,font=("bold", 10))
    label_4.place(x=900,y=330)

    list1 = ['India','Canada','UK','Nepal','Iceland','South Africa'];
    c=StringVar()
    droplist=OptionMenu(a,c, *list1)
    droplist.config(width=15)
    c.set('select your country') 
    droplist.place(x=1140,y=330)

    label_4= Label(a, text="Suggestion",width=20,font=("bold", 10))
    label_4.place(x=900,y=380)


    entry_4 = Entry(a,textvar=s)
    entry_4.place(x=1140,y=380,width=150,height=50)


    Button(a, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=1010,y=460)





picc=PhotoImage(file="su.png")
ma=PhotoImage(file="15.png")
img=PhotoImage(file="13.png")
dec=img.subsample(1,1)
c = PhotoImage(file="9.png")
d=c.subsample(1,1)
imgg = PhotoImage(file = "8.png")
root.configure(bg="SlateBlue4")
a = tkinter.Label(root,text="MORSE CODE TRANSLATOR",background="SlateBlue4",width=25,height=2,fg="white")
a.place(relx=0.25,rely=0.004,anchor=NW)
a.configure(font=("calibri",40,"bold"))
btn1 = tkinter.Button(root,text="About Morse Code",command=about,background="steel blue",width=70,height=4,fg="white")
btn1.place(relx=0.01,rely=0.20,anchor=NW)
btn1.configure(font=("bold"))
btn2 = tkinter.Button(root,text="Learn morse code",command=learn,background="steel blue",width=70,height=4,fg="white")
btn2.place(relx=0.01,rely=0.33,anchor=NW)
btn2.configure(font=("bold"))
btn3 = tkinter.Button(root,text="Translate",command=project,background="steel blue",width=70,height=4,fg="white")
btn3.place(relx=0.01,rely=0.46,anchor=NW)
btn3.configure(font=("bold"))
btn4 = tkinter.Button(root,text="Suggestions",command=sugges,background="steel blue",width=70,height=4,fg="white")
btn4.place(relx=0.01,rely=0.59,anchor=NW)
btn4.configure(font=("bold"))
btn5 = tkinter.Button(root,text="EXIT",command=root.destroy,background="steel blue",width=70,height=4,fg="white")
btn5.place(relx=0.01,rely=0.72,anchor=NW)
btn5.configure(font=("bold"))

p=PhotoImage(file = "ab.png")
b = p.subsample(1,1)
btn6 = tkinter.Button(root,image = b,command=about)
btn6.place(relx=0.45,rely=0.20,anchor=NW)
btn6.configure(font=("bold"))
btn6.configure(background="dark slate gray",width=334,height=102)
                      
photo = PhotoImage(file = "4.png")
photoimage = photo.subsample(1,1)
btn7 = tkinter.Button(root,image = photoimage)
btn7.configure(background="bisque4",width=334,height=102)
btn7.place(relx=0.45,rely=0.33,anchor=NW)
btn7.configure(font=("bold"))

pi=PhotoImage(file = "1234.png")
ba = pi.subsample(2,2)
btn8 = tkinter.Button(root,image = ba)
btn8.configure(background="navajo white",width=334,height=102)
btn8.place(relx=0.45,rely=0.46,anchor=NW)
btn8.configure(font=("bold"))

pic=PhotoImage(file = "12.png")
bas = pic.subsample(1,1)
btn9 = tkinter.Button(root,image = bas)
btn9.configure(background="navajo white",width=334,height=102)
btn9.place(relx=0.45,rely=0.59,anchor=NW)
btn9.configure(font=("bold"))

pict=PhotoImage(file = "1.png")
basa = pict.subsample(1,1)
btn10 = tkinter.Button  (root,image = basa)
btn10.place(relx=0.45,rely=0.72,anchor=NW)
btn10.configure(background="black",width=334,height=102)
btn10.configure(font=("bold"))




photo = PhotoImage(file = "morse.png")
w = Label(root, image=photo)
w.place(relx=0.69,rely=0.33,anchor=NW)


root.mainloop()






