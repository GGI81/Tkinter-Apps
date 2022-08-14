import imaplib
import email
from tkinter import *
from tkinter import messagebox

my_messages = []

def get_inbox():
    host = 'imap.gmail.com'
    username = mail_entry.get()
    password = password_entry.get()
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select('inbox')
    _, search_data = mail.search(None, 'UNSEEN')
    search_data = search_data[::-1]
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            # print(f'{header}: {email_message[header]}')
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
                # print(body.decode())
                email_data['body'] = body.decode()
            elif part.get_content_type() == 'text/html':
                html_body = part.get_payload(decode=True)
                # print(html_body.decode())
                email_data['html_body'] = html_body.decode()
            # print()
        my_messages.append(email_data)


def mailbox():
    try:
        get_inbox()
        if len(my_messages) > 0:
            try:
                top = Tk()
                top.title('Mailbox')
                scrollbar = Scrollbar(top)
                scrollbar.pack(side=RIGHT, fill=Y)
                scrollbar2 = Scrollbar(top, orient='horizontal')
                scrollbar2.pack(side=BOTTOM, fill=X)
                array = Listbox(top, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar2.set)
                for line in range(len(my_messages)):
                    # array.insert(END, f'Subject: {my_messages[line]["subject"]}'
                    #              f'Receiver: {my_messages[line]["to"]}' + '\n' +
                    #              f'Sender: {my_messages[line]["from"]}' + '\n' +
                    #              f'Date: {my_messages[line]["date"]}' + '\n' +
                    #              f'Body: {my_messages[line]["body"]}' + '\n'
                    #              )
                    array.insert(END, f'  Subject: {my_messages[line]["subject"]}')
                    array.insert(END, f'  Receiver: {my_messages[line]["to"]}')
                    array.insert(END, f'  Sender: {my_messages[line]["from"]}')
                    array.insert(END, f'  Date: {my_messages[line]["date"]}')
                    array.insert(END, f'  Body: {my_messages[line]["body"]}')
                    array.insert(END, '')
                    array.insert(END, '  ------------------------------------')
                    array.insert(END, '')
                array.pack(side=LEFT, fill=BOTH, ipadx=500, ipady=90)
                scrollbar.config(command=array.yview)
                scrollbar2.config(command=array.xview)
            except Exception as e:
                print(e)
                messagebox.showinfo('Message', 'Wrong Credentials')
        else:
            messagebox.showinfo('Message', 'Your mailbox is empty')
    except Exception as e:
        print(e)
        messagebox.showinfo('Message', 'Wrong Credentials')

def authenticate():
    top = Toplevel()
    top.title('Authentication')
    top.geometry('300x125')

    mail_name = StringVar()
    password = StringVar()

    mail_label = Label(top, text='Enter E-Mail')
    mail_label.grid(row=1, column=1, pady=20)

    password_label = Label(top, text='Enter Password')
    password_label.grid(row=2, column=1, padx=10)

    global mail_entry
    mail_entry = Entry(top, textvariable=mail_name)
    mail_entry.grid(row=1, column=2)

    global password_entry
    password_entry = Entry(top, textvariable=password, show='*')
    password_entry.grid(row=2, column=2)

    submit = Button(top, text='Submit', command=mailbox)
    submit.grid(row=3, column=2, pady=10)
