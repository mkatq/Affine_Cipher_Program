from tkinter import *
import tkinter.messagebox
import tkinter


#  3 functions below check if the inputs are correct or not

def CheckA(a: int):  # here we check if the KEY A is valid or not!
    for x in range(1, 26):
        if (((a % 26) * (x % 26)) % 26 == 1):
            return a

    return tkinter.messagebox.showinfo("Warning", "Error - 'Key a' it should has inverse number to decrypt. \nTry with diffrent key!")


def CheckB(b: int):  # here we check if the KEY B is in range or not!
    if b in range(0, 25):
        return b
    else:
        return tkinter.messagebox.showinfo("Warning", "Error - 'Key b' it should be from 0 to 25. \nTry again!")


def CheckX(x: str):  # here we check if massage contain symbols or numbers will not be accepted! , otherwise its okay
    x = x.strip().replace(" ", "").upper()

    if x.isalpha() == True:
        return x
    else:
        return tkinter.messagebox.showinfo("Warning", "Error - the 'plaintext' must not contain numbers and symbols.\n Try again!")


#  2 functions below will do some useful opration
# this function will convert for example A TO 0 , O TO 14 , Z TO 25
def convLettersToNum(letters, numbers):
    for char in letters:
        for charAph in alphabet:
            if(char == charAph):
                numbers.append(alphabet.index(charAph))
    return numbers


def findInverse(a_key):  # This function find the inverse for a key
    for n in range(1, 26):
        if (((a_key % 26) * (n % 26)) % 26 == 1):
            return n


#  2 functions below one for Encryption the other for Decryption
def Encryption(a_key, b_key, x_originalMessage, alphabet):
    x_originalMessageInNUM = []
    cipherText = ""

    # here we get the original massage AS numbers like O is 14 , A is 0
    x_originalMessageInNUM = convLettersToNum(
        x_originalMessage, x_originalMessageInNUM)

    for num in x_originalMessageInNUM:
        y = int((a_key * num + b_key) % 26)
        for charAph in alphabet:
            if(y == alphabet.index(charAph)):
                cipherText += charAph

    return cipherText


def Decryption(a_key, b_key, cipherText, alphabet):

    x_cipherTextInNUM = []
    plainText = ""

# here we get the cipher massage AS numbers like O is 14 , A is 0
    x_cipherTextInNUM = convLettersToNum(cipherText, x_cipherTextInNUM)

    for y in x_cipherTextInNUM:
        x = (a_key * (y - b_key)) % 26
        for char in alphabet:
            if(x == alphabet.index(char)):
                plainText += char

    return plainText


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# 3 main function below will work while the interface is running

def deleteText():  # reset all entry
    entryKeyA.delete(first=0, last=END)
    entryKeyB.delete(first=0, last=END)
    entryKeyMassage.delete("1.0", END)
    entryCiphertext.delete("1.0", END)


def mainEncryption():

    a_key = CheckA(int(entryKeyA.get()))
    b_key = CheckB(int(entryKeyB.get()))
    x_originalMessage = CheckX(str(entryKeyMassage.get("1.0", END)))
    cipherText = Encryption(a_key, b_key, x_originalMessage, alphabet)

    entryCiphertext.delete("1.0", END)
    entryCiphertext.insert(END, cipherText)
    inveresA = findInverse(a_key)
    tkinter.messagebox.showinfo(
        "Note", "Encryption has done successfully. \nRemember your inverse key to decrypt is {}. ".format(inveresA))


def mainDecryption():

    a_key = CheckA(int(entryKeyA.get()))
    b_key = CheckB(int(entryKeyB.get()))
    x_originalMessage = CheckX(str(entryKeyMassage.get("1.0", END)))
    plainText = Decryption(a_key, b_key, x_originalMessage, alphabet)

    entryCiphertext.delete("1.0", END)
    entryCiphertext.insert(END, plainText)


# user_interface
window = Tk()
window.title("Afiine cipher")
window.geometry('830x680')
window.config(bg="#34495E")

# Label of key A and textfield
LabelKeyA = Label(window, text="Enter the key A", fg='white')
LabelKeyA.place(x=50, y=22)
LabelKeyA.config(bg="#34495E")
entryKeyA = Entry(window, highlightbackground="black",
                  highlightthickness=1, bd=0)
entryKeyA.place(x=150, y=22)


# Label of key B and textfield
LabelKeyB = Label(window, text="Enter the key B", fg='white')
LabelKeyB.place(x=50, y=65)
LabelKeyB.config(bg="#34495E")
entryKeyB = Entry(window, highlightbackground="black",
                  highlightthickness=1, bd=0)
entryKeyB.place(x=150, y=66)


# Label of massage and textfield
LabelKeyMassage = Label(window, text="Enter the massage", fg='white')
LabelKeyMassage.place(x=50, y=180)
LabelKeyMassage.config(bg="#34495E")
entryKeyMassage = Text(highlightbackground="black", highlightthickness=1, bd=0)
entryKeyMassage.pack()
entryKeyMassage.config(height=10, width=60, bg="White")
entryKeyMassage.place(x=156, y=120)

# 3 Buttons
EnterButton = Button(window, text="Encrypt", command=mainEncryption)
EnterButton.place(x=250, y=300, width=100)

EnterButton = Button(window, text="Decrypt", command=mainDecryption, )
EnterButton.place(x=460, y=300, width=100)

DeleteButton = Button(window, text="Reset all", command=deleteText)
DeleteButton.place(x=680, y=240, width=100)

# Label of result and textfield
LabelCiphertext = Label(window, text="The result", fg='white')
LabelCiphertext.place(x=380, y=450)
LabelCiphertext.config(bg="#34495E")
entryCiphertext = Text(highlightbackground="black", highlightthickness=1, bd=0)
entryCiphertext.pack()
entryCiphertext.config(height=8, width=40, bg="White")
entryCiphertext.place(x=240, y=480)


window.mainloop()
