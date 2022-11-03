# A Phone and Email Scraper Tool

import re, pyperclip, tkinter, tkinter.messagebox

root = tkinter.Tk()
root.title("Return Phone Numbers and Emails Tool")
root.geometry("400x100")

def app():
    #TODO: Create a regex for phone numbers
    phoneRegex = re.compile(r"""
    # 858-111-0000, 431 0000, (858) 111-0000, 111-0000 ext 12345, ext. 12345, x12345
    (
    ((\d\d\d)|(\(\d\d\d\)))?    # area code (optional) #could be 858 or (858), the ? is to let this appear 0 or 1 time
    (\s|-)    # first separator #could be space or dash
    \d\d\d    # first 3 digits
    (\s|-)    # second separator #could be space or dash
    \d\d\d\d    # last 4 digits
    (((ext(\.)?\s) | x) # extension word-part (optional)
    (\d{1,5}))?    # extension number-part (optional)
    )
    """, re.VERBOSE) #VERBOSE helps to add whitespace and comments to the regex string passed to re.compile()

    #TODO: Create a regex for email addresses
    emailRegex = re.compile(r"""

    # some.+_thing@otherthing(\d{2,5})?.someotherthing

    [a-zA-Z0-9_.+]+   # name part #Characters inside the character class [] don't need to use backslash
    @    # @ symbol
    [a-zA-Z0-9_.+]+   # domain name part, the + is to let this appear one or more times
    """, re.VERBOSE)

    #TODO: Get the text off the clipboard
    text = pyperclip.paste()
    #TODO: Extract the email/phone from this text
    extractedPhone = phoneRegex.findall(text)
    extractedEmail = emailRegex.findall(text)

    listPhoneNumbers = []

    for phone_num in extractedPhone:
        listPhoneNumbers.append(phone_num[0])
    #TODO: Copy the extracted email/phone to the clipboard
    results = "\n".join(listPhoneNumbers) + "\n" + "\n".join(extractedEmail)
    pyperclip.copy(results)
    tkinter.messagebox.showinfo(title = "Action", message = "Phone Numbers and Emails are copied to clipboard!")
    
action_button = tkinter.Button(root, text = "Click to extract phone numbers and emails", command = app)
action_button.place(x = 80, y = 25)

root.mainloop()


