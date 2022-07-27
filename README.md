# CRUD_app_using_python_and_mySQL
Here we will see how CRUP operations are run in databses using python.
**We are building a small login registration system using python and databases.**

**XAMP-** This is a software using which we can run databases on our own machine, so we dont need to use server like AWS.
1. XAMP offeres **Apache**- Using this we can work with our databases through our web-browser .
2. XAMP offers **MariaDB**- This gives us MySQL databases functionalities.


# Setup-
Required Libraries:
1.  **mysql.connector-** For conection between python and mysql. So, that we can make changes in mysql databases by writing codes in python. OR access the mysql databases using codes written in python.

![Screenshot (37)](https://user-images.githubusercontent.com/92416952/181185243-70e20372-4f0e-4a05-ade6-50ef53c46fdc.png)

Now, for accessing the database through browser using Apache- we need to put 'localhost/phpmyadmin/' in our browser. Now, we can access our database on this locally hosted server. 

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


