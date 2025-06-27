import tkinter as tk
from tkinter import ttk

class EditableTextWidget:
    def __init__(self, parent=None, title=None):
        # Create window if no parent provided
        if parent is None:
            self.root = tk.Tk()
            if title:
                self.root.title (title)
            else:
                self.root.title("Editable Field")
            self.root.geometry("300x100")
            parent = self.root
        else:
            self.root = None
        
        # Create the main frame
        self.frame = ttk.Frame(parent, padding=10)
        self.frame.pack(expand=True, fill="both")
        
        # Create label
        self.label = ttk.Label(self.frame, text="Value:")
        self.label.pack(anchor="w", pady=(0, 5))
        
        # Create entry field
        self.value_var = tk.StringVar()
        self.entry = ttk.Entry(self.frame, textvariable=self.value_var, width=20)
        self.entry.pack(anchor="w")
        
        # Bind events - only Enter key and focus loss
        self.entry.bind('<Return>', self._on_user_action)
        self.entry.bind('<FocusOut>', self._on_user_action)
    
    def _on_user_action(self, event):
        """Internal handler for when user presses Enter or field loses focus"""
        current_value = self.value_var.get()
        print (f'user entered {current_value}')
        self.display (current_value)
    
    def display(self, x):
        self.value_var.set(str(x))
    
    def run(self):
        """Start the GUI main loop (only call if no parent was provided)"""
        if self.root:
            self.root.mainloop()
            




            
