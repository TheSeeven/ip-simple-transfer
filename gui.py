from tkinter import *
from turtle import bgcolor, bgpic


def test(text):
    print(text)


class Interface:
    backgroundColor = '#1b1b1b'

    def copyToClipboard(self, text):
        self.interface.clipboard_clear()
        self.interface.clipboard_append(text)
        self.interface.update()

    def configureLayouts(self):
        self.interface.grid_columnconfigure(0, weight=1)
        self.interface.grid_rowconfigure(0, weight=22)
        self.interface.grid_rowconfigure(1, weight=60)
        self.interface.grid_rowconfigure(2, weight=18)

        self.middleFrame.grid_rowconfigure(0, weight=1)
        self.middleFrame.grid_columnconfigure(0, weight=1)
        self.middleFrame.grid_columnconfigure(1, weight=1)

        self.buttomFrame.grid_rowconfigure(0, weight=1)
        self.buttomFrame.grid_columnconfigure(0, weight=1)
        self.buttomFrame.grid_columnconfigure(1, weight=1)

        self.bottomRightFrame.grid_columnconfigure(0, weight=1)
        self.bottomRightFrame.grid_rowconfigure(0, weight=1)
        self.bottomRightFrame.grid_rowconfigure(1, weight=1)

        self.middleLeftFrame.grid_columnconfigure(0, weight=1)
        self.middleLeftFrame.grid_rowconfigure(0, weight=1)
        self.middleLeftFrame.grid_rowconfigure(1, weight=5)

        self.middleRightFrame.grid_columnconfigure(0, weight=1)
        self.middleRightFrame.grid_rowconfigure(0, weight=1)
        self.middleRightFrame.grid_rowconfigure(1, weight=5)

        self.middleFrame.grid(column=0, row=1, sticky="nesw")
        self.topFrame.grid(column=0, row=0, sticky="nesw")
        self.buttomFrame.grid(column=0, row=2, sticky="nesw")
        self.middleLeftFrame.grid(column=0, row=0, sticky="nesw")
        self.middleRightFrame.grid(column=1, row=0, sticky="nesw")
        self.bottomRightFrame.grid(column=1, row=0, sticky="nesw")
        self.bottomLeftFrame.grid(column=0, row=0, sticky="nesw")
        self.rightBottomBottomFrame.grid(column=0, row=1, sticky="nesw")
        self.rightBottomTopFrame.grid(column=0, row=0, sticky="nesw")
        self.middleLeftTopFrame.grid(column=0, row=0, sticky="nesw")
        self.middleLeftBottomFrame.grid(column=0, row=1, sticky="nesw")
        self.middleRightTopFrame.grid(column=0, row=0, sticky="nesw")
        self.middleRightBottomFrame.grid(column=0, row=1, sticky="nesw")

        self.topFrame.configure(background='red')
        self.buttomFrame.configure(background='green')
        self.middleLeftFrame.configure(background='purple')
        self.middleRightFrame.configure(background='yellow')
        self.bottomLeftFrame.configure(background='white')
        self.bottomRightFrame.configure(background='blue')
        self.bottomRightFrame.configure(background='green')
        self.rightBottomBottomFrame.configure(background='red')
        self.rightBottomTopFrame.configure(background='black')
        self.middleLeftTopFrame.configure(background='green')
        self.middleLeftBottomFrame.configure(background='red')
        self.middleRightTopFrame.configure(background='blue')
        self.middleRightBottomFrame.configure(background='green')

    def __init__(self, ipAdress):

        #BASE
        #background an other customizations
        self.interface = Tk(className="Simple IP transfer - Idle")
        self.interface.geometry("600x500")
        self.interface.resizable(True, True)
        self.interface['background'] = Interface.backgroundColor
        #BASE
        self.middleFrame = Frame(self.interface)
        self.topFrame = Frame(self.interface)
        self.buttomFrame = Frame(self.interface)
        self.middleLeftFrame = Frame(self.middleFrame)
        self.middleRightFrame = Frame(self.middleFrame)
        self.bottomLeftFrame = Frame(self.buttomFrame)
        self.bottomRightFrame = Frame(self.buttomFrame)
        self.rightBottomBottomFrame = Frame(self.bottomRightFrame)
        self.rightBottomTopFrame = Frame(self.bottomRightFrame)
        self.middleLeftTopFrame = Frame(self.middleLeftFrame)
        self.middleLeftBottomFrame = Frame(self.middleLeftFrame)
        self.middleRightTopFrame = Frame(self.middleRightFrame)
        self.middleRightBottomFrame = Frame(self.middleRightFrame)

        # #LABELS
        # #my ip label customization
        # self.currentIp_label = Label(self.topFrame,
        #                              text="My Ip: " + ipAdress,
        #                              fg="#dddddd",
        #                              bg=Interface.backgroundColor)

        # #password label customization
        # self.currentPassword_label = Label(self.frame2,
        #                                    text="<< NOT PASSWORD SET >>",
        #                                    fg="#dddddd",
        #                                    bg=Interface.backgroundColor)
        # #selected file label
        # self.currentFile_label = Label(self.interface,
        #                                text="<< NO FILE >>",
        #                                fg="#dddddd",
        #                                bg=Interface.backgroundColor)
        #LABELS

        #BINDS to functions
        # self.currentIp_label.bind("<Button-1>",
        #                           lambda e: self.copyToClipboard(ipAdress))
        # self.currentPassword_label.bind(
        #     "<Button-2>", lambda e: self.copyToClipboard(ipAdress))

        # #INPUTS
        # self.receivingPassword_field = Entry(self.frame2)
        # self.receivingPort_field = Entry(
        #     self.topFrame, textvariable="<< NO RECEIVING PORT >>")

        # # self.sendingPort_field = Entry(self.interface,
        # #                                textvariable="<< NO SENDING PORT >>")
        # # self.sendingIp_field = Entry(self.interface,
        # #                              textvariable="<< NO SENDING IP >>")

        # self.receivingPassword_field.insert(0, "<< NO RECEIVING PASSWORD >>")
        # self.receivingPort_field.insert(0, "<< NO RECEIVING PORT >>")
        # # self.sendingPort_field.insert(0, "<< NO SENDING PORT >>")
        # # self.sendingIp_field.insert(0, "<< NO SENDING IP >>")
        # #INPUTS

        # #BUTTONS
        # self.setPort_button = Button(self.topFrame,
        #                              text="Set receiving port")
        # self.setPassword_button = Button(self.frame2,
        #                                  text="Generate/Set password")
        # self.addFriend_button = Button(self.interface, text="Add friend")
        # self.deleteFriend_button = Button(self.interface, text="Delete friend")
        # self.setSavingLocation_button = Button(self.interface,
        #                                        text="Set saving location")
        # self.openDownload_button = Button(self.interface, text="Downloads")
        # self.selectFile_button = Button(self.interface, text="Select file")
        # self.send = Button(self.interface, text="Send")
        #BUTTONS

        #GRID ARANGEMENT
        #LABELS
        # self.currentIp_label.grid(row=0, column=0, sticky='e')
        # self.currentPassword_label.grid(row=1, column=0, sticky='e')
        # #LABELS

        # #INPUTS
        # self.receivingPort_field.grid(row=0, column=1, sticky='e')
        # self.receivingPassword_field.grid(row=1, column=1, sticky='e')
        # #INPUTS

        # #BUTTONS
        # self.setPort_button.grid(row=0, column=2, sticky='e')
        # self.setPassword_button.grid(row=1, column=2, sticky='e')
        #BUTTONS
        #GRID ARANGEMENT

        #packing
        # self.currentIp_label.grid(row=0, column=0)
        # self.currentPassword_label.grid(row=1, column=0)

        # self.receivingPort_field.grid(row=0, column=1)
        # self.receivingPassword_field.grid(row=1, column=1)

        # self.setPort_button.grid(row=0, column=2)
        # self.setPassword_button.grid(row=1, column=2)

        self.configureLayouts()