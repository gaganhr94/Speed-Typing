import random
from tkinter import *
from timeit import default_timer
import difflib
from historydatabase import *
from PIL import ImageTk,Image
import subprocess

start=0
pos=0
k=0
j=0
count=0
count1=0
expire=0
sentence=""
wordcount=0
score=0 #Variable list from Basic Trainer
time=3

enteredstr=""


# Code for Splash Screen seen at the beginning
def splashscreen():
    splash_root=Tk()
    splash_root.title("SPLASH")
    splash_root.geometry("600x455+382+132")
    splash_root.overrideredirect(True)      #Removes the title bar
    splash_root.after(3000,splash_root.destroy)
    img=ImageTk.PhotoImage(Image.open("Splash.png"))
    frame1 = Frame(splash_root, highlightbackground="#2F50D4", highlightthickness=5,bg="white")
    frame1.pack()
    l1=Label(frame1,image=img,bg='white')
    l1.pack()
    contributors=Label(frame1,text="PROJECT BY:\nGAGAN H R | DIGVIJAY SUNIL | HRIDAY PRADHAN",font=('book antiqua',10,'bold'),bg="white",padx=120)
    contributors.pack()
    splash_root.mainloop()

splashscreen()


root = Tk()
root.title('SPEED TYPING')
root.geometry("600x455+382+132")

# LOGO
root.iconbitmap("TypingLOGO.ico")
entered = StringVar()

fscreen1=Frame(root,highlightbackground="#191970",highlightthickness=5,bg="lightblue")
fscreen1.pack()
fscreen2=Frame(fscreen1,highlightbackground="darkblue",highlightthickness=3,bg="#00FFFF")
fscreen2.pack(padx=25,pady=15)
greet = Label(fscreen2, font=('book antiqua', 25, 'bold'), text="WELCOME TO THE WORLD OF \nSPEED TYPING !",fg="darkblue",bg="#00FFFF")
greet.pack(padx=10)


def choice():
    global window
    window = Tk()   # Try to make a separate window
    window.geometry("575x475+380+100")
    window.title("SPEED TYPING - MAIN MENU")
    window.iconbitmap("TypingLOGO.ico")

    framewindow=Frame(window,highlightbackground="indigo", highlightthickness=5,bg="#5ba8ff")
    framewindow.pack()
    frame2=Frame(framewindow,highlightbackground="blue",highlightthickness=3,bg="#a7e7ff")
    frame2.pack(padx=15,pady=15)
    labeln=Label(frame2, text="CLICK AN OPTION BELOW",font=("bookman old style",25,'bold'),bg="#a7e7ff",fg="indigo")
    labeln.pack(pady=5,padx=35)

    b1 = Button(framewindow, text="TYPING SPEED TEST", font=("book antiqua",20,"bold"),command=clicked,borderwidth=3,bg="white",fg="#1b4d89")
    b1.pack(padx=10,pady=13,ipadx=100,ipady=5)
    b2 = Button(framewindow, text="TYPING TRAINER", command=opentrainer, font=("book antiqua",20,"bold"),borderwidth=3,bg="white",fg="#1b4d89")
    b2.pack(padx=10,pady=13,ipadx=90,ipady=5)
    b3 = Button(framewindow, text="LOGOUT",command=b3operation, font=("book antiqua",20,"bold"),borderwidth=3,bg="white",fg="#1b4d89")
    b3.pack(padx=10,pady=13,ipadx=70,ipady=5)
    b4 = Button(framewindow, text="EXIT", command=b4operation, font=("book antiqua", 20, "bold"),borderwidth=3,bg="white",fg="#1b4d89")
    b4.pack(padx=10, pady=13, ipadx=50, ipady=5)


def b4operation():
    window.destroy()
    root.destroy()


def b3operation():
    window.destroy()
    root.deiconify()


def opentrainer():
    subprocess.call("Speed_Trainer.py", shell=True)


