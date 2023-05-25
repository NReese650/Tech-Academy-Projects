import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.master.geometry("600x200")  # Set the size of the GUI window

        # Create a frame to hold the buttons and entry field
        frame = Frame(self.master)
        frame.pack(pady=(10), anchor="w")  # Add vertical padding to position the frame from the top

        # Label above the entry field
        label = Label(frame, text="Enter custom text or click the Default HTML page button:")
        label.grid(row=0, column=0, columnspan=2,sticky="w", padx=10, pady=10)

        # Entry field for user input
        self.text_entry = Entry(frame, width=75)
        self.text_entry.grid(row=1, column=0, columnspan=2, padx=10)

        # Button to generate default HTML page
        self.btn = Button(frame, text="Default HTML Page", width=20, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=0, pady=(10,0))

        # Button to generate custom HTML page
        self.custom_btn = Button(frame, text="Custom HTML Page", width=20, height=2, command=self.customHTML)
        self.custom_btn.grid(row=2, column=1, padx=10, pady=(10,0))

    def defaultHTML(self):
        # Default text
        htmlText = "Stay tuned for our amazing summer sale!"

        # Create and write to the HTML file
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()

        # Open the HTML file in a new browser tab
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        # Get the user input from the entry field
        htmlText = self.text_entry.get()

        # Create and write to the HTML file
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()

        # Open the HTML file in a new browser tab
        webbrowser.open_new_tab("index.html")


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
