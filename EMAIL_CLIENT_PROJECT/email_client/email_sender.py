import imghdr
import smtplib
from tkinter import *
from tkinter import filedialog
from email.message import EmailMessage

attachments = []

def attach_file():
    file_name = filedialog.askopenfilename(initialdir='C:/', title='Select a File')
    attachments.append(file_name)
    hidden_message.config(text=f'Attached {str(len(attachments))} files', fg='green')


def send_email():
    try:
        msg = EmailMessage()
        current_mail = mail_entry.get()
        current_pass = password_entry.get()
        current_receiver = receiver_entry.get()
        current_subject = subject_entry.get()
        current_body = body_entry.get('1.0', 'end-1c')

        msg['subject'] = current_subject
        msg['from'] = current_mail
        msg['to'] = current_receiver
        msg.set_content(current_body)

        for file_name in attachments:
            file_type = file_name.split('.')
            # print(file_type)  # ['C:/Users/Georg/OneDrive/Desktop/7', '8_OTSO', 'jpg']
            file_type = file_type[-1]  # [-1 because it is possible to has more than one "." in the filename]
            if file_type == 'jpg' or file_type == 'png' or file_type == 'jpeg':
                with open(file_name, 'rb') as f:
                    data = f.read()
                    img_type = imghdr.what(file_name)
                msg.add_attachment(data, maintype='image', subtype=img_type, filename=f.name)
            else:
                with open(file_name, 'rb') as f:
                    data = f.read()
                msg.add_attachment(data, maintype='application', subtype='octet-stream', filename=f.name)
        if current_mail == '' or current_pass == '' or current_receiver == '' \
                or current_subject == '' or current_body == '':
            hidden_message.config(text='All fields are required!', fg='red')
        else:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(current_mail, current_pass)
            server.send_message(msg)
            hidden_message.config(text='Email has been sent!', fg='green')
    except Exception as e:
        print(e)
        hidden_message.config(text='Error sending email', fg='red')

    attachments.clear()


def reset_forms():
    mail_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    receiver_entry.delete(0, 'end')
    subject_entry.delete(0, 'end')
    body_entry.delete('1.0', 'end')
    hidden_message.config(text='')

def email_sender():
    top = Toplevel()
    top.title('Email Sender')
    top.geometry('300x300')

    global mail_entry
    global password_entry
    global receiver_entry
    global subject_entry
    global body_entry
    global hidden_message

    title1_Label = Label(top, text='Email Sender', font=('Garamond', 15))
    title1_Label.grid(row=0, sticky=N)

    mail_label = Label(top, text='Email', font=('Calibri', 11))
    mail_label.grid(row=2, sticky=W, padx=5)

    password_label = Label(top, text='Password', font=('Calibri', 11))
    password_label.grid(row=3, sticky=W, padx=5)

    receiver_label = Label(top, text='Receiver', font=('Calibri', 11))
    receiver_label.grid(row=4, sticky=W, padx=5)

    subject_label = Label(top, text='Subject', font=('Calibri', 11))
    subject_label.grid(row=5, sticky=W, padx=5)

    body_label = Label(top, text='Body', font=('Calibri', 11))
    body_label.grid(row=6, sticky=W, padx=5)

    hidden_message = Label(top, text='', font=('Calibri', 13))
    hidden_message.grid(row=7, sticky=S, padx=5)

    mail_var = StringVar()
    password_var = StringVar()
    receiver_var = StringVar()
    subject_var = StringVar()

    mail_entry = Entry(top, textvariable=mail_var)
    mail_entry.grid(row=2, column=0, padx=80)

    password_entry = Entry(top, textvariable=password_var, show='*')
    password_entry.grid(row=3, column=0)

    receiver_entry = Entry(top, textvariable=receiver_var)
    receiver_entry.grid(row=4, column=0)

    subject_entry = Entry(top, textvariable=subject_var)
    subject_entry.grid(row=5, column=0)

    body_entry = Text(top, width=15, height=4)
    body_entry.grid(row=6, column=0)

    send_button = Button(top, text='Send', command=send_email)
    send_button.grid(row=7, sticky=W, pady=10, padx=5)

    reset_button = Button(top, text='Reset', command=reset_forms)
    reset_button.grid(row=7, sticky=W, pady=40, padx=45)

    attach_button = Button(top, text='Attachments', command=attach_file)
    attach_button.grid(row=7, sticky=W, pady=40, padx=85)
