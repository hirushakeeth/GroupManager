from tkinter import *
import re


class GUIClass:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()


        self.label1 = Label(frame, text="input you Sentence")
        self.label1.pack()



        self.entry_1 = Entry(frame)
        self.entry_1.pack()

        self.printButton = Button(frame, text="Translate", command=self.sendSentence)
        self.printButton.pack()

        self.T = Text(frame, height=5, width=30 ,borderwidth=2, relief="groove")
        self.T.pack()

    def sendSentence(self):

        getInput = self.entry_1.get()
        print(getInput)

        print(getInput.strip())
        find = getInput.split()

        file = open('words.txt', 'r')
        lines = file.read().splitlines()

        sin_sentence = " "

        for l in find:
            for line in lines:
                 if re.findall('\\b' + l + '\\b', line, re.I):
                    print(line)
                    sin_word = (line.split('-')[1]).strip()
                    sin_sentence = (sin_sentence + " " + sin_word).strip()
                    print(sin_sentence)

        self.T.insert(0.0, sin_sentence)








root = Tk()
root.title('English-SinhalaTranslator')
root.geometry('400x200')
b = GUIClass(root)
root.mainloop()
