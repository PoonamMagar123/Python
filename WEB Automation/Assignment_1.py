import os
import csv
import time
import psutil
import urllib.request as urllib2
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib2.urlopen('https://mail.google.com/mail/u/0/#inbox',timeout=1)
        print("Connected to the internet!")
        return True
    except urllib2.URLError as err:
        print("Not Connected to the internet!")
        return False

def MailSender(toaddr, cname, file_path ):
    try:
        fromaddr = "poonammagar3562@gmail.com"
        
        msg  = MIMEMultipart()
        
        msg['From'] = fromaddr
        
        msg['To'] = toaddr
        
        body = """
        
        Dear Hiring Team,

        I hope this email finds you well. I'm writing to express my interest in the Software Developer positions at %s Private Limited


        I have sent my resume  "Application for  Back End Developer - Poonam Dhanaji Magar" and 
        Reference "Future Creation Placement Consultancy."

        I am enthusiastic about contributing my skills to your team and am confident in my ability to excel in these roles.

        Thank you for considering my application.

        Thanks & Regards,
        Poonam Dhanaji Magar
        Contact : +91 7057073562
        Email : poonammagar3562@gmail.com
          """%(cname)
        
        Subject = """Application for Software Developer - Poonam Dhanaji Magar"""
        
        msg['Subject'] = Subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        attachment = open(file_path, "rb")
        
        p = MIMEBase('application', 'octet-stream')
        
        p.set_payload((attachment).read())
        
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename = %s" % file_path)
        
        msg.attach(p)
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        s.starttls()
        
        s.login(fromaddr, "qxgj ybjl opqf cvvh")
        
        text = msg.as_string()
        
        s.sendmail(fromaddr, toaddr, text)
        
        s.quit()
        
        print("Log File successfully sent through Mail %s"%toaddr)
    
    except Exception as E:
        print("Unable to send mail", E)

def ProcessLog(file_path,log_dir = 'Marvellous'):
    listprocess = []
    
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    separator = "-" * 80
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
   
    connected = is_connected()
        
    if connected:
        startTime = time.time()
        
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check if the 'email' field is present and not empty
                if 'email' in row and row['email'].strip():
                    to_email = row['email'].strip()
                    cname = row['company'].strip()
                    MailSender(to_email, cname, "Poonam_Magar_Python.pdf")
                else:
                    print(f"Invalid or empty email address found in row: {row}")

                
        endTime = time.time()
        
        print('Took %s seconds to send mail '%(endTime - startTime))
    else:
        print("There is no internet connection")

def main():
    print("---- Automation Script-----")

    print("Application name : " +argv[0])

    if (len(argv) != 3):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used  to create log file and send through mail ")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: python script_name.py AbsolutePath_of_File")
        exit()

    try:
        ProcessLog(argv[1], argv[2])    
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()