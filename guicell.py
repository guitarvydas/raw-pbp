import sys
sys.path.insert(0, 'pbp/kernel')
import kernel0d as zd
import editabletextwidget as etw

# Create the widget with the callback
widgetA = etw.EditableTextWidget(title="Widget A")

# Example of programmatically setting values
widgetA.display("A")

# Start the GUI
widgetA.run()
