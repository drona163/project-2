print("1. Insert new data ")
print( "2. Update the table")
print("3.Delete the record from the table")
print(" 4. Search a record from the table")
print(" 5. Display the table")
print("6.Quit")
choice=input("Enter the function you want to apply in the Anime table from this list:")
if choice==1:    # To insert new data
    import mysql.connector as sq
    def insert():
            Name=input("Enter the name of Anime you want to enter:")
            Genre= input("Enter the genre of the anime you are insert in:")
            DOR=input("Enter the date of release of the anime (in YYYY-MM-DD format):")
            Episodes=int(input("Enter the No. of Epispodes in the Anime:"))
            Site=input("Enter a suggested site to watch the Anime:")
          
            mydb = sq.connect(host="localhost",user="root",password="root",database="project")

            mycursor = mydb.cursor()

            sql = "INSERT INTO Anime ( Anime_Name, Genre, Date_of_release, No_of_episodes, Site) VALUES (%s, %s,%s,%s,%s)"
            val = (Name, Genre,DOR, Episodes, Site)
            mycursor.execute(sql, val)


            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            #col=0
#sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue",command=insert).place(x = 100, y = 230)
#top.mainloop
elif choice==2:  #To update
    def update():
        up=input("Enter the Anime name whose record you want to update:")
        field= input("Enter the field you want to update:")
        fieldch=input("Enter the record you want thr field to change to:")
        import mysql.connector as sq
        mydb= sq.connect(host="localhost",user="root",passwd="root",database="project")
        cursor=mydb.cursor()
        update="UPDATE Anime set field like '%{}%' WHERE Anime_Name like '%{}%'".fromat(fieldch,up)
        cursor.execute(update)
        mydb.commit()
        #col=0
elif choice==3:
    def delete():
        dele=input("Enter the Anime name whose data you want to delete:")
        import mysql.connector as sq
        c=sq.connect(host="localhost",user="root",passwd="root",database="project")
        cursor=c.cursor()
        sql = "DELETE FROM Anime WHERE Anime_Name like '%{}%'".format(dele)
        cursor.execute(sql)
        c.commit()
        #col=0
#To search a record
elif choice==4:
    def search():
        import mysql.connector as mysql
        try:
            conn=mysql.connect(host='localhost',user='root',password='root',db='project')
            cmd=conn.cursor()
    
            pat=input("Enter Anime Name whose record you want to see:")
    
            q="select * from anime where Anime_Name like '%{}%'".format(pat)
            cmd.execute(q)
            print("Record is available")
        except :
            print("Record is not available")
        #col=0
            

#To Display the data
elif choice==5:
    def display():
        import mysql.connector as sq

        mydb = sq.connect(host="localhost",user="root",password="root",database="project")

        cursor = mydb.cursor()

        sql = "SELECT * FROM Anime ORDER BY Anime_Name"

        cursor.execute(sql)
            

        myresult = cursor.fetchall()
        col=0

        for x in myresult:
            print( x)
#elif choice==6:
    #break
   
