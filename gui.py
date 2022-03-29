from tkinter import *


def test(text):
    print(text)


class Interface:
    backgroundColor = '#1b1b1b'

    def copyToClipboard(self, text):
        self.interface.clipboard_clear()
        self.interface.clipboard_append(text)
        self.interface.update()

    def __init__(self, ipAdress):

        #BASE
        #background an other customizations
        self.interface = Tk(className="Simple IP transfer - Idle")
        self.interface.geometry("600x500")
        self.interface.resizable(False, False)
        self.interface['background'] = Interface.backgroundColor
        #BASE

        #LABELS
        #my ip label customization
        self.currentIp_label = Label(self.interface,
                                     text="My Ip: " + ipAdress,
                                     fg="#dddddd",
                                     bg=Interface.backgroundColor)

        #password label customization
        self.currentPassword_label = Label(self.interface,
                                           text="<< NOT PASSWORD SET >>",
                                           fg="#dddddd",
                                           bg=Interface.backgroundColor)
        #selected file label
        self.currentFile_label = Label(self.interface,
                                       text="<< NO FILE >>",
                                       fg="#dddddd",
                                       bg=Interface.backgroundColor)
        #LABELS

        #BINDS to functions
        self.currentIp_label.bind("<Button-1>",
                                  lambda e: self.copyToClipboard(ipAdress))
        self.currentPassword_label.bind(
            "<Button-2>", lambda e: self.copyToClipboard(ipAdress))

        #INPUTS
        self.receivingPassword_field = Entry(self.interface)
        self.receivingPort_field = Entry(
            self.interface, textvariable="<< NO RECEIVING PORT >>")

        self.sendingPort_field = Entry(self.interface,
                                       textvariable="<< NO SENDING PORT >>")
        self.sendingIp_field = Entry(self.interface,
                                     textvariable="<< NO SENDING IP >>")

        self.receivingPassword_field.insert(0, "<< NO RECEIVING PASSWORD >>")
        self.receivingPort_field.insert(0, "<< NO RECEIVING PORT >>")
        self.sendingPort_field.insert(0, "<< NO SENDING PORT >>")
        self.sendingIp_field.insert(0, "<< NO SENDING IP >>")
        #INPUTS

        #BUTTONS

        self.setPort = Button(self.interface,
                              text="Set receiving port",
                              width=30)
        self.setPassword = Button(self.interface,
                                  text="Generate/Set password",
                                  width=30)
        self.addFriend = Button(self.interface, text="Add friend")
        self.deleteFriend = Button(self.interface, text="Delete friend")
        self.setSavingLocation = Button(self.interface,
                                        text="Set saving location")
        self.openDownload = Button(self.interface, text="Downloads")
        self.selectFile = Button(self.interface, text="Select file")
        self.send = Button(self.interface, text="Send")

        #BUTTONS

        #packing
        self.currentIp_label.pack()
        self.currentFile_label.pack()
        self.currentPassword_label.pack()

        self.receivingPassword_field.pack()
        self.receivingPort_field.pack()
        self.sendingPort_field.pack()
        self.sendingIp_field.pack()

        self.setPort.pack()
        self.setPassword.pack()
        self.addFriend.pack()
        self.deleteFriend.pack()
        self.setSavingLocation.pack()
        self.openDownload.pack()
        self.selectFile.pack()
        self.send.pack()