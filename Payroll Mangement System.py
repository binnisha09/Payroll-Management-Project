'''     PAYROLL MANAGEMENT PROJECT         '''

from os import remove, rename

#Operation 1- Addition of records for new employees in Employee file
def addrec():
    p=[]
    no= empcode()    
    fout= open('EMPLOYEE_FILE.TXT', 'a')
    for k in range(n):
        no+=1
        while True:
            na= input('Employee Name? ')
            if not na.isalnum() or na.isdigit():
                    print('Please enter proper Name')
                    na= input('Employee Name? ')
            elif na.isalpha() and len(na)<3 :
                print('Please enter Proper Name')
                na= input('Employee Name? ')
            else:
                break
      
        sex= input('Sex [F/M]? ')
        while True:
            if not sex.isalpha():
                print('Please enter Gender in one Character F for Female or M for Male')
                sex= input('Sex [F/M]? ')  
            elif sex.isalpha() and len(sex)!=1 :
                print('Please enter G1ender in one Character F for Female or M for Male')
                sex= input('Sex [F/M]? ')
            elif sex.upper()!='F' and sex.upper()!='M' :
                print('Please enter G2ender in one Character F for Female or M for Male')
                sex= input('Sex [F/M]? ')
            else:
                break  
        #Validation 3(b)- Validation for DOB ,year should be 1950 or after        
        print('Enter employee Date of Birth details')
        dob= dateval()
        while len(dob)!=10:
            print(dob)
            print('Please enter Correct DOB')
            dob= dateval()
                  
        print('Enter employee Date of Joining details')
        doj= dateval()
        while len(doj)!=10:
            print(doj)
            doj= dateval()

        des= input('Employee Designation? ')

        bs= input('Basic Salary? ')

        #Validation 3(b)- Validation for Phone numbers
        pn= input('Phone number?')
        validphone=phonevalidate(pn)
        while validphone==1:
            print('Please enter new phone number as it already exist')
            pn=input('Phone number?')
            validphone=phonevalidate(pn)
        while True:
            if(pn in p):
                print('Please enter new phone number as it already exist')
                pn=input('Phone number?')
            else:
                p+=[pn]
                break   
        mob= input('Mobile number? ')
        add= input('Address? ')
        data= str(no)+ ','+ na.upper()+ ','+ sex.upper()+ ','+ dob+ ','+ doj+ ','+ des.upper()+ ','+ bs+ ','+ str(pn)+ ','+ mob+ ','+ add.upper()+ '\n'
        fout.write(data) 
    print('Employee records successfully added')
    fout.close()
    
#Operation 2- Modification of existing records in Employee file except Employee number and Employee name

#Modification in Basic Salary
def modif1():
    fin=open('EMPLOYEE_FILE.TXT')
    fout=open('TEMPORARY.TXT','w')
    desig=input("Enter the Designation for which Basic Pay to be changed")
    inc=int(input("Enter the Amount to be increased"))
    for data in fin:
        data=data.strip()
        arr=data.split(',')
        if arr[5]==desig.upper():
            arr[6]=str(int(arr[6])+inc)
        rec=(',').join(arr)
        fout.write(rec +"\n")
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')

#Modification in Designation
def modif2():
    fin=open('EMPLOYEE_FILE.TXT')
    fout=open('TEMPORARY.TXT','w')
    code=int(input("Enter the Code for changing the Designation"))
    for data in fin:
        data=data.strip()
        arr=data.split(",")
        if int(arr[0])==code:
            print("Name :",arr[1])
            print("Designation:",arr[5],"\t\t", "Basic Salary :",arr[6])
            newdes=input('New designation:')
            newbs=input('New basic salary:')
            print("Are you sure yo want to change:\n Y/y for Yes or N/n for No")
            ch=input("ENter your Choice[Y/y or N/n]")
            if ch=='Y' or ch=='y':
                arr[5]=newdes
                arr[6]=newbs
                print("Record Updated....\n\n\n")
            else:
                print("Record Not Updated\n\n\n")
        rec=(',').join(arr)
        fout.write(rec +"\n")
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')
    

