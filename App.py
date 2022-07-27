import sys
import mysql.connector
class Flipkart:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
        self.mycursor = self.conn.cursor()
        self.menu()


    def menu(self):
        user_input=input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Enter anything else to leave
        """)
        if user_input=='1':
            self.register()
        elif user_input=='2':
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name=input("Enter your name")
        password=input("Set a  password")
        email=input("Enter your email id")
        try:
            self.mycursor.execute(
            """INSERT INTO `credentials` (`id`, `name`, `email`, `password`) VALUES (NULL,'{}','{}','{}');""".format(
                name, email, password))
            self.conn.commit()
        except:
            print("Registration Failed")
        else:
            print("Registration Successful")
        self.menu()
    def login(self):
        email=input("Enter email")
        password=input("Enter password")
        self.mycursor.execute("""SELECT * FROM credentials WHERE email LIKE '{}' AND password LIKE '{}'""".format(email,password))
        data=self.mycursor.fetchall()
        if len(data)!=0:
            print("Welcome {} !!! You are logged in ".format(data[0][1]))
        else:
            print("Wrong credentials")
            self.menu()

omk=Flipkart()

