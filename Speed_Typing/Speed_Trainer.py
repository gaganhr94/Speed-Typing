from tkinter import *
import random
import difflib


i=0
j=0
k=0
count=0
expire=0
sentence=""
wordcount=0
score=0
pos=0   # Variable List from Basic Trainer
counttime=0


check_letpractice=False
check_wordpractice=False

dusermistakes=[]
dmistakewords=[]

genwordlist=[] # Generated Word List
entwordlist=[] # Entered Word List

mistakewords=[]  #List which stores all the mistake words
usermistake=[]   #List which stores the user mistakes

genstr="" # Generated word list
userstr="" # User word entered list

displaybutton=True
display_tryagain=True
finalkeys=[] # Stores the final error keys


wintrain = Tk()
wintrain.geometry('1100x650')
wintrain.state('zoomed')
wintrain.iconbitmap("TypingLOGO.ico")
wintrain.configure(bg='#000337')
wintrain.title('SPEED TYPING TRAINER')


#display the the list of words
def display():
    d=random.sample(words,5)
    text1 = ""
    for i in d:
        text1 += i + " "
    return text1


def labelSlider():
    global count, sliderwords
    text = 'WELCOME TO TYPING TRAINER'
    if (count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(1000, labelSlider)


def startGame(event):
    global score, miss ,x,i
    if (timeleft == 5):   # Change to 60
        time()

    labelSlider()
    gamePlayDetailLabel.configure(text='',bg='#000337',padx=0)
    gamePlayDetailLabel.place(x=225,y=450)
    wordarray=sentence.split()
    #print("len=",len(wordarray))
    i=+1
    if(i==5):
        i=0
    i=score+miss
    wordEntry.delete(0, END)


def sent():
    global display
    if check_letpractice == False and check_wordpractice == False:
        global words
        words = []
        file = open("WordList.txt", "r")
        for word in file:
            words.append(word.strip())

    display = random.sample(words, 5)
    sentence = ""
    for word in display:
        sentence += word + " "
    sentence = sentence.strip()
    sentence =" "+sentence + " "
    return sentence


def initialcolor():
    global i, j,k
    j = 0
    k = 0
    j = sentence.index(" ") + 1
    k = sentence.index(" ", j)
    #print(sentence[j:k])
    text.tag_add("current", '%d.%d' % (1, j), '%d.%d' % (1, k))
    text.tag_config("current", background="green", foreground="white")


def color(event):
    global j,k
    global expire
    global sentence,wordcount

    checkword()
    j=k+1
    #print("j=",j)

    try:
        k=sentence.index(" ",j)
    except ValueError:
        k=j

    #print("k=",k)
    #print(sentence[j:k])

    change()
    wordEntry.delete(0,END)
    text.tag_add("current", '%d.%d' %(1,j),'%d.%d' %(1,k))
    text.tag_config("current",background="green",foreground="white")
    expire += 1

    if (expire==5):
        text.configure(state=NORMAL)
        text.delete(1.0, END)
        sentence = sent()
        text.insert(INSERT, sentence)
        text.tag_add("center", 1.0, 'end')

        initialcolor()
        expire=0
        wordcount=0
        text.configure(state='disabled')
    #print(expire)


def change():
    text.tag_remove("current",  "1.0", 'end')


def checkword():
    global wordcount,score,miss
    userword=wordEntry.get().strip()
    word5=sentence.split()
    #print(word5)
    #print(wordcount)

    realword = (word5[wordcount]).strip()
    genwordlist.append(realword)
    entwordlist.append(userword)

    wordcount += 1

    if realword == userword:
        score+=1
        text.tag_add("correct", '%d.%d' % (1, j), '%d.%d' % (1, k))
        text.tag_config("correct", background="white", foreground="green")
    else:
        miss+=1
        mistakewords.append(realword)
        usermistake.append(userword)
        text.tag_add("mistake", '%d.%d' % (1, j), '%d.%d' % (1, k))
        text.tag_config("mistake", background="white", foreground="red")

    print(realword," ",userword)
    print("score=",score)


def time():
    global timeleft, score, miss,counttime,accuracy,finalkeystr,valuelist
    global letterpra, wordpra , wpmscore , pabutton, finalkeylabel, display_tryagain,detailrep

    if (timeleft > 0):
        timeleft -= 1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000, time)
        scoreLabelCount.configure(text=score)

    else:
        scoreLabelCount.configure(text=score)
        wintrain.unbind('<space>')
        wordEntry.unbind('<space>')
        wordEntry.delete(0, END)
        wordEntry.config(state="disable")
        analyser()
        gamePlayDetailLabel.configure(text='Correct Words = {}  |  Wrong Words = {}  |  Accuracy = {}'.format(score, miss, str(accuracy)+"%"),bg='yellow')
        gamePlayDetailLabel.place(x=190,y=450)
        #Displaying WPM (Words per minute)

        framewpm = Frame(wintrain, highlightbackground="white", highlightthickness=3, bg="white")
        framewpm.place(x=630, y=100)
        wpmlabel=Label(framewpm,text=" WPM ",font=('bookman old style', 25, 'bold'), bg='white',fg="red")
        wpmlabel.pack()
        wpmscore = Label(framewpm, text=wpmres, font = ('bookman old style', 25, 'bold'), bg = 'white')
        wpmscore.pack()

        if (len(finalkeys) != 0):
            finalkeystr=finalkeystr.split(",")
            finaltext=""
            if (len(finalkeys) == 3):
                finaltext = "Error Keys: " + "  " + finalkeystr[0] + "  |  " + finalkeystr[1] + "  |  " + finalkeystr[2]
            elif(len(finalkeys)==2):
                finaltext="Error Keys: "+"  "+finalkeystr[0]+"  |  "+finalkeystr[1]
            else:
                finaltext="Error Keys: "+"  "+finalkeystr[0]

            finalkeylabel=Label(wintrain,text=finaltext,font=('times', 25, 'italic bold'), bg='red',fg="white",padx=20)
            finalkeylabel.place(x=517,y=530)

        if(displaybutton==True):
            letterpra=Button(wintrain,text="Letter Practice",command=letterpractice,font=('book antiqua',12,'bold'),bg="red",fg="white",padx=10,pady=10)
            letterpra.place(x=370,y=610)

            if display_tryagain==True:
                print("Try Again Executed")
                pabutton=Button(wintrain,text="Try Again",command=backtopractice,font=('book antiqua',12,'bold'),bg="#00FFFF",padx=10,pady=10)
                pabutton.place(x=630,y=610)

            wordpra=Button(wintrain,text="Word Practice",command=wordpractice,font=('book antiqua',12,'bold'),bg="red",fg="white",padx=10,pady=10)
            wordpra.place(x=860,y=610)
            if accuracy!=100:
                detailrep=Button(wintrain,text="Detailed Report",font=('book antiqua',12,'bold'),bg="#00FFFF", command=detailedreport,padx=10,pady=10)
                detailrep.place(x=100,y=610)
        else:
            if(check_wordpractice==False and check_letpractice==False):
                pabutton = Button(wintrain, text="Try Again", command=backtopractice,font=('book antiqua',12,'bold'),bg="#00FFFF", padx=10, pady=10)
                pabutton.place(x=630, y=610)
            else:
                pabutton.configure(text="Try Again")
                pabutton.place(x=630, y=610)