#Modification in Sex
def modif3():
    fin=open('EMPLOYEE_FILE.TXT')
    fout=open('TEMPORARY.TXT','w')
    found=0
    code=int(input("Enter the Code for changing the Gender"))
    for data in fin:
        data=data.strip()
        arr=data.split(",")
        if int(arr[0])==code:
            found=1
            print("Name :",arr[1])
            print("Gender:",arr[2],"\t\t")
            sex= input('Sex [F/M]? ')
            while True:
                if not sex.isalpha():
                    print('Please enter Gender in one Character F for Female or M for Male')
                    sex= input('Sex [F/M]? ')  
                elif sex.isalpha() and len(sex)!=1 :
                    print('Please enter G1ender in one Character F for Female or M for Male')
                    sex= input('Sex [F/M]? ')
                elif sex.upper()!='F' and sex.upper()!='M' :
                    print('Please enter G2ender in one Character F for Female or M for Male')
                    sex= input('Sex [F/M]? ')
                else:
                    print("Are you sure yo want to change:\n Y/y for Yes or N/n for No")
                    ch=input("ENter your Choice[Y/y or N/n]")
                    if ch=='Y' or ch=='y':
                        arr[2]=sex
                        print("Record Updated....\n\n\n")
                    else:
                        print("Record Not Updated\n\n\n")
                    break
    
        rec=(',').join(arr)
        fout.write(rec +"\n")
    if found==0:
        print("Employee COde not found..")
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')

    


#Modification in Date of Birth
def modif4():
    fin=open('EMPLOYEE_FILE.TXT')
    fout=open('TEMPORARY.TXT','w')
    found=0
    code=int(input("Enter the Code for changing the DOB"))
    for data in fin:
        data=data.strip()
        arr=data.split(",")
        if int(arr[0])==code:
            found=1
            print("Name :",arr[1])
            print("DOB:",arr[3],"\t\t")
            print("Enter a Correct Data of Birth")
            newdob=dateval()
            while len(newdob)!=10:
                print(newdob)
                print('Please enter Correct DOB')
                newdob=dateval()
            print("Are you sure yo want to change:\n Y/y for Yes or N/n for No")
            ch=input("ENter your Choice[Y/y or N/n]")
            if ch=='Y' or ch=='y':
                arr[4]=newdob
                print("Record Updated....\n\n\n")
            else:
                print("Record Not Updated\n\n\n")
        rec=(',').join(arr)
        fout.write(rec +"\n")
    if found==0:
        print("Employee Code not found..")
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')

#Modification in Date of Joining
def modif5():
    fin=open('EMPLOYEE_FILE.TXT')
    fout=open('TEMPORARY.TXT','w')
    found=0
    code=int(input("Enter the Code for changing the DOJ"))
    for data in fin:
        data=data.strip()
        arr=data.split(",")
        if int(arr[0])==code:
            found=1
            print("Name :",arr[1])
            print("DOJ:",arr[4],"\t\t")
            print("Enter a Correct Data of Joining")
            newdoj=dateval()
            while len(newdoj)!=10:
                print(newdoj)
                print('Please enter Correct DOJ')
                newdoj=dateval()
            print("Are you sure yo want to change:\n Y/y for Yes or N/n for No")
            ch=input("ENter your Choice[Y/y or N/n]")
            if ch=='Y' or ch=='y':
                arr[5]=newdoj
                print("Record Updated....\n\n\n")
            else:
                print("Record Not Updated\n\n\n")
        rec=(',').join(arr)
        fout.write(rec +"\n")
    if found==0:
        print("Employee Code not found..")
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')

#Modification in Phone number
def modif6():
    fin=open('EMPLOYEE_FILE.TXT')
    fout=open('TEMPORARY.TXT','w')
    code=int(input("Enter the Code for changing the Phone No"))
    newpn=input('New phone number? ')
    for data in fin:
        data=data.strip()
        arr=data.split(",")
        if int(arr[0])==code:
            print("Name :",arr[1])
            print("Phone No:",arr[7])
            print("Are you sure yo want to change:\n Y/y for Yes or N/n for No")
            ch=input("ENter your Choice[Y/y or N/n]")
            if ch=='Y' or ch=='y':
                arr[7]=newpn
                print("Phone Number updated....")
            else:
                print("Phone Number  not changed")
        rec=(',').join(arr)
        fout.write(rec +"\n")
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')

#Modification in Mobile number
def modif7():
    fin=open('EMPLOYEE_FILE.TXT')
    fout=open('TEMPORARY.TXT','w')
    newmn=input('New mobile number? ')
    for data in fin:
        data=data.strip()
        arr=data.split(",")
        arr[6]=newmn
        rec=(',').join(arr)
        fout.write(rec +"\n")
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')

#Modification in Address
def modif8():
    fin=open('EMPLOYEE_FILE.TXT')
    fout=open('TEMPORARY.TXT','w')
    newadd=input('New address? ')
    for data in fin:
        data=data.strip()
        arr=data.split()
        arr[7]=newadd
        rec=(',').join(arr)
        fout.write(rec +"\n")
    fin.close()
    fout.close()
    remove('EMPLOYEE_FILE.TXT')
    rename('TEMPORARY.TXT','EMPLOYEE_FILE.TXT')

