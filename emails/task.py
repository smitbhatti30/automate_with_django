from awd_main.celery import app
from dataentry.utils import send_email_notification

@app.task
def send_email_task(mail_subjects,message,to_email,attachment):
    send_email_notification(mail_subjects,message,to_email,attachment)
    return 'Email task executed successfully'