#initialize variables
score = 0
timeleft = 5 #Change to 60
count = 0
sliderwords = ''
miss = 0


#Welcome Label
fontLabel = Label(wintrain, text='SPEED TYPING TRAINER', font=('times', 25, 'italic bold'),
                  bg='white', width=40)
fontLabel.config(anchor=CENTER)
fontLabel.pack(pady=5)

text = Text(wintrain, font=('Bookman Old Style', 20,), width=50, height=2)
text.tag_configure("center", justify="center")
sentence = sent()
text.insert(INSERT, sentence)
text.tag_add("center", 1.0,'end')
text.place(x=260, y=250)
text.configure(state='disabled')
initialcolor()

framescore=Frame(wintrain,highlightbackground="white",highlightthickness=3,bg="white")
framescore.place(x=100,y=100)
scoreLabel = Label(framescore, text="YOUR SCORE", font=('bookman old style', 25, 'bold'), bg='white',fg="red")
scoreLabel.pack()
scoreLabelCount = Label(framescore, text=score, font=('bookman old style', 25, 'bold'), bg='white')
scoreLabelCount.pack()

frametime=Frame(wintrain,highlightbackground="white",highlightthickness=3,bg="white")
frametime.place(x=1050,y=100)
timerLabel = Label(frametime, text='TIME LEFT', font=('bookman old style', 25, 'bold'), bg='white',fg="red")
timerLabel.pack()
timeLabelCount = Label(frametime, text=timeleft, font=('bookman old style', 25, 'bold'), bg='white')
timeLabelCount.pack()

