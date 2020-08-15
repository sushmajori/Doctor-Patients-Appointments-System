class person(object):
    def __init__(self,name,email,contact,aadhar,dept,docin,timein,date1):
        self.name = name
        self.email = email
        self.contact = contact
        self.aadhar = aadhar
        
        self.dept=dept
        self.docin=docin
        self.timein=timein1
        
        self.date1=date1
        
    @property
    def email(self):
        return(self.__email)
    @email.setter
    def email(self,email):
        self.__email = email

    """@property
    def contact(self):
        return(self.__contact)
    @contact.setter
    def contact(self,contact):
        
        while True:
            if(len(contact) == 10) :                          #validation
                self.__contact=contact
                break
            else:
                self.__contact=input("Invalid contact number,try again:")
    """
    @property
    def contact(self):
        return(self.__contact)
    @contact.setter
    def contact(self,contact):
        self.__contact = contact
    """
    def contact(self):
        return (self.__contact)
    @contact.setter
    def contact(self,contact):
        while True:
            if(len(contact) |= 11) :                          #validation
                self.__contact=contact
                break
            else:
                #contact=raw_input("Invalid contact,try again:")
                self.__contact=contact

    """
            
                    
    @property
    def aadhar(self):
        return(self.__aadhar)
    @aadhar.setter
    def aadhar(self,aadhar):
        #self.__aadhar=aadhar
        while True:
            if(len(aadhar) == 12) :                          #validation
                self.__aadhar=aadhar
                break
            else:
                aadhar=input("Invalid aadhar number,try again:")
       
    
    


class patient(object):
    
    list2={}
    list3={1:'Ayurvedic',2:'Haemopathic',3:'Dentist'}
    docname={1:'Dr.ROY',2:'Dr.ROSIE',3:'Dr.JAMIE'}
    time={1:'8 AM',2:'9 AM',3:'10 AM',4:'11 AM',5:'1 PM',6:'2 PM',7:'3 PM',8:'4 PM',9:'5 PM',10:'6 PM',11:'7 PM',12:'8 PM'}
    
    
        
    @staticmethod
    def login():
        
        em=input("Enter the email(email address:Email):")
        
        #f2=open("stu.txt","r")
        for line in f2:
            
            x=line.split(",")
            if (em == x[3]):
                print(x)
                #print(x[1],x[2],x[3],x[4],x[5],x[6],x[7])
                
                
            elif(em != x[3]):
                print("pateint not found")
                
    @staticmethod
    def bookpoint():
        
        name=input("Enter the name:")
        email=input("Enter the email:")
        contact=input("Enter the contact:")
        aadhar=input("Enter the aadhar no.")
        

        
        

        print("Select city")
        print("1.Pune")
        print("2.Mumbai")
        choice=int(input("Select option:"))

        
        for deptid in patient.list3:
            print (deptid, ".)",patient.list3[deptid])
        dept=input("Enter your choice:")
            

        print("Select doctor or book")
        for dc in patient.docname:
            print(dc, ".)",patient.docname[dc])
        docin=input("Enter your choice:")
                    
        print("Choose date or time:")
        
        date1=input("Enter the date(dd/mm/yy)")
    

        print("Choose time:")
        for tm in patient.time:
            print( tm,".)",patient.time[tm])
        timein=input("Select time:")
        patient.list2[aadhar]=person(name,email,contact,aadhar,dept,docin,timein,date1)
        
        patient.confirm()

    @staticmethod
    def confirm():
        print("1.)Confirm")
        print("2.)Cancel")
    
        choice=int(input("Enter the choice:"))
        if choice == 1:
            print("Booking confirmed")
            #patient.viewdetails(name,email,contact,aadhar,dept,docname,date,time)
            '''fh=open("stu.txt","a")
            for i,j in patient.list2.iteritems():
                data=' '
                data=str(i) + ":Aadhar," + str(j.name) + ":Name," + str(j.email) + ":Email," + str(j.contact) + ":Contact," + str(patient.list3[j.dept]) + ":Department," + str(patient.docname[j.docin]) + ":DoctorName," + str(patient.time[j.timein]) + ":Time," + str(j.date1) + ":Date"
                fh.write(data)
                fh.write("\n")
            fh.close()'''

                
        
                    
                
    @staticmethod
    def viewdetails(name,email,contact,aadhar,dept,docname,date,time):
        print("Aadhaar\t\t\tName\t\t\tEmail\t\t\tContact\t\t\tDepartment\t\tDoctorName\tTimeSlot\tDate")
        #if dept == None:
        for i,j in patient.list2.viewdetails():
            #print("Name:", self.name)
            #print(" cust_id:", self.cust_id)1
                
            #print("Prn No:", self.prn)
            #1
            # print("Date Of Birth:", self.dob)
            print("Email:", self. email)
            print("Contact No:", self.contact)
                
        '''else:
            for i,j in patient.list2.viewdetails():
                if dept == j.dept:
                    print (j.aadhar,"\t\t",j.name,"\t\t",j.email,"\t\t",j.contact,"\t\t",patient.list3[j.dept],"\t\t",patient.docname[j.docin],"\t\t",patient.time[j.timein],"\t\t",j.date1)
        '''


    
        


