import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class ImageViewerApp:
    def __init__(self, root, image_directory):
        self.root = root
        self.root.title("PNG Image Viewer")
        self.root.geometry = ("800x600")
        self.image_directory = image_directory

        # Create a dropdown to list PNG files
        self.image_files = [f for f in os.listdir(image_directory) if f.endswith('.png')]
        self.selected_image = tk.StringVar()
        
        #FOR A LISTBOX
        left_frame = tk.Frame(root)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Create a listbox to list PNG files
        self.image_files = [f for f in os.listdir(image_directory) if f.endswith('.png')]
        self.image_listbox = tk.Listbox(left_frame, selectmode=tk.SINGLE)
        for image_file in self.image_files:
            self.image_listbox.insert(tk.END, image_file)
        self.image_listbox.pack(side=tk.LEFT, fill=tk.Y)
        self.image_listbox.bind('<<ListboxSelect>>', self.display_image)


        self.text_box = tk.Text(left_frame, height=10, width=30)
        self.text_box.pack(side=tk.BOTTOM, fill=tk.X, pady=10)
        self.text_box.insert(tk.END, "This is some example text.\nYou can add more details here.")


        #FOR A DROPDOWN
        #self.dropdown = ttk.Combobox(root, textvariable=self.selected_image, \
        #                             values=self.image_files, width =100)
        #self.dropdown.pack(pady=10)
        #self.dropdown.bind('<<ComboboxSelected>>', self.display_image)

        # Create a label to display the image
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

#    def display_image(self, event):
#        # Get the selected image file
#        selected_file = self.selected_image.get()
#        image_path = os.path.join(self.image_directory, selected_file)
#
#        # Open the image file
#        image = Image.open(image_path)
#        image = image.resize((400, 400), Image.LANCZOS)
#        photo = ImageTk.PhotoImage(image)
#
#        # Update the label with the image
#        self.image_label.config(image=photo)
#        self.image_label.image = photo



    def display_image(self, event):
        # Get the selected image file
        selected_index = self.image_listbox.curselection()
        if not selected_index:
            return
        selected_file = self.image_listbox.get(selected_index)

        image_path = os.path.join(self.image_directory, selected_file)

        # Open the image file
        image = Image.open(image_path)
        image = image.resize((600, 400), Image.LANCZOS)  # Resize the image to fit the window
        photo = ImageTk.PhotoImage(image)

        # Update the label with the image
        self.image_label.config(image=photo)
        self.image_label.image = photo


if __name__ == "__main__":
    root = tk.Tk()
    image_directory = 'plots'  # Replace with the path to your PNG files
    app = ImageViewerApp(root, image_directory)
    root.mainloop()
