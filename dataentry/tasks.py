from awd_main.celery import app
import time
from django.core.management import call_command
from .utils import generate_csv_file,send_email_notification
from django.conf import settings

@app.task
def celery_test_task():
    time.sleep(5)

    mail_subject = 'Test subject'
    message = 'This is a test email'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)
    return 'Email sent successfully.'


@app.task
def import_data_task(file_path,model_name):
    try:
        call_command('importdata', file_path,model_name)
    except Exception as e:
        raise e
    mail_subject = 'Import data Completed'
    message = 'Your data import has been successful'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)
    return 'Data Imported Successfully!'

@app.task
def export_data_task(model_name):
    try:
        call_command('exportdata',model_name)
    except Exception as e:
        raise e
    
    file_path = generate_csv_file(model_name)
    print('file_path==>',file_path)
    
    mail_subject = 'Export data Successful'
    message = 'Export Data Successful. Please find the attachment'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email,attachment=file_path)
    return 'Export Data task executed successfully.'


