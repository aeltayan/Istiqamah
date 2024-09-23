import tkinter as tk
from tkinter import ttk

def main():

    window = tk.Tk()

    window.attributes('-fullscreen', True)

    window.bind('<Escape>', lambda event : window.quit())

    window.mainloop()

if __name__ == '__main__':
    main()