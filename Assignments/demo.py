
import csv
import smtplib
import schedule
import time
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_birthday_email(email, name):
    sender_email = "poonammagar3562@gmail.com"
    sender_password = "qxgj ybjl opqf cvvh"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = "Happy Birthday, {}!".format(name)

    body = "Dear {},\n\nHappy Birthday! Wishing you a fantastic day filled with joy and laughter.\n\nBest regards,\nPoonam Dhanaji Magar".format(name)
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
        print("Birthday email sent to {}".format(email))
    except Exception as e:
        print("Failed to send email to {}: {}".format(email, str(e)))

def check_birthdays():
    today = datetime.now().strftime('%d-%m')  # Current day and month only, ignoring the year
    file_path = "E:\\Assignments\\Assignment_12\\birthday.csv"  # Correct the file path if necessary

    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Birthday'][:5] == today:  # Compare only the day and month (ignoring the year)
                email = row['Email']
                name = row['Name']
                send_birthday_email(email, name)

# schedule.every().day.at("17:38").do(check_birthdays)  # Schedule the task to run every day at 9:00 AM

# while True:
#     schedule.run_pending()
#     time.sleep(1)
schedule.every(1).minutes.do(send_birthday_email)
while True:
    schedule.run_pending()
    time.sleep(1)