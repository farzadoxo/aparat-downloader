
from tkinter import Tk,Label,Button,Text


# define window
window = Tk()
window.title("Aparat Downloader")
window.geometry('500x500')
window.maxsize = False


# components
url_lbl = Label(text="URL:")
path_lbl = Label(text="Path:")
url_txtbox = Text()
path_txtbox = Text()
downloads_btn = Button(text="Download")




# locating components



window.mainloop()