gamePlayDetailLabel = Label(wintrain, text='Type Word And Hit Space Button', font=('times', 30, 'italic bold'),
                            bg='yellow',padx=100)
gamePlayDetailLabel.place(x=300, y=450)

#Entry Box
wordEntry = Entry(wintrain, font=('times', 25, 'bold'), bd=10, justify='center')
wordEntry.place(x=500, y=350)
wordEntry.bind('<space>',color)
wordEntry.focus_set()
wintrain.bind('<space>', startGame)

finalkeys=[]
errorkeys=[]
accuracy=0


def analyser():
    global usermistake,mistakewords,genwordlist,entwordlist,genstr,userstr,accuracy,finalkeystr,finalkeys,valuelist
    global errorkeys,displaybutton,wpmres, dusermistakes , dmistakewords
    global congolabel

    for ele in genwordlist:
        genstr+=ele+" "
    for ele in entwordlist:
        userstr+=ele+" "
    accuracy = difflib.SequenceMatcher(None, userstr.strip(), genstr.strip()).ratio()
    accuracy = str(round(accuracy * 100, 2))
    print(accuracy)

    accuracy=float(accuracy)

    totalchar=len(genstr)
    print(totalchar)

    wpmres=round((accuracy*totalchar/100)//5)  # Calculates the total words per minute
    print("wpm=",wpmres)

    print("usermistake ",usermistake)
    print("mistakewords ",mistakewords)

    dusermistakes=usermistake
    dmistakewords=mistakewords     # Variables for detailed report

    for i in range(len(mistakewords)):
        userletters=list(usermistake[i])
        genletters=list(mistakewords[i])

        for j in genletters:
            if j not in userletters:
                errorkeys.append(j)         # Takes note of "absent letters" not entered by user

        #print("gen= ",len(genletters))
        #print("user= ",len(userletters))       # Testing purpose print statement

        if len(genletters)==len(userletters):
            for k in range(len(genletters)):

                try:
                    if genletters[k]!=userletters[k]:
                        errorkeys.append(genletters[k])   # Takes care of mismatch of letters and 'handles IndexError'
                except IndexError:
                    break

    if len(errorkeys)==0:
        displaybutton=False
    else:
        displaybutton=True

    print(errorkeys)
    errorkeys.sort()
    errorkeyset=set(errorkeys)
    dicterror={}


    def frequency():
        for i in errorkeyset:
            dicterror[i]=errorkeys.count(i)
    frequency()
    finalkeys=[]

    while len(finalkeys)<3:
        keylist=list(dicterror.keys())
        valuelist=list(dicterror.values())

        if len(dicterror)==0:
            break

        maxvalue=max(valuelist)
        pos=valuelist.index(maxvalue)
        maxkey=keylist[pos]
        dicterror.pop(maxkey)
        finalkeys.append(maxkey)

    if (len(errorkeys) == 0):
        if(miss==0):
            Msg5 = "Congratulations !!\n You have no errors in your typing"
        else:
            Msg5 = "You are clicking the right keys ! \n Try to improve the accuracy"

        congolabel = Label(wintrain, text=Msg5, font=('times', 20, 'italic bold'), bg='white',fg='red')
        congolabel.place(x=500, y=525)

    print("final ",finalkeys)
    print("allerror",errorkeys)  # Testing purpose print statement

    finalkeystr=""
    for i in finalkeys:
        finalkeystr+=i+","
    finalkeystr.strip()
    b=len(finalkeystr)
    finalkeystr=finalkeystr[0:b-1]
    reset1()

def backtopractice():
    global finalkeys, s, wordlist, check_letpractice, timeleft, k, j, i, sentence, expire, display, score, wordcount, miss, userstr, genstr
    global genwordlist, entwordlist ,pabutton,wordpra,letterpra
    global check_wordpractice , finalkeylabel, display_tryagain,congolabel
    display_tryagain=True
    check_letpractice = False
    check_wordpractice = False
    timeLabelCount.configure(text=60)
    try:
        detailrep.destroy()
    except NameError:
        pass

    try:
        finalkeylabel.configure(text='',bg='#000337')
        wordpra.destroy()
        letterpra.destroy()
        pabutton.place_forget()
    except TclError:
        pass
    except NameError:
        pass

    gamePlayDetailLabel.configure(text='',bg='#000337')
    scoreLabelCount.configure(text="0")
    try:
        congolabel.destroy()
    except NameError:
        pass

    reset1()
    finalkeys=[]
    check_letpractice=False
    check_wordpractice=False
    sentence = ""
    wordcount = 0
    miss = 0
    timeleft = 5
    score = 0
    i = 0
    j = 0
    k = 0
    expire = 0
    userstr = ""
    genstr = ""
    genwordlist = []
    entwordlist = []

    wpmscore.configure(text="0")
    text.configure(state=NORMAL)
    text.delete(1.0, END)

    sentence=sent()

    text.insert(INSERT, sentence)
    text.tag_add("center", 1.0, 'end')
    text.tag_configure("center", justify=CENTER)
    initialcolor()

    wordEntry.config(state=NORMAL)

    wordEntry.bind('<space>', color)
    wintrain.bind('<space>', startGame)


def reset1():
    global usermistake,mistakewords,errorkeys
    usermistake=[]
    mistakewords=[]
    errorkeys=[]


def letterpractice():
    global finalkeys,s,wordlist,check_letpractice,timeleft,k,j,i,sentence,expire,display,score,wordcount,miss,userstr,genstr
    global genwordlist,entwordlist,pabutton
    global wpmscore,words,display_tryagain,finalkeylabel
    global letterpra,wordpra

    letterpra.destroy()
    wordpra.destroy()
    detailrep.destroy()
    display_tryagain=False

    finalkeylabel.destroy()
    a=finalkeys
    scoreLabelCount.configure(text="0")
    timeLabelCount.configure(text=timeleft)
    wpmscore.configure(text="0")
    sentence=""
    wordcount=0
    miss=0
    letterlist=[]

    if(len(finalkeys)==3 or len(finalkeys)==2):
        for i in range(0,20):
            strt=""
            for i in range(0,random.randint(1,5)):
                strt+=random.choice(a)
            letterlist.append(strt)

    elif(len(finalkeys)==1):
         for i in range(0,20):
             strt = ""
             for i in range(0,random.randint(1,5)):
                 strt+=a[0]
             letterlist.append(strt)

    timeleft=5
    score=0
    i=0
    j=0
    k=0
    expire=0
    userstr=""
    genstr=""
    genwordlist=[]
    entwordlist=[]
    check_letpractice = True

    text.configure(state=NORMAL)
    text.delete(1.0, END)
    words=[]

    words=letterlist
    sentence=sent()
    print(sentence)

    text.insert(INSERT, sentence)
    text.tag_add("center", 1.0, 'end')
    text.tag_configure("center", justify=CENTER)
    initialcolor()

    pabutton.configure(text="Back to Normal Practice")
    pabutton.place(x=570,y=610)

    wordEntry.config(state=NORMAL)

    wordEntry.bind('<space>',color)
    wintrain.bind('<space>',startGame)


def reset():
    global usermistake
    global finalkeys, s, wordlist, check_letpractice, timeleft, k, j, i, sentence, expire, display, score, wordcount, miss, userstr, genstr
    global genwordlist, entwordlist, pabutton,words,check_wordpractice
    sentence = ""
    wordcount = 0
    miss = 0
    words=[]
    timeleft = 5
    score = 0
    i = 0
    j = 0
    k = 0
    expire = 0
    userstr = ""
    genstr = ""
    genwordlist = []
    entwordlist = []


def wordpractice():
    reset()
    global wordpra, letterpra
    wordpra.destroy()
    letterpra.destroy()
    detailrep.destroy()
    global sentence
    global pabutton
    global check_wordpractice,display,words,display_tryagain
    global check_wordpractice,finalkeylabel

    finalkeylabel.destroy()
    check_wordpractice = True

    display_tryagain=False

    scoreLabelCount.configure(text="0")
    wpmscore.configure(text="0")
    timeLabelCount.configure(text=timeleft)
    text.configure(state=NORMAL)
    text.delete(1.0, END)

    a = finalkeys
    file = open("WordList.txt", "r")
    filex = open("WordList.txt", "r")
    words = []
    if len(a)==3:
        for word in file:
            if a[0] in word and a[1] in word and a[2] in word:
                words.append(word.strip())

    if (len(words) < 100):
        for word in filex:
            if len(a)==3:
                print(a)
                if (a[0] in word and a[1] in word) or (a[1] in word and a[2] in word) or (a[2] in word and a[0] in word):
                    words.append(word.strip())
                if len(words) == 100:
                    break
            elif len(a)==2:
                if (a[0] in word and a[1] in word):
                    words.append(word.strip())
                if len(words) == 100:
                    break
            else:
                if a[0] in word:
                    words.append(word.strip())
                if len(words) ==100:
                    break

    sentence=sent()

    text.insert(INSERT, sentence)
    text.tag_add("center", 1.0, 'end')
    text.tag_configure("center", justify=CENTER)
    initialcolor()

    pabutton.configure(text="Go Back to Normal Practice")
    pabutton.place(x=570, y=610)

    wordEntry.config(state=NORMAL)
    wordEntry.bind('<space>', color)
    wintrain.bind('<space>', startGame)


def detailedreport():
    global dusermistakes,dmistakewords
    detailreport_text1=""
    detailreport_text2=""
    report=Tk()
    report.geometry("548x600+400+50")
    report.iconbitmap("TypingLOGO.ico")
    report.configure(bg="lightblue")
    report.title("DETAILED REPORT")

    l1=Label(report,text="Given Word        Entered Word",font=('bookman old style', 24, 'bold'), bg='darkblue',fg="white",padx=17)
    l1.place(x=0,y=0)
    for k in range(len(dmistakewords)):
        if dusermistakes[k]=="":
            dusermistakes[k]="-"
        detailreport_text1+=dmistakewords[k]+"\n"
        detailreport_text2+=dusermistakes[k]+"\n"


    l2=Label(report,text=detailreport_text1,font=('times', 15,), bg='lightblue',fg="black",pady=10)
    l2.place(x=80,y=75)
    l3 = Label(report, text=detailreport_text2, font=('times', 15,), bg='lightblue', fg="black",pady=10)
    l3.place(x=380,y=75)

    drexit=Button(report, text="Exit Detailed Report", command=report.destroy,font=('book antiqua',12,'bold'),bg="blue",fg="white", padx=10, pady=10)
    drexit.place(x=200,y=500)



exitbutton=Button(wintrain,text="Exit",command=wintrain.destroy,font=('book antiqua',12,'bold'),bg="#00FFFF",padx=20,pady=10)
exitbutton.place(x=1120,y=610)

wintrain.mainloop()

#print(usermistake)
#print(mistakewords)


