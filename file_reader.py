from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class FileReader():
    def __init__(self, calling_app):
        self.calling_app = calling_app

    
    def openfile(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
            )
        
        filename = fd.askopenfilename(
            initialdir='/',
            filetypes=filetypes
        )

        showinfo(
            title='Selected File',
            message=filename
            )
            
        with open(filename) as f:
            lines = f.readlines()
        
        print(lines[4])