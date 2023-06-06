#PROJECT OF PAYROLL MANAGEMENT
print("\t\t\t\t\t\tWelcome to the 'INNOVATIVE PAYROLL SERVICE'.")
print("The Payroll management system that meets all your needs to maintain an employees overall account.")
print("LET'S BEGIN WITH INTIALIZATION PROCESS.")

import mysql.connector
import datetime

db=input("Enter name of your database : ")
mydb=mysql.connector.connect(host='localhost', user='root', password='GannuJi#123')
mycursor=mydb.cursor()
sql="CREATE DATABASE if not exists %s"%(db,)
mycursor.execute(sql)
print("Data base created successfully.....")
#mycursor=mydb.cursor()
mycursor.execute("Use "+db)
Tablename=input("Enter name of Table to be created : ")
query="Create table if not exists "+Tablename+"\
(empno int primary key,\
name varchar(30) not null,\
job varchar(15),\
BasicSalary int,\
DA float,\
HRA float,\
GrossSalary float,\
Tax float,\
NetSalary float)"
#print(query)

print("Table "+Tablename+" Created successfully...")
print("Intialization Completed.Now you can easily manitain your employees record.") 
mycursor.execute(query)

while True:
    print('\n\n\n')
    print("*"*95)
    print('\t\t\t\t\tMAIN MENU')
    print("*"*95)
    print('\t\t\t\tPress 1 For Adding Employee records') 
    print('\t\t\t\tPress 2 For Displaying Record of all the employees')
    print('\t\t\t\tPress 3 For Displaying Record of a particular employee')
    print('\t\t\t\tPress 4 For Deleting  Record of all the employees')
    print('\t\t\t\tPress 5 For Deleting a Record of a particular employee')
    print('\t\t\t\tPress 6 For Modification in a record')
    print('\t\t\t\tPress 7 For displaying  salary slip of all the Employees')
    print('\t\t\t\tPress 8 For Displaying Salary slip of a particular Employee')
    print('\t\t\t\tPress 9 For Exit')
    print('Enter Choice...',end='')
    choice=int(input())
    if choice==1:
        try:
            print("Enter Employee information.......")
            mempno=int(input("Enter employee no: "))
            mname=input("Enter employee name : ")
            mjob=input("Enter employee job :")
            mbasic=float(input("enter basic salary :"))
            if mjob.upper()=='OFFICER':
                mda=mbasic*0.5
                mhra=mbasic*0.35
                mtax=mbasic*0.2
            elif mjob.upper()=='MANAGER':
                 mda=mbasic*0.45
                 mhra=mbasic*0.38
                 mtax=mbasic*0.15
            else:
                 mda=mbasic*0.40
                 mhra=mbasic*0.25
                 mtax=mbasic*0.1
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec=(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet)
            query="insert into "+Tablename+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,rec)
            mydb.commit()
            print("Record added successfully....")
        except Exception as e: 
            print("something went wrong ",e)

    elif choice==2:
           try:
             query="SELECT * from "+Tablename
             mycursor.execute(query)
             myrecords=mycursor.fetchall()
             for rec in myrecords:
                 print(rec)
           except:
               print("something went wrong")

    elif choice==3:
        try:
            en=input("Enter employee no. of the record to be displayed ...")
            query="SELECT * from "+Tablename+" WHERE empno="+en
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\nRecord of Employee No: "+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==0:
                print("Nothing to display")
        except :
            print("something went wrong ")
            
    elif choice==4:
        try:
            ch=input("Do you want to delete all the records (y/n) ...")
            if ch.upper()=='Y':
                mycursor.execute('DELETE from '+Tablename)
                mydb.commit() 
                print('All the records are deleted ....')
        except :
            print("something went wrong ")

    elif choice==5:
        try:
            en=input("Enter employee no. of the record to be deleted ...")
            query="DELETE from "+Tablename+" WHERE empno="+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print("Deletion Done")
            else:
                print('Employee no ',en,' not found')
        except:
            print("something went wrong ")        
        
    elif choice==6:
         try:
             en=input('Enter employee no. of the record to be modified...')
             query='SELECT * from '+Tablename+' WHERE empno='+en
             mycursor.execute(query)
             myrecord=mycursor.fetchone()
             c=mycursor.rowcount
             if c==0:
                 print('Empno '+en+' does  not exists')
             else:
                 mname=myrecord[1]
                 mjob=myrecord[2]
                 mbasic=myrecord[3]
                 print('empno : ',myrecord[0])
                 print('name  : ',myrecord[1])
                 print('job   : ',myrecord[2])
                 print('basic : ',myrecord[3])
                 print('da    : ',myrecord[4])
                 print('hra   : ',myrecord[5])            
                 print('gross : ',myrecord[6])
                 print('tax   : ',myrecord[7])
                 print("Type value to modify or just press Enter for no change")
                 x=input("Enter name ")
                 if len(x)>0:
                     mname=x
                 x=input('Enter job ')
                 if len(x)>0:
                     mjob=x
                 x=input('Enter basic salary ')
                 if len(x)>0:
                     mbasic=float(x)
                 query='Update '+Tablename+' SET name ='+"'"+mname+"'"+','+'job='+"'"+mjob+"'"\
                        +','+'Basicsalary='+str(mbasic)+' WHERE empno='+en
                 print(query)
                 mycursor.execute(query)
                 mydb.commit()
                 print("Record modified .......")
                 
         except:
            print("something went wrong ")

    elif choice==7:
         try:
             query='SELECT * from '+Tablename
             mycursor.execute(query)
             myrecords=mycursor.fetchall()
             print("\n\n\n")
             print(95*'*')
             print("\t\t\t\t\t\t\tSalary Slip")
             now=datetime.datetime.now()
             print("Current date and Time: ",end='')
             print(now.strftime("%Y-%m-%d %H:%M:%S"))
             print()
             print(95*'*')
             for rec in myrecords:
                 print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f' %rec)
                     
             print(95*'-')
             
         except:
            print("Something went wrong ")
            
    elif choice==8:
         try:
             en=input('Enter employee no. of the record whose salary slip is to displayed...')
             query='SELECT * from '+Tablename+" WHERE EMPNO="+en
             print(query)
             mycursor.execute(query)
             
             myrecords=mycursor.fetchone()
             print("\n\n\n")
             print(95*'*')
             print("\t\t\t\tSalary Slip")
             now=datetime.datetime.now()
             print("Current date and Time: ",end='')
             print(now.strftime("%Y-%m-%d %H:%M:%S"))
             print()
             print(95*'*')
             print(myrecords)
             print(95*'-')
             
         except:
            print("Something went wrong ")

    elif choice==9:
       break
    else:
       print("WRONG CHOICE ....")
             
   


    
     
                         
                 
                 
                     
        
       
        

                              
                              
                              
                              

                              
