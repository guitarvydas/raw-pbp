import tkinter as tk
from tkinter import ttk
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd

class EditableTextWidget:
    def __init__(self, parent=None, on_user_edit_callback=None, title=None):
        self.on_user_edit_callback = on_user_edit_callback
        
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
        if self.on_user_edit_callback:
            self.on_user_edit_callback()
    
    def display(self, x):
        self.value_var.set(str(x))
    
    def get_value(self):
        return self.value_var.get()
    
    def run(self):
        """Start the GUI main loop (only call if no parent was provided)"""
        if self.root:
            self.root.mainloop()

# Example usage and test
if __name__ == "__main__":
    
    # User-supplied on_user_edit function
    def on_user_edit():
        current_value = widgetA.get_value()
        print (f'user entered {current_value}')
        widgetA.display (current_value)
        zd.send (eh, "manual_change", current_value, causingMevent=None)

    # Create the widget with the callback
    widgetA = EditableTextWidget(on_user_edit_callback=on_user_edit,title="Widget A")
    
    # Example of programmatically setting values
    widgetA.display("A")
    
    # Start the GUI
    widgetA.run()
