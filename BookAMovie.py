import sys                                                                                  #importing sys for exiting program
import mysql.connector as sql                                                               #connecting sql and python
conn=sql.connect(host="localhost",user="root",passwd="ayathmysql",database="PROJECTXII")
if conn.is_connected():
    print("Successfully Connected")
cur=conn.cursor()

print("\n\n\n\t\t\t\t\t*******************WELCOME TO COCHIN THEATER******************")

def login():                                                          #defining login function
    acc = input("\nDO YOU HAVE A ACCOUNT (Y/N):")
    if acc=='y' or acc=='yes' or acc=='Y' or acc=='YES' or acc=='Yes':
        user=input("\nENTER USER ID:")                                #loging in with exsisting account
        passwd=input("\nENTER PASSWORD:")
        pno=input("\nENTER YOUR PHONE NO:")

        print("\n-------LOGIN SUCCESSFUL-------")

    elif acc=='n' or acc=='no' or acc=='N' or acc=='NO' or acc=='No':
        nam = input("\nENTER YOUR FULL NAME(IN CAPS):")               #creating a new account
        pno = int(input("\nENTER YOUR PHONE NO:"))
        user = input("\nENTER YOUR USER ID(use only lowercase):")
        passwd = input("\nENTER YOUR PASSWORD(atleast 8 words):")

        print("\n-------ACCOUNT CREATED SUCCESSFULLY-------")

    else:
        print("Error occured, please try again")
        print(login())

    

    
    
def menu():                                                           #defining menu function
    while True:                                                       #infinite loop
                  print("\n\n\t\tMENU")                               
                  print("PLEASE CHOOSE ANY OPTION FROM BELOW")        #display of menu
                  print("1.Movie Details")
                  print("2.Show Times")
                  print("3.Reservation of Ticket")
                  print("4.Display Ticket Status")
                  print("5.Cancellation of Ticket")
                  print("6.Exit")

                  print("\n")

                  opt=int(input("ENTER OPTION NO:"))                  #menu number entered by user
                  try:
                      if opt==1:
                          details()
    
                      if opt==2:
                          showtimes()

                      if opt==3:
                          reservation()

                      if opt==4:
                          display()

                      if opt==5:
                          cancellation()

                      if opt==6:
                          
                          print("Thank you for choosing Cochin Theater. Have a nice day!")          #for exiting program
                          sys.exit()     

                      else:
                          print("Invalid option, please try again.")
                          print(menu())


                  except ValueError:
                      print("Wrong Entry, try again.")
                      print(menu())


def details():                                           #function for displaying the names of movies showing
    print("Here are the list of the movies:")
    print('\n')
    m="SELECT * FROM movie_name"
    cur.execute(m)
    r=cur.fetchall()
    for i in r:
        print(i)
    print('\n')
    a=input("Do you want to go back to menu?(Y/N):")
    print(a)
    if a=='y' or a=='yes' or a=='Y' or a=='YES':
        print(menu())                                    #calling main program for menu
    elif a=='n' or a=='no' or a=='N' or a=='NO':
        print("Thank you for your time!")
        sys.exit()

        
 
def showtimes():                                         #function for displaying                                   
    print("Here are the timings for the movies")
    print('\n')
    n='SELECT * FROM show_times'
    cur.execute(n)
    s=cur.fetchall()
    for i in s:
        print(i)
    print('\n')
    b=input("Do you want to go back to menu?(Y/N):")
    if b=='y' or b=='yes' or b=='Y' or b=='YES':
        print(menu())                                    #calling main program for menu
    elif b=='n' or b=='no' or b=='N' or b=='NO':
        print("Thank you for your time!")
        sys.exit()
    
    

def reservation():
    print("PLEASE ENTER YOUR DETAILS FOR THE FOLLOWING:-")
    print("!PLEASE ENTER YOUR USER ID WITHOUT ANY MISTAKES!")
    user=str(input("ENTER YOUR USER ID:"))                     #unique user id for each user
    print('\n')
    fname=str(input("Enter your First name(IN CAPS):"))
    print('\n')
    lname=str(input("Enter your Last name(IN CAPS):"))
    print('\n')
    movie=str(input("Enter the Movie name to watch:"))
    print('\n')
    ticket=str(input("How many seats?:"))
    print('\n')

    print("[1.Front  2.Middle  3.Back]")                                 #choosing seating position
    pos=input("Which position do you want?:")
    if pos=='Front' or pos=='front' or pos=='FRONT' or pos=='1':
        post="Front"
    elif pos=='Middle' or pos=='middle' or pos=='MIDDLE' or pos=='2':
        post="Middle"
    elif pos=='Back' or pos=='back' or pos=='BACK' or pos=='3':
        post="Back"
    print("Confirmation:Position you choosed is",post)
    print('\n')
        
    ar=("----------- \n\n1 2 3 4 5 6 \n0 0 0 0 0 0 A \n0 0 0 0 0 0 B \n0 0 0 0 0 0 C \n0 0 0 0 0 0 D")      #theater demonstration
    print(ar)
    print('\n')
    ar1=str(input("Choose the seats(Example: 3A,4B..):"))
    print("Confirmation: Seats you have choosen are",ar1)
    print('\n')

    sn=input("Do you prefer any snacks?(Y/N):")                       
    if sn=='Y' or sn=='y' or sn=='YES' or sn=='yes' or sn=='Yes':               #choosing snacks by the user
        p='SELECT * FROM snacks'
        cur.execute(p)
        q=cur.fetchall()
        for i in q:
            print(i)
        sc=str(input("Which snack do you want:"))                         
    elif sn=='n' or sn=='N' or sn=='NO' or sn=='No' or sn=='no':
        print("Noted.")
        sc="NIL"
    print('\n')

    dr=input("Do you prefer any drinks(Y/N):")
    if dr=='Y' or dr=='y' or dr=='YES' or dr=='Yes' or dr=='yes':               #choosing drinks by the user
        d='SELECT * FROM drinks'
        cur.execute(d)
        w=cur.fetchall()
        for i in w:
            print(i)
        dn=str(input("Which drink do you want:"))
    elif dr=='N' or dr=='n' or dr=='NO' or dr=='no' or dr=='No':
        print("Noted.")
        dn="NIL"
    print('\n')

    #appending details to the table
    sql_insert="insert into details values(""'"+user+"','"+fname+"','"+lname+"','"+movie+"','"+ticket+"','"+post+"','"+ar1+"','"+sc+"','"+dn+"')"    
    cur.execute(sql_insert)
    print("REGISTERED SUCCESSFULLY")
    conn.commit()
    print('\n')
    ans=input("Do you want to go back to menu?:")
    if ans=='n' or ans=='N' or ans=='no' or ans=='NO' or ans=='No':
        print("Thank your for your time!")
        cur.close()
        conn.close()
    elif ans=='y' or ans=='Y' or ans=='yes' or ans=='YES' or ans=='Yes':
        print(menu())


