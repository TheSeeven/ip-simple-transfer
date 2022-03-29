from globals import *

if __name__ == "__main__":
    freeze_support()
    samplethread.start()
    GUI.interface.mainloop()
    samplethread.terminate()
