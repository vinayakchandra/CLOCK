# import all the libraries
from tkinter import *  # To make the GUI
from time import *  # To get the time
import tkinter.messagebox  # To display pop up
import quotesCollection as qc  # To get the quotes
import os  # to use os.system() and speak the time
import pyttsx3  # text to speech

"""SPEAK FUNCTIONALITY ONLY WORKS FOR MAC"""


class Clock:
    color = "black"  # color for the background
    time_format = ' %I : %M : %S   %p '  # format of the time -> 12 hour format
    checking = False  # for changing time format
    startTime = strftime("%I : %M : %S")  # time when Program is started
    start_minutes = int(strftime(" %M"))  # starting minute time
    start_hours = int(strftime("%H"))  # starting hour time
    spent_minutes = int
    spent_hours = int
    font_style = ("Courier", 30, "bold")  # font style for Quote label and Date label

    def __init__(self):
        self.root = Tk()
        self.engine = pyttsx3.init()
        self.quotes = qc.QuotesCollection()

        self.root.configure(bg=self.color)  # background of window
        # self.root.geometry("650x360")  # size of the window

        self.root.title("CLOCK")  # Title

        # Time Label
        self.label = Label(self.root, font=("times", 80, "bold"), background="yellow", foreground="black", bd=1,
                           relief="solid", padx=10)
        self.label.pack(anchor="center", fill=X)

        self.time()  # calling time Method

        # date Label
        self.date_label = Label(self.root, font=self.font_style, fg="white", text=strftime("%d %B %Y %a"),
                                bg=self.color, pady=10)
        self.date_label.pack()

        # quote label
        self.quoteLabel = Label(self.root, text=self.quotes.getQuote(), highlightbackground=self.color,
                                font=self.font_style, bg=self.color, fg="white",
                                padx=20, pady=20, wraplength=900)
        self.quoteLabel.pack()

        self.changingQuote()  # calling changingQuote Method to change the quote label every 30 minutes

        # 12 24 hour format button
        self.button = Button(self.root, text="12/24", highlightbackground=self.color, command=self.change_time)
        self.button.pack()

        # start time Button
        self.start_button = Button(self.root, text="START", highlightbackground=self.color, command=self.start_time)
        self.start_button.pack()

        # End time Button
        self.end_button = Button(self.root, text="END", fg="black", highlightbackground=self.color,
                                 command=self.time_spent)
        self.end_button.pack()

        # start time label
        start_label_text = "You started at: {}".format(self.startTime)
        self.start_label = Label(self.root, text=start_label_text, bg=self.color, fg="white", pady=10)
        self.start_label.pack()

        # Total time spent button
        self.time_button = Button(self.root, highlightbackground=self.color, text="Total Time Spent",
                                  command=self.time_spent)
        self.time_button.pack()

        # EXIT button
        self.exit_button = Button(self.root, text="EXIT", font=("times", 20, "bold",), fg='red',
                                  highlightbackground=self.color, command=self.pop_exit)
        self.exit_button.pack()

        self.root.attributes('-alpha', .9)  # Transparent window

        self.speak("Program Started")  # speaks Program Started
        time_text = str(strftime("%I %M"))
        self.speak("time is " + ("00" in time_text and time_text.strip("0") + "o clock" or time_text.lstrip("0")))

        self.root.mainloop()  # mainloop

    # changing time on the label
    def time(self):
        string = strftime(self.time_format)
        self.label.config(text=string)
        self.changingQuote()  # calling changing quote method
        self.label.after(500, self.time)

    # Changing time format
    def change_time(self):
        if self.checking:  # if checking = true
            self.time_format = ' %I : %M : %S   %p '
            self.time()
            self.checking = False
            print("changed to 12 hour format")
        else:
            self.time_format = '  %H : %M : %S  '
            self.time()
            self.checking = True
            print("changed to 24 hour format")

    # Exit pop up
    def pop_exit(self):
        # pop up Window
        popup_window = tkinter.messagebox.askquestion('Popup Window(Title)', 'Are you sure you want to EXIT')
        if popup_window == "yes":
            self.root.destroy()
            print("Program Exited")
        else:
            pass

    # Timer
    def time_spent(self):
        self.spent_hours = int(strftime('%H'))
        self.spent_minutes = int(strftime('%M'))

        total_spent_time = 'Your time spent is: {} Hours {} Minutes'.format(
            (abs(self.spent_hours - self.start_hours)), (abs(self.spent_minutes - self.start_minutes)))

        current_time2 = strftime(' %H : %M %S ')

        # time spent pop-up
        tkinter.messagebox.showinfo('Popup Window(Title)', total_spent_time)
        print('printed the total time spent')

    # starting time
    def start_time(self):
        new_starttime = strftime(' %H : %M %S ')
        self.start_hours = int(strftime('%H'))
        self.start_minutes = int(strftime('%M'))

    # changing quote in quote label in every 30 minutes and saying time
    def changingQuote(self):
        if int(strftime("%M")) == 30 or int(strftime("%M")) == 0:
            if int(strftime("%S")) == 0:
                quoteText = self.quotes.getQuote()
                self.quoteLabel.config(text=quoteText)
                time_text = str(strftime("%I %M"))
                self.speak(
                    "time is " + ("00" in time_text and time_text.strip("0") + "o clock" or time_text.lstrip("0")))
                # print("changed quoteText at " + strftime("%I : %M %p") + "\n")

    # for cross platform.  -> HAVING PROBLEMS IN THIS
    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    @staticmethod  # only works in Mac os
    def speak(text):  # Speaking the text given to it
        print(text)
        os.system("say {}".format(text))


if __name__ == "__main__":
    print("Program started at " + strftime("%I-%M-%S  %p") + "\n")
    Clock().speak("Have a great day ahead!")  # speaks when the program gets Exited

    ''' if in WINDOWS -> Don't use speak() '''