class doctor(patient):
    @staticmethod
    def displayall():
        
        for i,j in patient.list2.iteritems():
            print("Name",j.name,"Email",j.email,"Contact",j.contact,"Aadhar card no.",i)
        f1=open("stu.txt",'r')
        for line in f1:
            x=line.split(",")
            print(x[1],x[2])
            

    @staticmethod
    def patientdetails():
        search=raw_input("Enter the patient details to search:(Ex:name of patient:Name)")
        fi3=open("stu.txt",'r')
        for line in fi3:
            x=line.split(",")
            if search == x[1]:
                print(x[0],x[1],x[2])
            else:
                print("not find")
        
        
                    

                
class admin(object):
    def __init__(self,receiver):
        
        self.receiver = receiver


    @staticmethod
    def showpatient():
        f2=open("stu.txt","r")
        for line in f2:
            x=line.split(",")
            print(x[1],x[2])

    @staticmethod
    def sendemail():
        import smtplib
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEText import MIMEText


        receiver=raw_input("Enter email address of patient to send remainder:")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login("smmahale@mitaoe.ac.in","password")

        msg = MIMEMultipart()
        msg['From'] = "Administrator"
        msg['To'] = receiver
        msg['Subject'] = "DOCAPP"
        msg.attach(MIMEText("Your appointment is tomorrow"))

        text = msg.as_string()

        server.sendmail("Shivam Mahale",receiver, text)

        server.quit()
        






def main():
    e=patient()
    q=doctor()
    
    while True:
        print("*"*150)
        print("                                              DOCTOR-PATIENT APPOINTMENT APP                                                      ")
        print("*"*150)
        print("Who are you?")
        print("1.Patient\n2.Doctor\n3.Admin\n4.Exit")
        choice=int(input("Enter choice:"))
        if choice == 1:

            print("1.Book appointment")
            print("2.Login")
            choic=int(input("Enter chocie:"))
            if choic == 1:
                e.bookpoint()
            if choic == 2:
                e.login()
                
               
        if choice == 2:

            print("1.Displayall patients")
            print("2.Display specific patient details")
            
            choic=int(input("Enter chocie:"))
            if choic == 1:
                q.displayall()
            elif choic == 2:
                q.patientdetails()
        if choice == 3:
            print("1.)Patient GetDetails")
            print("2.)Send email")
            v=int(input("Enter choicee:"))
            if v == 1:
                admin.showpatient()
            elif v == 2:
                admin.sendemail()
        else:
            break
    

if __name__ == '__main__':
    main()