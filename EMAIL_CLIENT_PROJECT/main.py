from tkinter import *
from email_client.email_sender import email_sender
from email_client.mailbox import authenticate

"""------------------------------"""
# sender_pass_goshomaster97@gmail.com = 'roxxnjywjqjlyklu'
"""------------------------------"""


root = Tk()
root.geometry('400x280')
root.title('George\'s Email Client')

main_label = Label(root, text='Welcome to Email Client', font='Calibri 16 underline')
main_label.pack(pady=10)

mailbox_button = Button(root, text='Check Mailbox', font=('Calibri', 12), command=authenticate)
mailbox_button.pack(pady=50, side=LEFT, padx=30, ipady=10)

mailsender_button = Button(root, text='Send E-Mail', font=('Calibri', 12), command=email_sender)
mailsender_button.pack(pady=85, ipady=10, side=RIGHT, padx=40)


root.mainloop()
