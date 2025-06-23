import tkinter as tk
from tkinter import ttk

class EditableField:
    def __init__(self, parent=None, on_edit_callback=None):
        self.on_edit_callback = on_edit_callback
        self._updating_from_code = False  # Flag to prevent callback during display()
        
        # Create window if no parent provided
        if parent is None:
            self.root = tk.Tk()
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
        
        # Bind events for when user changes the field
        self.value_var.trace_add("write", self._on_change)
        self.entry.bind('<Return>', self._on_enter)
        self.entry.bind('<FocusOut>', self._on_focus_out)
    
    def _on_change(self, *args):
        if not self._updating_from_code and self.on_edit_callback:
            self.on_edit_callback()
    
    def _on_enter(self, event):
        if not self._updating_from_code and self.on_edit_callback:
            self.on_edit_callback()
        print (self.get_value ())

    
    def _on_focus_out(self, event):
        if not self._updating_from_code and self.on_edit_callback:
            self.on_edit_callback()
        print (self.get_value ())
    
    def display(self, x):
        self._updating_from_code = True
        self.value_var.set(str(x))
        self._updating_from_code = False
    
    def get_value(self):
        return self.value_var.get()
    
    def set_on_edit_callback(self, callback):
        self.on_edit_callback = callback
    
    def run(self):
        if self.root:
            self.root.mainloop()


# Example usage and test
if __name__ == "__main__":
    # User-supplied onEdit function
    def onEdit():
        current_value = field.get_value()
    
    # Create the field with the callback
    field = EditableField(on_edit_callback=onEdit)
    
    # Example of programmatically setting values
    field.display("123.45")
    
    # Start the GUI
    field.run()