#Operaton 3- Searching in Employee file using following fields: Employee number and Employee name

#Searching using Employee number
def search1():
    fout= open('EMPLOYEE_FILE.TXT', 'r')
    no= int(input('Emplyee number? '))
    found= 0
    for line in fout:
        line= line.strip()
        arr= line.split(',')
        if arr[0]== str(no):
            print(line)
            found= 1
    if found:
        print('Record found')
    else:
        print('Error: Record not found')
    fout.close()
    
#Searching using Employee name
def search2():
    fout= open('EMPLOYEE_FILE.TXT', 'r')
    na= int(input('Emplyee name? '))
    found= 0
    for line in fout:
        line= line.strip()
        arr=line.split(',')
        if arr[1]== na.upper():
            print(line)
            found= 1
    if found:
        print('Record found')
    else:
        print('Error: Record not found')
    fout.close()
        
#Operation 4- Input number of days worked and other deductions of each employee in Monthly Pay file
def mpayfile():
    m,y=0,1
    maxdays_work=0
    while True:
        if m not in [1,2,4,5,6,7,8,9,10,11,12] and y<2015 :
            m= int(input('Month? '))
            y= int(input('Year? '))
        else:
            break
    if m in [1,3,5,7,8,9,10,12]:
        maxdays_work= 27
    elif m in [4,6,9,11]:
        maxdays_work= 26
    elif m==2:
        if y%4==0 and y%100!=0 or y%400==0:
            maxdays_work= 25
        else:
            maxdays_work= 24
        
    file_name="Monthly_pay"+str(m)+"_"+str(y)+".txt"        
    fout= open(file_name, 'a')
    no= input('Employee Number? ')
    fin= open('EMPLOYEE_FILE.TXT','r')
    for line in fin:
        line= line.strip()
        arr= line.split(',')
        if arr[0]== str(no):
            print('Employee Name  :',arr[1])
            act_basic= int(arr[6])
            print('Basic  :',act_basic)
            #Validation 3(a)- Validation for Number of working days
            
        #Validation 4- Calculation of Basic salary
            leaves= int(input('Number of leaves taken in the month? '))
            if leaves>=0 and leaves<=maxdays_work:
                days= maxdays_work- leaves
                mon_sal=(act_basic//maxdays_work)* days
            else:
                while leaves>=0 and leaves<=days_work:
                    print('Please enter valid number of leaves')
                    leaves= int(input('Number of leaves taken in the month? '))
                    days= maxdays_work- leaves
            if days>=0 and leaves<=days:
                mon_sal=(act_basic//maxdays_work)* (days)
                da= round(0.55* mon_sal,2)
                hra= round(0.35* mon_sal,2)
                conv= round(0.15* mon_sal,2)
                gross= round(mon_sal+ da+ hra+ conv,2)
                itax= round(0.05* mon_sal,2)
                loan= round(0.1* mon_sal,2)
                ded= round(itax+ loan,2)
                net= round(gross- ded,2)
                print(mon_sal,da,hra,conv,gross,itax,loan,ded,net ," Added in month pay file\n\n")
                data= str(no)+ ','+ arr[1].upper()+','+ arr[5].upper()+ ','+ str(days)+ ','+ str(mon_sal)+ ','+ str(da)+ ','+ str(hra)+ ','+ str(conv)+ ','+ str(gross)+ ','+ str(itax)+ ','+ str(loan)+ ','+ str(net)+ '\n'
                fout.write(data)
    fout.close()

#Operation 5(a)- Displaying Slary statement
def sal_statement():
    a= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    m= int(input('Month? '))
    y= int(input('Year? '))
    if m in [1,3,5,7,8,9,10,12]:
        maxdays_work= 27
    elif m in [4,6,9,11]:
        maxdays_work= 26
    elif m==2:
        if y%4==0 and y%100!=0 or y%400==0:
            maxdays_work= 25
        else:
            maxdays_work= 24
    print('Salary Statement for the month of:', a[m-1], str(y))
    print(90*'-')
    print('ENo\tName\t\tDesignation\tBasic\tGross\tDeduction\tNet')
    print(90*'-')
    file_name="Monthly_pay"+str(m)+"_"+str(y)+".txt" 
    try: 
        with open(file_name,'r')as fin:
            for line in fin:
                line= line.strip()
                arr= line.split(',')
                ded=float(arr[9])+float(arr[10])
                print(arr[0],'\t',arr[1],'\t\t',arr[2],'\t',arr[4],'\t',arr[8],'\t',ded,'\t',arr[11])
                print(90*'-')
    except:
        print("No Pay file found for this Month and year")
             
#Operation 5(b)- Displaying Slary slip
def sal_slip():
    a= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    m= int(input('Month? '))
    y= int(input('Year? '))
    no= input('Employee number to display salary slip? ')
    file_name="Monthly_pay"+str(m)+"_"+str(y)+".txt"
    try: 
        with open(file_name, 'r')as fout:
            print('Salary Slip for the month of:',a[m-1],str(y))
            for line in fout:
                line= line.strip()
                arr= line.split(',')
                if arr[0]== str(no):
                    print("*"*30,"\tABC COMPANY \t","*"*30,"\n\n")
                    print(90*'=')
                    print('Employee No:',arr[0]+'\t\t\t\t\t'+'Employee Name:',arr[1])
                    print(90*'-')
                    print('Designation No:'+'\t\t',arr[2]+'\t\t\t\t'+'Basic:'+'\t\t',arr[4])
                    print(90*'-')
                    print('Working days'+'\t'+arr[3]+'\t\t\t\t\t'+'Deductions'+'\t'+ str(float(arr[9])+float(arr[10]))) 
                    print('DA'+'\t\t',arr[5])
                    print('HRA'+'\t\t',arr[6])
                    print('Conveyance'+'\t',arr[7])
                    print(90*'-')
                    print('Gross Pay'+'\t'+arr[8]+'\t\t\t\t\t'+'Net'+'\t\t'+arr[11])
                    print(90*'=')
                    print("\n\n")
                else:
                    print("Employee Number is Invalid")
    except:
            print("Pay File for This Month and Year does not exist")
        
            
#Validation 1- Automatic Generation of Employee Number
def empcode():
    code= 1000
    fin= open('EMPLOYEE_FILE.TXT', 'r')
    fin.seek(0)
    first_char= fin.read(1)
    if not first_char:
         code=1000
    else:
        for line in fin:
            line= line.strip()
            rec= line.split(',')
            code= int(rec[0])
    return(code)

#Validation 2- Validations for inputted date
def dateval():
    d= int(input('Day? '))
    m= int(input('Month? '))
    y= int(input('Year? '))
    maxd= 0
    if m in [1,3,5,7,8,9,10,12]:
        maxd= 31
    elif m in [4,6,9,11]:
        maxd= 30
    elif m== 2:
        if y%4== 0 and y%100!= 0 or y%400== 0:
            maxd= 29
        else:
            maxd= 28
    if maxd==0:
        return('Please input valid month')
    elif (d<1 or d>maxd):
        return('Please input valid Date')
    elif y<1950:
        return ("Please input valid Year it should be 1950 or after")
    else:
        if len(str(m))==1:
            m='0'+str(m)
        if len(str(d))==1:
               d='0'+str(d)
        return (str(d)+"/"+str(m)+"/"+str(y))

def phonevalidate(n):
    fin=open('EMPLOYEE_FILE.TXT','r')
    fin.seek(0)
    found=0
    for line in fin:
        line=line.strip()
        rec=line.split(',')
        ph=rec[7]
        if ph==n:
            found=1
            print("Same Phone Number Found in our records")
            break
    if len(fin.read())==0:
        found=0
        
    return(found)
    

while True:
    print('''Main Menu:
1.Addition of new Employee records in Employee file
2.Addition of new Employee records in Monthly Pay file
3.Modification in existing records
4.Search for Employee records
5.Print salary statement
6.Print salary slip
0.Exit Menu''')
    ch=int(input('Choice[0-6]? '))
    if ch==1:
        n=int(input('Number of employees to be added? '))
        addrec()
    elif ch==2:
        mpayfile()
    elif ch==3:
        print('''Modification in Employee details Menu:
1. Modify basic salary
2. Modify designation
3. Modify sex
4. Modify date of birth
5. Modify date of joining
6. Modify phone number
7. Modify mobile number
8. Modify address
0. Exit Menu''')
        a=int(input('Choose[0-8]? '))
        while True:
            if a==1:
                modif1()
                break
            elif a==2:
                modif2()
                break
            elif a==3:
                modif3()
                break
            elif a==4:
                modif4()
                break
            elif a==5:
                modif5()
                break
            elif a==6:
                modif6()
                break
            elif a==7:
                modif7()
                break
            elif a==8:
                modif8()
            elif a==0:
                break 
    elif ch==4:
        print('''Searching for Employee details Menu:
1. Searching by Employee number
2. Searching by Employee name
0. Exit Search Menu''')
        a= int(input('Choose[0-2]? '))
        while True:
            if a==1:
                search1()
                break
            elif a==2:
                search2()
                break
            elif a==0:
                break
    elif ch==5:
        sal_statement()
    elif ch==6:
        sal_slip()
    elif ch==0:
        break
