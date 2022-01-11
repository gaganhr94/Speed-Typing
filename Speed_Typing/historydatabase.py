from tkinter import *
import sqlite3
import sys
login=True
cr = 0

def main():
    global username_exist
    username_exist=False
    cr = 0 # Count variable for displaying users
    datawindow = Tk()
    datawindow.title("USER LOGIN / REGISTER")
    datawindow.iconbitmap("TypingLOGO.ico")
    datawindow.geometry("400x500+475+75")
    datawindow.configure(bg="#FFBF33")

    conn = sqlite3.connect('userhistory.db')
    c = conn.cursor()

    '''
    c.execute("""CREATE TABLE  users (
            name text,
            username text
            wpm1 integer
            wpm2 integer
            wpm3 integer
            wpm4 integer
            wpm5 integer
            )""")
    '''

    name = Entry(datawindow, width=30)
    name.grid(row=0, column=1, padx=20,pady=20)
    name.focus_set()

    username = Entry(datawindow, width=30)
    username.grid(row=1, column=1, padx=20)

    dele = Entry(datawindow, width=30)
    dele.grid(row=4, column=1)

    name_label = Label(datawindow, text="Name",font=('book antiqua',10,'bold'),bg="#FFBF33",fg="#652121")
    name_label.grid(row=0, column=0,pady=20)
    username_label = Label(datawindow, text="Username",font=('book antiqua',10,'bold'),bg="#FFBF33",fg="#652121")
    username_label.grid(row=1, column=0)
    dell = Label(datawindow, text="Select User Number",font=('book antiqua',10,'bold'),bg="#FFBF33",fg="#652121")
    dell.grid(row=4, column=0, pady=10,ipadx=10)

    # Creating Login Function

    def login():
        global login
        global username_exist

        hellowindow=Tk()
        hellowindow.title("INTRODUCTION")
        hellowindow.iconbitmap("TypingLOGO.ico")
        hellowindow.geometry("630x500+370+100")
        hellolabel=Label(hellowindow,font=('bookman old style',20,'bold'),bg="white",fg="red")
        hellolabel.pack(pady=10,ipadx=10)
        instructions=Label(hellowindow,font=('book antiqua',10,'bold'),anchor='e',fg="darkblue")
        instructions.pack()
        helloexitbutton=Button(hellowindow,text="EXIT THIS SCREEN TO CONTINUE",font=('book antiqua',12,'bold'),command=hellowindow.destroy,bg="blue",fg="white")
        helloexitbutton.pack(padx=10,pady=10,ipady=10,ipadx=100)

        login=True
        names = name.get()
        if len(names) != 15:
            if len(names) < 15:
                for i in range(0, 15 - len(names)):
                    names += " "
            else:
                names = names[0:15]

        usernames = username.get()
        if len(usernames) != 15:
            if len(usernames) < 15:
                for i in range(0, 15 - len(usernames)):
                    usernames += " "
            else:
                usernames = usernames[0:15]

        conn = sqlite3.connect('userhistory.db')
        c = conn.cursor()
        c.execute("SELECT *,oid FROM users")
        records=c.fetchall()

        # Insert Lines into the Table

        for record in records:
            if(record[1]==usernames):
                username_exist=True
                hellolabel.configure(text="Hello "+record[0].strip()+'\n'+"Welcome Back to Speed Typing")
                instructions.configure(text="Since your already aware of the features of the application, lets not "
                                            "waste time.\nClick on the button below and start typing !\n\n\n\n\n")

        if username_exist==False:
            c.execute("INSERT INTO users VALUES (:name, :username)",
                      {
                          'name': names,
                          'username': usernames
                      })

            hellolabel.configure(text="Hello "+names.strip()+"\nLooks like you are here for the first time !")
            instructions.configure(text="Let's quickly run through the features: \n\n"+
            "1. Speed Typing Test : Gives the user a paragraph to type  \nand displays the Gross WPM (Without considering wrong \nentries, "+
            "Net WPM (Considering Wrong Entries), Accuracy, \nand the total time taken for typing the paragraph."+
            "\n\n2. Speed Typing Trainer : A complete trainer package that\n lets the user type the words displayed on "
            +"the screen for a\ntime period of 60 seconds. The trainer identifies keyboard\n keys in which the user is frequently making mistakes"+
            " and\n provides the user a unique and customized practice and\n analysis features to improve your typing skills:\n(i) Letter Practice \n(ii) Word Practice \n(iii) Detailed Mistake Report \n\n"+
            "The user can practice in these modes until he becomes a TYPE MASTER.")


        conn.commit()
        conn.close()

        # Clear Text Boxes
        name.delete(0, END)
        username.delete(0, END)
        datawindow.destroy()

    login_button = Button(datawindow, text="Login/Register",font=('book antique',9,'bold'),command=login,bg="#f70d1a",fg="white")
    login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

    def update():
        namestr = n_e.get()
        if len(namestr) != 15:
            if len(namestr) < 15:
                for i in range(0, 15 - len(namestr)):
                    namestr += " "
            else:
                namestr = namestr[0:15]

        usernamestr = u_e.get()
        if len(usernamestr) != 15:
            if len(usernamestr) < 15:
                for i in range(0, 15 - len(usernamestr)):
                    usernamestr += " "
            else:
                usernamestr = usernamestr[0:15]

        conn = sqlite3.connect("userhistory.db")
        c = conn.cursor()

        record_id = dele.get()

        c.execute("""UPDATE users SET
            name = :name_ent,
            username = :user_ent

            WHERE oid = :oid""",
                  {
                      'name_ent': namestr,
                      'user_ent': usernamestr,
                      'oid': record_id
                  })

        conn.commit()
        conn.close()

        editor.destroy()

    def query():
        global cr, q_l
        try:
            q_l.configure(bg="yellow")
        except NameError:
            pass

        conn = sqlite3.connect("userhistory.db")
        c = conn.cursor()
        c.execute("SELECT *,oid FROM users")
        records = c.fetchall()

        print_records = '     \tName\t              Username\t     User Number   \n'
        for record in records:
            print_records += str(record[0]) + " " + "\t" + str(record[1]) + " " + "\t" + str(record[2]) + '\n'
        cr += 1
        if (cr == 1):
            q_l = Label(datawindow, text=print_records, bg="yellow" )
            q_l.grid(rows=11, column=0, columnspan=2)
        else:
            q_l.configure(
                text=print_records)  # If a Label is already present, configure it - no creation of new label when already present

        conn.commit()
        conn.close()

    def edit():
        global n_e, u_e, editor

        editor = Tk()
        editor.title("EDIT USER DETAILS")
        editor.iconbitmap("TypingLOGO.ico")
        editor.geometry("390x400+900+120")
        editor.configure(bg="#FFBF33")

        if dele.get() == "":
            editor.withdraw()

        else:
            conn = sqlite3.connect("userhistory.db")
            c = conn.cursor()

            # Declaring name and username variables to store string variables

            # Create textboxes
            n_e = Entry(editor, width=30)
            n_e.grid(row=0, column=1)

            u_e = Entry(editor, width=30)
            u_e.grid(row=1, column=1)

            record_id = dele.get()

            try:
                c.execute("SELECT * FROM users WHERE oid = " + record_id)
            except sqlite3.OperationalError:
                pass

            records = c.fetchall()
            # Loop through results
            for record in records:
                n_e.insert(0, record[0])
                u_e.insert(0, record[1])

            """  #Not Required   
            print_records = ''
            for record in records:
                print_records += str(record[0] + "\t" + str(record[1]+ "\t"+ str(record[2]))) + '\n'
            """

            # create lables for the textboxes
            name_l = Label(editor, text="Name",font=('book antiqua',10,'bold'),bg="#FFBF33",fg="#652121")
            name_l.grid(row=0, column=0)
            username_l = Label(editor, text="Username",font=('book antiqua',10,'bold'),bg="#FFBF33",fg="#652121")
            username_l.grid(row=1, column=0)

            # Create an Save Record
            edit_btn = Button(editor, text="Save Record",font=('book antique',9,'bold'), command=update,bg="#f70d1a",fg="white")
            edit_btn.grid(row=8, column=0, columnspan=2, padx=15, pady=10, ipadx=136)

    # Delete a record
    def delete():
        conn = sqlite3.connect("userhistory.db")
        c = conn.cursor()

        try:
            c.execute("DELETE from users WHERE oid= " + dele.get())

        except sqlite3.OperationalError:
            pass

        conn.commit()
        conn.close()

        dele.delete(0, END)

    # Create a query button
    query_btn = Button(datawindow, text="Show Users",font=('book antique',9,'bold'), command=query,bg="#f70d1a",fg="white")
    query_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

    def hideusers():
        try:
            q_l.configure(text="",bg="#FFBF33")
        except NameError:
            pass

    # Hide User Button
    hideuser = Button(datawindow, text="Hide Users",font=('book antique',9,'bold'), command=hideusers,bg="#f70d1a",fg="white")
    hideuser.grid(row=9, column=0, columnspan=2, padx=25, pady=10, ipadx=140)

    # Create an Update Button
    edit_btn = Button(datawindow, text="Edit User Details",font=('book antique',9,'bold'), command=edit,bg="#f70d1a",fg="white")
    edit_btn.grid(row=7, column=0, columnspan=2, padx=25, pady=10, ipadx=125)

    # Create a Delete Button
    delete_btn = Button(datawindow, text="Delete User",font=('book antique',9,'bold'), command=delete,bg="#f70d1a",fg="white")
    delete_btn.grid(row=5, column=0, columnspan=2, padx=25, pady=10, ipadx=137)


    conn.commit()
    conn.close()

    datawindow.mainloop()

if __name__ == "__main__":
    main()