def clicked():
    global entered
    global word
    global start
    global sentence,enteredstr

    enteredstr=""
    top =Tk()
    top.title("TYPING SPEED TEST")
    top.configure(bg="#D4F1F4")
    top.iconbitmap("TypingLOGO.ico")
    top.geometry("1300x590+35+50")

    wordfile = open("Text_Lines.txt", "r")
    words = wordfile.readlines()
    wordfile.close()

    word = random.choice(words)
    sentence=word

    sentence = sentence.strip()
    sentence = sentence + " "


    def TryAgain():
        global enteredstr,time
        time=3
        top.destroy()
        clicked()
        enteredstr=""


    def initialcolor():
        global count, count1, expire,sentence
        #print(sentence)
        j = 0
        k = sentence.index(" ")
        #print(j,k)
        #print(sentence[j:k])
        text.tag_add("current", '%d.%d' % (1, j), '%d.%d' % (1, k))
        text.tag_config("current", background="green", foreground="white")
        count = j
        count1 = k


    def color(event):
        global count, count1, j, k
        global expire
        global sentence
        global stop
        global enteredstr

        print(enteredstr)
        enteredstr = enteredstr + (enter.get()).strip() + " "

        try:
            j = sentence.index(" ", count) +1
            k = sentence.index(" ", count1+1)
            #print(j,k)
        except ValueError:
            k = j
            text.tag_remove("current", "1.0", 'end')
            check()

        #Color Result Code
        if(enter.get().strip()!=sentence[count:count1].strip()):
            text.tag_add("mistake", '%d.%d' % (1, count), '%d.%d' % (1, count1))
            text.tag_config("mistake", background="white", foreground="red")
        else:
            text.tag_add("correct", '%d.%d' % (1, count), '%d.%d' % (1, count1))
            text.tag_config("correct", background="white", foreground="green")

        enter.delete(0, END)

        text.tag_remove("current", "1.0", 'end')
        text.tag_add("current", '%d.%d' % (1, j), '%d.%d' % (1, k))
        text.tag_config("current", background="green", foreground="white")

        count = j
        count1 = k
        expire += 1
        # print(expire)


    def check(event=None):
        global enteredstr

        string = f"{enteredstr.strip()}"
        end = default_timer()
        time = round(end - start, 2)

        speed = round(len(sentence)/5 * 60 / time)  # Change the WPM formula

        accuracy = difflib.SequenceMatcher(None, word.strip(), string.strip()).ratio()
        accuracy = str(round(accuracy * 100, 2))

        if accuracy.strip()=="100.0":
            accuracy="100"

        speed1=round(((((float(accuracy)*len(sentence)/100)/5)*60)/time))

        framedata=Frame(top,highlightthickness=3,highlightbackground="black",bg="#a7e7ff")
        framedata.grid(row=10,column=3)

        Msg1 = "Total Time Taken= " + str(time) + ' seconds'
        Msg2 = " Accuracy= " + accuracy + '%'
        Msg4 = " Gross Speed= " + str(speed) + ' WPM'  # words per minute
        Msg3 = " Net Speed= "+ str(speed1) + ' WPM' #words per minute - mistake words excluded

        label = Label(framedata, font=('book antiqua', 15, 'bold'), text=Msg1,bg="#a7e7ff")
        label.pack()

        label = Label(framedata, font=('book antiqua', 15, 'bold'), text=Msg2,bg="#a7e7ff")
        label.pack()

        if (float(accuracy) >= 30):
            label = Label(framedata, font=('book antiqua', 15, 'bold'), text=Msg4,bg="#a7e7ff")
            label.pack()
            label1=Label(framedata, font=('book antiqua',15,"bold"),text=Msg3,bg="#a7e7ff")
            label1.pack()
        else:
            label = Label(framedata, font=("book antiqua", 15, 'bold'), text=Msg3,bg="#a7e7ff")
            label.pack()
            label1 = Label(framedata, font=('book antiqua', 15, "bold"),text="Sorry Gross Speed cannot be displayed\n"+
                                                                "Improve on your accuracy !", fg="red",bg="#a7e7ff")
            label1.pack()


    def play():
        initialcolor()
        global word
        global start,start1
        global entered
        global enter

        label = Label(top, font=('bookman old style', 15,'bold'), text="TYPE HERE : ",bg="#D4F1F4")
        label.grid(row=6, column=1)

        entered = StringVar()
        enter = Entry(top, textvariable=entered, font=('arial', 15), width=50)
        enter.grid(row=6, column=3,pady=15)
        enter.bind('<Return>',check)
        top.bind('<space>',color)

        counttime = 3
        timetextl = Label(top, text="You can start typing in ...", font=('book antiqua', 25,'italic'), justify=CENTER,bg="#D4F1F4",fg="black")
        timetextl.grid(row=16, column=3)
        timelabel = Label(top, text=counttime, font=('book antiqua', 20,'italic'),bg="#D4F1F4")
        timelabel.grid(row=17, column=3)


        def timer():
            nonlocal counttime
            if (counttime > -1):
                timelabel.configure(text=counttime)
                counttime -= 1
                timelabel.after(1000, timer)
            else:
                enter.focus_set()
                timetextl.destroy()
                timelabel.destroy()
        timer()

        btn = Button(top, text="Check", command=check, bg="blue", fg="white", font=('book antiqua', 12,'bold'), pady=10)
        btn.grid(row=5,column=3,pady=10)

        retrybutton = Button(top, text="Try Again", command=TryAgain, font=('book antiqua',12,'bold'),fg="white",bg="red")
        retrybutton.grid(row=14,column=3,pady=10)  # TRY AGAIN

        backbutton = Button(top,text="Go to Main Menu",command=top.destroy,font=("book antiqua",12,'bold'),fg="white",bg='red')
        backbutton.grid(row=15,column=3,pady=5)

    text = Text(top, font=('Bookman Old Style', 20,), height=3, width=68,padx=17,pady=10)
    text.insert(INSERT, sentence)
    text.grid(row=3,column=0,columnspan=9,padx=50,pady=10)
    text.configure(state='disabled')

    btn = Button(top, text=" Start typing", command=play, bg="blue", fg="white", font=('book antiqua', 12,'bold'),padx=20,relief=RAISED)
    btn.grid(row=4,column=3,pady=10)

    start=default_timer()


def databasegate():
    root.withdraw()
    subprocess.call("historydatabase.py", shell=True)
    #print(login)
    if(login==True):
        choice()

# Button redirects to the Login Window
button1 = Button(fscreen1, text="CLICK HERE TO GET STARTED !",font=('book antiqua',15,'bold'), command=databasegate,fg="blue",bg="#F0FFFF",borderwidth=4)
button1.pack(padx=20,pady=50,ipadx=30,ipady=25)

exitbutton = Button(fscreen1, text="EXIT" ,font=('book antiqua', 15,'bold'), command=root.destroy,fg="blue",bg="#F0FFFF",borderwidth=4)
exitbutton.pack(padx=20,pady=30,ipadx=30,ipady=25)


root.mainloop()