def display():
    try:
        conn=sql.connect(host="localhost",user="root",passwd="ayathmysql",database="PROJECTXII")
        cur=conn.cursor()
        while True:
            print("TO DISPLAY YOUR TICKET DETAILS,PLAESE ENTER THE FOLLOWING DETAILS")
            print('\n')
            user_id=input("ENTER YOUR USER ID:")                                                     #entering your unique userid
            qry='select * from details where UserID=("{}")'.format(user_id)
            cur.execute(qry)
            cols=cur.column_names
            rec=cur.fetchone()
            if rec==None:
                print("Sorry! No Record for User:",user_id)
            else:                                                                                    #displaying ticket status
                print("-"*20)
                for i in range(len(rec)):
                    print(cols[i].upper(),'\t:',rec[i])
                    print("-"*20)
                    print('\n')
            ans=input("Do you want to go back to menu(Y/N):")
            if ans =='n' or ans=='no' or ans=='NO' or ans=='No':
                print("Thank you for your time!")
                sys.exit()
            elif ans=='y' or ans=='Y' or ans=='Yes' or ans=='YES' or ans=='yes':
                print(menu())
    except ValueError:
        return None
            

def cancellation():
    try:
        conn=sql.connect(host='localhost',user='root',passwd='ayathmysql',database='projectxii')
        cur=conn.cursor()
        conn.autocommit=True
        while True:
            print("TO CANCEL YOUR TICKET RESERVATION, PLEASE ENTER THE FOLLOWING DETAILS")
            print('\n')
            user_id=input("ENTER YOUR USERID:")                                                      #entering unique userid
            qry='select * from details where UserID=("{}")'.format(user_id)
            cur.execute(qry)
            rows=cur.fetchall()
            if rows==[]:
                print("Sorry! No tickets are reserved for",user_id)
                print('\n')
                cn=input("Do you want to go back to go back to menu(Y/N):")
                if cn=='y' or cn=='Y' or cn=='yes' or cn=='YES' or cn=='Yes':
                    print(menu())
                elif cn=='n' or cn=='N' or cn=='NO' or cn=='no' or cn=='No':
                    print("Thank you for your time!")
                    sys.exit()
            else:                                                                                   #Cancelling your ticket reservation
                ans=input("ARE YOU SURE YOU WANT TO CANCEL YOUR MOVIE TICKET(y/n)?:")
                print('\n')
                if ans=='y' or ans=='Y' or ans=='yes' or ans=='YES' or ans=='Yes':
                    qr='delete from details where UserID=("{}")'.format(user_id)
                    cur.execute(qr)
                    conn.commit()
                    print("Tickets reserved for User:",user_id,"has been Cancelled!")
                    print('\n')
                    ch=input("Do you want to go back menu(Y/N):")
                    if ch=='n' or ch=='N' or ch=='no' or ch=='NO' or ch=='No':
                        print("Thank you for your time")
                        break
                        cur.close()
                        conn.close()
                    elif ch=='y' or ch=='Y' or ch=='yes' or ch=='YES' or ch=='yes':
                        print(menu())
                elif ans=='n' or ans=='N' or ans=='no' or ans=='NO' or ans=='No':
                    print("Your Cancellation request has been declined!")
                    ch=input("Do you want to go back menu(Y/N):")
                    if ch=='n' or ch=='N' or ch=='no' or ch=='NO' or ch=='No':
                        print("Thank you for your time")
                        break
                        cur.close()
                        conn.close()
                    elif ch=='y' or ch=='Y' or ch=='yes' or ch=='YES' or ch=='yes':
                        print(menu())
    except ValueError:
        return None
        
    
login()
menu()

    


          
    
            
    

        


    
              
          

    
      

        
