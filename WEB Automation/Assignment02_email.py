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
from datetime import datetime

def is_connected():
    try:
        urllib2.urlopen('https://mail.google.com/mail/u/0/#inbox',timeout=1)
        print("Connected to the internet!")
        return True
    except urllib2.URLError as err:
        print("Not Connected to the internet!")
        return False

def MailSender(toaddr, Message, time):
    try:
        fromaddr = "poonammagar3562@gmail.com"
        
        msg  = MIMEMultipart()
        
        msg['From'] = fromaddr
        
        msg['To'] = toaddr
        
        body = Message
        
        Subject = """Simple Text Message : %s"""%(time)
        
        msg['Subject'] = Subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        s.starttls()
        
        s.login(fromaddr, "qxgj ybjl opqf cvvh")
        
        text = msg.as_string()
        
        s.sendmail(fromaddr, toaddr, text)
        
        s.quit()
        
        print("An Auto mail sent through Mail %s"%toaddr)
    
    except Exception as E:
        print("Unable to send mail", E)
       
def ProcessLog(file_path):
    
    connected = is_connected()
        
    if connected:
        startTime = time.time()
        
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check if the 'email' field is present and not empty
                if 'email' in row and row['email'].strip():
                    to_email = row['email'].strip()
                    Message = row['Message'].strip()
                    MailSender(to_email, Message, timestamp)
                else:
                    print(f"Invalid or empty email address found in row: {row}")

        endTime = time.time()
        
        print('Took %s seconds to send mail '%(endTime - startTime))
    else:
        print("There is no internet connection")

def main():
    print("---- Automation Script-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used send a auto birthday message and send through mail ")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: python script_name.py Time")
        exit()

    try:
        
        # schedule.every().day.at("24:00").do(ProcessLog) 
        # schedule.every(1).minutes.do(ProcessLog)
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)
        ProcessLog(argv[1])
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error :an occured error ",E)

if __name__ == "__main__":
    main()