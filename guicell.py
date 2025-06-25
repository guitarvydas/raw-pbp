import tkinter as tk
from tkinter import ttk
import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd
import editabletextwidget

# Example usage and test
if __name__ == "__main__":
    
    # Create the widget with the callback
    widgetA = EditableTextWidget(title="Widget A")
    
    # Example of programmatically setting values
    widgetA.display("A")
    
    # Start the GUI
    widgetA.run()
