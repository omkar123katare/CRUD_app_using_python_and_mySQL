# CRUD_app_using_python_and_mySQL
Here we will see how CRUP operations are run in databses using python.
**We are building a small login registration system using python and databases.**

**XAMP-** This is a software using which we can run databases on our own machine, so we dont need to use server like AWS.
1. XAMP offeres **Apache**- Using this we can work with our databases through our web-browser .
2. XAMP offers **MariaDB**- This gives us MySQL database management functionalities.


# Setup-
Required Libraries:
1.  **mysql.connector-** For conection between python and mysql. So, that we can make changes in mysql databases by writing codes in python. OR access the mysql databases using codes written in python.

![Screenshot (37)](https://user-images.githubusercontent.com/92416952/181185243-70e20372-4f0e-4a05-ade6-50ef53c46fdc.png)

Now, for accessing the database management system through browser using Apache- we need to put 'localhost/phpmyadmin/' in our browser. Now, we can access our databases on this locally hosted DBMS server. This is our DBMS (a software that interracts with our database by issuing appropriate requests typically in SQL statements.)

Changes made using python in the MySQL database will be reflected here.

![Screenshot (38)](https://user-images.githubusercontent.com/92416952/181186719-0412fa04-4e27-4f7b-a18b-044641ad014a.png)

2.  We need to create a 'connection' object to pass in all the credentials like host name,user name, password, database name. **self.conn=mysql.connector.connect(host="localhostw",user="root",password="",database="users")**
We commit the changes made to the database usgn this object (after we make change to ht etable by running queries using the cursor object) by **self.conn.commit()**
     
3.  We need to create a cursor object to communicate with the database.
This is our database server. so, this is a computer where all our databases are stores.
**self.mycursor=self.conn.cursor()**
We use cursor object to run the SQL queries using self.mycursor.execute(""" SQL QUERY """)

In database, we perform only 4 types of operations
1.**C**rud.
2.**R**etrieve.
3.**U**pdate.
4.**D**elete.


Lets create an account for Hritik Roshan !!!

![Screenshot (39)](https://user-images.githubusercontent.com/92416952/181248774-f5578dd0-98ef-4a5d-aa05-f7eca8a8a533.png)

Lets see if it got reflected in our MySQL database :

![Screenshot (41)](https://user-images.githubusercontent.com/92416952/181249016-ca439247-e778-44af-956a-c2eb61c4f329.png)

Now that hritik's account is created, lets login to his account:

![Screenshot (40)](https://user-images.githubusercontent.com/92416952/181249227-2397a67b-c40f-4422-ba79-122c33aa5b04.png)

**Logged in !!!!**



