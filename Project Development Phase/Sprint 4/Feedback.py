import mysql.connector


def submit(name,email,phone_number,message):
   mydb = mysql.connector.connect(host="localhost",user="root",password="2002",database="submit")
   mycursor = mydb.cursor()
   sql = "INSERT INTO customers (Name,Email,Phone_number,Feedback) VALUES (%s, %s,%s,%s)"
   val = (name,email,phone_number,message)
   mycursor.execute(sql, val)
   mydb.commit()

"""
CREATE DATABASE submit;
USE submit;
CREATE TABLE submit(ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,Name varchar(30),Email varchar(40),Phone_number varchar(20),Feedback varchar(300));
INSERT INTO submit(Name, Email, Phone_number, Feedback) VALUES ('trj', 'trj08012002@gmail.com', '6369671812', 'Add a live virutal assistance on chatbot');
show tables;
select * from submit;
"""
