#!/usr/bin/env python

from Tkinter import *
from random import *
import string


def random_password():
    chars = string.ascii_letters + string.digits
    vowels = ["a", "e", "i", "o", "u"]
    consonants = [
        "b", "c", "d", "f", "g", "h", "j",
        "j", "k", "l", "m", "n", "o", "p",
        "q", "v", "w", "x", "y", "z"]
    pairs = [
        "ba", "be", "bi", "bo", "bu", "ca", "ce", "ci", "co", "cu", "da", "de",
        "di", "do", "du", "ea", "ee", "ei", "eo", "eu", "fa", "fb", "fc", "fd",
        "fe", "ff", "fi", "fo", "fu", "ga", "ge", "gi", "go", "gu", "ha", "he",
        "hi", "ho", "hu", "ia", "ie", "io", "iu", "ja", "je", "ji", "jo", "ju",
        "jz", "ka", "ke", "ki", "ko", "ku", "la", "lb", "lc", "ld", "le", "lf",
        "lg", "lh", "li", "lj", "lk", "lo", "lu", "ma", "me", "mi", "mo", "mu",
        "na", "ne", "ni", "no", "nu", "oa", "oe", "oi", "oo", "ou", "pa", "pe",
        "pi", "po", "pu", "qu", "ra", "re", "ri", "ro", "ru", "sa", "se", "si",
        "so", "su", "ta", "te", "ti", "to", "tu", "ua", "ue", "ui", "uo", "va",
        "ve", "vi", "vo", "vu", "wa", "we", "wo", "wu", "xa", "xe", "xo", "xu",
        "ya", "ye", "yi", "yo", "yu", "za", "ze", "zi", "zo", "zu"
    ]
    passwordBase = "".join(choice(pairs) for x in range(randint(4, 5)))
    items  = [True, False]
    change = choice([True, False])
    passwordList1 = []
    passwordList2 = []
    count1 = 0
    count2 = 0
    
    for letter in passwordBase:
        if (choice([True, False]) == True) and (count1 < 3):
            passwordList1.append(letter.swapcase())
            count1 = count1 + 1
        else:
            passwordList1.append(letter)
    for letter in passwordList1:
        if (choice([True, False]) == True) and count2 < 3:
#            passwordList2.append(choice(
#                ["0","1","2", "3", "4", "5", "6", "7", "8", "9"]
#            ))
            if letter.lower() == "o":
                passwordList2.append("0")
            elif letter.lower() == "e":
                passwordList2.append("3")
            else:
                passwordList2.append(letter)
        else:
            passwordList2.append(letter)
    password = "".join(["%s" % (k) for k in passwordList2])
    return password
    
#    return "".join(choice(chars) for x in range(randint(8, 16)))

if '__main__' in __name__:
#    print random_password()
    root = Tk()
    root.title("Password Generator")
    root.resizable(0,0)
    root.minsize(300,0)
     
    frame = Frame(root)
    frame.pack(pady=10, padx=5)
     
    content = StringVar()
    updater = lambda:content.set(random_password())
     
    gen_btn = Button(frame, text="Generate", command=updater)
    gen_btn.config(font=("sans-serif", 14),  bg="#92CC92")
    gen_btn.pack(side=LEFT, padx=5)
     
    field = Entry(frame, textvariable=content)
    field.config(fg='blue', font=('courier',  16, "bold"), justify='center')
    field.pack(fill=BOTH, side=RIGHT, padx=5)
     
    root.mainloop()
