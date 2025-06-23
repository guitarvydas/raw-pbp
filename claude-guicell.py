import tkinter as tk
from tkinter import ttk

class EditableField:
    def __init__(self, parent=None, on_edit_callback=None):
        """
        Create an editable numeric field GUI component.
        
        Args:
            parent: Parent tkinter widget (if None, creates own root window)
            on_edit_callback: Function to call when user edits the field
        """
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
        """Internal handler for when the field value changes"""
        if not self._updating_from_code and self.on_edit_callback:
            self.on_edit_callback()
    
    def _on_enter(self, event):
        """Internal handler for when user presses Enter"""
        if not self._updating_from_code and self.on_edit_callback:
            self.on_edit_callback()
    
    def _on_focus_out(self, event):
        """Internal handler for when field loses focus"""
        if not self._updating_from_code and self.on_edit_callback:
            self.on_edit_callback()
    
    def display(self, x):
        """
        Update the field to display the value x.
        
        Args:
            x: String value to display in the field
        """
        self._updating_from_code = True
        self.value_var.set(str(x))
        self._updating_from_code = False
    
    def get_value(self):
        """
        Get the current value in the field as a string.
        
        Returns:
            String value currently displayed in the field
        """
        return self.value_var.get()
    
    def set_on_edit_callback(self, callback):
        """
        Set or change the callback function for when field is edited.
        
        Args:
            callback: Function to call when user edits the field
        """
        self.on_edit_callback = callback
    
    def run(self):
        """Start the GUI main loop (only call if no parent was provided)"""
        if self.root:
            self.root.mainloop()


# Example usage and test
if __name__ == "__main__":
    # User-supplied onEdit function
    def onEdit():
        current_value = field.get_value()
        print(f"Field was edited! Current value: '{current_value}'")
        
        # Example: Convert to uppercase and display back
        if current_value:
            try:
                # Try to parse as number and format
                num = float(current_value)
                formatted = f"{num:.2f}"
                print(f"Auto-formatting number to: {formatted}")
                # Uncomment next line to see auto-formatting in action:
                # field.display(formatted)
            except ValueError:
                print("Not a valid number")
    
    # Create the field with the callback
    field = EditableField(on_edit_callback=onEdit)
    
    # Example of programmatically setting values
    field.display("123.45")
    
    # Add some test buttons to demonstrate programmatic control
    button_frame = ttk.Frame(field.frame)
    button_frame.pack(pady=10)
    
    def set_pi():
        field.display("3.14159")
    
    def set_zero():
        field.display("0")
    
    def clear_field():
        field.display("")
    
    ttk.Button(button_frame, text="Set π", command=set_pi).pack(side="left", padx=2)
    ttk.Button(button_frame, text="Set 0", command=set_zero).pack(side="left", padx=2)
    ttk.Button(button_frame, text="Clear", command=clear_field).pack(side="left", padx=2)
    
    # Start the GUI
    field.run()
