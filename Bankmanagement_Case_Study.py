
from datetime import datetime
from datetime import date
from dateutil.tz import gettz
now = datetime.now(tz=gettz('Asia/Kolkata'))
	

class BankManagement:
    
    
    
    
    def calculateAge(self,birthDate):# method to caluclate age according to birth month and day
    	today = datetime.today()
    	age = today.year - birthDate.year -((today.month, today.day) <(birthDate.month, birthDate.day))
    
    	return age
    
    def Account_creation(self,account_number):#method for account creation
        
        
        name= input('Enter Account holder Name')
        t=dict()
        dob=int(input('Date of Birth 1 to 31'))
        mob=int(input('month of Birth'))
        yob=int(input('year of Birth'))
        f_name=input('enter father name')
        gender=input('enter Male or Female or others')
        curr_age=bankobj.calculateAge(date(yob,mob,dob))
        if curr_age>18:
            print("You are major so we can proceed")
        else:
            print("We can create Minor Account") 
       
        phone_num=input('enter phone number')
        userid=input('enter your userid ')
        u.append(userid)
        account_pin_number=input("ENTER YOUR 6 DIGIT PIN (ONLY DIGITS ARE ALLOWED)")
        p.append(account_pin_number)
        
        account_directory=dict()
        if name not in all_account_directory:
            
            account_directory.__setitem__('Acc_Name',name) # to set key value pair "Acc_Name": "Name of Account Holder"
            account_directory.__setitem__('Acc_No',account_number)
            account_directory.__setitem__('Gender',gender)
            account_directory.__setitem__('Year of Birth',yob)
            account_directory.__setitem__('Age',curr_age)
            account_directory.__setitem__('father Name',f_name)
            account_directory.__setitem__('phone_num',phone_num)
            account_directory.__setitem__('Balance',0)
            account_directory.__setitem__('User id',userid)
            account_directory.__setitem__('Pin_Number',account_pin_number)
        
        all_account_directory.__setitem__(account_number,account_directory)#using nested Dictionary where each account is stored as a dictionary with Account number as a key in dictionary all_account_directory 
        print("Account Created Sucessfully ")
        print("Account Nunmber ",account_number)
        
        
        return userid,account_pin_number

    
    def passbook(self,account_number):#method to display Bank passbook
        for key, value in (all_account_directory[account_number]).items():
            if key!='Pin_Number ':# Blocking the Secret Pin_Number
                print(f"{key}: {value}")
        
        
    def deposit(self,account_number):
        # method to deposit money in bank
        amount=int(input('enter deposit amount'))
        all_account_directory[account_number]['Balance']=(all_account_directory[account_number]['Balance'])+amount
        date_time = now.strftime("%m/%d/%Y %H:%M:%S")
        message=("Deposit of ",amount)
        t.__setitem__(date_time,message)
        
        
        # accsesing our account balance through "all_account_directory" as our account is stored as dictionary with account number as index
    def withdraw(self,account_number):# method to withdraw money in bank 
        need=int(input('enter withdraw amount'))
        if all_account_directory[account_number]['Balance']>need:
            all_account_directory[account_number]['Balance']=all_account_directory[account_number]['Balance']-need
            date_time = now.strftime("%m/%d/%Y %H:%M:%S")
            message=("Withdrawal of ",need)
            t.__setitem__(date_time,message)
        else:
            print('Insufficient Balance')
        
    def balance_enquiry(self,account_number):# method to know account balance
        bal=(all_account_directory[account_number]['Balance'])
        print("CURRENT BALANCE : ",bal)
    def fund_transfer(self):# method to transfer amount between accounts
        from_ac_no=int(input("Enter your Account number"))
        to_ac_no=int(input("Enter reciever Account number"))
        amount=int(input('enter amount you want to send'))
        if all_account_directory[from_ac_no]['Balance']>amount:
           all_account_directory[to_ac_no]['Balance']+=amount 
           all_account_directory[from_ac_no]['Balance']-=amount
        print(amount,'Transferred Successfully from ',end="")
        print('from',all_account_directory[from_ac_no]['Acc_Name'])
        print('to',all_account_directory[to_ac_no]['Acc_Name'])
        date_time = now.strftime("%m/%d/%Y %H:%M:%S")
        message=(amount,"Transferred from,",all_account_directory[from_ac_no]['Acc_Name']," and recieved by ",all_account_directory[to_ac_no]['Acc_Name'] )
        t.__setitem__(date_time,message)
        t.__setitem__(date_time,message)
        
    def transaction_history(self,account_number):
        transactions.__setitem__(account_number,t)
        for key, value in transactions[account_number].items():
            
            print(f"{key}: {value}")
        
        
            
if __name__== "__main__":
    all_account_directory=dict()
    transactions=dict()
    t=dict()
    account_number=0
    Balance=0
    u=[]
    p=[]
    
    bankobj=BankManagement()
    while(True):
        
        print("1. ACCOUNT CREATION ")
        print('2. PASBOOK ')
        print("3. DEPOSIT ")
        print("4. WITHDRAW ")
        print("5. BALANCE ENQUIRY ")
        print("6. FUND TRANSFER ")
        print("7. TRANSCATION HISTORY")
        print("8. EXIT")
        
        choice=int(input('Enter choice : '))
        if choice>=1 or choice<=8:
            if choice==1:
                usid,pswd=bankobj.Account_creation(account_number)
                
                account_number+=1
            elif choice==2:
                ac_no= int(input("enter account number : "))
                uid=input('enter user_id : ')
                psd=input('enter password: ')
                if uid==u[ac_no] and psd==p[ac_no]:
                    
                    bankobj.passbook(ac_no)
            elif choice==3:
                ac_no= int(input("enter account number: "))
                uid=input('enter user_id : ')
                psd=input('enter password: ')
                if uid==u[ac_no] and psd==p[ac_no]:
                    
                    bankobj.balance_enquiry(ac_no)
                    bankobj.deposit(ac_no)
                    bankobj.balance_enquiry(ac_no)
            elif choice==4:
                ac_no= int(input("enter account number"))
                uid=input('enter user_id : ')
                psd=input('enter password: ')
                if uid==u[ac_no] and psd==p[ac_no]:
                    
                    bankobj.balance_enquiry(ac_no)
                    bankobj.withdraw(ac_no)
                    print("After withdrawal")
                    bankobj.balance_enquiry(ac_no)
            elif choice==5:
                ac_no= int(input("enter account number"))
                uid=input('enter user_id : ')
                psd=input('enter password: ')
                if uid==u[ac_no] and psd==p[ac_no]:
                    bankobj.balance_enquiry(ac_no)
            elif choice==6:
                ac_no= int(input("enter account number"))
                uid=input('enter user_id : ')
                psd=input('enter password: ')
                if uid==u[ac_no] and psd==p[ac_no]:
                    bankobj.fund_transfer()
            elif choice==7:
                ac_no= int(input("enter account number"))
                uid=input('enter user_id : ')
                psd=input('enter password: ')
                if uid==u[ac_no] and psd==p[ac_no]:
                    
                    bankobj.transaction_history(ac_no)
            elif choice==8:
                print('THANK YOU')
                break                

    
    

