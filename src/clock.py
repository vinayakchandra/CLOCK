# import all the libraries
from tkinter import *
from time import *
import tkinter.messagebox
import quotesCollection as qc
import os
import pyttsx3
# from Speaker import Speaker


class Clock:
    """Color for the background"""
    color = "black"

    time_format = ' %I : %M : %S   %p '
    checking = False
    spent_minutes: int
    spent_hours: int
    start_minutes = int(strftime(" %M"))
    start_hours = int(strftime("%H"))
    starttime = strftime("%I : %M : %S")

    def __init__(self):  # , window):
        self.root = Tk()
        # self.sp = Speaker()
        self.engine = pyttsx3.init()
        # self.root = window

        self.quotes = qc.QuotesCollection()

        # self.root = Tk()
        self.root.configure(bg=self.color)
        # self.root.geometry("650x360")

        self.root.title("CLOCK")  # title

        # Time Label
        self.label = Label(self.root, font=("times", 80, "bold"), background="yellow", foreground="black", bd=1,
                           relief="solid",
                           padx=10)
        self.label.pack(anchor="center", fill=X)

        # calling time function
        self.time()

        # date Label
        self.date_label = Label(self.root, font=("Courier", 30, "bold"), fg="white", text=strftime("%d %B %Y %a"),
                                bg=self.color,
                                pady=10)
        self.date_label.pack()

        # quote label
        self.quoteLabel = Label(self.root, text=self.quotes.getQuote(), highlightbackground=self.color,
                                font=("Courier", 30, "bold"), bg=self.color, fg="white",
                                padx=20, pady=20, wraplength=1000)
        self.quoteLabel.pack()
        # calling changingQuote Function to change the quote label every 5 secs
        self.changingQuote()

        # Quote Button
        # self.quoteButton = Button(self.root, text="Quote", command=self.changingQuote)
        # self.quoteButton.pack()

        # 12 24 hour format button ✅
        self.button = Button(self.root, text="12/24", highlightbackground=self.color, command=self.change_time)
        self.button.pack()

        # start time Button ✅
        self.start_button = Button(self.root, text="START", highlightbackground=self.color, command=self.start_time)
        self.start_button.pack()

        # End time Button
        self.end_button = Button(self.root, text="END", fg="black", highlightbackground=self.color,
                                 command=self.time_spent)
        self.end_button.pack()

        # start time label
        start_label_text = "You started at: {}".format(self.starttime)
        self.start_label = Label(self.root, text=start_label_text, bg=self.color, fg="white", pady=10)
        self.start_label.pack()

        # Total time spent button
        self.time_button = Button(self.root, highlightbackground=self.color, text="Total Time Spent",
                                  command=self.time_spent)
        self.time_button.pack()

        # EXIT button ✅
        self.exit_button = Button(self.root, text="EXIT", font=("times", 20, "bold",), fg='red',
                                  highlightbackground=self.color,
                                  command=self.pop_exit)
        self.exit_button.pack()

        """Transparent window"""
        self.root.attributes('-alpha', .9)

        # self.engine.say("Program started")
        # self.engine.runAndWait()
        os.system("say Program Started")
        # self.say("time is " + str(strftime("%I %M")))
        os.system("say time is " + str(strftime("%I %M")))
        # self.sp.say("Program Started")

        # mainloop
        self.root.mainloop()

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
        time_spent_popup = tkinter.messagebox.showinfo('Popup Window(Title)', total_spent_time)
        print('printed the total time spent')

    # starting time
    def start_time(self):
        new_starttime = strftime(' %H : %M %S ')
        self.start_hours = int(strftime('%H'))
        self.start_minutes = int(strftime('%M'))

    # changing quote in quote label in every 30 mins (1800000 = 30 mins)
    # saying the time in every 30 minutes
    def changingQuote(self):
        if int(strftime("%M")) == 30 or int(strftime("%M")) == 0:
            if int(strftime("%S")) == 0:
                quoteText = self.quotes.getQuote()
                self.quoteLabel.config(text=quoteText)
                # self.say("time is " + str(strftime("%I %M")))
                os.system("say time is " + str(strftime("%I %M")))
                print("changed quoteText at " + strftime("%I : %M %p") + "\n")

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


def main():
    # root = Tk()
    # Clock(root)
    Clock()
    # root.mainloop()


if __name__ == "__main__":
    print("Program started at " + strftime("%I-%M-%S  %p") + "\n")
    main()
    # sp = Speaker()
    # sp.say("test")
    # os.system("say isudhfuasfd")
